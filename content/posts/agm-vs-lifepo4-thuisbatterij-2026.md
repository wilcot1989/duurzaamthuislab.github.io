---
title: 'AGM vs LiFePO4 2026: welke batterijchemie voor welk gebruik?'
date: '2026-08-30 08:00:00+02:00'
lastmod: '2026-08-21 08:00:00+02:00'
draft: false
description: AGM (loodzuur) is goedkoop per nominale kWh, LiFePO4 gaat veel langer mee en mag dieper leeg. De chemie vergeleken op cycli, DoD, veiligheid, gewicht en toepassing.
categories:
- thuisbatterijen
tags:
- agm
- lifepo4
- batterijchemie
- off-grid
keywords:
- agm vs lifepo4
- lifepo4 thuisbatterij
- agm batterij thuis
- batterij chemie vergelijking
- lithium ijzer fosfaat
affiliate: true
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: Wat is het verschil tussen AGM en LiFePO4?
  a: 'AGM is een loodzuuraccu waarbij het zuur in glasvezelmatten is opgenomen; LiFePO4 is lithium-ijzerfosfaat. De drie verschillen die praktisch uitmaken: AGM mag doorgaans tot circa 50% worden ontladen en LiFePO4 tot 80-90%, LiFePO4 haalt volgens fabrikantopgaven een veelvoud van het aantal cycli, en LiFePO4 weegt bij gelijke bruikbare capaciteit een fractie van AGM. Daar staat een hogere aanschafprijs per nominale kWh tegenover.'
- q: Hoeveel cycli haalt elk van de twee?
  a: 'Kijk altijd in het datasheet van het specifieke model, want de spreiding tussen fabrikanten is groot en de opgave hangt af van de gebruikte ontlaaddiepte. De ordegrootte: AGM-datasheets geven bij dagelijks cyclisch gebruik op 50% DoD enkele honderden tot ruim duizend cycli, LiFePO4 doorgaans enkele duizenden tot ruim 6.000 cycli tot 80% restcapaciteit. Een cyclusopgave zonder bijbehorende DoD is waardeloos.'
- q: Welke chemie is veiliger?
  a: 'Ze hebben verschillende risico''s. AGM kan bij overladen waterstofgas afgeven, dus een geventileerde opstelling is nodig; het chemische risico op thermische runaway is er niet. LiFePO4 is binnen de lithiumfamilie de variant met de hoogste thermische stabiliteit — beduidend stabieler dan NMC — maar staat of valt bij een goed werkend batterijmanagementsysteem. "Geen enkel risico" bestaat bij geen van beide.'
- q: Mag ik AGM en LiFePO4 parallel gebruiken?
  a: 'Nee. De laadspanningen, de laadcurve en de manier waarop de spanning tijdens ontladen verloopt zijn te verschillend, en een BMS kan niet zien wat de loodaccu doet. Het resultaat is dat één van de twee structureel verkeerd wordt geladen. Vervang bij overstap altijd de hele bank en check of je omvormer of laadregelaar een LiFePO4-laadprofiel heeft.'
- q: Kan ik LiFePO4 in een onverwarmde ruimte plaatsen?
  a: 'Ontladen kan onder nul meestal wel, laden niet: onder het vriespunt laden veroorzaakt lithiumplating en dus permanente celschade. Veel modules hebben daarom een BMS dat laden bij lage temperatuur blokkeert, en sommige hebben cel-verwarming. Voor een schuur of garage die kan bevriezen, kijk je naar de bedrijfstemperatuur voor laden in het datasheet — niet naar de opslagtemperatuur.'
schema_type: Article
last_updated: '2026-08-21'
---
*Disclosure: dit artikel bevat één affiliate link, naar Renogy. Als je via die link iets koopt, kunnen wij een commissie ontvangen — dat kost jou niets extra en het verandert niets aan wat er in dit artikel staat. Met de andere merken die genoemd worden hebben wij geen affiliate- of commissierelatie. Wij vergelijken op basis van datasheets, handleidingen en publieke data.*

