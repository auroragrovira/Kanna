import os
import asyncio
import json
import argparse
import uuid
from openai import AsyncOpenAI

# Configuration
CONCURRENT_REQUESTS = 3
OUTPUT_FILE = "output.jsonl"

def get_api_key():
    try:
        with open('api_keys', 'r') as f:
            for line in f:
                if line.startswith('chatGPT='):
                    return line.strip().split('=')[1]
    except FileNotFoundError:
        return None
    return None

async def generate_fanfic(client, sem):
    async with sem:
        try:
            response = await client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Eres un escritor creativo experto en fanfics de Anatomía de Grey en español. Escribe historias emotivas y dramáticas."},
                    {"role": "user", "content": "Escribe un fanfic corto (aprox. 500 palabras) sobre un momento intenso en el hospital Grey Sloan Memorial. Céntrate en las emociones de los personajes."}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating text: {e}")
            return None

async def main():
    parser = argparse.ArgumentParser(description="Generate Grey's Anatomy fanfics.")
    parser.add_argument("num_files", type=int, help="Number of fanfics to generate")
    args = parser.parse_args()

    api_key = get_api_key()
    if not api_key:
        print("Error: Could not find chatGPT API key in api_keys file.")
        return

    client = AsyncOpenAI(api_key=api_key)
    sem = asyncio.Semaphore(CONCURRENT_REQUESTS)
    
    print(f"Starting generation of {args.num_files} fanfics...")
    
    tasks = []
    for _ in range(args.num_files):
        tasks.append(generate_fanfic(client, sem))

    results = await asyncio.gather(*tasks)

    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
        for content in results:
            if content:
                record = {
                    "id": str(uuid.uuid4()),
                    "content": content
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
    
    print(f"Generation complete. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
