import requests
import json

stationId = -1
serverURL = ""
with open("settings.json", "r") as f:
    stationId = int(json.load(f).get("stationId"))
    serverURL = json.load(f).get("serverURL")

def upload(lon, lat, time):
    answer = requests.get(f"{serverURL}upload", {"id": stationId, "lon": lon, "lat": lat, "time": time})
    if answer.raw == 'Thanks for uploading data!':
        return True
    return False
upload(321,123,213)