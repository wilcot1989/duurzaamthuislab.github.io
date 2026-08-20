---
title: 'String-omvormer: met of zonder optimizers'
date: 2026-10-21 08:00:00+02:00
lastmod: 2026-08-20 08:00:00+02:00
description: 'String-omvormer, micro-omvormer of string met optimizers: wat het verschil technisch is, wanneer optimizers hun meerprijs verdienen en welke ontwerpgrenzen uit de datasheets in offertes zelden voorbijkomen.'
draft: false
categories:
- zonne-energie
tags:
- omvormer
- optimizers
- SolarEdge
- Huawei
- zonnepanelen
keywords:
- string omvormer
- string omvormer met optimizers
- optimizers zonnepanelen
- string omvormer of micro omvormer
- power optimizer nodig
- optimizers bij schaduw
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1509391366360-2e959784a276&w=1200&output=webp&q=70
faq:
- q: Wat is het verschil tussen een string-omvormer en een micro-omvormer?
  a: 'Bij een string-omvormer staan de panelen in serie geschakeld en zet één centraal apparaat de gelijkspanning van de hele reeks om naar 230 V wisselspanning. Bij een micro-omvormer zit er onder elk paneel een eigen omvormertje dat daar al naar wisselspanning omzet. Het praktische gevolg: een string-omvormer regelt op reeksniveau, een micro-omvormer per paneel — en een string-omvormer is één apparaat dat kan uitvallen, waar micro-omvormers over het dak verdeeld zijn.'
- q: Heb ik optimizers nodig bij mijn zonnepanelen?
  a: 'Dat hangt van je dak af, niet van het merk. Op één schaduwvrij dakvlak met dezelfde oriëntatie voegt paneelniveau-optimalisatie weinig opbrengst toe; de winst zit dan vooral in monitoring per paneel. Heb je harde schaduw van een schoorsteen, dakkapel of boom op enkele panelen, of meerdere dakvlakken met verschillende hellingen en richtingen, dan wordt optimalisatie per paneel functioneel. Vraag je installateur om het schaduwverloop per dakvlak te onderbouwen.'
- q: Hoeveel opbrengst leveren optimizers extra op?
  a: 'Huawei noemt op de datasheet van de Smart Module Controllers een bereik van 5 tot 30 procent en zet daar zelf een disclaimer bij: de waarden zijn gemeten door een intern laboratorium in een specifieke omgeving en werkelijke waarden kunnen afwijken. Wij lezen die 30 procent daarom als bovengrens bij ongunstige schaduw en niet als iets wat op een vrij dak haalbaar is. Wij hebben zelf geen opbrengstmetingen gedaan; harde getallen voor jouw dak horen uit een schaduwsimulatie van de installateur te komen.'
- q: Zijn optimizers bij SolarEdge optioneel?
  a: 'Nee. In een SolarEdge-systeem hoort onder elk paneel een power optimizer; de omvormer werkt niet zonder. Bij Huawei is het omgekeerd: de Smart Module Controllers zijn een optie die je gericht kunt plaatsen op de panelen die het nodig hebben. Dat verschil in filosofie bepaalt hoe de kosten zich opbouwen bij een schaduwvrij dak.'
- q: Wat is de minimale stringlengte en waarom is dat belangrijk?
  a: 'De minimale stringlengte is het kleinste aantal panelen dat op één reeks mag zitten. Volgens de S-serie datasheet van SolarEdge geldt bij de S440 en S500 op een 1-fase Home Wave- of Home Hub-omvormer een minimum van 8 optimizers en een maximum van 25. Huawei noemt met optimizers een minimum van 4 bij de L1-serie en 6 bij de M1-, M5- en MB0-series. Bij een klein dakvlak van zes panelen kun je die ondergrens dus niet halen en moet het ontwerp anders — dat is een reëel ontwerpprobleem dat pas op de montagedag opduikt als er niet naar gekeken is.'
schema_type: Article
---
*Disclosure: de merken in dit artikel (SolarEdge, Huawei, Enphase) worden hier redactioneel besproken — wij hebben met geen van deze partijen een affiliate- of commissierelatie. Wij baseren ons op fabrieksdatasheets, handleidingen en publieke documentatie.*

De vraag "string-omvormer met of zonder optimizers?" komt in offertes bijna altijd als prijsverschil langs: variant A met een gewone string-omvormer, variant B met dezelfde omvormer plus een kastje onder elk paneel en een meerprijs van vaak vier cijfers. Wat er technisch achter zit, staat er zelden bij.

