from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import pandas as pd

ua = UserAgent()
#defining headers reduces chances of getting blocked by the website
#user-agent can be fake/random
obj = {}
arr = []

headers = {"User-Agent": "ua.random"}
url = 'https://www.flipkart.com/samsung-galaxy-s21-fe-5g-graphite-128-gb/p/itm7be0f72fff180?pid=MOBGBPFZSPRG8GSU&param=312132888881&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJpbmNsIG9mIG9mZmVycyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNhbXN1bmcgUzIxIEZFIDIwMjMgNUciXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJNT0JHQlBGWlNQUkc4R1NVIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fX19fQ%3D%3D'
response = requests.get(url, headers = headers).text
soup = BeautifulSoup(response, 'html.parser')

obj["name"] = soup.find("span",{"class":"B_NuCI"}).text

obj["price"] = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).text

obj["rating"] = soup.find("div",{"class":"_3LWZlK"}).text

obj["review_count"] = soup.find("span",{"class":"_2_R_DZ"}).find("span").text

arr.append(obj)
df = pd.DataFrame(arr)
df.to_csv('flipkart_data.csv', index = False, encoding = 'utf-8')
print(arr)
