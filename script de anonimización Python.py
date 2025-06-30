import os
import requests

# URL del PDF a descargar
pdf_url = "https://ejemplo.com/documento.pdf"  # Reemplaza con la URL real

# Carpeta donde se guardará el PDF
download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)

# Nombre del archivo a guardar
output_path = os.path.join(download_folder, "documento-descargado.pdf")

try:
    print(f"📥 Descargando PDF desde: {pdf_url}")
    response = requests.get(pdf_url)
    response.raise_for_status()  # Lanza un error si el status no es 200

    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"✅ PDF guardado en: {output_path}")
except requests.exceptions.RequestException as e:
    print(f"❌ Error al descargar el PDF: {e}")
