---
title: 'Thuisbatterij grootte berekenen: 5, 10 of 15 kWh? (rekenmodel)'
date: '2026-08-28 08:00:00+02:00'
lastmod: '2026-08-21 08:00:00+02:00'
draft: false
description: Hoe groot moet je thuisbatterij zijn? Een narekenbare maatvoeringsmethode op basis van jaarverbruik, teruglevering en de 150-zoncycli-vuistregel, met voorbeeldsommen.
categories:
- thuisbatterijen
tags:
- thuisbatterijen
- rekenmodel
- capaciteit
- thuisbatterij
keywords:
- thuisbatterij grootte
- welke kwh thuisbatterij
- batterij capaciteit berekenen
- thuisbatterij rekenmodel
- hoeveel kwh batterij nodig
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: Hoe bepaal ik hoe groot mijn thuisbatterij moet zijn?
  a: 'Niet op je jaarverbruik, maar op het volume dat je daadwerkelijk kunt verschuiven. Dat is de laagste van drie grenzen: de capaciteit maal het aantal bruikbare zoncycli per jaar (wij rekenen met 150), je jaarlijkse overschot maal het retourrendement van 90%, en je eigen avond- en nachtafname. De kleinste van die drie bepaalt wat de batterij oplevert — extra kWh boven die grens staat stil.'
- q: Waarom rekenen jullie met 150 cycli en niet met 365?
  a: 'Omdat een batterij alleen een volle cyclus maakt op dagen met een echt zonoverschot én een avondvraag die groot genoeg is. In de winter is er weken achter elkaar geen overschot en in de zomer is de avondvraag soms kleiner dan de accu. 150 volledige zoncycli per jaar is onze gelabelde aanname; met een dynamisch contract kun je daar netarbitrage in de winter bovenop rekenen, en dat zit apart in het model.'
- q: Levert de tweede 5 kWh net zoveel op als de eerste?
  a: 'Nee. De opbrengst per kWh capaciteit is in het model gelijk zolang je overschot en je avondvraag groot genoeg blijven, maar bij de meeste huishoudens is één van die twee eerder verzadigd dan de capaciteit. Zodra dat gebeurt, daalt de marginale opbrengst per extra kWh en loopt de terugverdientijd op. Reken daarom altijd de drie grenzen apart uit voordat je een maat kiest.'
- q: Heb ik een dynamisch contract nodig om een batterij rendabel te maken?
  a: 'Zonder dynamisch contract heb je alleen de zelfverbruikwinst: je gebruikt eigen stroom in plaats van teruggeleverde stroom. Met een dynamisch contract komt daar netarbitrage bij, ook in de winter. In ons canonieke model is dat circa €8 per kWh capaciteit per jaar; dat is een aanname op basis van ongeveer honderd wintercycli met een netto spreiding van €0,10 per kWh, geen gemeten opbrengst.'
- q: Wat betekent het einde van de saldering voor de maatvoering?
  a: 'De saldering stopt volledig per 1 januari 2027. Vanaf dat moment is het verschil tussen wat je voor teruglevering krijgt en wat je voor inkoop betaalt de kern van het rendement — en dat verschil bepaalt de waarde van elke verschoven kWh. Reken je maatvoering dus door met een terugleververgoeding-aanname, niet met salderen.'
schema_type: Article
last_updated: '2026-08-21'
---
*Dit artikel bevat geen affiliate links en geen commerciële verwijzingen. De prijzen die wij als ijkpunt gebruiken komen van sessy.nl (prijspeil augustus 2026). Alle uitkomsten zijn modelberekeningen met expliciete aannames, geen metingen.*

De vraag "5, 10 of 15 kWh?" is niet met een vuistregel per gezinsgrootte te beantwoorden. Wat een batterij oplevert, hangt niet af van hoeveel je verbruikt maar van hoeveel je kunt **verschuiven** — en dat volume zit vast aan drie grenzen die je zelf kunt uitrekenen. Hieronder de methode, met de sommen erbij.

