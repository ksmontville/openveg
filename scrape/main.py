import os
from dotenv import load_dotenv
import requests as r
from bs4 import BeautifulSoup
from search.google_search import GoogleSearch

# This script works best on websites that use og: (Facebook OpenGraph) tags in their <head>.

load_dotenv()

api_url = os.environ.get("API_URL")

terms = "vegan restaurant"
state = "new hampshire"

search = GoogleSearch(terms, state)
search.stop = 10
search.exclude = "-inurl:facebook.com -inurl:tripadvisor.com -inurl:yelp.com -inurl:happycow.net " \
                 "-inurl:businessinnewengland.com -inurl:npr.com -inurl:nhpr.com -inurl:boston.eater.com" \
                 "-inurl:reddit.com -inurl:aroundconcord.com -inurl:wokq.com -inurl:visitconcord-nh.com" \
                 "-inurl:wmur.com -inurl:nhanimalrights.org -inurl:godairyfree.org"

results = search.query()
print(results)

for result in results:
    try:
        url = f"{result}"
        page = r.get(url)

        soup = BeautifulSoup(page.content, "html.parser")

        restaurant = {
            "title": soup.find("meta", property="og:title").attrs["content"],
            "description": soup.find("meta", property="og:description").attrs["content"],
            "website": soup.find("meta", property="og:url").attrs["content"]
        }

    except AttributeError or TypeError:
        print(f"Error in {result}, trying different parameters......")
        restaurant['title'] = soup.find("title").text
        if restaurant['title']:
            print("Success.")

    data = {
        "name": f'{restaurant["title"]}',
        "description": f'{restaurant["description"]}',
        "vegan": True,
        "web": f'{restaurant["website"]}',
        "email": None,
        "phone": None,
        "address": None,
        "state": "new hampshire",
        "city": "",
        "zip": "",
    }

    response = r.post(url=api_url, json=data)
    print(response.status_code)
