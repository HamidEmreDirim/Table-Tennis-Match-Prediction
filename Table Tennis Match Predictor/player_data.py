import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Getting current year to evaluate players age
current_year = datetime.datetime.now().year

# In the website there is a chart that shows players previous rating. This function gets average of previous rating.
def get_avarage_point():
    point_list = []
    try:
        for i in range(1, 60):
            x = driver.find_element(By.ID, f"point-0-{i}")
            x.click()
            point = driver.find_elements(By.CLASS_NAME, "legend_highlight")
            point = point[1].text
            point_list.append(int(point))
        avg = sum(point_list) / len(point_list)
        avg = round(avg, 2)
        return avg
    except:
        if len(point_list) > 1:
            avg = sum(point_list) / len(point_list)
            avg = round(avg, 2)
            return avg
        else:
            return 1

# get players picture
def get_photo():
    try:
        photo = driver.find_element(By.CLASS_NAME, "bordered")
        photo = photo.get_attribute("src")

        return photo

    except:
        photo = "https://tabletennis.guide/images/project/boy.png"
        return photo

# get players country, age, dominant hand and their grip data
def get_more():

    data = driver.find_elements(By.CLASS_NAME, "row")

    country = data[0].text.split()[-1]
    age = current_year - int(data[1].text.split()[-1])
    dominant_hand = data[2].text.split()[-1]
    play_style = data[3].text.split()[-1]
    grip = data[4].text.split()[-1]




    return [country, age, dominant_hand, grip, rank, play_style]

# get players name
def get_name(x):
    tournaments = driver.find_elements(By.CLASS_NAME, "row")
    tournament = tournaments[x].find_element(By.CLASS_NAME, "ta_left")
    name = tournament.text
    time.sleep(1)
    tournament = tournament.find_element(By.TAG_NAME,'a')
    tournament.click()

    return name



# get players current rank
def get_ranking(x):
    rows = driver.find_elements(By.CLASS_NAME, "row")
    rank = rows[x].find_element(By.CLASS_NAME, "ta_center")
    rank = rank.text

    return rank

driver = webdriver.Chrome(ChromeDriverManager().install())

all_player_data = []

# Go trough page 1 to 10 in the website and collect all the data with the functions
for page in range(1,11):

    driver.get(f"https://tabletennis.guide/rating_ittf.php?gender=1&country=&day=27&month=12&year=2022&page={page}")
    players = driver.find_elements(By.CLASS_NAME, "row")
    
    

    for i in range(1, len(players)):

        try:
            rank = get_ranking(i)
            name = get_name(i)


            player_data = [name, get_photo(), rank, get_avarage_point()]
            player_data.extend(get_more())

            all_player_data.append(player_data)
            driver.get(f"https://tabletennis.guide/rating_ittf.php?gender=1&country=&day=27&month=12&year=2022&page={page}")

            df = pd.DataFrame(all_player_data)
            df.to_csv("player_data.csv", index=False)
        except:

            driver.get(
                f"https://tabletennis.guide/rating_ittf.php?gender=1&country=&day=27&month=12&year=2022&page={page}")

            df = pd.DataFrame(all_player_data)
            df.to_csv("player_data.csv", index=False)
            df.to_sql("player_data.sql", index=False)
















