# this script returns text content within html tag
import requests
from bs4 import BeautifulSoup

# ask the website for its HTML
url = 'https://www.fernandomc.com/posts/dynamodb-key-terms-explained/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'lxml')
content = soup.find_all("div", class_="entry-content")

# print the text to the console
for el in content:
    print(el.text)

# save the content as .txt
txt = ''
for el in content:
    txt += str(el.text)
with open('file_to_save.txt', 'w') as open_file:
    open_file.write(txt)