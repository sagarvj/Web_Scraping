import requests
from bs4 import BeautifulSoup
from word2number import w2n
import pandas as pd

Books = []
for i in range(1,51):
    url = f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html"
    res = requests.get(url)
    re = res.content
    soup = BeautifulSoup(re, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_ = 'product_pod')
    for article in articles:
        title = article.find('img')
        title = title.attrs['alt']
        rating = article.find('p')
        rating = rating['class'][1]
        star = w2n.word_to_num(rating)
        price = article.find('p',class_= 'price_color').text
        price = float(price[1:])
        Books.append([title,star,price])

df = pd.DataFrame(Books, columns = ['Title','Rating','Price'])
df.to_csv('Scraped_books.csv')