> **Kort antwoord:** bereken drie grenzen en neem de laagste. Eén: capaciteit × 150 bruikbare zoncycli per jaar. Twee: je jaarlijkse overschot (teruglevering) × 0,9 retourrendement. Drie: je afname in de uren zonder zon. De laagste grens is je werkelijk verschuifbare volume; capaciteit boven die grens levert niets op. Vermenigvuldig dat volume met de spread tussen inkoop en teruglevering, tel er bij een dynamisch contract netarbitrage bij op, en zet het tegen de aanschafprijs.

## Stap 1: haal je eigen cijfers op

Je hebt drie getallen nodig, en alle drie staan al ergens:

1. **Jaarlijkse afname** in kWh (van het net) — je jaarafrekening of het portaal van je leverancier.
2. **Jaarlijkse teruglevering** in kWh — zelfde plek. Dit is je overschot: stroom die je hebt opgewekt en niet meteen zelf gebruikte.
3. **Je verbruiksprofiel per kwartier** — via een P1-meter of, bij de meeste leveranciers, als download van je meetdata. Hiermee zie je hoeveel je 's avonds en 's nachts verbruikt.

Heb je nog geen panelen, dan bestaat je overschot nog niet en is het gebruik van een batterij beperkt tot netarbitrage op een dynamisch contract. Dat is een wezenlijk andere rekensom — en een veel krappere.

Meten kost weinig: de HomeWizard P1-meter staat op de eigen webshop voor €24,95 (prijspeil augustus 2026, homewizard.com). Een jaar meten voordat je duizenden euro's aan capaciteit koopt, is de goedkoopste stap in dit hele traject.

## Stap 2: de drie grenzen

Het verschuifbare volume per jaar is de **laagste** van deze drie:

| Grens | Formule | Waarom hij bindt |
|---|---|---|
| Cyclusgrens | capaciteit × 150 | Een batterij maakt niet elke dag een volle cyclus: in de winter is er weken geen overschot, in de zomer is de avondvraag soms kleiner dan de accu |
| Overschotgrens | teruglevering × 0,9 | Je kunt niet meer opslaan dan je overhoudt, en van wat erin gaat komt door laad- en ontlaadverlies circa 90% er weer uit |
| Afnamegrens | afname in de uren zonder zon | Opgeslagen stroom die je niet gebruikt, blijft in de accu staan |

De 150 zoncycli is een gelabelde aanname, geen meting: het is ons canonieke uitgangspunt voor een Nederlands dak met een normale zomer-winterverdeling. Reken je liever conservatief, gebruik dan 120; optimistischer dan 180 is bij een netgekoppelde woning niet te verdedigen.

## Stap 3: waarde per verschoven kWh

Wat een verschoven kWh waard is, is het verschil tussen wat je níet inkoopt en wat je niet terugkrijgt voor teruglevering:

- **Inkoopprijs op een passief verbruiksprofiel: €0,272 per kWh.** Opgebouwd uit een all-in aanname van €0,26 (beursprijs, energiebelasting 2026, opslagen) met een opslag van 8% omdat een huishouden zonder sturing gemiddeld op de duurdere uren verbruikt. Gelabelde aanname.
- **Terugleververgoeding vanaf 2027: €0,07 per kWh.** Ook een aanname: leveranciers hebben hun tarieven voor na de saldering nog niet gepubliceerd.
- **Spread: €0,272 − €0,07 = €0,202 per kWh.**

Per kWh capaciteit per jaar levert dat op: 150 cycli × 0,9 retourrendement × €0,202 = **€27,3**. Heb je een dynamisch contract, dan komt daar netarbitrage bij: in ons canonieke model **€8 per kWh capaciteit per jaar** (aanname: circa 100 wintercycli met een netto spreiding van €0,10 per kWh). Samen **€35,3 per kWh capaciteit per jaar**.

## Stap 4: de uitkomst per maat

Dit is het canonieke model van DuurzaamThuisLab, en dezelfde getallen gebruiken wij in al onze batterijberekeningen. Uitgangspunt: overschot en avondvraag zijn groot genoeg om de cyclusgrens bindend te laten zijn, en er is een dynamisch contract.

