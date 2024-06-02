import requests
import json

stationId = -1
with open("settings.json", "r") as f:
    stationId = int(json.load(f).get("stationId"))

def upload(lon, lat, time):
    answer = requests.get("http://127.0.0.1:5000/upload", {"id": stationId, "lon": lon, "lat": lat, "time": time})
    if answer.raw == 'Thanks for uploading data!':
        return True
    return False
upload(321,123,213)