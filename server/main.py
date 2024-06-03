from flask import Flask, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = ""
with open("server/secret.json", "r") as f:
    uri = json.load(f).get("uri")

monClient = MongoClient(uri, server_api=ServerApi('1'))
monCollection = monClient['ThunderTracker']['thurderData']

app = Flask(__name__)
@app.route('/upload', methods=['GET'])
def uploadData():
    stationId = request.args.get('id', type=float)
    lon = request.args.get('lon', type=float)
    lat = request.args.get('lat', type=float)
    time = request.args.get('time', type=int)
    monCollection.insert_one({'stationId': stationId, 'lon': lon, 'lat': lat, 'time': time})
    return 'Thanks for uploading data!'
@app.route('/check', methods=["GET"])
def checkCurrentData():
    values = monCollection.find({}, {'_id': False}).sort('_id', -1)
    return json.dumps(values[0])

if __name__=='__main__': 
    app.run()