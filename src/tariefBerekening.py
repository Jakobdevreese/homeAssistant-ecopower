# Berekening van het tarief

import vastTariefGetter

# de variabelen
verbruik = 0 # zal aan sensor gekoppeld worden 
productie = 0 # zal aan sensor gekoppeld worden
maandpiek = 0 # zal aan sensor gekoppeld worden
vastTarief = vastTariefGetter.getAfnameTarief()
terugleverTarief = vastTariefGetter.getTerugleverTarief()
capaciteitsTarief = 0
maximumTarief = 0
minimumTarief = 0
databeheerTarief = 0
afnameTarief = 0
energieBijdrageTarief = 0.0019261
accijnzenTarief_0_3000 = 0.04748
accijnzenTarief_3000_20000 = 0.04748
accijnzenTarief_20000_50000 = 0.04546
accijnzenTarief_50000 = 0.04478
btwTarief = 0.06 

# energiekosten
def energiekosten(verbruik, productie, vastTarief, terugleverTarief):
    vast = verbruik * vastTarief
    teruglever = productie * terugleverTarief

    return vast - teruglever

def netkosten(verbruik, maandpiek, capaciteitsTarief, databeheerTarief, afnameTarief, maximumTarief, minimumTarief):
    # de totale netkosten hebben een maximum en minimum tarief
    
    # berekening van de netkosten
    capaciteit = (maandpiek * capaciteitsTarief) / 12
    databeheer = databeheerTarief / 12
    afname = verbruik * afnameTarief

    # maximumtarief controleren
    if ((capaciteit + databeheer + afname)/verbruik) > maximumTarief * verbruik:
        return maximumTarief * verbruik
    
    # minimumtarief controleren
    if capaciteit + databeheer + afname < minimumTarief:
        return minimumTarief

    return capaciteit + databeheer + afname


def heffingen(verbruik, energieBijdrageTarief, accijnzenTarief):
    bijdrage = verbruik * energieBijdrageTarief
    accijnzen = verbruik * accijnzenTarief

    return bijdrage + accijnzen

def bepaalAccijnzenTarief(verbruik):
    if verbruik <= 3000:
        return accijnzenTarief_0_3000
    elif verbruik <= 20000:
        return accijnzenTarief_3000_20000
    elif verbruik <= 50000:
        return accijnzenTarief_20000_50000
    else:
        return accijnzenTarief_50000

# formule
totalePrijsExcBtw = energiekosten(verbruik, productie, vastTarief, terugleverTarief) + netkosten(verbruik, maandpiek, capaciteitsTarief, databeheerTarief, afnameTarief, maximumTarief, minimumTarief) + heffingen(verbruik, energieBijdrageTarief, bepaalAccijnzenTarief(verbruik)) 
totalePrijsIncBtw = totalePrijsExcBtw * (1 + btwTarief)






