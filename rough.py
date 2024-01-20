import requests
from bs4 import BeautifulSoup
import pandas as pd
l=list()
o={}
e={}
d={}
m={}
c={}

target_url="https://www.netflix.com/in/title/80057281"
resp = requests.get(target_url)

soup = BeautifulSoup(resp.text, 'html.parser')

o["name"]=soup.find("h1", {"class":"title-title"}).text

o["seasons"] = soup.find("span", {"class":"duration"}).text

o["about"] = soup.find("div", {"class":"hook-text"}).text
l.append({**o})

episodes = soup.find("ol",{"class":"episodes-container"}).find_all("li")

for i in range(0,len(episodes)):

    e["episode-title"]=episodes[i].find("h3",{"class":"episode-title"}).text
    e["episode-description"]=episodes[i].find("p",{"class":"epsiode-synopsis"}).text
    l.append({**e})
    e={}

genres = soup.find_all("span",{"class":"item-genres"})
for x in range(0,len(genres)):
  d["genre"]=genres[x].text.replace(",","")
  
  d={}

mood = soup.find_all("span",{"class":"item-mood-tag"})
for y in range(0,len(mood)):
  m["mood"]=mood[y].text.replace(",","")
  
  m={}

o["facebook"]=soup.find("a",{"data-uia":"social-link-facebook"}).get("href")
o["twitter"]=soup.find("a",{"data-uia":"social-link-twitter"}).get("href")
o["instagram"]=soup.find("a",{"data-uia":"social-link-instagram"}).get("href")

cast=soup.find_all("span",{"class":"item-cast"})
for t in range(0,len(cast)):
  c["cast"]=cast[t].text
  c={}
l.append({**e, **d, **m,**c})
print(l)
df = pd.DataFrame(l)
df.to_csv('Data.csv',index = False)