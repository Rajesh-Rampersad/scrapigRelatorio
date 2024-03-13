import requests
import os
from datetime import datetime

# URL del sitio web con el enlace de descarga
url = "https://bloqueiotelmkt.natal.rn.gov.br/telefone/listaConsolidada.php"

try:
    # Realizar una solicitud GET a la URL
    response = requests.get(
        'https://bloqueiotelmkt.natal.rn.gov.br/telefone/listaConsolidada.php')

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener la URL de descarga del enlace directamente del contenido HTML
        download_url = "https://bloqueiotelmkt.natal.rn.gov.br/telefone/arquivoTelefone.php"

        # Descargar el archivo
        file_response = requests.get(
            'https://bloqueiotelmkt.natal.rn.gov.br/telefone/arquivoTelefone.php')

        # Verificar si la descarga fue exitosa
        if file_response.status_code == 200:
            # Obtener la fecha actual para incluir en el nombre del archivo
            fecha_actual = datetime.now().strftime("%Y%m%d")

            # Nombre del archivo con el formato deseado
            nombre_archivo = f"RN_NATAL_{fecha_actual}.xls"

            # Guardar el archivo en el disco con el nuevo nombre
            with open(nombre_archivo, "wb") as f:
                f.write(file_response.content)
            print(f"Archivo descargado con éxito como '{nombre_archivo}'")
        else:
            print("Error al descargar el archivo")
    else:
        print("Error al obtener el enlace de descarga. Código de estado:",
              response.status_code)

except Exception as e:
    print("Ocurrió un error:", e)
