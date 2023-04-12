import requests
import json





r = requests.get("https://zylalabs.com/api/1068/table+tennis+live+scores+api/940/fetch+live+table+tennis+matches")
j=r.json()
print(j)