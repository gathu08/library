import json
import requests
import sys

if len(sys.argv) != 2:
    print("Too few arguements")
    sys.exit()
response = requests.get(
    "https://itunes.apple.com/search/?entity=song&limit=1000&term=" + sys.argv[1]
)

if response.status_code != 200:
    print(f"Invalid url:{response.status_code}")
    sys.exit()
try:
    songs = response.json()
except json.JSONDecodeError:
    print("json couldn't load")
    sys.exit()
if "results" in songs:
    for result in songs["results"]:
        print(result["trackName"])
else:
    pass
