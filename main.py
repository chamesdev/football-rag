import os
from dotenv import load_dotenv, dotenv_values
import http.client
import json

load_dotenv()
sports_api = (os.getenv("sports_api"))

web = http.client.HTTPSConnection("v3.football.api-sports.io")

# Premier League 39
# La Liga 140
# Champions League 2

league_ids = [2, 39, 140]

i = 0

for league_id in league_ids:
    print("test", i)
    i += 1

    # web = http.client.HTTPSConnection("v3.football.api-sports.io")

    # headers = {
    #    'x-apisports-key': sports_api
    # }

    # web.request("GET", "/leagues?", headers=headers)

    # res = web.getresponse()
    # data = res.read()

    # leagues = data.decode("utf-8")

    # leagues_json = json.loads(leagues)
    
    # with open("leagues.json", "w") as f:
    #     json.dump(leagues_json, f, indent=4)


with open("all_leagues.json", "r") as file:
    all_leagues = json.load(file)
    print(all_leagues)

id = 1

result = next((item for item in all_leagues if item["id"] == id))



league_file = "leagues.json"
test_data = '{ "name":"John", "age":30, "city":"New York"}'

test_json = json.loads(test_data)

for league_id in league_ids:
    if os.path.isfile(league_file):
        print("File Found")
        print("Adding Stuff to File")
        with open("leagues.json", "a") as f:
            json.dump(test_json, f, indent=4)
    else:     
        print("No File Found")
        print("Creating File")
        with open("leagues.json", "a") as f:
            json.dump(test_json, f, indent=4)

