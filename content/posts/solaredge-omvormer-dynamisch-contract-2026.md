---
title: SolarEdge Omvormer + Dynamisch Contract 2026
date: 2026-10-18 08:00:00+02:00
lastmod: 2026-08-21 08:00:00+02:00
draft: false
description: "SolarEdge omvormer combineren met een dynamisch contract (Tibber of Frank Energie)? Tijdgestuurd laden, peak shaving en smart EV — en voor wie de meerprijs zich niet terugverdient."
categories:
- zonnepanelen
tags:
- SolarEdge
- omvormer
- dynamisch contract
- Tibber
- Frank Energie
- peak shaving
keywords:
- solaredge dynamisch contract
- solaredge tibber
- solaredge frank energie
- solaredge home battery
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1559302504-64aae6ca6b6d&w=1200&output=webp&q=70
faq:
- q: Werkt SolarEdge automatisch samen met Tibber?
  a: 'Nee, er is geen native Tibber-knop in de mySolarEdge-app. Wat wél kan: tijdgestuurde profielen handmatig instellen, of sturen via het betaalde SolarEdge-cloudabonnement, of Home Assistant als tussenlaag gebruiken die de prijzen ophaalt en de omvormer via Modbus aanstuurt. Die laatste route is de populairste onder gebruikers die het zelf inrichten.'
- q: Wat kost een SolarEdge-omvormer in 2026?
  a: 'SolarEdge publiceert geen consumentenprijzen; het merk wordt via installateurs en groothandels verkocht en de straatprijs verschilt per kanaal en per week. Wat structureel geldt: een SolarEdge-set met optimizers per paneel ligt boven een vergelijkbare string-omvormer zonder optimizers, omdat je per paneel hardware bijkoopt. Vraag drie offertes met dezelfde paneelconfiguratie en vergelijk die.'
- q: Is de SolarEdge Home Battery beter dan een losse thuisbatterij voor dynamisch laden?
  a: 'Ze doen iets anders. De SolarEdge-batterij is DC-gekoppeld aan de eigen omvormer, wat één omzetstap scheelt en de installatie tot één systeem met één garantieloket maakt. Losse batterijen zijn AC-gekoppeld en daarmee merkonafhankelijk, wat meer keuzevrijheid geeft in de sturing. Wil je één pakket van één merk, dan is SolarEdge logisch; wil je vrij blijven, dan niet.'
- q: Wat is peak shaving precies?
  a: 'Peak shaving is het afvlakken van je piekafname uit het net. Bij een dynamisch contract met dure ochtend- en avonduren laat je de batterij die uren overbruggen, zodat je alleen in de goedkope uren afneemt. Wat het oplevert is je afgevlakte kWh × het prijsverschil tussen piek en dal; dat verschilt per dag en per seizoen, en laat zich niet in één jaarbedrag vangen.'
- q: Werkt SolarEdge met Home Assistant?
  a: 'Ja, via Modbus TCP of via de officiële SolarEdge-integratie. Voor monitoring werkt dat goed. Voor sturen op prijs heb je ofwel de lokale Modbus-route ofwel het betaalde SolarEdge-cloudabonnement nodig; de actuele prijs en voorwaarden daarvan staan op solaredge.com.'
- q: Kun je een dynamisch contract op een bestaande SolarEdge gebruiken?
  a: 'Ja, elke omvormer werkt met een dynamisch contract — je omvormer bepaalt niet je tariefvorm. De winst zit in sturing: laden en ontladen op prijs. Zonder batterij blijft alleen het verschuiven van wasmachine, droger en EV-laden over, en daar heb je geen SolarEdge voor nodig.'
