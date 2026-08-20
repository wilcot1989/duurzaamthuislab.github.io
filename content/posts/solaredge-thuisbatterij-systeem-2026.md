---
title: 'SolarEdge-systeem samenstellen: omvormer, thuisbatterij en optimizers'
date: 2026-08-30 08:00:00+02:00
lastmod: 2026-08-30 08:00:00+02:00
description: 'Hoe een SolarEdge-systeem is opgebouwd: Home Hub- of Home Wave-omvormer, optimizers per paneel en de Home Battery 48V. Met datasheetwaarden, 1-fase versus 3-fase en wat DC-gekoppeld betekent.'
draft: false
categories:
- zonne-energie
- thuisbatterijen
tags:
- SolarEdge
- omvormer
- optimizers
- thuisbatterij
- DC-gekoppeld
keywords:
- solaredge systeem vergelijking
- solaredge systeem samenstellen
- solaredge home hub
- solaredge thuisbatterij
- solaredge optimizers
- solaredge 1 fase of 3 fase
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1509391366360-2e959784a276&w=1200&output=webp&q=70
faq:
- q: Uit welke onderdelen bestaat een SolarEdge-systeem?
  a: 'Drie lagen: één optimizer onder elk paneel, één centrale omvormer (Home Wave zonder batterij, Home Hub met batterij) en optioneel de SolarEdge Home Battery 48V. Daarnaast een meter voor terugleverbegrenzing en energiebeheer, en bij noodstroom extra componenten. De optimizers zijn geen losse keuze: zonder optimizers werkt een SolarEdge-omvormer niet.'
- q: Wat is het verschil tussen Home Wave en Home Hub?
  a: Home Wave is de omvormer zonder batterijaansluiting; Home Hub heeft een batterijingang en stuurt PV, huisverbruik en batterij in één apparaat. Wil je later een batterij, dan is de Home Hub de logische keuze, want een Home Wave omzetten naar een batterijsysteem betekent in de praktijk een tweede apparaat of een nieuwe omvormer.
- q: Wat betekent DC-gekoppeld bij SolarEdge?
  a: 'De batterij hangt aan de gelijkspanningszijde van de omvormer. Zonnestroom gaat rechtstreeks naar de batterij zonder tussentijdse omzetting naar 230 V. SolarEdge geeft in de datasheet van de 3-fase Home Hub 98,4 procent op voor PV naar batterij en 96,1 procent voor batterij naar net; een AC-gekoppelde batterij verliest per omzetting een paar procent meer.'
- q: Hoeveel batterijmodules kan ik aan één omvormer hangen?
  a: 'Volgens de datasheet van de 3-fase Home Hub (SE5K/SE8K/SE10K-RWB48) worden 1 tot 5 modules van het type BAT-05K48 ondersteund. Bij 4,6 kWh per module komt dat op ongeveer 23 kWh. Het maximale laad- en ontlaadvermogen blijft daarbij 5000 W: meer capaciteit betekent niet meer vermogen.'
- q: Wat kost een SolarEdge-systeem?
  a: 'Dat verschilt per installateur, omdat arbeid, bekabeling en groepenkast zwaarder wegen dan de componentprijs. Losse componentprijzen bij Nederlandse dealers, prijspeil augustus 2026: SolarEdge Home Battery 48V 4,6 kWh circa €1.495 (batterijmodule, exclusief omvormer en installatie) en de 1-fase SE2200H circa €599. Vraag altijd twee of drie offertes met de complete componentlijst erbij.'
schema_type: Article
---

*Disclosure: de verwijzingen naar SolarEdge in dit artikel zijn gewone verwijzingen — wij hebben met SolarEdge geen affiliate- of commissierelatie. Wij schrijven op basis van specificaties, publieke documentatie en vendorinformatie.*

