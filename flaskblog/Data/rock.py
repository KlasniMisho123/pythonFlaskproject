import requests
from bs4 import BeautifulSoup

rock_url = 'https://ew.com/music/best-rock-songs/'

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_3_3) AppleWebKit/533.5 (KHTML, like Gecko)/48.0.3113.233 Safari/534"}

r = requests.get(rock_url, headers=headers)

content = r.text
access = r.status_code
#print(access)

soup = BeautifulSoup(content, 'html.parser')
sections = soup.find_all('span', {'class': 'listicle-headline--inner'})

rock_music = []

index = 1
for i in sections:
    rock_music.append(f"{index}) {i.text.replace(',', '')}")
    index += 1

#print(rock_music)

"""mtavari linki ---> https://chartex.com/genre-statistics/hip-hop-2/songs/sort/total-views-desc """
