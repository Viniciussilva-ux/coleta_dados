import pandas
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
print('requests: ')
response = requests.get('https://finance.yahoo.com/quote/%5EBVSP/', headers = headers)
print(response.text[:600])

print('BeautifulSoup: ')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

print('pandas: ')
url_dados = pandas.read_html('https://finance.yahoo.com/quote/%5EBVSP/')
print(url_dados[0].head(10))
