import os
from dotenv import load_dotenv, dotenv_values
import http.client

load_dotenv()
apikey = (os.getenv("apikey"))

print(apikey)

web = http.client.HTTPSConnection("v3.football.api-sports.io")





headers = {
    'x-apisports-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

web.request("GET", "/leagues", headers=headers)

res = web.getresponse()
data = res.read()

print(data.decode("utf-8"))