import requests
import json

r = requests.get("http://api.ittf.com/1/matches/?tournamentId=1111&eventType=MS")
j=r.json()
print(j)