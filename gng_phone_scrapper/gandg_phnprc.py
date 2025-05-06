# import requests
# from bs4 import BeautifulSoup
# import pandas as pd


# r = requests.get('https://gadgetandgear.com/category/phone')


# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')

# base_class = soup.find('div', class_="ProductList_productRow__Q4VMB")
# # base_class = soup.find_all('p', class_="ProductCard_CardPriceTag__SRo_X ProductCard_cardPriceTag__3nqTU")


# # product_row = base_class.find_all('div', class_="ProductList_productRow__Q4VMB")
# # product_card = product_row.find('div', class_="ProductCard_ProductCard___Lbvt ProductCard_sm__BA3zF")
# # product_card2 = product_card.find('div', class_="ProductCard_cardBody__8nPmw")
# model = base_class.find_all('h4').text

# print(model)
# # print(product_card)
# # print(soup)


import requests
from bs4 import BeautifulSoup
import pandas as pd


r = requests.get('https://www.startech.com.bd/lenovo-laptop')

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

    data.append({
        "Model": model,
        "Price": price
    })

page_num = 7

for i in range(2,page_num+1):
    print(f"Scrapping Page:{i}......")
    r = requests.get(f'https://www.startech.com.bd/lenovo-laptop?page={i}')


    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    base_class = soup.find('div', class_="main-content p-items-wrap")
    items = base_class.find_all('div', class_="p-item")

    for product in items:

        link = product.find('a').get('href')

        individual_product = requests.get(f'{link}')
        soup = BeautifulSoup(individual_product.content, 'html.parser')

        