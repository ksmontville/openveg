import os
import requests as r
from dotenv import load_dotenv

load_dotenv()

api_url = os.environ.get("API_URL")

# PUT call to API to change ["vegan"] bool
put_ids = []
restaurants_to_change = []

# Get restaurants by their id, append to restaurants to be changed
responses = r.get(f"{api_url}")
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
    response = r.put(url=f"{api_url}/id/{restaurant['id']}", json=data)
    print(response.status_code, response.content)


# DELETE call to API
delete_ids = []
for id in delete_ids:
    response = r.delete(f"{api_url}/id/{id}")
    print(response.status_code, response.content)
