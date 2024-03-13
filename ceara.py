# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from datetime import datetime

# # Inicializar el navegador Selenium
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)  # Establecer una espera implícita de 20 segundos

# # Obtener la URL actual del navegador Selenium

# wait = WebDriverWait(driver, 20)
# base_url = driver.get(
#     "http://wapp.mpce.mp.br/DeconAntiMarketing/visao/con_Telefones.aspx")

# # Encontrar los campos de fecha de inicio y fin e ingresar las fechas
# fecha_inicio_input = driver.find_element(
#     By.ID, "ContentPlaceHolder1_txtDtIni")
# fecha_inicio_input.clear()
# # Cambiar la fecha según sea necesario
# fecha_inicio_input.send_keys("01/01/2000")

# fecha_fin_input = driver.find_element(
#     By.ID, "ContentPlaceHolder1_txtDtFim")
# fecha_fin_input.clear()
# fecha_fin_input.send_keys(
#     datetime.now().strftime("%d/%m/%Y"))  # Fecha actual

# # Hacer clic en el botón "Buscar"
# buscar_button = driver.find_element(By.ID, "ContentPlaceHolder1_btnBuscar")
# buscar_button.click()

# # Esperar a que se carguen los resultados (opcional)
# wait = WebDriverWait(driver, 20)
# download_link = wait.until(EC.presence_of_element_located(
#     (By.ID, 'ctl00_ContentPlaceHolder1_lbDown')))

# try:
#     # Realizar la solicitud POST con la URL actual del navegador
#     response = requests.post(
#         'http://wapp.mpce.mp.br/DeconAntiMarketing/visao/con_Telefones.aspx', data=payload)

#     # Verificar si la solicitud fue exitosa (código de estado 200)
#     if response.status_code == 200:
#         # Analizar el contenido HTML de la respuesta
#         soup = BeautifulSoup(response.content, "html.parser")

#     else:
#         print("Error al enviar la solicitud. Código de estado:",
#               response.status_code)
# finally:
#     # Cerrar el navegador Selenium
#     driver.quit()


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Inicializar el navegador Selenium
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # Establecer una espera implícita de 20 segundos

# Obtener la URL actual del navegador Selenium
driver.get("http://wapp.mpce.mp.br/DeconAntiMarketing/visao/con_Telefones.aspx")

try:
    # Encontrar los campos de fecha de inicio y fin e ingresar las fechas
    fecha_inicio_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_txtDtIni")
    fecha_inicio_input.clear()
    # Cambiar la fecha según sea necesario
    fecha_inicio_input.send_keys("01/01/2000")

    fecha_fin_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_txtDtFim")
    fecha_fin_input.clear()
    fecha_fin_input.send_keys(
        datetime.now().strftime("%d/%m/%Y"))  # Fecha actual

    # Hacer clic en el botón "Buscar"
    buscar_button = driver.find_element(By.ID, "ContentPlaceHolder1_btnBuscar")
    buscar_button.click()

    # Esperar a que aparezca el enlace de descarga
    wait = WebDriverWait(driver, 30)
    download_link = wait.until(EC.presence_of_element_located(
        (By.ID, 'ctl00_ContentPlaceHolder1_lbDown')))

    # Obtener el URL de descarga y hacer clic en él
    download_url = download_link.get_attribute("href")
    driver.get(download_url)
    os.system(f"wget {download_link}")

    # Obtener la URL de descarga del enlace
    # file_url = download_link.get_attribute("href")

    # # Descargar el archivo
    # os.system(f"wget {file_url}")

    print("Archivo descargado con éxito")

except Exception as e:
    print("Ocurrió un error:", e)

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
