from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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


driver = webdriver.Chrome(service=service, options=options)
driver.get("http://wapp.mpce.mp.br/DeconAntiMarketing/visao/con_Telefones.aspx")

try:
    fecha_inicio_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_txtDtIni")
    fecha_inicio_input.clear()
    fecha_inicio_input.send_keys("01/01/2000")

    fecha_fin_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_txtDtFim")
    fecha_fin_input.clear()
    # Cambiar la fecha según sea necesario
    fecha_fin_input.send_keys("28/02/2024")

    buscar_button = driver.find_element(By.ID, "ContentPlaceHolder1_btnBuscar")
    buscar_button.click()

    wait = WebDriverWait(driver, 10)
    download_link = wait.until(EC.visibility_of_element_located(
        (By.ID, 'ContentPlaceHolder1_lbDown')))
    download_link.click()

    print("Esperando que aparezca el cuadro de diálogo de descarga...")

    # Esperar 10 segundos para que aparezca el cuadro de diálogo de descarga
    time.sleep(10)

    print("Descarga completada")

except Exception as e:
    print("Ocurrió un error:", e)

finally:
    driver.quit()