- q: 'Heeft het zin als ik nog saldering heb?'
  a: 'Financieel niet. Tot 1 januari 2027 krijg je voor teruglevering hetzelfde tarief als voor afname, dus batterij-arbitrage kost je per saldo rendement en cyclusslijtage. De saldering stopt daarna volledig, zonder afbouwpad. Overweeg dus de omvormer nu en de batterij vanaf het moment dat teruglevering minder waard wordt. Ons overzicht [dynamische energiecontracten vergelijking](/posts/dynamische-energiecontracten-vergelijking-2026/) gaat hier dieper op in.'
schema_type: Article
last_updated: '2026-08-21'
---

Een veelvoorkomende situatie: veertien panelen op het zuiddak, een SolarEdge-omvormer en een dynamisch contract — en toch een besparing die achterblijft bij de verwachting. Leg de productiecurve naast de uurtarieven en het patroon is meteen zichtbaar: de omvormer levert keurig terug rond het middaguur, precies wanneer de beursprijs op zijn laagst staat, terwijl de EV in de avondspits laadt tegen het duurste tarief van de dag. Het gat zit niet in de hardware maar in de instellingen.

*Disclosure: wij hebben geen affiliate- of commissierelatie met Tibber, Frank Energie, Sessy of Zonneplan (stand augustus 2026); de links naar deze partijen zijn gewone verwijzingen en wij ontvangen daar geen vergoeding voor. Wij hebben deze systemen niet zelf geïnstalleerd of doorgemeten: dit artikel is gebaseerd op fabrikantendocumentatie, publieke marktdata en narekenbare modellen.*

---

> **Kort antwoord:** SolarEdge plus een dynamisch contract loont bij een fors jaarverbruik in combinatie met een EV of warmtepomp. Bij een klein verbruik verdien je de meerprijs van optimizers per paneel niet terug.
>
> En de belangrijkste nuance: zolang je saldeert, levert batterij-arbitrage niets op. De rekensom verandert pas zodra de saldering per 1 januari 2027 stopt.

## Waarom SolarEdge populair is bij dynamisch-contract-gebruikers

SolarEdge heeft één eigenschap die bij een dynamisch contract goed uitpakt: power optimizers per paneel. Elk paneel heeft zijn eigen MPPT-tracker, wat betekent dat schaduw op één paneel niet de hele string platlegt.

Wat dat waard is, laat zich als volgt uitrekenen: het verschil in jaaropbrengst tussen mét en zonder optimizers, maal je gemiddelde kWh-waarde. Bij een rijtjeswoning met een schoorsteen of een boom die een deel van de dag schaduw geeft, kan dat verschil in de orde van enkele honderden kWh per jaar liggen. Laat je installateur dat verschil voor jouw dak doorrekenen met een schaduwsimulatie — dat is de enige manier om te weten of de meerprijs zinvol is.

De tweede reden is het ecosysteem. SolarEdge maakt niet alleen omvormers maar ook batterijen, EV-laders en de hub die alles aanstuurt. Voor wie op tarief wil sturen, betekent dat één app, één installatie en één garantieloket.

SolarEdge en Huawei zijn samen goed voor een groot deel van het Nederlandse segment van installaties met twaalf panelen of meer. Een vergelijking met de alternatieven staat in ons [overzicht van de beste omvormers voor 2026](/posts/beste-omvormer-zonnepanelen-2026/) en in de directe [Huawei vs SolarEdge vergelijking](/posts/huawei-vs-solaredge-omvormer-2026/).

## Hoe werkt de integratie met Tibber en Frank Energie?

Eerst een misverstand uit de wereld helpen: **SolarEdge heeft geen native koppeling met Tibber of Frank Energie**. Wie verwacht dat hij in de app op een knop drukt en klaar is, komt bedrogen uit. De integratie verloopt op drie manieren:

1. **Handmatige tijdprofielen in mySolarEdge** — je stelt zelf in welke uren de batterij laadt of ontlaadt. Werkt prima zolang je tariefpatroon voorspelbaar is: nacht goedkoop, avondspits duur.
2. **Het betaalde SolarEdge-cloudabonnement** — daarmee kan de hub prijsdata ophalen en daarop sturen. De ondersteunde leveranciers en de actuele prijs van dat abonnement staan op solaredge.com; controleer dat vóór je erop rekent, want die lijst verandert.
3. **Home Assistant als tussenlaag** — de populairste route onder gebruikers die het zelf inrichten. Je haalt de prijzen binnen via de integratie van je leverancier, schrijft die naar de SolarEdge Modbus-registers, en de omvormer doet de rest.

In de praktijk kiezen mensen die zelf willen tinkeren voor route 3, en mensen die het uit handen willen geven voor route 2. Welke leverancier voor jou voordeliger is, leggen wij uit in [Frank Energie vs Tibber](/posts/frank-energie-vs-tibber-2026/) en het uitgebreide [Frank Energie review](/posts/frank-energie-review-ervaringen-2026/).

<a href="https://go.duurzaamthuislab.nl/tibber" class="cta cta-affiliate" rel="noopener nofollow" target="_blank">Bekijk Tibber</a> (gewone verwijzing, wij ontvangen hiervoor geen vergoeding)

## Tijdgestuurd laden via mySolarEdge

SetApp is de installateursapp van SolarEdge — die zie je waarschijnlijk nooit. mySolarEdge is de consumentenapp, en daar gebeurt het werk. Onder **Batterij** → **Werkmodus** → **Aangepast schema** stel je tijdvensters in met drie opties:

- **Maximize self-consumption** — standaardmodus, de batterij laadt uit zon
- **Time of Use** — handmatige tijdsturing op tarief
- **Charge from grid** — actief laden uit het net

Een werkbare indeling in vier vensters, als startpunt:

| Uur | Modus | Reden |
|---|---|---|
| 00:00-06:00 | Charge from grid | Nachttarief is doorgaans het laagst |
| 06:00-11:00 | Maximize self-consumption | Ochtendzon, eigen verbruik |
| 11:00-15:00 | Maximize self-consumption | Piekproductie |
| 15:00-22:00 | Discharge to load | Avondspits |

**Wat dat oplevert, is een rekensom en geen belofte.** De rekenregel: je netto-afname in kWh × het verschil tussen je gemiddelde inkoopprijs vóór en ná het instellen van de vensters. Daalt je gemiddelde inkoopprijs bijvoorbeeld met tien cent per kWh over een netto-afname van 4.000 kWh, dan is dat €400 per jaar. Vul je eigen afname en je eigen tariefblad in; de uitkomst verschilt sterk per huishouden en per seizoen.

Wil je zelf zo'n schema bouwen? Ons [rekenmodel voor dynamisch contract met batterij](/posts/dynamisch-contract-met-batterij-rekenmodel-2026/) helpt bij het bepalen van de vensters op basis van je verbruik en de EPEX-spreads.

## SolarEdge Home Battery en peak shaving

De SolarEdge-thuisbatterij is DC-gekoppeld aan de eigen omvormer. Dat betekent dat er bij ontladen één omzetstap minder nodig is dan bij een AC-gekoppelde batterij, wat het rendement ten goede komt. Hoe groot dat verschil precies is, publiceren de fabrikanten niet op een vergelijkbare manier; verwacht een verbetering van enkele procentpunten, geen sprong.

Consumentenprijzen voor de batterij publiceert SolarEdge niet. Vraag die op in een offerte, samen met de omvormer, zodat je het systeem als geheel kunt vergelijken.

Peak shaving is bij een dynamisch contract de belangrijkste functie. De rekenregel: het aantal kWh dat je uit de dure uren weghaalt × het verschil tussen het piektarief en het tarief waartegen de batterij geladen is, minus het rendementsverlies van de opslag.

