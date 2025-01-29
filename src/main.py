from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data
import time

service = Service(executable_path=data.DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get(data.URL)
driver.fullscreen_window()

login = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@data-cypress='navBar-Accedi']"))
)
login.click()

username = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username.send_keys(data.USER)
password = driver.find_element(By.ID, "password")
password.send_keys(data.PSW)

send_data = driver.find_element(By.XPATH, "//input[@type='submit']")
send_data.click()

fast_booking = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "riprenota_title"))
)
fast_booking.click()

durata = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "durata"))
)
durata.click()

time_amount = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//option[@value='3600']"))
)
time_amount.click()
durata.click()

giorno = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='days']//div[@aria-description='selezionabile']"))
)
giorno.click()

time_slot = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='time select']//span[.='22:00 - 23:00']"))
)
time_slot.click()


time.sleep(10)


