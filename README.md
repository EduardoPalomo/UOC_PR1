# Práctica de Web Scraping - Wikipedia TOC Extractor

Este repositorio contiene la implementación de un proyecto de web scraping para la asignatura "Tipología y ciclo de vida de los datos" del Máster en Ciencia de Datos de la UOC.

## Miembros del Grupo
- Eduardo Palomo Rodriguez

## Descripción de los Archivos del Repositorio
- `/source/scraper.py`: Script principal de Python que implementa el web scraping
- `/dataset/wikipedia_toc.csv`: Dataset resultante en formato CSV
- `requirements.txt`: Lista de dependencias de Python necesarias
- `.gitignore`: Archivos excluidos del control de versiones

## Uso del Código

### Requisitos Previos
1. Python 3.6 o superior
2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

### Ejecución del Script
El script principal se puede ejecutar de la siguiente manera:
```bash
python source/scraper.py
```

### Parámetros y Ejemplos
El script está configurado para extraer la tabla de contenidos del artículo de Wikipedia sobre web scraping. Los principales componentes son:

1. **User-Agent**: El script utiliza un User-Agent específico para identificarse ante el servidor:
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
```

2. **Delay**: Implementa un retraso de 1 segundo entre solicitudes para evitar sobrecargar el servidor:
```python
time.sleep(1)
```

3. **Output**: El dataset se guarda automáticamente en `/dataset/wikipedia_toc.csv`

## Dataset
El dataset generado está disponible en Zenodo con el siguiente DOI:
[10.5281/zenodo.15178228](https://doi.org/10.5281/zenodo.15178228)

Para citar este dataset:
```
Eduardo, P. R. (2025). Wikipedia Web Scraping Article Structure Dataset [Data set]. Zenodo. https://doi.org/10.5281/zenodo.15178228
```