Dit artikel legt de drie architecturen naast elkaar en gebruikt daarvoor de harde waarden uit de fabrieksdatasheets. Wij hebben deze systemen niet zelf gemeten; waar een getal een fabrieksopgave is, staat dat erbij.

> **Kort antwoord:** een string-omvormer regelt op reeksniveau, optimizers en micro-omvormers regelen per paneel. Op één schaduwvrij dakvlak met dezelfde oriëntatie levert paneelniveau-regeling weinig extra opbrengst en betaal je vooral voor monitoring.
>
> Optimizers verdienen hun meerprijs bij harde schaduw op enkele panelen of bij een mix van dakvlakken met verschillende hellingen en richtingen. Bij SolarEdge zijn ze verplicht onderdeel van het systeem, bij Huawei een optie die je gericht plaatst.

## De drie architecturen in één alinea elk

**String-omvormer.** De panelen staan in serie. De omvormer zoekt met een MPP-tracker het optimale werkpunt voor de hele reeks. Eén apparaat, weinig componenten op het dak, de laagste aanschafprijs. De beperking: het werkpunt is een compromis over alle panelen in die string.

**String-omvormer met optimizers.** Onder elk paneel (of onder de panelen die het nodig hebben) zit een DC-DC-regelaar die het maximum power point van dát paneel regelt en de spanning naar de omvormer normaliseert. De centrale omvormer blijft, maar krijgt een gelijkmatiger aanbod en inzicht per paneel.

**Micro-omvormer.** Onder elk paneel zit een volledige omvormer die daar al naar 230 V wisselspanning omzet. Er ligt geen hoogspanning-gelijkstroom meer op het dak en er is geen centraal apparaat dat het hele systeem stillegt als het uitvalt. De uitgebreide vergelijking van die route staat in [micro-omvormer versus string-omvormer](/posts/micro-omvormer-vs-string-omvormer-2026/).

## Waarom een string het compromis is

In een serieschakeling loopt door alle panelen dezelfde stroom. Het paneel dat het minst presteert, bepaalt daarmee mede de stroom van de hele reeks. Dat is de kern van het schaduwprobleem, en het is ook waarom de vaak gehoorde formulering "één blad legt je hele dak stil" te grof is: moderne panelen hebben bypass-diodes die het aangetaste deel van het paneel overbruggen, dus het effect is een terugval en geen uitval.

De omvang van die terugval hangt af van twee dingen: hoe hard de schaduw is en hoeveel panelen erdoor geraakt worden ten opzichte van de stringlengte. Diffuse schaduw van een verre boom is een andere situatie dan de harde slagschaduw van een schoorsteen die 's ochtends over drie panelen trekt. Wie wil weten wat dat voor de jaaropbrengst betekent, kan de vertrekpunten narekenen met onze [rekenhulp voor zonnepaneel-opbrengst](/zonnepanelen-opbrengst-berekenen/).

Het tweede compromis is minder bekend: het aantal MPP-trackers. Een string-omvormer met twee trackers kan twee dakvlakken onafhankelijk regelen. Bij een oost-westopstelling is dat precies genoeg — één tracker per zijde. Bij drie of meer dakvlakken met verschillende hellingen en richtingen loopt het krap, en dat is het punt waarop regeling per paneel functioneel wordt in plaats van een luxe.

## Wat de SolarEdge-datasheet zegt

SolarEdge levert een systeem waarin de optimizer geen optie is: onder elk paneel hoort er een, en de omvormer werkt niet zonder. De S-serie datasheet (S440 / S500 / S500B / S650B, versiedatum 19 mei 2025) geeft deze waarden:

| Specificatie | Waarde |
|---|---|
| Nominaal DC-ingangsvermogen | 440 W (S440), 500 W (S500/S500B), 650 W (S650B) |
| Voor installaties na 1 april 2024 | S440 490 W, S500 en S500B 550 W |
| Maximaal rendement | 99,5% |
| Gewogen rendement | 98,6% |
| Veiligheidsspanning in stand-by | 1 V per optimizer |
| Beschermingsklasse | IP68 |
| Bedrijfstemperatuur | –40 tot +85 °C |
| Garantie | 25 jaar |

Drie observaties. Het nominale ingangsvermogen bepaalt welk paneel eronder past: een paneel van 550 Wp hoort niet onder een optimizer met 440 W nominaal. Dat gewogen rendement van 98,6 procent is een verlies dat je in ruil voor de optimalisatie inlevert — bij een schaduwvrij dak staat daar dus vrijwel geen opbrengstwinst tegenover. En die 1 V in stand-by is het veiligheidsargument: brandweer en installateur hebben bij dit systeem niet met honderden volt op het dak te maken.

