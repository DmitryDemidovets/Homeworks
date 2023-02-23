#парсинг
import requests
from bs4 import BeautifulSoup as bs

url = "https://quotes.toscrape.com/"
responce = requests.get(url)
soup = bs(responce.text, "lxml")
spans = soup.find.all('span', class_="text" )
author = soup.find.all('small', class_="author" )

with open('results.txt', 'w+') as res:
    for i in spans:
        res.write(i.text + "\n")




#author = soup.find_all('small', class_='author')
#for row in author:
    #print(row.get_text())