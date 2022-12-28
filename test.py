from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

match_data = []

for page in range(1):

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(f"https://tabletennis.guide/ittftournaments.php?page={page}")



    tournaments = driver.find_elements(By.CLASS_NAME, "row")
    print(tournaments)
    print(len(tournaments))
    for i in range(0, len(tournaments)):
        try:
            tournament = tournaments[i].find_element(By.CLASS_NAME, "cell.ta_left")
            tournament.click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
        except:
            driver.get(f"https://tabletennis.guide/ittftournaments.php?page={page}")
            tournaments = driver.find_elements(By.CLASS_NAME, "row")