Wat je daarbij realistisch moet aannemen: het duurste uur op de Nederlandse day-ahead-markt kwam in 2025 uit op €0,63/kWh, op 20 januari om 17:00. Uurprijzen boven de 80 cent zijn dus geen routine maar uitzondering, en een model dat daarop rekent, komt structureel te gunstig uit. Reken liever met de daadwerkelijke spreads van het afgelopen jaar: het jaargemiddelde lag in 2025 op €0,105/kWh, met 212 uren waarin de prijs negatief was.

De vergelijking met andere batterijen staat in [Sessy vs Marstek](/posts/sessy-vs-marstek-thuisbatterij-2026/) en het overzicht [thuisbatterij prijzen](/posts/thuisbatterij-prijzen-vergelijking-2026/).

<a href="https://go.duurzaamthuislab.nl/sessy" class="cta cta-affiliate" rel="noopener nofollow" target="_blank">Bekijk Sessy</a> (gewone verwijzing, wij ontvangen hiervoor geen vergoeding)

## Smart EV-laden via de SolarEdge-lader

De SolarEdge EV-lader is technisch geen uitzonderlijk apparaat — andere Type 2-laders doen hetzelfde — maar hij integreert direct in de hub. Drie modi:

- **Solar mode** — laadt alleen bij overschot boven het huisverbruik
- **Time of Use** — laadt op vooraf ingestelde uren
- **Smart energy management** — combineert beide: zon overdag, goedkope uren 's nachts

Die derde modus is waar de combinatie met een dynamisch contract interessant wordt. **Modelberekening met zichtbare aannames:** een EV die 16.000 km per jaar rijdt, komt op ongeveer 3.200 kWh laadbehoefte.

- 1.400 kWh uit eigen panelen
- 1.800 kWh uit het net tegen gemiddeld €0,13/kWh = €234

Tegen een vast tarief van €0,33/kWh zou diezelfde 3.200 kWh €1.056 kosten — in dit model een verschil van ruim €800 per jaar op alleen het laden.

Twee kanttekeningen bij die uitkomst. Ten eerste is "gratis" laden uit eigen panelen alleen echt gratis zolang je saldeert; daarna is die kWh de terugleververgoeding waard die je misloopt, en wordt de winst het verschil tussen afnameprijs en terugleververgoeding. Ten tweede staat of valt het model met de aanname dat je het laden daadwerkelijk naar de goedkope uren kunt verschuiven. Twijfel je over de lader zelf: lees [beste laadpaal thuis 2026](/posts/beste-laadpaal-thuis-2026/) en [EV laden met thuisbatterij](/posts/ev-laden-met-thuisbatterij/).

## Voor wie heeft deze combinatie zin?

Niet voor iedereen. Voor een tweepersoonshuishouden met acht panelen en een bescheiden jaarverbruik is SolarEdge plus dynamisch contract overkill: de meerprijs van optimizers per paneel haal je er niet uit.

De drempels waarbij de investering doorgaans begint te lonen:

| Profiel | Verbruik | EV of warmtepomp | Overweging |
|---|---|---|---|
| Klein gezin, geen EV | 3.000-4.500 kWh | nee | Eenvoudige string-omvormer plus dynamisch contract, geen batterij |
| Modaal gezin | 4.500-7.000 kWh | misschien | String-omvormer met losse batterij |
| Groot gezin met EV | 7.000-10.000 kWh | ja | SolarEdge met eigen batterij te overwegen |
| Groot gezin met EV en warmtepomp | 10.000+ kWh | ja | SolarEdge-systeempakket met grotere batterij |

**Modelberekening voor het segment "groot gezin met EV", met zichtbare aannames:**

- 14 panelen (5.880 Wp), opbrengst 5.500 kWh per jaar
- Verbruik: 8.400 kWh (huishouden plus EV)
- Netto-afname: 4.300 kWh
- Zonder batterij op een vast contract: circa €1.420 aan stroomkosten
- Met batterij en sturing op uurtarief: circa €570

