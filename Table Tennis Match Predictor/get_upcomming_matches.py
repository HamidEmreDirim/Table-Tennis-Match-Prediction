import requests
from bs4 import BeautifulSoup
import os

url = "https://worldtabletennis.com/events_calendar"
reponse = requests.get(url)

if reponse.ok:
	soup = BeautifulSoup(reponse.text)
	title = str(soup.find("title"))

	title = title.replace("<title>", "")
	title = title.replace("</title>", "")
	print("The title is : " + str(title))

os.system("pause")