| Capaciteit | Verschuifbaar volume | Opbrengst per jaar | Prijs (Sessy, aug 2026) | Terugverdientijd |
|---|---|---|---|---|
| 5 kWh | circa 675 kWh | **€177** | €3.550 | circa 20 jaar |
| 10 kWh | circa 1.350 kWh | **€353** | €5.500 | circa 16 jaar |
| 15 kWh | circa 2.025 kWh | **€530** | €9.400 (Sessy Plus) | circa 18 jaar |

Prijzen: sessy.nl, inclusief btw en exclusief installatie, prijspeil augustus 2026. Op een thuisbatterij geldt het reguliere btw-tarief van 21%; de 0%-regeling geldt alleen voor zonnepanelen en direct noodzakelijke onderdelen, en de ISDE dekt geen thuisbatterijen. Noodstroom is bij Sessy een aparte basisinstallatie van €1.200 — reken die mee als je die functie wilt.

Voor de 10 kWh-variant komt het model op een cumulatieve opbrengst van circa **€3.530 over tien jaar** en circa **€4.843 over vijftien jaar** (de opbrengst daalt met de capaciteitsafname van de cellen). Dat is de eerlijke uitkomst: bij deze aannames verdient een thuisbatterij zich binnen zijn levensduur niet met ruime marge terug, en de maatvoering bepaalt vooral hoe krap het is.

Wil je andere prijsaannames invullen — bijvoorbeeld een hogere spread of een lagere aanschafprijs — dan is [de terugverdientijdvergelijking](/thuisbatterij-terugverdientijd-vergelijken/) de plek waar we de gevoeligheid uitwerken.

## Voorbeeldsom A: gezin met panelen, geen EV

Aannames: afname 3.400 kWh, teruglevering 1.800 kWh, avond- en nachtafname circa 1.900 kWh, dynamisch contract.

- Cyclusgrens bij 5 kWh: 5 × 150 = 750 kWh
- Overschotgrens: 1.800 × 0,9 = 1.620 kWh
- Afnamegrens: 1.900 kWh
- **Bindend: de cyclusgrens (750 kWh).** Opbrengst: 5 × €35,3 = €177 per jaar.

Bij 10 kWh: cyclusgrens 1.500 kWh, nog steeds onder de overschot- en afnamegrens. Opbrengst €353 per jaar, extra investering €1.950 voor €176 extra per jaar — een betere verhouding dan de eerste 5 kWh, precies omdat de vaste kosten van installatie al gemaakt zijn. Bij 15 kWh loopt de cyclusgrens (2.250 kWh) juist boven de overschotgrens uit: dan is 1.620 kWh het maximum en levert de derde 5 kWh minder op dan de tweede.

**Les:** hier is 10 kWh de maat waarop het model het gunstigst uitpakt. Niet omdat het gezin groter is, maar omdat de drie grenzen daar het beste op elkaar aansluiten.

## Voorbeeldsom B: gezin met EV die thuis laadt

Aannames: afname 3.800 kWh huishoudelijk plus 7.000 kWh EV, teruglevering 2.100 kWh, dynamisch contract, EV laadt 's nachts.

De verleiding is om voor de EV extra capaciteit te kopen. Dat werkt in dit model niet: een EV die 's nachts op de goedkope uren laadt, haalt zijn stroom niet uit de batterij — die is dan al leeg voor de avondpiek, en 7.000 kWh gaat sowieso niet door een accu van 10 kWh. De afnamegrens die telt is dus de huishoudelijke avondvraag, niet het totaal.

- Overschotgrens: 2.100 × 0,9 = 1.890 kWh
- Cyclusgrens bij 10 kWh: 1.500 kWh → bindend
- Cyclusgrens bij 15 kWh: 2.250 kWh → nu is het overschot (1.890 kWh) bindend

Bij 15 kWh betaal je dus €3.900 extra voor circa 390 kWh extra verschuifbaar volume: grofweg €79 per jaar. Dat is een terugverdientijd van bijna vijftig jaar op die derde module. **Les:** een EV is een argument voor slim laden en voor een dynamisch contract, niet voor meer batterijcapaciteit.

## Voorbeeldsom C: laag verbruik zonder EV

