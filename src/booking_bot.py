from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import data
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SHORT_WAIT = 1

def scroll_and_click(driver, element, wait_time=SHORT_WAIT):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(wait_time)
    element.click()

def login(driver):
    try:
        login_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-cypress='navBar-Accedi']"))
        )
        login_button.click()

        username_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys(data.USER)

        password_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(data.PSW)

        submit_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
        )
        submit_button.click()
    except Exception as e:
        logging.error("Errore durante il login: %s", e)
        raise

def time_amount(driver, amount):
    try:
        durata_dropdown = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "durata"))
        )
        durata_dropdown.click()

        option_value = amount * 3600
        option = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, f"//option[@value='{option_value}']"))
        )
        option.click()

        durata_dropdown.click()
    except Exception as e:
        logging.error("Errore durante la selezione della durata: %s", e)
        raise

def time_slot(driver, start, amount):
    try:
        slot_start = datetime.strptime(start, "%H:%M")
        slot_end = slot_start + timedelta(hours=int(amount))
        
        slot_start_str = slot_start.strftime("%H:%M")
        slot_end_str = slot_end.strftime("%H:%M")

        xpath = (
            f"//div[@aria-label='time select']"
            f"//div[starts-with(@aria-label, '{slot_start_str}')]"
            f"//span[text()=' {slot_start_str}  - {slot_end_str}']"
        )
        
        time_slot_elem = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        scroll_and_click(driver, time_slot_elem)
    except Exception as e:
        logging.error("Errore durante la selezione della fascia oraria: %s", e)
        raise

def confirm(driver):
    try:
        data_confirm_link = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/portalePlanning/biblio/prenota/Riepilogo']"))
        )
        scroll_and_click(driver, data_confirm_link)

        booking_confirm_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.my-2"))
        )
        time.sleep(SHORT_WAIT)
        booking_confirm_button.click()
    except Exception as e:
        logging.error("Errore durante la conferma della prenotazione: %s", e)
        raise