De datasheet noemt ook ontwerpgrenzen. Voor een 1-fase Home Wave- of Home Hub-omvormer geldt bij de S440 en S500 een minimale stringlengte van 8 optimizers en een maximum van 25. Wie zes panelen op één dakvlak wil leggen, haalt die ondergrens niet.

## Wat de Huawei-datasheet zegt

Huawei noemt zijn optimizers Smart Module Controllers: de SUN2000-450W-P2 en de SUN2000-600W-P (datasheet versienummer 02-202311). Het verschil met SolarEdge is niet de techniek maar de systeemfilosofie — ze zijn optioneel. Ligt één paneel in de ochtendschaduw van een schoorsteen en de rest vrij, dan zet je er één onder dat paneel en niet twaalf.

Ook hier gelden ontwerpgrenzen die zelden in een offerte staan: met optimizers is de minimale stringlengte bij de L1-serie 4 en bij de M1-, M5- en MB0-series 6, met een maximum van 25. En het nominale ingangsvermogen van 450 W respectievelijk 600 W bepaalt weer welk paneeltype eronder past — een 550 Wp-paneel onder een 450W-P2 is niet correct gedimensioneerd. De volledige beoordeling van die lijn staat in onze [Huawei SUN2000-review](/posts/huawei-sun2000-omvormer-review-2026/), en de directe merkvergelijking in [SolarEdge versus Enphase](/posts/solaredge-vs-enphase-2026/).

## Wanneer optimizers lonen — en wanneer niet

**Wel:**

- **Harde schaduw op enkele panelen.** Een schoorsteen, dakkapel, antenne of naburig gebouw dat een deel van de dag slagschaduw geeft. De winst is het grootst als het om een klein deel van de panelen gaat in een lange string.
- **Een mix van oriëntaties en hellingen.** Drie of meer dakvlakken die je met twee MPP-trackers niet meer netjes kunt scheiden.
- **Wanneer je paneelniveau-inzicht nodig hebt.** Alleen met monitoring per paneel kun je aantonen dat één specifiek paneel structureel achterblijft. Dat is in de praktijk de enige manier om een garantieclaim onderbouwd in te dienen.
- **Wanneer de veiligheidsspanning meeweegt**, bijvoorbeeld bij een rieten kap of een monumentaal pand waar de brandweereis zwaarder telt.

**Niet:**

- **Één schaduwvrij dakvlak, één oriëntatie.** Hier ruil je een klein conversieverlies in voor een optimalisatie die er niets te optimaliseren vindt. Het argument dat overblijft is monitoring, en dat is een gemaksafweging.
- **Wanneer de meerprijs de opbrengstwinst niet kan halen.** Reken het door: meerprijs gedeeld door de verwachte extra jaaropbrengst in euro's. Komt dat boven de verwachte levensduur uit, dan koop je iets anders dan opbrengst.
- **Als de installateur de schaduw niet kan onderbouwen.** Zonder schaduwsimulatie per dakvlak is "voor de zekerheid optimizers" een prijsverhoging zonder motivering.

## Wat dit betekent voor betrouwbaarheid

Meer componenten op het dak betekent meer aansluitingen die kunnen falen — dat is een reëel nadeel van elke vorm van paneelniveau-elektronica. Daar staat tegenover dat SolarEdge 25 jaar garantie op de optimizers geeft, ruim boven de standaardgarantie op de centrale omvormer, en dat een falende optimizer één paneel raakt in plaats van het hele systeem.

Bij een string-omvormer zonder optimizers is het risico omgekeerd verdeeld: minder componenten, maar één apparaat waarvan uitval het hele systeem stillegt. Welke foutmeldingen daarbij horen en wat je zelf kunt nakijken, staat in ons overzicht van [omvormer-storingen en foutcodes](/posts/omvormer-storing-foutcodes-2026/).

## Conclusie

De keuze is geen merkenkwestie maar een dakkwestie. Op één vrij dakvlak met dezelfde oriëntatie is een gewone string-omvormer technisch de logische keuze en betaal je bij optimizers vooral voor monitoring. Bij harde schaduw op een deel van de panelen of bij drie of meer dakvlakken kantelt dat, en dan is regeling per paneel — via optimizers of via micro-omvormers — een onderbouwde meerprijs.

Vraag daarom in elke offerte om drie dingen: de schaduwsimulatie per dakvlak, het aantal MPP-trackers van de voorgestelde omvormer en de gecontroleerde koppeling tussen paneelvermogen en optimizertype. Die drie antwoorden maken het prijsverschil tussen variant A en variant B beoordeelbaar; zonder die antwoorden is het een aanname.