Aannames: afname 1.900 kWh, teruglevering 900 kWh.

- Overschotgrens: 900 × 0,9 = 810 kWh → bindend, ook bij 5 kWh (cyclusgrens 750 kWh ligt er net onder)
- Opbrengst 5 kWh: €177 per jaar tegen €3.550 → circa 20 jaar

**Les:** bij een verbruik onder circa 2.000 kWh en geen EV haalt een batterij zijn terugverdientijd zelden binnen de levensduur. Een dynamisch contract en het verschuiven van wasmachine, droger en vaatwasser leveren dan meer op per geïnvesteerde euro. Waar de goedkope uren liggen, staat in [de beste tijd om de wasmachine aan te zetten](/beste-tijd-wasmachine/).

## Vijf rekenfouten die je maat te groot maken

1. **Rekenen op nominale capaciteit in plaats van bruikbare AC-output.** Van 5 kWh nominaal houd je na conversie- en standbyverliezen ongeveer 4,5 kWh aan de wisselstroomzijde over. Reken met de waarde uit het datasheet.
2. **Zeldzame pieken meenemen.** Een droger die één keer per week 3 kWh vraagt, rechtvaardigt geen 3 kWh extra capaciteit.
3. **EV-verbruik in de zelfconsumptie meerekenen.** Zie voorbeeldsom B: het laadt te snel en te veel.
4. **Wintercapaciteit overschatten.** LiFePO4-cellen leveren bij lage temperaturen minder bruikbaar vermogen; datasheets geven daarvoor een deratingcurve. Bij plaatsing in een onverwarmde ruimte is dat een reëel verschil.
5. **Vergeten dat het laad- en ontlaadvermogen ook een grens is.** Een accu van 10 kWh met een ontlaadvermogen van 1,7 kW kan een avondpiek van 3 kW niet alleen opvangen. Kijk dus niet alleen naar kWh maar ook naar kW.

## Wanneer je geen batterij moet kopen

- **Verbruik onder circa 2.000 kWh zonder EV.** Zie voorbeeldsom C.
- **Geen zonnepanelen.** Dan resteert alleen netarbitrage: in ons model €8 per kWh capaciteit per jaar, dus circa €80 per jaar op 10 kWh. Dat verdient een investering van duizenden euro's niet terug.
- **Je werkt doordeweeks thuis.** Dan gebruik je overdag al direct uit de panelen en is je overschot klein; de overschotgrens bindt dan streng.
- **Je hebt geen dynamisch contract en bent niet van plan er een te nemen.** Dan verlies je de netarbitrage én de sturing die het model draagt.

## Wat na 2027 verandert aan deze rekensom

Per 1 januari 2027 stopt de saldering volledig — er is geen afbouwpad. Vanaf dat moment is de spread tussen inkoop en teruglevering de hele motor van het rendement, en die spread is nu nog een aanname: leveranciers hebben hun teruglevertarieven voor na de saldering niet gepubliceerd. Publiceren zij hogere tarieven dan onze €0,07, dan wordt de batterij minder aantrekkelijk; publiceren zij lagere, dan juist meer.

Dat is ook de eerlijkste reden om nu klein te beginnen. De maatvoering die je vandaag berekent, rust op één ongepubliceerd getal — en een module bijzetten kan later, bij een modulair systeem.

---

*Dit artikel is voor het laatst bijgewerkt op 21 augustus 2026 door de redactie van DuurzaamThuisLab. Klopt er iets niet? Laat het ons weten — wij houden dit artikel actief bij.*

---

**Bronnen:** prijzen thuisbatterij: [sessy.nl](https://www.sessy.nl/), prijspeil augustus 2026, inclusief btw en exclusief installatie. Prijs P1-meter: [homewizard.com](https://www.homewizard.com/). Wat de ISDE wel en niet dekt: [RVO — ISDE voor woningeigenaren](https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren) (thuisbatterijen vallen er niet onder). De energiebelastingtarieven 2026 en de prijsaannames achter €0,26 en €0,272 per kWh staan uitgewerkt in [onze stroomprijzen-datahub](/stroomprijzen/). Geraadpleegd op 21 augustus 2026.
