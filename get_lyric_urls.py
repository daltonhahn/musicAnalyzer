import requests
import sys
import csv
import os
import json

from dotenv import load_dotenv

load_dotenv(dotenv_path="/home/ubuntu/.env")

base_url = "http://api.genius.com"
headers = {'Authorization': 'Bearer ' + os.getenv("ACCESS_TOKEN")}
search_url = base_url + "/search"


fileWriter = open("urls.txt", "w")

csvReader = csv.reader(open(sys.argv[1], "r"))

for row in csvReader:
    song_title = row[1]
    params = {'q': song_title}
    response = requests.get(search_url, params=params, headers=headers)
    json = response.json()
    print(json["response"]["hits"][0]["result"]["url"])
    path = json["response"]["hits"][0]["result"]["url"]
    fileWriter.write(path + "\n")
