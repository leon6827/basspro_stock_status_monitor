import requests
from bs4 import BeautifulSoup

URL = 'https://www.basspro.com/shop/en/winchester-usa-handgun-ammo'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='fullView')
#print(results.prettify())

sku_elems = results.find_all('a', string='Add to Cart')
print(sku_elems)
#for sku_elem in sku_elems:
#    print(sku_elem, end='\n'*2)
