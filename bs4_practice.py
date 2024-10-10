import bs4.builder
import requests
from bs4 import BeautifulSoup
#######

url = 'http://localhost:8080/'

# DOWNLOAD HTML OF PAGE.
response = requests.get(url)
raw_html = response.content

# WORKING WITH BS4
parse_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

parser_my_site= parse_html.select_one('#main-header > div.main-header-content > p')
print(parser_my_site.text) # type: ignore


