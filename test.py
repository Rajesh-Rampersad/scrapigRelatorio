from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Inicializar el navegador Selenium
driver = webdriver.Chrome()

try:
    # Abrir la URL del sitio web
    wait = WebDriverWait(driver, 20)
    driver.get(
        "http://wapp.mpce.mp.br/DeconAntiMarketing/visao/con_Telefones.aspx")

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

    # Esperar a que se carguen los resultados (opcional)
    wait = WebDriverWait(driver, 20)
    download_link = wait.until(EC.presence_of_element_located(
        (By.ID, 'ctl00_ContentPlaceHolder1_lbDown')))

    # Puedes agregar una espera implícita o explícita aquí si es necesario

    # Una vez que se carguen los resultados, puedes continuar con tu lógica de extracción de datos

except Exception as e:
    print("Ocurrió un error:", e)

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
