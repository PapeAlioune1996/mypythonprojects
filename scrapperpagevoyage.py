from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

#les constantes
NB_ANNONCE_MAX = 50
EXPORT_PATH = "./exports/"


# connecter à la page avec selenium
url = "https://www.pretapartir.fr/recherche#!/search?th=SJ&sort=promo_desc&depart=A_PAR&f=3_AL&dureeNuit=7-99"
chrome_options = Options()
#chrome_options.add_argument('headless')

#creer un navigateur


browser = webdriver.Chrome( options=chrome_options)
browser.get(url)

#attendre 5s
time.sleep(2)

# recupere le nombre de resultats de la recherche
soup = BeautifulSoup(browser.page_source, "html.parser")

nb_elements = int(soup.find("h1").find("strong").get_text(strip=True))

# definir le nombre annonce à effectuer
nb_click = NB_ANNONCE_MAX / 10 - 1 if nb_elements >= NB_ANNONCE_MAX else nb_elements/10

#print(nb_click)

for i in range(0, int(nb_click)):
    button_next_10 = browser.find_element("css selector","a[ng-click='vm.loadMorePackage()']")
    #button_next_10.click()
    browser.execute_script("arguments[0].click()", button_next_10)
    time.sleep(2)

soup = BeautifulSoup(browser.page_source, "html.parser")

#fermer le navigateur
browser.quit()


def clean_text(str):
    return str.replace("\n","").replace("\t","")
# recuper les items

items = soup.find_all("div", {"class":"blocProduct-wrapper"})
#print(len(items))

# recuperer les informations de tous les items
#stocker tous sous forme de dictionnaire
voyages = []
for item in items:
    pays = clean_text(item.find("p",{"class":"blocProduct-place"}).get_text(strip=True))
    pays =  re.sub('[ ]{1,}-',' -', pays)
    #print(paysfinal)
    hotel = item.find("p",{"class":"blocProduct-title"}).text.strip()
    details = item.find("div",{"class":"blocProduct-detail"}).findChildren()
    
    duree = details[0].get_text()
    date = details[1].get_text()
    price = item.find("div",{"class":"blocProduct-price"}).findChildren()
    prices = price[1].get_text()
    

    voyage = {
        "pays" : pays,
        "hotel" : hotel,
        "duree" : duree,
        "price" : prices
    }

    voyages.append(voyage)

#print(voyages)

# exporter kes donnees sur excel

df = pd.DataFrame(voyages)
df.to_excel(EXPORT_PATH + "mes_vacances.xlsx", index=False)

    


