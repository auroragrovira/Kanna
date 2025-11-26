# Kanna - Grey's Anatomy Fanfic Generator

Este proyecto es una herramienta automatizada para generar fanfics cortos de *Grey's Anatomy* en español utilizando la API de OpenAI (GPT-4o).

## Características
- Genera historias emotivas y dramáticas ambientadas en el Grey Sloan Memorial.
- Salida en formato **JSONL** (JSON Lines), ideal para procesamiento de datos o entrenamiento de modelos.
- Soporte para generación masiva con control de concurrencia.

## Requisitos
- Python 3.8+
- Una clave de API de OpenAI (configurada en el archivo `api_keys`).

## Instalación

1. **Crear y activar el entorno virtual**:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. **Instalar dependencias**:
   ```bash
   pip install openai
   ```

3. **Configurar API Key**:
   Asegúrate de tener un archivo llamado `api_keys` en la raíz del proyecto con el siguiente formato:
   ```
   chatGPT=sk-tu-clave-de-api-aqui
   ```

## Uso

Para generar fanfics, ejecuta el script `generate_texts.py` indicando la cantidad de historias que deseas crear:

```bash
python generate_texts.py <cantidad>
```

### Ejemplo
Generar 5 historias:
```bash
python generate_texts.py 5
```

Esto creará (o añadirá a) un archivo `output.jsonl` con las historias generadas.

## Formato de Salida
El archivo `output.jsonl` contiene una línea por historia con el siguiente formato JSON:

```json
{"id": "uuid-unico", "content": "Texto del fanfic generado..."}
```
