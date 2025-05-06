import requests
from bs4 import BeautifulSoup
import pandas as pd


r = requests.get('https://www.startech.com.bd/laptop-notebook')

print("Scrapping Page:1......")
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

base_class = soup.find('div', class_="main-content p-items-wrap")
items = base_class.find_all('div', class_="p-item")

data = []

for product in items:
    model = product.find('h4', class_="p-item-name").text.strip()
    try:
        price = int(product.find('span', class_="price-old").text.replace(',','').strip('৳'))
    except:
        try:
                base = product.find('div', class_="p-item-price")
                price = int(base.find('span').text.replace(',','').strip('৳'))
        except:
            base = product.find('div', class_="p-item-price")
            price = base.find('span').text
            
    link = product.find('a').get('href')

    data.append({
        "Model": model,
        "Price": price, 
        "Link" : link
    })

page_num = 15

for i in range(2,page_num+1):
    print(f"Scrapping Page:{i}......")
    r = requests.get(f'https://www.startech.com.bd/laptop-notebook?page={i}')


    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    base_class = soup.find('div', class_="main-content p-items-wrap")
    items = base_class.find_all('div', class_="p-item")

    for product in items:
        model = product.find('h4', class_="p-item-name").text.strip()
        try:
            price = int(product.find('span', class_="price-old").text.replace(',','').strip('৳'))
        except:
            try:
                base = product.find('div', class_="p-item-price")
                price = int(base.find('span').text.replace(',','').strip('৳'))
            except:
                base = product.find('div', class_="p-item-price")
                price = base.find('span').text

        link = product.find('a').get('href')

        data.append({
            "Model": model,
            "Price": price, 
            "Link" : link
        })



    

df = pd.DataFrame(data)
df.to_csv("D:\Python Study\FDS\Web Scrapping\Phone Price\Star_tech_dataseet.csv", index=False)

print("Task Completed!!!")