Wie "SolarEdge" in een offerte ziet staan, ziet zelden waar het systeem uit bestaat. Er staat een omvormertype, een aantal optimizers en soms een batterij — en de vraag welke onderdelen bij elkaar horen en waarom, blijft onbeantwoord. Dit artikel legt de opbouw uit: welke lagen een SolarEdge-systeem heeft, hoe 1-fase en 3-fase verschillen, wat DC-gekoppeld precies betekent en welke getallen uit de officiële datasheets komen.

Wij hebben dit systeem niet zelf geïnstalleerd of doorgemeten. Alle specificaties hieronder komen uit de officiële SolarEdge-datasheets (Home Hub 3-fase NL, StorEdge 1-fase HD-Wave NL en de S-serie optimizer-datasheet) en de genoemde prijzen van Nederlandse dealers, opgehaald op 20 augustus 2026. Waar een getal uit een berekening komt, staat dat er nadrukkelijk bij.

## De drie lagen van een SolarEdge-systeem

Een SolarEdge-installatie is geen omvormer met accessoires, maar een systeem met drie lagen die alleen samen werken.

**Laag 1: een optimizer onder elk paneel.** De optimizer is een klein kastje dat op het frame van het paneel wordt geschroefd en het maximum power point van dát paneel regelt. De omvormer werkt niet zonder; dit is geen upgrade die je erbij koopt.

**Laag 2: de centrale omvormer.** Die staat in de meterkast, op zolder of aan een buitenmuur en zet de gelijkspanning van de strings om naar 230 V wisselspanning.

**Laag 3: optioneel de thuisbatterij**, aangesloten op de gelijkspanningszijde van de omvormer — mits je een omvormer met batterijingang hebt gekozen.

Daar zit de belangrijkste beslissing van het hele traject: SolarEdge levert omvormers zonder batterijaansluiting (de Home Wave-lijn met HD-Wave-technologie) en omvormers met batterijaansluiting (Home Hub). Kies je een omvormer zonder batterijingang omdat je "later nog wel ziet", dan is die stap later een stuk duurder dan een paar honderd euro meerprijs nu.

## Wat de optimizer volgens de datasheet doet

De S-serie optimizer-datasheet (S440 / S500 / S500B / S650B, versiedatum 19 mei 2025) geeft deze harde waarden:

| Specificatie | Waarde |
|---|---|
| Nominaal DC-ingangsvermogen | 440 W (S440), 500 W (S500/S500B), 650 W (S650B) |
| Vanaf installaties na 1 april 2024 | S440 490 W, S500 en S500B 550 W |
| Maximaal rendement | 99,5% |
| Gewogen rendement | 98,6% |
| Veiligheidsspanning in stand-by | 1 V per optimizer |
| Beschermingsklasse | IP68 |
| Bedrijfstemperatuur | –40 tot +85 °C |
| Garantie | 25 jaar |

Twee dingen zijn hier relevant. Het nominale ingangsvermogen bepaalt welk paneel eronder past: een paneel van 500 Wp hoort niet onder een optimizer met 440 W nominaal ingangsvermogen. En die 1 V veiligheidsspanning in stand-by is de reden dat brandweer en installateur bij een SolarEdge-dak niet met honderden volt op het dak te maken hebben.

De datasheet geeft ook minimale en maximale stringlengtes. Voor een 1-fase Home Wave- of Home Hub-omvormer geldt bij S440 en S500 een minimale stringlengte van 8 optimizers en een maximum van 25. Dat is een ontwerpgrens die vaker knelt dan mensen denken: met zes panelen op één dakvlak haal je de minimale stringlengte niet, en dan moet het ontwerp anders.

## 1-fase of 3-fase: waar de keuze werkelijk over gaat

De vraag "1-fase of 3-fase" gaat niet over het merk maar over je huisaansluiting. Heb je een 1-fase aansluiting, dan komt er een 1-fase omvormer. Bij 3-fase kan het beide, maar een 3-fase omvormer verdeelt het vermogen over de fasen en dat is bij hogere vermogens en bij een batterij met noodstroomambitie de logische route.

De officiële NL-datasheet van de 3-fase Home Hub (SE5K-RWB48 / SE8K-RWB48 / SE10K-RWB48) geeft:

