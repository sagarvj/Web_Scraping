from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": UserAgent().random}
url = 'https://www.netflix.com/in/title/80057281'
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, 'html.parser')

l = []

episodes = soup.find("ol", {"class": "episodes-container"}).find_all("li")
for i in range(0, len(episodes)):
    o = {}
    o["name"] = soup.find("h1", {"class": "title-title" }).text
    o["seasons"] = soup.find("span", {"class": "test_dur_str" }).text
    o["about"] = soup.find("div", {"class": "hook-text" }).text
    o["episode-title"] = episodes[i].find("h3", {"class":"episode-title"}).text
    o["episode-description"] = episodes[i].find("p", {"data-uia":"episode-synopsis"}).text
    
    
    o["genres"] = []
    o["mood"] = []

    
    genres = soup.find_all("span", {"class": "item-genres"})
    for x in range(0, len(genres)):
        o["genres"].append(genres[x].text.replace(",", ""))

    
    mood = soup.find_all("span", {"class":"item-mood-tag"})
    for y in range(0, len(mood)):
        o["mood"].append(mood[y].text.replace(",", ""))

    o["facebook"] = soup.find("a",{"data-uia":"social-link-facebook"}).get("href")
    o["twitter"] = soup.find("a",{"data-uia":"social-link-twitter"}).get("href")
    o["instagram"] = soup.find("a",{"data-uia":"social-link-instagram"}).get("href")

    
    cast = soup.find_all("span",{"class":"item-cast"})
    o["cast"] = []
    for t in range(0, len(cast)):
        o["cast"].append(cast[t].text)

    l.append(o)

df = pd.DataFrame(l)
df.to_excel('Netflix_data.xlsx', index=False)

#if csv is not required then remove the following code. 
df.to_csv('Netflix_data.csv', index=False)
