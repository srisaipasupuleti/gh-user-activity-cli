import requests, os, json, sys
from dotenv import load_dotenv

load_dotenv()

username = sys.argv[1]
endpoint = f"https://api.github.com/users/{username}/events"
headers = {"Authorization": f"token {os.getenv('ghToken')}"}

request = requests.get(endpoint, headers=headers, verify=False)
activity = request.json()
activity = json.dumps(activity, indent=4)
print(activity)