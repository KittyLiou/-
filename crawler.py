import requests
from bs4 import BeautifulSoup

query_link = 'http://www.hm.com/us/products/search?q=romper'
res = requests.get(query_link)
soup = BeautifulSoup(res.text, "html.parser")
for price in soup.select('.price'):
    print(price.text) 