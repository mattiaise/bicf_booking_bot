import time
import argparse
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import booking_bot as bb
import data

"""

Se si volesse usare il bot in modalità headless scommentare il codice sottostante,
sostituire la riga 35 con quanto segue -> driver = create_headless_driver()

from selenium.webdriver.chrome.options import Options

def create_headless_driver():
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')         
    chrome_options.add_argument('--disable-gpu')      
    chrome_options.add_argument("window-size=1920,1080")  

    service = Service(executable_path=data.DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
    
"""

def job(args, state):

    while True:
        try:
            service = Service(executable_path=data.DRIVER_PATH)
            driver = webdriver.Chrome(service=service)
            try:
                driver.get(data.URL)
                driver.fullscreen_window()
                
                bb.login(driver)

                fast_booking = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "riprenota_title"))
                )
                fast_booking.click()

                bb.time_amount(driver, args.time_amount)

                giorno = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//div[@class='days']//div[@aria-description='selezionabile']")
                    )
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

                if "Done" in code_text or "Fatto" in code_text:
                    print("Prenotazione completata con successo!")
                    state["done"] = True 
                    return
                else:
                    print("Access code non valido:", code_text)

            finally:
                driver.quit()

        except Exception as e:
            print(f"Errore: {e}. Riprovo tra 10 secondi...")

        time.sleep(10)


def main():
    parser = argparse.ArgumentParser(description="Booking Bot Scheduler")
    parser.add_argument("--time-amount", required=True, type=int, help="Quantità di tempo (in ore)")
    parser.add_argument("--session-start", required=True, help="Orario di inizio sessione")
    parser.add_argument(
        "--scheduled",
        action="store_true",
        help="Se presente, la prenotazione verrà eseguita alle 07:00"
    )
    args = parser.parse_args()

    if args.scheduled:
        state = {"done": False}
        print("Prenotazione impostata per le 07:00 del mattino.")
        schedule.every().day.at("07:00").do(lambda: job(args, state))
        while True:
            schedule.run_pending()
            if state.get("done", False):
                print("Booking completato, uscita dal ciclo di scheduling.")
                schedule.clear()
                break
            time.sleep(30)
    else:
        job(args, state={})


if __name__ == "__main__":
    main()
