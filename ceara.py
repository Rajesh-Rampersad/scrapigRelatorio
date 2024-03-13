import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Inicializar o navegador Selenium
# Initialize Selenium browser
# Inicializar el navegador Selenium
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # Estabelecer uma espera implícita de 20 segundos
# Set implicit wait to 20 seconds

# Obtener a URL atual do navegador Selenium
# Get the current URL of the Selenium browser
# Obtener la URL actual del navegador Selenium
driver.get("http://wapp.mpce.mp.br/DeconAntiMarketing/visao/con_Telefones.aspx")

try:
    # Encontrar os campos de data de início e fim e inserir as datas
    # Find the start and end date fields and enter the dates
    # Encontrar los campos de fecha de inicio y fin e ingresar las fechas
    fecha_inicio_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_txtDtIni")
    fecha_inicio_input.clear()
    # Alterar a data conforme necessário
    # Change the date as necessary
    # Cambiar la fecha según sea necesario
    fecha_inicio_input.send_keys("01/01/2000")

    fecha_fin_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_txtDtFim")
    fecha_fin_input.clear()
    fecha_fin_input.send_keys(
        datetime.now().strftime("%d/%m/%Y"))  # Data atual
    # Hacer clic en el botão "Buscar"
    # Click the "Buscar" button
    # Hacer clic en el botón "Buscar"
    buscar_button = driver.find_element(By.ID, "ContentPlaceHolder1_btnBuscar")
    buscar_button.click()

    # Esperar até que o link de download apareça
    # Wait until the download link appears
    # Esperar a que aparezca el enlace de descarga
    wait = WebDriverWait(driver, 30)
    download_link = wait.until(EC.presence_of_element_located(
        (By.ID, 'ctl00_ContentPlaceHolder1_lbDown')))

    # Obter o URL de download e clicar nele
    # Get the download URL and click on it
    # Obtener el URL de descarga y hacer clic en él
    download_url = download_link.get_attribute("href")
    driver.get(download_url)
    os.system(f"wget {download_link}")

    # Obter o URL de download do link
    # file_url = download_link.get_attribute("href")

    # Baixar o arquivo
    # Download the file
    # Descargar el archivo
    # os.system(f"wget {file_url}")

    print("Arquivo baixado com sucesso")
    # Archivo descargado con éxito

except Exception as e:
    print("Ocorreu um erro:", e)
    # An error occurred

finally:
    # Fechar o navegador ao terminar
    # Close the browser when finished
    # Cerrar el navegador al finalizar
    driver.quit()
