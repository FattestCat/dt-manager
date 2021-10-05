from pprint import pprint

import requests
from bs4 import BeautifulSoup as bs

BASE_URL: str = "https://liquipedia.net"
TEAMS_URL: str = "https://liquipedia.net/dota2/Portal:Teams"
teams = requests.get(TEAMS_URL)
teams_soup = bs(teams.text, "html.parser").find_all(class_="team-template-text")


pprint(teams_soup)
pprint(type(teams_soup))

# pprint(teams.text)
# pprint(type(teams.text))
