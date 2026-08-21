---
title: 'Pylontech US5000 review 2026: de goedkoopste kWh, maar niet voor iedereen'
date: 2026-07-04 08:00:00+02:00
lastmod: 2026-08-21 08:00:00+02:00
description: 'Pylontech US5000 beoordeeld op de datasheet: 4,8 kWh nominaal, 4,56 kWh bruikbaar, 48 V, wat het continu vermogen écht is en waarom deze batterij een omvormer én kennis vereist.'
draft: false
categories:
- thuisbatterijen
tags:
- Pylontech
- US5000
- thuisbatterij
- LFP
- review
keywords:
- pylontech review
- pylontech us5000
- pylontech nederland
- pylontech thuisbatterij prijs
- pylontech vs sessy
- pylontech off-grid
- pylontech 48v
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1589276534126-adef63a95e05&w=1200&output=webp&q=70
schema_type: Review
faq:
- q: 'Wat is de capaciteit van een Pylontech US5000?'
  a: 'De datasheet van de US5000-1C geeft 4.800 Wh nominaal en 4.560 Wh bruikbaar bij 95 procent ontlaaddiepte. Wie ergens 5,12 kWh of 4,8 kWh bruikbaar leest, kijkt naar een ander model of naar een verkeerd overgenomen getal.'
- q: 'Hoeveel vermogen levert één module?'
  a: 'De datasheet geeft 2.400 W continu per module, met 4.800 W gedurende maximaal vijf minuten en een piek van circa 5.800 W gedurende vijftien seconden. Meer modules parallel betekent meer vermogen, maar de omvormer bepaalt uiteindelijk wat er uit de muur komt.'
- q: 'Hoeveel garantie geeft Pylontech?'
  a: 'De basisgarantie op de US5000-1C is 7 jaar. Registreer je de batterij op het Pylontech-platform, dan wordt dat 10 jaar. Die registratie is dus geen formaliteit — vraag je installateur of hij het doet, of doe het zelf en bewaar de bevestiging.'
- q: 'Werkt Pylontech in Nederland?'
  a: 'Ja, mits je een hybride omvormer hebt die het Pylontech-protocol ondersteunt. In de praktijk zijn dat onder meer Victron, Deye, Goodwe, Solis, Sofar en Growatt. De communicatie loopt over CAN of RS485; welke van de twee je moet instellen, verschilt per omvormer.'
- q: 'Heeft Pylontech een eigen app?'
  a: 'Nee. Pylontech levert geen consumenten-app. Alles wat je ziet en instelt, gaat via de app of het portaal van je omvormer. Wie inzicht en bediening belangrijk vindt, koopt dus in feite de app van de omvormerfabrikant mee.'
- q: 'Kan ik modules bijplaatsen?'
  a: 'Tot 16 modules parallel op één stack, aldus de datasheet — ongeveer 73 kWh. Voorwaarde is wel dat het om dezelfde productlijn gaat. Meng geen US3000- en US5000-modules en geen modules uit verschillende generaties: de zwakste module bepaalt het gedrag van de hele stack.'
- q: 'Krijg ik subsidie op een Pylontech-systeem?'
  a: 'Nee. Er bestaat geen landelijke subsidie voor thuisbatterijen; de ISDE dekt volgens RVO isolatie, ventilatie in combinatie met isolatie, (hybride) warmtepompen, zonneboilers, een warmtenetaansluiting en elektrisch koken. Op een thuisbatterij betaal je bovendien 21 procent btw — het 0-procenttarief geldt alleen voor zonnepanelen en direct noodzakelijke onderdelen.'
---
Pylontech is in de off-grid wereld het werkpaard: recreatiewoningen, boerderijen en schuren zonder goede netaansluiting draaien er massaal op. De vraag die daarbij hoort is of zo'n 48 V-systeem ook zinvol is in een gewone woning met een dynamisch contract.