| Specificatie | SE5K-RWB48 | SE8K-RWB48 | SE10K-RWB48 |
|---|---|---|---|
| Nominaal AC-vermogen (totaal) | 5000 VA | 8000 VA | 10.000 VA |
| Per fase | 1667 VA | 2667 VA | 3333 VA |
| Maximaal DC-vermogen (paneel STC) | 10.000 W | 16.000 W | 20.000 W |
| Piekefficiëntie PV naar net | 98% | 98% | 98% |
| Europees gewogen rendement | 97,3% | 97,6% | 97,6% |
| Maximaal laad-/ontlaadvermogen batterij | 5000 W | 5000 W | 5000 W |
| Ondersteunde batterij | SolarEdge Home-Batterij 48V BAT-05K48, 1–5 modules | idem | idem |
| Omschakeltijd bij back-up | ≤ 6 seconden | ≤ 6 seconden | ≤ 6 seconden |
| Gewicht | 37 kg | 37 kg | 37 kg |
| Geluidsniveau | < 50 dBA | < 50 dBA | < 50 dBA |
| Beschermingsklasse | IP65 | IP65 | IP65 |
| Garantie | 12 jaar | 12 jaar | 12 jaar |

Let op de regel die het vaakst wordt overgeslagen: het maximale laad- en ontlaadvermogen is 5000 W, ongeacht welk van de drie modellen je kiest en ongeacht hoeveel batterijmodules eraan hangen. Wie 23 kWh stapelt om sneller te kunnen ontladen, koopt capaciteit maar geen vermogen.

Aan de 1-fase kant staat de HD-Wave-lijn. De NL-datasheet van de 1-fase StorEdge-omvormer met HD-Wave-technologie noemt de modellen SE2200H-RWS tot en met SE6000H-RWS, met een nominaal AC-uitgangsvermogen van respectievelijk 2200 tot 6000 VA, een maximale omvormerefficiëntie van 99,2 procent en een maximaal continu batterijlaad- en ontlaadvermogen van 5000 W. Belangrijk: die datasheet is een oudere generatie en noemt LG Chem RESU als compatibele batterij. Welke batterij bij jouw exacte 1-fase modelnummer en firmwareversie hoort, is precies het soort detail dat je bij de installateur moet neerleggen in plaats van uit een artikel overnemen.

Ook de geluidsnorm en het gewicht zijn praktisch: 37 kg aan de wand en tot 50 dBA aan koelventilatoren is geen apparaat dat je naast een slaapkamerwand hangt. Dat argument komt in de meeste offertes niet voorbij, en het is er wel een. Meer over het selecteren van een installateur die dit soort keuzes uitlegt staat in onze gids [installateur kiezen](/installateur-kiezen/).

## DC-gekoppeld: waarom SolarEdge dat noemt

DC-gekoppeld betekent dat de batterij aan de gelijkspanningszijde van de omvormer hangt. Zonnestroom die naar de batterij gaat, wordt dus niet eerst naar 230 V omgezet en daarna weer terug.

De datasheet van de 3-fase Home Hub kwantificeert dat met drie piekefficiënties: 98 procent van PV naar net, 98,4 procent van PV naar batterij en 96,1 procent van batterij naar net. Een AC-gekoppelde batterij zoals de Enphase IQ Battery of Sessy heeft per definitie een extra omzetting in het pad zon-naar-batterij.

**Modelberekening, met de aannames erbij.** Stel dat je per jaar 1.500 kWh zonnestroom door de batterij laat lopen. Een DC-gekoppeld pad met 98,4 procent laden en 96,1 procent ontladen levert een rondgangsrendement van ongeveer 94,6 procent volgens de opgegeven piekefficiënties. Scheelt een AC-gekoppeld systeem in de praktijk drie procentpunt in dat pad, dan is dat circa 45 kWh per jaar. Bij €0,30 per kWh gaat het om ongeveer €14 per jaar. Dat is echt: het is ook klein genoeg om de keuze niet te bepalen als je op andere punten liever een AC-batterij hebt. De tegenkant van DC-koppeling is namelijk vendor lock-in — de batterij werkt alleen achter de eigen omvormer.

