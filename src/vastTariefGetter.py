# Prijs voor afname en teruglevering van ecopower ophalen

import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.ecopower.be/groene-stroom/prijs-nieuw"

maand_mapping = {
        'January': 'JANUARI',
        'February': 'FEBRUARI',
        'March': 'MAART',
        'April': 'APRIL',
        'May': 'MEI',
        'June': 'JUNI',
        'July': 'JULI',
        'August': 'AUGUSTUS',
        'September': 'SEPTEMBER',
        'October': 'OKTOBER',
        'November': 'NOVEMBER',
        'December': 'DECEMBER'
    }

def getPrijzenText():

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.find_all('strong')




def getAfnameTarief():

    prijzen = getPrijzenText()
    huidigeMaand = maand_mapping[datetime.now().strftime('%B')]
    afname_prijs = None

    for prijs in prijzen:
        text = prijs.get_text(strip=True)
        if f"AFNAMEPRIJS {huidigeMaand}" in text:
            afname_prijs = text.split(": ")[1]
    
    return afname_prijs

def getTerugleverTarief():
    
    prijzen = getPrijzenText()
    teruglever_prijs = None

    for prijs in prijzen:
        text = prijs.get_text(strip=True)
        if "TERUGLEVERPRIJS" in text:
            teruglever_prijs = text.split(": ")[1]
        
    return teruglever_prijs

