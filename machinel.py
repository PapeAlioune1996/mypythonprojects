"""import requests

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# Voir le code html source
print(page.content)"""
import requests

from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
soup.title.string