Hoe die afweging uitpakt tegenover micro-omvormers staat in onze vergelijking [SolarEdge versus Enphase](/posts/solaredge-vs-enphase-2026/).

## Indicatieve componentopbouw

Hieronder de opbouw van een systeem, met alleen prijzen die wij bij Nederlandse dealers hebben kunnen verifiëren (prijspeil augustus 2026). Voor de rest staat expliciet dat je het bij de installateur moet opvragen — een gefantaseerd bedrag helpt je niet bij het beoordelen van een offerte.

| Component | Aantal | Geverifieerde prijs |
|---|---|---|
| Optimizer S-serie | 1 per paneel | vraag installateur (25 jaar garantie) |
| Omvormer 1-fase SE2200H (HD-Wave) | 1 | circa €599 bij een Nederlandse webshop, btw-vermelding ontbrak op de pagina |
| Omvormer 3-fase Home Hub SE5K/SE8K/SE10K-RWB48 | 1 | vraag installateur |
| Home Battery 48V, module BAT-05K48 (4,6 kWh) | 1–5 | circa €1.495 per module bij een Nederlandse dealer, exclusief omvormer, toebehoren en installatie |
| Meter voor energiebeheer/terugleverbegrenzing | 1 | vraag installateur |
| Back-upcomponenten | n.v.t. | vraag installateur; SolarEdge noemt in de datasheet expliciet dat aanvullende componenten en een firmware-upgrade nodig kunnen zijn |

Wat een dealer voor de batterijmodule van 4,6 kWh vraagt, zegt daarmee weinig over de systeemprijs. De omvormer, de optimizers, de meter, de bekabeling en de arbeid zitten er niet in, en juist daar loopt het verschil tussen offertes op.

## Waar wij op zouden letten in een SolarEdge-offerte

**Staat er een Home Hub of een Home Wave?** Dat bepaalt of een batterij later nog kan zonder de omvormer te vervangen.

**Klopt het optimizertype bij het paneelvermogen?** Een paneel van 500 Wp hoort niet onder een S440 met 490 W nominaal ingangsvermogen.

**Wordt de minimale stringlengte gehaald?** Voor een 1-fase omvormer met S440 of S500 is dat 8 optimizers per string volgens de datasheet.

**Staat er hoeveel batterijmodules het worden, en met welk vermogen?** De capaciteit stapelt, de 5000 W laad- en ontlaadvermogen niet. Voor wie de batterij op prijsverschillen wil laten sturen, is dat vermogen de bepalende grootheid — zie [SolarEdge-omvormer en een dynamisch contract](/posts/solaredge-omvormer-dynamisch-contract-2026/) en de actuele uurtarieven op onze pagina met [dynamische stroomprijzen](/stroomprijzen/).

**Is noodstroom onderdeel van de afspraak of een wens?** SolarEdge zet in de eigen datasheet dat back-up alleen voor residentiële installaties beschikbaar is, onderhevig is aan lokale regelgeving en aanvullende componenten kan vergen. Laat dat expliciet op papier zetten.

## Conclusie

Een SolarEdge-systeem is een keten: optimizer per paneel, één centrale omvormer, en bij de Home Hub een DC-gekoppelde batterij van 1 tot 5 modules met een gezamenlijk laad- en ontlaadvermogen van 5000 W. De belangrijkste keuze maak je vóór de installatie, namelijk of de omvormer een batterijingang heeft. De rest is ontwerpwerk: stringlengte, optimizertype bij het paneelvermogen en de vraag of noodstroom echt in de opdracht zit.

De rendementswinst van DC-koppeling is meetbaar maar bescheiden — in ons model circa €14 per jaar bij 1.500 kWh door de batterij. Het echte verschil met een AC-gekoppeld alternatief zit in de vrijheid: bij SolarEdge zit je aan één merk vast, en dat is een prijs die niet in de offerte staat.