AGM en LiFePO4 zijn geen twee prijsklassen van hetzelfde product. Het zijn twee chemieën met een ander gedrag bij ontladen, bij kou, bij lang stilstaan en bij overladen — en die verschillen bepalen voor welke toepassing ze geschikt zijn. Dit artikel vergelijkt ze op de eigenschappen die er praktisch uitmaken, en behandelt daarna waar elk van de twee thuishoort: camper en off-grid tegenover een netgekoppelde thuisbatterij.

> **Kort antwoord:** vergelijk niet op prijs per nominale kWh maar op prijs per bruikbare kWh maal het aantal cycli. AGM mag doorgaans tot de helft leeg en haalt enkele honderden tot ruim duizend cycli; LiFePO4 mag tot 80-90% leeg en haalt daar een veelvoud van. Daardoor is AGM alleen nog logisch bij weinig cycli, een klein budget en een koude standplaats — en LiFePO4 in vrijwel elk scenario waarin je dagelijks laadt en ontlaadt.

## De chemie naast elkaar

| Eigenschap | AGM (loodzuur) | LiFePO4 (lithium-ijzerfosfaat) |
|---|---|---|
| Bruikbare ontlaaddiepte (DoD) | doorgaans circa 50% voor acceptabele levensduur | doorgaans 80-90% |
| Cycli volgens datasheets | enkele honderden tot ruim 1.000 bij 50% DoD | enkele duizenden tot ruim 6.000 tot 80% restcapaciteit |
| Energiedichtheid | laag; ordegrootte enkele tientallen Wh per kg | hoog; ordegrootte drie tot vier keer AGM |
| Gedrag bij ontladen | spanning zakt geleidelijk; capaciteit valt terug bij hoge stroom (Peukert) | vlakke spanningscurve tot bijna leeg; nauwelijks capaciteitsverlies bij hoge stroom |
| Laadsnelheid | traag, met een lange absorptiefase | snel, tot hoge C-rates afhankelijk van model |
| Zelfontlading bij stilstand | relatief hoog; sulfatering bij lang leeg staan | laag; lang stilstaan is minder schadelijk |
| Laden onder 0 °C | mogelijk, met verminderde opname | **niet toegestaan** zonder cel-verwarming of BMS-blokkade |
| Veiligheidsrisico | waterstofgas bij overladen; ventilatie nodig | vereist werkend BMS; thermisch stabielste lithiumvariant |
| Onderhoud | terminalcorrosie, spanning per accu monitoren | in de praktijk geen; wel BMS-uitlezing wenselijk |
| Prijs per nominale kWh | het laagst van alle chemieën | een meervoud van AGM |
| Prijs per bruikbare kWh over de levensduur | het hoogst zodra je dagelijks cyclet | het laagst bij cyclisch gebruik |

Twee dingen bij deze tabel. De cyclusopgaven komen uit fabrikantendatasheets en zijn niet onderling vergelijkbaar tenzij ze bij dezelfde DoD en dezelfde temperatuur zijn opgegeven — een opgave "6.000 cycli" zonder DoD zegt niets. En de prijzen laten wij bewust in relatieve termen staan: de spreiding tussen leveranciers is groot en de prijzen bewegen, dus reken met de actuele dealerprijs van het specifieke model.

## Waarom je op bruikbare kWh moet rekenen

De vergelijking gaat mis zodra je nominale capaciteiten naast elkaar zet. Een voorbeeld met expliciete aannames, geen meting:

**Modelberekening.** Een AGM-bank van 4 × 200 Ah bij 12 V is nominaal 9,6 kWh.

- Bij een ontlaaddiepte van 50% (wat de datasheets voor acceptabele levensduur aanhouden): **4,8 kWh bruikbaar** in nieuwstaat.
- Na een aantal jaren cyclisch gebruik, bij 60% resterende capaciteit: **circa 2,9 kWh bruikbaar**.
- Een LiFePO4-module van 4,8 kWh nominaal geeft bij 90% DoD **circa 4,3 kWh bruikbaar**, en houdt dat volgens de datasheets veel langer vast.

