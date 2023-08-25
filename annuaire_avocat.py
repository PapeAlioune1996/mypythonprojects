from bs4 import BeautifulSoup
import requests

import re

"""extraire les donnée"""
def get_allpages():
    urls = []
    page_number = 1
    for i in range(104):
        i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={page_number}"
        page_number+=1
        urls.append(i)

    return urls

"""extraire les avocats"""
def parse_avocat(url):
    r = requests.get("https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=1")
    soup = BeautifulSoup(r.content, "html.parser")
    
    avocats = soup.find_all('div', class_ = 'callout secondary annuaire-single')

    """extraire le element"""
    for avocat in avocats:
        try:
            nom = avocat.find('h3').text.strip()
        except AttributeError as e:
            nom = ""
        
        adresse = avocat.find('span', class_="adresse").text.strip()
        """utiluse les regex"""
        try:
            adressefinal =  re.sub(r"\s+", " ", adresse)
        except AttributeError as e:
            adressefinal = ""
        try:
            telephone = avocat.find('span', class_="telephone").text.strip()
        except AttributeError as e:
            telephone = ""
        try:
            email = avocat.find('span', class_="email").a.text.strip()
        except AttributeError as e:
            email = ""
        """sauvegarder les donner dans un fichier texte"""
        chemin = r"C:\Users\DELL\Desktop\MyPythonExercises\attoney_file.txt"
        with open(chemin, 'a') as f:
            f.write(f"{nom}\n")
            f.write(f"{adressefinal}\n")
            f.write(f"{telephone}\n")
            f.write(f"{email}\n\n")
            """formater le fichier"""


def parse_all_avocats():
    pages = get_allpages()
    for page in pages:
        parse_avocat(url=page)
        print(f"Je scrape + {page}")

parse_all_avocats()