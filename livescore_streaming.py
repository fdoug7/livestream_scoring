import requests
import bs4
import csv
import json


livescore_url = "https://livescores.computerscore.com.au/"
center = "view-lanes.php?centre=137"

x = requests.get(livescore_url+center)

if x.status_code == 200:
    print("Get request has worked")
else:
    print("Get request failed with code " + x.status_code)

soup = bs4.BeautifulSoup(x.text, 'html.parser')

table = soup.find_all('table')[0]
rows = table.find_all('tr')

lanes={}

for row in rows[1:]:
    cells = row.find_all('td')
    lane = cells[0].text.strip()

    select_a = row.select('a')[0]
    lane_view = select_a.get('href')

    lanes[lane]=lane_view

    print(lane + ' | ' + livescore_url + lane_view)
print(lanes)