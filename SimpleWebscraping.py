from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_largest_banks'
url_data=requests.get(url)
html_data=url_data.text

print(html_data[101:124])

soup=BeautifulSoup(html_data)

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[3].find_all('tr'):
    col = row.find_all('td')
    for td in col:
        try:
            data.append(td.text.replace('\n', ''))
        except:
            continue

print(data.head())
