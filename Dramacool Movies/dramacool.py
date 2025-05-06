import requests
from bs4 import BeautifulSoup

import pandas as pd


print(f"Scraping page:1...")# Making a GET request
r = requests.get('https://asianc.sh/recently-added-movie')


# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('ul', class_='switch-block list-episode-item')
movie_title = s.find_all('h3')
sub_type = s.find_all('span', class_=["type RAW", "type SUB"])
realise_time = s.find_all('span', class_="time")


# for i in content:
#     print(i.text)

data = []
fields = ["Title", "Subtitle", "Realise Time"]

for i in range(len(movie_title)):
    dic = {
        "Title": movie_title[i].text,
        "Subtitle": sub_type[i].text,
        "Realise Time": realise_time[i].text
    }

    data.append(dic)

page_num = 50

for i in range(2,page_num+1):
    print(f"Scraping page:{i}...")
    r = requests.get(f'https://asianc.sh/recently-added-movie?page={i}')


    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('ul', class_='switch-block list-episode-item')
    movie_title = s.find_all('h3')
    sub_type = s.find_all('span', class_=["type RAW", "type SUB"])
    realise_time = s.find_all('span', class_="time")


    for i in range(len(movie_title)):
        dic = {
            "Title": movie_title[i].text,
            "Subtitle": sub_type[i].text,
            "Realise Time": realise_time[i].text
        }

        data.append(dic)


df = pd.DataFrame(data)
df.to_csv('D:\Python Study\FDS\Web Scrapping\daramacool_movies.csv')

print("Task Completed!!!")


