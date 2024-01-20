import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

url = 'https://indepest.com/2024/01/09/suicided-by-society/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

output_folder = '/Users/sagarvijay/Desktop/downloaded_images'
os.makedirs(output_folder, exist_ok=True)

for img_tag in img_tags:
    img_url = img_tag.get('src')
    if img_url:
        img_url = urljoin(url, img_url)

    
        img_name = os.path.join(output_folder, os.path.basename(urlparse(img_url).path))

        with open(img_name, 'wb') as img_file:
            img_file.write(requests.get(img_url).content)

        print(f"Downloaded: {img_name}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