Het verschil is in dit model circa €850 per jaar. Zet daar je eigen offertes tegenover: de meerprijs van SolarEdge boven een string-omvormer, plus de batterij. Bij een batterij-investering van €5.400 komt de terugverdientijd in dit model op ruim zes jaar — maar alleen ná het einde van de saldering, want zolang je saldeert levert de arbitrage niets op. Doe dezelfde som met je eigen cijfers; onze vergelijking [beste dynamisch contract met zonnepanelen](/posts/beste-dynamisch-contract-met-zonnepanelen-2026/) helpt daarbij.

<a href="https://go.duurzaamthuislab.nl/frank-energie" class="cta cta-affiliate" rel="noopener nofollow" target="_blank">Bekijk Frank Energie</a> (gewone verwijzing, wij ontvangen hiervoor geen vergoeding)

## Nadelen: prijs, abonnementen, complexiteit

**Prijs.** SolarEdge publiceert geen consumentenprijzen, maar de systematiek is duidelijk: je koopt per paneel een optimizer bij. Dat maakt een SolarEdge-set structureel duurder dan een vergelijkbare string-omvormer zonder optimizers. Die meerprijs is te rechtvaardigen als je daadwerkelijk paneeloptimalisatie nodig hebt — schaduw, of een oost-westopstelling — of als je het hele ecosysteem gaat gebruiken. Voor een schaduwvrij zuiddak is het geld dat je niet terugziet.

**Abonnementen.** De geavanceerde functies, waaronder de dynamische tariefintegratie en de uitgebreidere rapportage, zitten achter een betaald cloudabonnement. Op zich geen groot bedrag, maar wel een terugkerende post — en bij sommige concurrenten zijn vergelijkbare functies inbegrepen. Zonder dat abonnement kom je uit bij de Home Assistant-route.

**Complexiteit.** Die Home Assistant-route werkt prima als je technisch bent: Modbus TCP configureren, een automation schrijven die de prijzen met je drempelwaarde vergelijkt, en alles testen. Wie nooit eerder met Home Assistant heeft gewerkt, moet rekenen op een flinke leercurve. Onze [Home Assistant integratie guide voor warmtepompen](/posts/home-assistant-warmtepomp-integratie-2026/) geeft een idee van de denkwijze.

**Lock-in.** SolarEdge-omvormers werken met SolarEdge-optimizers en SolarEdge-batterijen. Wil je later een batterij van een ander merk, dan moet je AC-koppelen en verlies je het rendementsvoordeel van DC-koppeling.

**Servicekwaliteit.** Voor een omvormer die vijftien jaar mee moet, is de garantieafhandeling belangrijker dan de specificaties. Kies een installateur die die afhandeling volledig overneemt en vraag vooraf naar de RMA-procedure — in gebruikersfora is de klacht die het vaakst terugkomt niet een defect, maar dat installateur en fabrikant naar elkaar verwijzen.

**Firmware-onzekerheid.** SolarEdge heeft in het verleden firmware-updates uitgerold die de Modbus-registers wijzigden, met kapotte Home Assistant-automations tot gevolg. Wie op die route bouwt, moet erop rekenen dat een update af en toe onderhoud vraagt. Niet onoverkomelijk, wel iets om te weten voordat je erop vertrouwt.

## SolarEdge vs Huawei vs Enphase voor dynamisch contract

Korte vergelijking op de drie punten die bij een dynamisch contract tellen: prijssturing, batterij-ecosysteem en Home Assistant-ondersteuning. Prijzen laten wij weg — geen van de drie fabrikanten publiceert consumentenprijzen, en straatprijzen verschillen per kanaal.

| Punt | SolarEdge | Huawei | Enphase |
|---|---|---|---|
| Architectuur | string met optimizers per paneel | string, optimizers optioneel | micro-omvormer per paneel |
| Eigen batterij-ecosysteem | ja, DC-gekoppeld | ja, DC-gekoppeld | ja, AC-gekoppeld |
| Sturing op dynamisch tarief | via betaald cloudabonnement | via eigen app | via eigen platform |
| Home Assistant via Modbus TCP | ja, stabiel | ja, gevoelig voor firmwarewijzigingen | beperkt, vooral via cloud |
| Peak shaving | configureerbaar | ondersteund | ondersteund |

