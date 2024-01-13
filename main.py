import datetime

from bs4 import BeautifulSoup
import requests

year = int(input('Enter a year: '))
while year not in range(1899, 2025):
    year = int(input('Enter a valid year: '))
    print()

month = int(input('Enter a month: '))
while month not in range(1, 13):
    month = int(input('Enter a valid month: '))
    print()

day = int(input('Enter a day: '))
while day not in range(1, 32):
    day = int(input('Enter a valid day: '))
    print()

date1 = datetime.date(year, month, day)
print(date1)

website_url = 'https://www.billboard.com/charts/hot-100/' + str(date1) +'/'
response = requests.get(website_url)
# print(response.text)

top_hits = response.text

soup = BeautifulSoup(top_hits, "html.parser")
#print(soup.prettify())

#all_hits = soup.find_all(name="h3", id="title-of-a-story")
#print(all_hits)

#for hit in all_hits:
    #print(hit.string)

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)