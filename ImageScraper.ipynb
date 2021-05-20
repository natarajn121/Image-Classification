import os

import requests
from bs4 import BeautifulSoup

link = requests.get('https://in.pinterest.com/divs17rathore/mahesh-babu/')
soup = BeautifulSoup(link.content, 'html.parser')
images = soup.findAll('img')
print(len(images))
count = 0

try:
    folder_name = input('Enter Folder Name: ')
    os.mkdir(folder_name)
except:
    print("Folder Exists with that Name")

if len(images) !=0:
    for i, item in enumerate(images):
        image_link = item['src']
        try:
            r = requests.get(image_link).content
            try:
                r = str(r, 'utf-8')
            except UnicodeDecodeError:
                with open(f"{folder_name}/images{i+1}.jpg", "wb") as f:
                    f.write(r)

                    count += 1
        except:
            pass

    if count == len(images):
        print("All images are downloaded")
    else:
        print(f"{count} files are downloaded out of {len(images)}")
