from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import data
import time

def login(driver):
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
    
def time_amount(driver, amount):
    durata = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "durata"))
    )
    durata.click()

    time_amount = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//option[@value='{amount*3600}']"))
    )
    time_amount.click()
    durata.click()
    
def time_slot(driver, start, amount):
    slot_start = datetime.strptime(start, "%H:%M")
    slot_end = slot_start + timedelta(hours=int(amount))

    slot_end_str = slot_end.strftime("%H:%M")
    slot_start_str = slot_start.strftime("%H:%M")

    time_slot = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='time select']//div[starts-with(@aria-label, '{slot_start_str}')]//span[text()=' {slot_start_str}  - {slot_end_str}']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", time_slot)
    time.sleep(2)
    time_slot.click()
    
def confirm(driver):
    data_confirm = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/portalePlanning/biblio/prenota/Riepilogo']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", data_confirm)
    time.sleep(2)
    data_confirm.click()
    
    booking_confirm = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.my-2"))
    )
    booking_confirm.click()
    time.sleep(2)
    booking_confirm.click()