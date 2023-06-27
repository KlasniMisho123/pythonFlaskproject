import requests
from bs4 import BeautifulSoup

pop_url = 'https://www.timeout.com/music/best-pop-songs-of-all-time'

headers = {
    "user-agent": "Mozilla / 5.0 (compatible; MSIE 11.0; Windows; Windows NT 10.2; x64; en-US Trident / 7.0"}
r = requests.get(pop_url, headers=headers)

content = r.text
access = r.status_code
# print(access)

soup = BeautifulSoup(content, 'html.parser')
sections = soup.find_all('h3')
# sections_1 = soup.find("div", {"_zoneItems_4w5ul_1 zoneItems"},)
# section_1 = sections_1.find_all("img")


pop_music = []
index = 0
for i in range(25):
    section = sections[index].text.replace('\xa0', ' ')
    pop_music.append(section)
    # print(section)
    index += 1

# print(pop_music)
""" xa0 . gafiltvra"""
"""mtavari linki ---> https://chartex.com/genre-statistics/pop-5/songs/sort/total-views-desc """
"""imgs / text"""
""" sidebar-"""