Deze review is opgebouwd uit de datasheet van de US5000-1C zoals die door Europese distributeurs wordt gepubliceerd (opgehaald op 21 augustus 2026), aangevuld met de productinformatie op de site van Pylontech zelf. Wij hebben deze batterij niet zelf geïnstalleerd, niet doorgemeten en geen meterstanden vergeleken. Waar wij een oordeel geven, is dat een redactionele afweging op basis van die specificaties.

*Disclosure: de verwijzingen naar Pylontech, Sessy, Marstek en Tibber in dit artikel zijn gewone verwijzingen. Met geen van deze partijen hebben wij een affiliate- of commissierelatie.*

> **Kort antwoord:** de US5000 is de goedkoopste manier om kilowatturen in huis te halen, maar hij is een kale batterijmodule: geen app, geen sturing, geen handel op dynamische prijzen. Alles wat de batterij "slim" maakt, koop je in de vorm van een hybride omvormer en richt je zelf in.
>
> Voor wie technisch is of een goede installateur heeft, is dat een uitstekende ruil. Voor wie plug-and-play wil, is het de verkeerde batterij.

## Wat Pylontech maakt

Pylon Technologies is een Chinese batterijfabrikant uit Shanghai, actief sinds 2009. Het bedrijf maakt vooral 48 V LFP-batterijen voor zonne-installaties, telecom-backup en datacenters; de thuisbatterijmarkt is voor hen één segment van meerdere. Dat verklaart het karakter van het product: rackmodules zonder consumentenlaag eromheen.

In Europa is de US5000 het meest verkochte model. Daarnaast voert Pylontech onder meer de kleinere US3000C, de hoogvolt Force-lijn voor grotere installaties en de modulaire Pelio-lijn. Welke daarvan op enig moment leverbaar is, verschilt per distributeur — vraag dat na in plaats van af te gaan op een overzicht dat een jaar oud kan zijn.

## Specificaties US5000-1C

Onderstaande waarden komen uit de datasheet van de US5000-1C, stand 21 augustus 2026.

| Specificatie | Waarde |
|---|---|
| Nominale energie | 4.800 Wh |
| Bruikbare energie | 4.560 Wh |
| Ontlaaddiepte (DoD) | 95% |
| Systeemspanning | 48 V (laagvolt) |
| Celchemie | LFP (lithium-ijzerfosfaat) |
| Continu ontlaadvermogen | 2.400 W |
| Maximaal ontlaadvermogen (5 min) | 4.800 W |
| Piekvermogen (15 s) | circa 5.800 W |
| Maximaal laadvermogen (5 min) | 4.800 W |
| Communicatie | CAN en RS485 |
| Maximaal parallel | 16 modules (circa 73 kWh) |
| Gewicht | circa 40 kg per module |
| Afmetingen | 442 × 420 × 132 mm |
| Beschermingsklasse | IP20 — uitsluitend binnen |
| Garantie | 7 jaar basis, 10 jaar na registratie |

Twee dingen springen eruit. Ten eerste het continu vermogen: 2.400 W per module is minder dan veel samenvattingen op internet suggereren. Wil je een oven, vaatwasser en droger tegelijk uit de batterij voeden, dan heb je meerdere modules nodig — én een omvormer die dat vermogen aankan. Ten tweede de garantie: die is 7 jaar tenzij je de batterij registreert op het platform van Pylontech, waarna hij op 10 jaar komt. Dat is een administratieve handeling met een waarde van drie jaar dekking.

## Wat je erbij moet kopen

De US5000 is geen systeem maar een component. Om hem in een woning te laten werken heb je minimaal nodig:

1. **Een hybride omvormer** die het Pylontech-protocol spreekt. Victron, Deye, Goodwe, Solis, Sofar en Growatt worden het meest gecombineerd met deze batterij.
2. **Een rack of montageframe.** Dat wordt los besteld en zit niet bij de module.
3. **Communicatiebekabeling** tussen de modules onderling en tussen de mastermodule en de omvormer.
4. **Een instelling in het omvormermenu** die het juiste batterijprotocol selecteert, en de keuze tussen CAN en RS485.