Voor ongeveer hetzelfde volume in het rek levert de LiFePO4-module dus meer bruikbare kWh dan de nieuwe AGM-bank, en een veelvoud van de verouderde bank. Tel daar het gewichtsverschil bij op — voor een camper of boot vaak de beslissende factor — en de vergelijking op nominale capaciteit wordt onbruikbaar.

Reken bij een keuze dus altijd: **prijs ÷ (bruikbare kWh × verwacht aantal cycli)**. Dat is de enige getalsmatige vergelijking die tussen de twee chemieën standhoudt.

## Camper, boot en off-grid: hier speelt de keuze echt

In een camper, op een boot of in een off-gridopstelling koop je losse accu's en bouw je zelf de bank. Dat is de context waarin AGM nog een positie heeft, en waarin de afweging per gebruikspatroon verschilt.

**AGM blijft verdedigbaar als:**

- je enkele keren per maand kort ontlaadt in plaats van dagelijks;
- de accu 's winters in een onverwarmde loods of op een koude standplaats staat en er tussendoor geladen moet worden;
- het budget klein is en het gaat om een beperkte bank;
- er geen ruimte of behoefte is voor een BMS en bijbehorende monitoring.

**LiFePO4 is vrijwel altijd de betere keuze als:**

- je dagelijks laadt en ontlaadt (vrijwel elk campergebruik in het seizoen, elk off-gridhuisje);
- gewicht of volume beperkt is — het verschil is een factor drie tot vier;
- je omvormer of inductiekookplaat kortdurend een hoge stroom vraagt: AGM levert dan minder bruikbare capaciteit dan het datasheet bij lage stroom suggereert;
- de bank soms weken ongebruikt staat: sulfatering is bij loodzuur een reëel risico, bij LiFePO4 nauwelijks.

Wat er in beide gevallen bij hoort: een laadregelaar of omvormer die het juiste laadprofiel ondersteunt. Niet elke oudere MPPT-regelaar of omvormer heeft een LiFePO4-profiel; check dat vóór aanschaf, want een AGM-laadcurve op een LiFePO4-bank betekent structureel verkeerd laden.

Renogy is een van de partijen die zowel AGM- als LiFePO4-accu's voor camper- en off-gridgebruik levert, inclusief laadregelaars en zonnepanelen voor dezelfde toepassing — praktisch als je één laadprofiel over de hele set wilt houden. Specificaties, capaciteiten en actuele prijzen per model staan op de eigen site.

<a href="https://go.duurzaamthuislab.nl/renogy?ref=/posts/agm-vs-lifepo4-thuisbatterij-2026/" class="cta cta-affiliate" rel="noopener nofollow sponsored" target="_blank">Bekijk het accu-assortiment van Renogy</a>

## Thuisbatterij aan het net: een andere productcategorie

Voor een netgekoppelde thuisbatterij is de chemievraag in de praktijk al beantwoord. De systemen die in Nederland als kant-en-klare thuisbatterij worden verkocht, zijn nagenoeg allemaal LiFePO4, en je koopt daar geen losse cellen maar een compleet systeem: accu, omvormer, BMS, behuizing, app en garantie in één. AGM speelt in die categorie geen rol meer — niet omdat de chemie niet werkt, maar omdat de cycluseis van dagelijks laden en ontladen AGM binnen enkele jaren opbrandt.

De relevante vraag verschuift daarmee van "welke chemie" naar "welke maat en rendeert het". Ter ijking, met de canonieke aannames uit ons rekenmodel: een verschoven kWh is €0,202 waard (inkoop op een passief profiel €0,272 minus een terugleververgoeding-aanname van €0,07 vanaf 2027), bij 150 bruikbare zoncycli per jaar en 90% retourrendement, plus €8 per kWh capaciteit per jaar aan netarbitrage op een dynamisch contract. Dat komt uit op **€177 per jaar bij 5 kWh, €353 bij 10 kWh en €530 bij 15 kWh**.

Zet je dat tegen de prijzen van Sessy — €3.550 voor 5 kWh, €5.500 voor 10 kWh en €9.400 voor de Plus met 15 kWh, inclusief btw en exclusief installatie (prijspeil augustus 2026, sessy.nl) — dan liggen de terugverdientijden in het model tussen ruim vijftien en twintig jaar. Dat is de enige terugverdientijd die wij hier noemen; kortere getallen in oudere versies van dit artikel rustten op te hoge spreads.

