# Actividad09

Proyecto base en **Python** con estructura modular, pruebas unitarias y configuración para **Docker**.

## 🚀 Ejecución local

1. Crear entorno virtual:
   ```bash
   python -m venv venv
   ```

2. Activar entorno:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar el programa:
   ```bash
   python src/main.py
   ```

5. Ejecutar pruebas:
   ```bash
   pytest
   ```

## 🐳 Ejecutar con Docker

```bash
docker build -t actividad09 .
docker run actividad09
```
