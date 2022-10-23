import os
import requests as r
from dotenv import load_dotenv

load_dotenv()

# Heroku DB
api_url = os.environ.get("API_URL")
# Local DB for backup, INITIALIZE SERVER BEFORE RUNNING SCRIPT
local_host = 'http://localhost:8000/restaurants'

urls = [local_host]


# PUT call to API to change ["vegan"] bool
for url in urls:
    put_ids = [140,163,167]
    restaurants_to_change = []
# Get restaurants by their id, append to restaurants to be changed
    responses = r.get(url)
    for response in responses.json():
        if response["id"] in put_ids:
            restaurants_to_change.append(response)

    for restaurant in restaurants_to_change:
        data = {
            "name": restaurant["name"],
            "description": restaurant["description"],
            "vegan": False,
            "web": restaurant["web"],
            "email": restaurant["email"],
            "phone": restaurant["phone"],
            "address": restaurant["address"],
            "state": restaurant["state"],
            "city": restaurant["city"],
            "zip": restaurant["zip"],
            "id": restaurant["id"]
        }
        response = r.put(url=f"{url}/id/{restaurant['id']}", json=data)
        print(f"POST to {url} {response.status_code}\n{response.content}")


# DELETE call to API
for url in urls:
    delete_ids = []
    for id in delete_ids:
        response = r.delete(f"{url}/id/{id}")
        print(f"DELETE to {url} {response.status_code}\n{response.content}")
