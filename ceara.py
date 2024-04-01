import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

# # Inicializar o navegador Selenium
# # Initialize Selenium browser
# # Inicializar el navegador Selenium
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)  # Estabelecer uma espera implícita de 20 segundos
# # Set implicit wait to 20 seconds

# # Obtener a URL atual do navegador Selenium
# # Get the current URL of the Selenium browser
# # Obtener la URL actual del navegador Selenium
# driver.get("http://wapp.mpce.mp.br/DeconAntiMarketing/visao/con_Telefones.aspx")


service = webdriver.ChromeService()
options = webdriver.ChromeOptions()

# Agregar las opciones para evitar el cuadro de diálogo de confirmación de descarga
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--remote-debugging-address=0.0.0.0")
options.add_argument("--incognito")

driver = webdriver.Chrome(service=service, options=options)
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
    wait = WebDriverWait(driver, 0.5)
    download_link = wait.until(EC.visibility_of_element_located(
        (By.ID, 'ContentPlaceHolder1_lbDown')))
    download_link.click()

    print("Esperando que aparezca el cuadro de diálogo de descarga...")

    # Esperar 10 segundos para que aparezca el cuadro de diálogo de descarga
    time.sleep(10)

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
