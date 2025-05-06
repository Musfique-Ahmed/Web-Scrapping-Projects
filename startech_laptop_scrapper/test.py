import requests
from bs4 import BeautifulSoup

product_spec = {}

url = "https://www.startech.com.bd/lenovo-ideapad-1-15amn7-ryzen-5-7520u-fhd-laptop"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)
base_class = soup.find('table', class_="data-table flex-table")
# print(base_class)
tbodys = base_class.find_all('tbody')

for tbody in tbodys:
    trs = tbody.find_all('tr')
    for tr in trs:
        key = tr.find('td', class_="name").text
        value = tr.find('td', class_="value").text
        product_spec[key] = value

print(product_spec)