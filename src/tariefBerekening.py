# Berekening van de maandfactuur op basis van verbruik en productiegegevens van afgelopen maand alsook de gemiddelde maandpiek

import vastTariefGetter
import gemiddeldeMaandpiekBerekening
import variabelTariefGetter

# de variabelen
postcode = 9052 # zal ingegeven worden door de gebruiker -> om capaciteitstarief te bepalen
verbruik = 0 # zal aan sensor gekoppeld worden 
productie = 0 # zal aan sensor gekoppeld worden
maandpiek = gemiddeldeMaandpiekBerekening.getGemiddeldeMaandpiek()
vastTarief = vastTariefGetter.getAfnameTarief()
variabelTarief = variabelTariefGetter.getVariabelTarief()
terugleverTarief = vastTariefGetter.getTerugleverTarief()
capaciteitsTarief = 39.4068693 # op basis van postcode bepalen - zoeken naar api die dit kan ophalen (voorlopig ingesteld op imewo)
maximumTarief = 0.1920264
minimumTarief = 0 # bepalen aan de hand van minimum maandpiek van 2.5kw 
databeheerTarief = 13.16 # per jaar - zoeken naar api die dit kan ophalen
afnameTarief = 0
energieBijdrageTarief = 0.0019261 # zoeken naar api die dit kan ophalen
accijnzenTarief_0_3000 = 0.04748 # zoeken naar api die dit kan ophalen
accijnzenTarief_3000_20000 = 0.04748 # zoeken naar api die dit kan ophalen
accijnzenTarief_20000_50000 = 0.04546 # zoeken naar api die dit kan ophalen
accijnzenTarief_50000 = 0.04478 # zoeken naar api die dit kan ophalen
btwTarief = 0.06 

# energiekosten
def energiekosten(verbruik, productie, vastTarief, variabelTarief, terugleverTarief, btwTarief):
    vast = ((verbruik/2) * vastTarief) * (1 + btwTarief)
    variabel = ((verbruik/2) * variabelTarief) * (1 + btwTarief)
    teruglever = productie * terugleverTarief

    return (vast + variabel) - teruglever


def netkosten(verbruik, maandpiek, capaciteitsTarief, databeheerTarief, afnameTarief, maximumTarief, minimumTarief, btwTarief):
    # de totale netkosten hebben een maximum en minimum tarief
    
    # berekening van de netkosten
    capaciteitEx = (maandpiek * capaciteitsTarief) / 12
    databeheerEx = databeheerTarief / 12
    afnameEx = verbruik * afnameTarief

    # maximumtarief controleren
    if ((capaciteitEx + databeheerEx + afnameEx)/verbruik) > maximumTarief:
        return maximumTarief * verbruik
    
    # minimumtarief controleren
    if capaciteitEx + databeheerEx + afnameEx < minimumTarief:
        return minimumTarief

    return pasBTWToe(capaciteitEx, btwTarief) + pasBTWToe(databeheerEx, btwTarief) + pasBTWToe(afnameEx, btwTarief)


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
    

def bepaalMinimumTarief(capaciteitsTarief):
    # minimumtarief is een maandpiek van 2.5 kwh
    return 2.5 * capaciteitsTarief

def pasBTWToe(bedrag, btwTarief):
    return bedrag * (1 + btwTarief)
    

# formule
energiekost = energiekosten(verbruik, productie, vastTarief, variabelTarief, terugleverTarief, btwTarief)
netkost = netkosten(verbruik, maandpiek, capaciteitsTarief, databeheerTarief, afnameTarief, maximumTarief, bepaalMinimumTarief(capaciteitsTarief))
heffing = heffingen(verbruik, energieBijdrageTarief, bepaalAccijnzenTarief(verbruik))

totaal = energiekost + netkost + heffing