Punt vier is waar het bij zelfbouw het vaakst misgaat: een verkeerd gekozen protocol betekent dat de omvormer de batterij niet ziet, en dat lijkt op een defect terwijl het een menu-instelling is. Het meest gemelde storingsbeeld is trouwens ook geen defect maar een montagepunt: een losgeraakte CAN-kabel tussen batterij en omvormer, waardoor de communicatie wegvalt en de stack niet meer meedoet. Laat die verbinding bij installatie borgen en labelen.

## Wat een systeem kost

Pylontech publiceert geen consumentenprijzen, en wij verzinnen ze niet. Wat wij wel kunnen zeggen: in het Europese distributiekanaal ligt de prijs per kilowattuur aan kale batterijhardware bij deze klasse duidelijk onder die van kant-en-klare systemen als Sessy of een Powerwall. Dat is een **marktrichtprijs, geen fabrikantsprijs** — vraag altijd een actuele offerte op.

Belangrijker dan de prijs per kWh is de vergelijkingsbasis. Bij Pylontech koop je alleen de opslag; bij Sessy of Tesla zit de omvormer, de behuizing, de app en de sturing in dezelfde doos. Vergelijk daarom op de totaalprijs van een wérkend systeem, inclusief omvormer, rack, materialen en arbeid. Doe je dat, dan blijft Pylontech doorgaans voordeliger, maar het verschil is kleiner dan de kale kWh-prijs suggereert.

Ter oriëntatie op de andere kant van het spectrum: Sessy publiceert wél prijzen. Charged noemt voor de 5 kWh-variant €3.550 en voor de 10 kWh-variant €5.500, inclusief btw en exclusief installatie; een basisinstallatie met noodstroom staat op €1.200 (prijspeil augustus 2026).

## Rendement: de omvormer bepaalt

Op batterijniveau haalt LFP een hoog rendement, maar dat is niet het getal dat op je jaarrekening staat. De omzetting van 48 V gelijkspanning naar 230 V wisselspanning kost enkele procenten, en bij een AC-gekoppelde opstelling gaat de zonnestroom eerst naar AC en daarna weer naar DC.

Een concreet rendementspercentage voor jouw combinatie geven wij daarom niet. Vraag de datasheet van je omvormer op — dat is de component die het verschil maakt, niet de batterij.

## Waar Pylontech sterk in is

**Prijs per kilowattuur.** Dit is het hoofdargument en het is een sterk argument, mits je de kosten van de omvormer eerlijk meetelt.

**Off-grid.** Een 48 V-systeem werkt naadloos met Victron- en Deye-omvormers die in eilandbedrijf kunnen. Voor recreatiewoningen, schuren en boten is dit de standaardkeuze.

**Modulariteit.** Tot 16 modules parallel is meer dan vrijwel elke concurrent toestaat. Voor een grote opslagbehoefte is dat relevant.

**Geen lock-in.** De batterij werkt met tientallen omvormermerken. Je kunt later van omvormer wisselen zonder de batterij te vervangen — het omgekeerde van wat er gebeurt bij een DC-gekoppeld merksysteem.

**Geen cloudafhankelijkheid.** Geen app die kan stoppen, geen server die kan verdwijnen, geen firmware-update die iets breekt. Dat is de keerzijde van het ontbreken van slimme functies, en voor sommige kopers een pluspunt.

## Waar Pylontech tekortschiet

**Geen consumenten-app.** Je bent volledig afhankelijk van de monitoring van je omvormer. Is die matig, dan heb je geen alternatief.

**Configuratie is geen consumentenwerk.** De protocolkeuze, de netcode-instellingen en de ESS-configuratie zijn installateurswerk.

