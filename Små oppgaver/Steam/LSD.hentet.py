import json
import requests

with open("gamesLærer.json", "r", encoding="utf-8") as f:
    data = json.load(f)

antall_spill = len(data["spill"]) + 1
print(f"Antall spill: {antall_spill}\n")

sorted_games = sorted(data["spill"], key=lambda game: game["playtime_forever_hours"],reverse=True)
mostplayed_game = sorted_games[0]

for game in sorted_games:
    if game["playtime_forever_hours"] > 5:
        print(f"{game['name']} – {game['playtime_forever_hours']} timer")

print(f"""-------------------------------------------------------
Mest spillte spill: {mostplayed_game['name']} – {mostplayed_game['playtime_forever_hours']} timer
-------------------------------------------------------
""")