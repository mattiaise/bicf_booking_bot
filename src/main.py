from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking_bot as bb
import argparse
import schedule
import data
import time

def job():
    while True:
        try:
            service = Service(executable_path=data.DRIVER_PATH)
            driver = webdriver.Chrome(service=service)
            
            driver.get(data.URL)
            driver.fullscreen_window()
            
            bb.login(driver)
            
            fast_booking = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "riprenota_title"))
            )
            fast_booking.click()
            
            bb.time_amount(driver, int(args.time_amount))
            
            giorno = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='days']//div[@aria-description='selezionabile']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", giorno)
            time.sleep(2)
            giorno.click()
            
            bb.time_slot(driver, args.session_start, args.time_amount)
            bb.confirm(driver)
            
            access_code = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "success"))
            )
            
            code_text = access_code.text.strip() 
            
            if "Done" in code_text:
                print("Prenotazione completata con successo!")
                break
            
        except Exception as e:
            print(f"Errore: {e}, riprovo...")
        
        finally:
            time.sleep(10)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-amount", required=True)
    parser.add_argument("--session-start", required=True)
    parser.add_argument("--scheduled", required=False)
    global args
    args = parser.parse_args()

    if args.scheduled == "y":
        print("Prenotazione impostata per le 07:00 del mattino.")
        schedule.every().day.at("07:00").do(job)
    else:
        job()

if __name__ == "__main__":
    main()