**Geen automatische handel op dynamische prijzen.** De batterij doet uit zichzelf niets met de uurprijs. Wil je dat, dan bouw je het zelf via Home Assistant of een vergelijkbare laag bovenop de omvormer. Zie onze [vergelijking van dynamische energiecontracten](/posts/dynamische-energiecontracten-vergelijking-2026/) en de gids [dynamisch contract met thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

**Service loopt via de importeur.** Er is geen Nederlandse consumentendesk van Pylontech. Bij een claim is de importeur je aanspreekpunt en gaat er tijd overheen omdat onderdelen uit het Europese kanaal komen. Vraag je leverancier vooraf welke doorlooptijd hij toezegt.

## Voor wie is deze batterij bedoeld?

**Wel kiezen als:** je technisch onderlegd bent of een installateur met Pylontech-ervaring hebt; je off-grid bouwt; je een groot systeem wilt zonder de prijs van een kant-en-klaar merksysteem; je budget zwaarder weegt dan gebruiksgemak.

**Niet kiezen als:** je een systeem wilt dat uit de doos werkt; je een Nederlandse helpdesk wilt (dan is <a href="https://go.duurzaamthuislab.nl/sessy" target="_blank" rel="nofollow noopener">Sessy</a> de logische route); je vooral op de uurprijs wilt handelen (dan komen systemen met eigen sturing, zoals <a href="https://go.duurzaamthuislab.nl/marstek" target="_blank" rel="nofollow noopener">Marstek</a>, dichter bij wat je zoekt); je verbruik onder de 2.500 kWh per jaar ligt, want dan is een stack van 10 kWh overgedimensioneerd.

## Modelberekening: wat een stack kan opleveren

Onderstaande berekening is een **model met expliciete aannames**, geen meting. Uitgangspunt: een stack van circa 10 kWh met hybride omvormer en rack, een totale investering in de orde van €6.000, een woning met zonnepanelen, een dynamisch contract en sturing die via Home Assistant is ingericht.

- Besparing door hogere zon-zelfconsumptie: in dit model €510 per jaar
- Opbrengst uit prijsverschuiving op een dynamisch contract: in dit model €220 per jaar
- Samen circa €730 per jaar, en daarmee een terugverdientijd van rond de acht jaar

Wat dit model vooral laat zien: de lage prijs per kWh compenseert het ontbreken van slimme sturing alleen als je die sturing zelf inricht. Doe je dat niet, dan valt de tweede post weg en loopt de terugverdientijd fors op. Reken het door met je eigen verbruik via onze pagina [terugverdientijd thuisbatterij](/posts/thuisbatterij-terugverdientijd-berekenen-2026/).

## Saldering stopt per 1 januari 2027

De salderingsregeling stopt per 1 januari 2027 volledig. Er is geen afbouwpad: het wetsvoorstel met een geleidelijke afbouw is verworpen. Vanaf dat moment telt alleen nog wat je zélf verbruikt van je eigen opwek, plus wat je leverancier voor teruglevering betaalt.

Dat maakt zelfconsumptie de belangrijkste post in elke batterijberekening — ook bij Pylontech, mits je hybride omvormer correct is geconfigureerd. Meer daarover in onze [transitie-planner voor 2027](/posts/saldering-2027-transitie-planner/).

## Gedrag in lastige omstandigheden

**Stroomuitval.** De batterij schakelt niet zelf om. Of je bij een storing doorloopt, hangt volledig af van de omvormer: Deye-omvormers hebben een EPS-uitgang en Victron kan in eilandbedrijf. In beide gevallen krijg je een aparte noodstroomgroep, geen naadloze overname van het hele huis. Bepaal bij de installatie welke groepen op dat circuit komen.

**Vorst.** De batterij mag alleen binnen (IP20) en onder het vriespunt blokkeert het BMS het laden. Praktisch belangrijker is dat de opbrengst in die periode toch laag is: bij vorst en weinig zon maak je minder cycli, dus minder opbrengst. De batterij is dan niet de beperkende factor.

**Hoge gelijktijdige belasting.** Met 2.400 W continu per module loop je bij een enkele module snel tegen de grens aan. Draaien oven, vaatwasser en droger tegelijk, dan levert de batterij zijn maximum en vult het net de rest aan. Dat kost je geen besparing, maar je staat op zulke momenten niet los van het net.

## Waar je bij de aanschaf op moet letten

**Meng geen generaties.** Combineer geen US3000- met US5000-modules en geen modules uit verschillende generaties in één stack. BMS-firmware en energiedichtheid verschillen, en de zwakste module bepaalt het gedrag van het geheel. Koop alles in één keer, of koop een rack met ruimte voor identieke modules.

**Registreer de garantie.** Zeven jaar wordt tien jaar na registratie op het Pylontech-platform. Doe dat, en bewaar de bevestiging bij je installatiepapieren.

**Koop bij een Nederlandse of Europese leverancier.** Bij directe import uit China moet je bij een claim zelf internationaal verzenden, wat de garantie in de praktijk waardeloos maakt. Betaal het verschil.

**Reken op de omvormerkeuze als hoofdbeslissing.** Een Deye of Solis is de budgetroute; een Victron MultiPlus II is de keuze wanneer je noodstroom of echt eilandbedrijf wilt. Die keuze bepaalt meer aan je systeem dan het batterijmerk.

**Documenteer de configuratie.** Schrijf de protocolinstellingen en de netcode-instellingen op. Bij een vervanging of een firmware-update ben je daar blij mee.

## Nederlandse randvoorwaarden

Op een thuisbatterij betaalt een particulier 21 procent btw, en die is niet terug te vorderen. Het 0-procenttarief geldt uitsluitend voor zonnepanelen en de daarvoor direct noodzakelijke onderdelen — een accupakket valt daar volgens de Belastingdienst nadrukkelijk niet onder, ook niet bij gelijktijdige aanschaf.

Er is geen landelijke subsidie voor thuisbatterijen. Gemeentelijke en provinciale regelingen bestaan soms wel, maar wisselen per jaar; controleer dat bij je eigen gemeente en reken in je terugverdienberekening met de volle investering.

Voor een netgekoppelde installatie geldt een meldplicht bij de netbeheerder en moet de installatie voldoen aan NEN 1010 en de geldende netcode-eisen. Wij vonden geen wettelijke eis die een aparte technische ruimte of brandwerende afscheiding voorschrijft voor een stack boven 5 kWh — die claim circuleert wel, maar staat niet in het Besluit bouwwerken leefomgeving. Wat je verzekeraar eist, is een tweede vraag: leg de plaatsing vooraf voor en vraag schriftelijk bevestiging.

## Ons oordeel

Pylontech verkoopt geen belevenis maar opslag. Geen app, geen designbehuizing, geen marketing, geen algoritme dat 's nachts voor je handelt. Wat je krijgt is een stabiele LFP-module met een hoge cyclusverwachting, een openbaar protocol en de laagste prijs per kilowattuur van de merken die serieus in Nederland worden verkocht.

Die ruil is uitstekend voor wie de omvormer en de sturing zelf goed regelt — en slecht voor wie dat niet doet, want dan betaal je voor capaciteit die maar half wordt benut. Dat is geen productgebrek maar een keuze van de fabrikant, en het is precies de reden dat de prijs is wat hij is.

Lees ook [beste thuisbatterij eengezinswoning](/posts/beste-thuisbatterij-eengezinswoning-2026/), [thuisbatterij vergelijking 2026](/posts/thuisbatterij-vergelijking-2026/), [Sessy vs Marstek](/posts/sessy-vs-marstek-vergelijking-2026/) en [thuisbatterij subsidie 2026](/posts/thuisbatterij-subsidie-2026-overzicht/).

---

**Externe bron:** [RVO — ISDE voor woningeigenaren](https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren) — het officiële overzicht van welke maatregelen de ISDE wel en niet dekt (thuisbatterijen, zonnepanelen en laadpalen vallen er niet onder).
