import requests
from bs4 import BeautifulSoup

rap_url = 'https://middermusic.com/best-rap-songs-of-all-time/'

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_2_3) AppleWebKit/603.29 (KHTML, like Gecko) Chrome/54.0.1921.375 Safari/600"}
r = requests.get(rap_url, headers=headers)

content = r.text
access = r.status_code
#print(access)

soup = BeautifulSoup(content, 'html.parser')

sections = soup.find_all('h2')

rap_music = []
# rap_music_dict = {}
index = 0
for i in range(25):
    section = sections[index].text.replace('', '')
    rap_music.append(section)
    index += 1

# print(rap_music)
# print(rap_music_dict)

""" dict ebit rogormekna,
mtavari linki ---> https://chartex.com/genre-statistics/hip-hop-2/songs/sort/total-views-desc """