**Onze afweging**: wie bewust voor één systeempakket gaat — panelen, omvormer, batterij en lader van één merk — zit bij SolarEdge het meest volwassen. Wie de batterij later los wil kopen of al Home Assistant draait, zit bij Huawei doorgaans goedkoper en even flexibel. Enphase is de keuze voor wie per paneel wil kunnen uitbreiden en de langste omvormergarantie zoekt; de sturing op dynamisch tarief is daar het minst uitgewerkt.

Een uitgebreide vergelijking staat in [Huawei vs SolarEdge](/posts/huawei-vs-solaredge-omvormer-2026/); moet je nog panelen kiezen, dan helpt [beste zonnepanelen 2026](/posts/beste-zonnepanelen-2026/) of het scenario [na saldering 2027](/posts/beste-zonnepanelen-2026-na-saldering/).

## Home Assistant-integratie: wat werkt en wat niet

De Home Assistant SolarEdge-integratie heeft twee smaken: de officiële, cloud-gebaseerde REST-API en de community-Modbus-integratie die lokaal werkt. Op basis van de integratiedocumentatie en de meldingen in de Home Assistant-community:

**Werkt goed:**

- Live productiedata uitlezen via Modbus, met een korte interval
- Batterijstatus: laadtoestand, laad- en ontlaadvermogen, temperatuur
- De batterijmodus sturen via een Modbus-register
- Prijsdata van je leverancier koppelen aan een batterij-automation

**Werkt half:**

- Aansturing van de EV-lader — via de cloud-API, met merkbare vertraging
- Laden op zonvoorspelling — werkt met een externe forecastbron erbij
- De uitgebreidere cloudfuncties — abonnementsgebonden, en niet alle endpoints zijn open

**Werkt niet:**

- Sturen onder de minuut via de cloud; daarvoor moet je lokaal via Modbus werken
- Per-paneel optimizerdata lokaal uitlezen; dat loopt via de cloud
- Een kant-en-klare component voor dynamische profielen — de logica schrijf je zelf

In de praktijk bouwen mensen een automation die periodiek de actuele prijs leest, die vergelijkt met een drempel (bijvoorbeeld de mediaan van de komende 24 uur) en het Modbus-register voor de batterijmodus op laden, ontladen of automatisch zet. Het werkt — maar reken op enkele avonden inregelen voordat het stabiel draait.

---

**Conclusie**: SolarEdge plus een dynamisch contract is geen instapcombinatie. Het is een bewust premium-pakket dat zich terugverdient bij een fors jaarverbruik in combinatie met een EV of warmtepomp, en dan vooral vanaf het moment dat de saldering per 1 januari 2027 wegvalt. Voor die doelgroep is het een van de stabielste set-ups die je kunt laten installeren: alles werkt samen, één garantieloket, één app.

Onder die drempel: kies een eenvoudiger omvormer met eventueel een losse batterij, of blijf bij je huidige omvormer en voeg alleen een dynamisch contract toe. Dat laatste kost niets en levert het grootste deel van het effect.

Twijfel je? Reken door met ons [batterij-rekenmodel](/posts/dynamisch-contract-met-batterij-rekenmodel-2026/), of vergelijk eerst de omvormers in de [omvormer-vergelijking](/posts/beste-omvormer-zonnepanelen-2026/).

Meer over de regels rond saldering en dynamische tarieven lees je bij [Milieu Centraal: salderingsregeling voor zonnepanelen](https://www.milieucentraal.nl/energie-besparen/zonnepanelen/salderingsregeling-voor-zonnepanelen/).
