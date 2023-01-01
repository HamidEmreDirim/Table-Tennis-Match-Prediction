import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd


match_data = []

def pick_category():
    category = Select(driver.find_element(By.ID, "category"))
    category.select_by_visible_text("Men's Singles")

def click_tournament(i):
    tournament = tournaments[i].find_element(By.CLASS_NAME, "cell.ta_left")
    tournament.click()
jh



for page in range(1, 6):

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(f"https://tabletennis.guide/ittftournaments.php?page={page}")

    tournaments = driver.find_elements(By.CLASS_NAME, "row")


    for i in range(len(tournaments)):
        tournaments = driver.find_elements(By.CLASS_NAME, "row")
        try:
            click_tournament(i)
            time.sleep(1)
            pick_category()

            players = driver.find_elements(By.CLASS_NAME, "row")

            for z in range(1, len(players)):
                x = players[z].find_elements(By.CLASS_NAME, "cell")
                match_data.append([x[2].text, x[3].text, x[4].text, x[5].text])

            driver.get(f"https://tabletennis.guide/ittftournaments.php?page={page}")
            time.sleep(1)
            print(f"{i} th tournament data has been successfuly added.")
            df = pd.DataFrame(match_data)
            df.to_csv("match_data.csv", index=False)

        except:

            print(f"An error occurred in {i} th tournament.")
            driver.get(f"https://tabletennis.guide/ittftournaments.php?page={page}")
            time.sleep(1)






