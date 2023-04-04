from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


#open driver

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(f"https://tabletennis.guide/rating_ittf.php?gender=1&country=&day=27&month=12&year=2022&page=1")
players = driver.find_elements(By.CLASS_NAME, "row")
player = players[1].find_element(By.CLASS_NAME, "ta_left")

link = player.find_element(By.TAG_NAME,'a')
link.click()




