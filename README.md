# homeAssistant-ecopower
Het berekenen van de energiefactuur voor elektriciteit is behoorlijk complex in vlaanderen, en wordt steeds complexer. De invoering van het capaciteitstarief, zonneproductie, netkosten,... 
Deze integratie probeert een inschatting te maken van de energiefactuur per maand op basis van de tarieven gehanteerd door ecopower.

Het heeft volgende gegevens nodig van de gebruiker:
    - postcode

Het heeft toegang nodig tot volgende gegevens:
    - p1 meter
        - Verbruik tarief 1
        - Verbruik tarief 2
        - Productie tarief 1
        - Productie tarief 2
        - Gemiddelde maandpiek

Het haalt volgende gegevens op:
    - variabel tarief
        - variabele belpex tarieven afgelopen maand
    
    - vast tarief voor de vorige maand (ecopower website)

Volgende gegevens zijn 'hardcoded'
    - RPL profiel
    - Nettarieven (nog op te lijsten)
    - Databeheer tarief
