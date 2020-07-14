import requests
import json
from bs4 import BeautifulSoup

def getDataByID(id):
    url = 'https://llsif.org/en/cards/' + str(id)
    page = requests.get(url) 
    soup = BeautifulSoup(page.text, 'html.parser')
    data = soup.find_all('card-skill')
    if len(data) > 0:
        return json.loads(data[0].get('json'))
    else:
        return "This is a N card"