Hoe je de maat bepaalt en welke van de drie grenzen bij jou bindt, staat in [thuisbatterij grootte berekenen](/posts/thuisbatterij-grootte-berekenen-2026/). De gevoeligheid van de aannames werken we uit in [de terugverdientijdvergelijking](/thuisbatterij-terugverdientijd-vergelijken/).

Wat verder geldt voor de thuiscategorie: op een thuisbatterij is het reguliere btw-tarief van 21% van toepassing — de 0%-regeling geldt alleen voor zonnepanelen en direct noodzakelijke onderdelen — en de ISDE dekt thuisbatterijen niet.

## Zelfbouw: waar het misgaat

Een bank zelf samenstellen is technisch goed te doen, maar er zijn drie punten waarop het in de praktijk vastloopt:

1. **Verzekering en garantie.** Bij zelfbouw is er geen systeemgarantie en kan een verzekeraar vragen stellen bij schade. Voor een netgekoppelde installatie in een woning is dat een reden om voor een kant-en-klaar systeem te kiezen.
2. **De installatie zelf.** De aansluiting op de woninginstallatie is werk voor een installateur, en de eisen daarvoor volgen uit de installatienormen — niet uit de handleiding van de accu.
3. **Het BMS is geen accessoire.** Een LiFePO4-bank zonder werkend, uitleesbaar BMS kun je bij celafwijking niet diagnosticeren; je merkt het pas als de capaciteit al is ingezakt. Kies dus een BMS dat je per cel kunt uitlezen.

## Vijf fouten bij de keuze

1. **AGM kopen om de instapprijs.** Per bruikbare kWh-cyclus is AGM bij dagelijks gebruik veelvouden duurder over de levensduur.
2. **Cyclusopgaven zonder DoD vergelijken.** 1.000 cycli bij 50% en 3.000 cycli bij 90% zijn geen vergelijkbare getallen; reken ze eerst om naar bruikbare kWh over de levensduur.
3. **LiFePO4 zonder uitleesbaar BMS kopen.** Zie hierboven: je kunt niets diagnosticeren.
4. **Laden onder het vriespunt.** Dit is de meest voorkomende oorzaak van vroegtijdige celschade bij LiFePO4 in campers en schuren. Check de bedrijfstemperatuur voor **laden**, niet die voor opslag.
5. **Chemieën mengen of een oude laadregelaar hergebruiken.** Verkeerd laadprofiel, structureel verkeerd geladen bank.

## Conclusie

Voor dagelijks cyclisch gebruik — camper in het seizoen, off-gridwoning, thuisbatterij — is LiFePO4 de rationele keuze: dieper ontlaadbaar, veel meer cycli, lichter en per bruikbare kWh over de levensduur goedkoper. AGM houdt één duidelijk domein over: weinig cycli, klein budget, koude standplaats, geen behoefte aan monitoring. Een caravan of boot die 's winters in de loods staat en een paar keer per maand wordt gebruikt, is daar het schoolvoorbeeld van.

En voor de netgekoppelde thuisbatterij is de chemie niet meer de vraag. Die vraag is: hoeveel kWh kun je daadwerkelijk verschuiven, en wat is dat waard tegen de aanschafprijs. Dat blijft, ook met de beste chemie, een krappe rekensom.

---

*Dit artikel is voor het laatst bijgewerkt op 21 augustus 2026 door de redactie van DuurzaamThuisLab. Klopt er iets niet? Laat het ons weten — wij houden dit artikel actief bij.*

---

**Bronnen:** cyclus- en DoD-opgaven komen uit de datasheets van de betreffende fabrikanten; controleer altijd het specifieke model. Prijzen thuisbatterij: [sessy.nl](https://www.sessy.nl/), prijspeil augustus 2026, inclusief btw en exclusief installatie. Wat de ISDE wel en niet dekt: [RVO — ISDE voor woningeigenaren](https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren) (thuisbatterijen vallen er niet onder). Geraadpleegd op 21 augustus 2026.
