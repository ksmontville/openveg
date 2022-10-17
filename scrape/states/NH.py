import os
import time
import requests as r
import requests.exceptions
import urllib3.exceptions
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from search.google_search import GoogleSearch

# This script works best on websites that use og: (Facebook OpenGraph) tags in their <head>.
# Need to find a more efficient way to filter search results

load_dotenv()

api_url = os.environ.get("API_URL")

state = "new hampshire"
terms = f"vegan restaurant {state}"

search = GoogleSearch(terms)
search.stop = 50
search.exclude = "-inurl:facebook.com -inurl:tripadvisor.com -inurl:yelp.com -inurl:happycow.net" \
                 " -inurl:businessinnewengland.com -inurl:npr.com -inurl:nhpr.org -inurl:boston.eater.com" \
                 " -inurl:reddit.com -inurl:aroundconcord.com -inurl:wokq.com -inurl:visitconcord-nh.com" \
                 " -inurl:wmur.com -inurl:nhanimalrights.org -inurl:godairyfree.org -inurl:949whom.com -inurl:vrg.org" \
                 " -inurl:nhtasty.com -inurl:portsmouthnh.com -inurl:opentable.com -inurl:vegnews.com -inurl:news.com" \
                 " -inurl:pinterest.com -inurl:newenglandwithlove.com -inurl:sirved.com -inurl:tasteoftheseacost.com" \
                 " -inurl:zomato.com -inurl:wikipedia.org -inurl:stoutheart.com -inurl:eatthis.com"

results = search.query()

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4040.128"
}

for result in results:
    try:
        url = f"{result}"
        page = r.get(url, headers=headers, timeout=20)

        soup = BeautifulSoup(page.content, "html.parser")

        if soup.find("meta", property="og:title") is not None:
            title = soup.find("meta", property="og:title").attrs["content"]
        elif soup.find("title") is not None:
            title = soup.find("title").text
        else:
            title = f"[restaurant name for {result} invalid]"

        if soup.find("meta", property="og:description") is not None:
            description = soup.find("meta", property="og:title").attrs["content"]
        else:
            description = f"[restaurant description for {result} invalid]"

        if soup.find("meta", property="og:url") is not None:
            url = soup.find("meta", property="og:url").attrs["content"]
        else:
            url = f"{result}"

        restaurant = {
            "title": title,
            "description": description,
            "website": url
        }

    except AttributeError or TypeError or NameError:
        print(f"Attribute, Type, or Name error occurred in {result}")
        restaurant = {
            "title": title,
            "description": description,
            "website": url,
        }

    except TimeoutError:
        print(f"Timeout error occurred in {result}")

    except requests.exceptions.ReadTimeout or requests.exceptions.ConnectTimeout or requests.exceptions.Timeout:
        print(f"Timeout error occurred in {result}")

    except requests.exceptions.ConnectionError or urllib3.exceptions.ConnectionError or urllib3.exceptions.ProtocolError:
        print(f"Connection error occurred in {result}")

    data = {
        "name": title,
        "description": description,
        "vegan": True,
        "web": url,
        "email": None,
        "phone": None,
        "address": None,
        "state": "new hampshire",
        "city": "",
        "zip": "",
    }

    response = r.post(url=api_url, json=data)
    print(response.status_code, response.content)
    time.sleep(4)
