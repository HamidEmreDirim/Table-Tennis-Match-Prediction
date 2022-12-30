from player_data import player_rankings
from match_data import matches


players = list(player_rankings.keys())
top_players = [player.split(",")[1].lower().strip() + " " + player.split(",")[0].lower().strip()  for player in players]
top_players += [player.split(",")[0].lower().strip() + " " + player.split(",")[1].lower().strip()  for player in players]

useful_matches = []
for match in matches:

    if match[0].lower() in top_players and match[1].lower() in top_players :
         useful_matches.append(match)

print(useful_matches)
