import requests
import json
from temp_data import data
import datetime


current_year = datetime.datetime.now().year
api_key = "2525vxjtg63svye237adz2ea"
url = f"https://api.sportradar.com/tabletennis/trial/v2/en/rankings.json?api_key={api_key}"

# r = requests.get(url)
# data = r.json()

def get_attributes(data):
    attributes = dict()
    for player in data['competitor_rankings']:
        try:
            attributes[player['competitor']["name"]] = [player['competitor']["id"], player['rank'],
                                                            player['competitor']["country"], current_year - int(
                    player['competitor']["date_of_birth"].split("-")[0])]
        except:
            pass
    return attributes

men_single_data = data["rankings"][0]
women_single_data = data["rankings"][2]

men_attributes = get_attributes(men_single_data)
women_attributes = get_attributes(women_single_data)

print(men_attributes)






