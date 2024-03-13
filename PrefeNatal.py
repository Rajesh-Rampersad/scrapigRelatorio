import requests
import os
from datetime import datetime

# URL do site com o link de download
# Website URL with the download link
# URL del sitio web con el enlace de descarga
url = "https://bloqueiotelmkt.natal.rn.gov.br/telefone/listaConsolidada.php"

try:
    # Realizar uma solicitação GET para a URL
    # Make a GET request to the URL
    # Realizar una solicitud GET a la URL
    response = requests.get(
        'https://bloqueiotelmkt.natal.rn.gov.br/telefone/listaConsolidada.php')

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    # Check if the request was successful (status code 200)
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obter o URL de download do link diretamente do conteúdo HTML
        # Get the download URL from the link directly from the HTML content
        # Obtener el URL de descarga del enlace directamente del contenido HTML
        download_url = "https://bloqueiotelmkt.natal.rn.gov.br/telefone/arquivoTelefone.php"

        # Baixar o arquivo
        # Download the file
        # Descargar el archivo
        file_response = requests.get(
            'https://bloqueiotelmkt.natal.rn.gov.br/telefone/arquivoTelefone.php')

        # Verificar se o download foi bem-sucedido
        # Check if the download was successful
        # Verificar si la descarga fue exitosa
        if file_response.status_code == 200:
            # Obter a data atual para incluir no nome do arquivo
            # Get the current date to include in the file name
            # Obtener la fecha actual para incluir en el nombre del archivo
            fecha_actual = datetime.now().strftime("%Y%m%d")

            # Nome do arquivo no formato desejado
            # File name in the desired format
            # Nombre del archivo con el formato deseado
            nombre_archivo = f"RN_NATAL_{fecha_actual}.xls"

            # Salvar o arquivo no disco com o novo nome
            # Save the file to disk with the new name
            # Guardar el archivo en el disco con el nuevo nombre
            with open(nombre_archivo, "wb") as f:
                f.write(file_response.content)
            print(f"Arquivo baixado com sucesso como '{nombre_archivo}'")
            # File downloaded successfully as '{nombre_archivo}'
        else:
            print("Erro ao baixar o arquivo")
            # Error downloading the file
    else:
        print("Erro ao obter o link de download. Código de status:",
              response.status_code)
        # Error getting the download link. Status code:
except Exception as e:
    print("Ocorreu um erro:", e)
    # An error occurred
