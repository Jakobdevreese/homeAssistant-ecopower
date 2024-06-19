# Berekening van het tarief

# de variabelen
vastTarief = 0
terugleverTarief = 0
capaciteitsTarief = 0
databeheerTarief = 0
afnameTarief = 0
energieBijdrageTarief = 0
accijnzenTarief = 0
btwTarief = 0.06 

# energiekosten
def energiekosten(verbruik, productie, vastTarief, terugleverTarief):
    vast = verbruik * vastTarief
    teruglever = productie * terugleverTarief

    return vast - teruglever

def netkosten(verbruik, maandpiek, capaciteitsTarief, databeheerTarief, afnameTarief):
    capaciteit = (maandpiek * capaciteitsTarief) / 12
    databeheer = databeheerTarief / 12
    afname = verbruik * afnameTarief

    return capaciteit + databeheer + afname

def heffingen(verbruik, energieBijdrageTarief, accijnzenTarief):
    bijdrage = verbruik * energieBijdrageTarief
    accijnzen = verbruik * accijnzenTarief

    return bijdrage + accijnzen

# formule
totalePrijsExcBtw = energieKosten(verbruik, productie, vastTarief, terugleverTarief) + netkosten(verbruik, maandpiek, capaciteitsTarief, databeheerTarief, afnameTarief) + heffingen(verbruik, energieBijdrageTarief, accijnzenTarief) 
totalePrijsIncBtw = totalePrijsExcBtw * (1 + btwTarief)






