---
title: "ROI thuisbatterij na saldering 2027: complete berekening"
date: 2026-08-11T08:00:00+02:00
lastmod: '2026-08-21 08:00:00+02:00'
description: "Een narekenbaar ROI-model voor een thuisbatterij na het einde van de saldering op 1-1-2027, met vier doorgerekende scenario's en een IRR die niet dubbeltelt."
categories: ["thuisbatterijen"]
tags: ["thuisbatterij", "ROI", "saldering 2027", "rendement", "berekening", "terugverdientijd"]
keywords: ["roi thuisbatterij 2027", "thuisbatterij rendement na saldering", "thuisbatterij berekening 2027", "terugverdientijd batterij saldering", "rendement thuisbatterij"]
affiliate: true
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1671785253964-bdb43087ed99&w=1200&output=webp&q=70"
schema_type: "Article"
faq:
  - q: "Wanneer verdient een thuisbatterij zich terug na het einde van de saldering?"
    a: 'Dat hangt bijna volledig af van de aanschafprijs. Ons model komt op een jaarwaarde van €353 voor een batterij van 10 kWh op een dynamisch contract, vanaf 1-1-2027: €273 zonverschuiving plus €80 netarbitrage. Bij een plug-in systeem van €2.898 is dat een terugverdientijd van 8,2 jaar; bij een vast ingebouwd systeem van €6.500 tot €7.500 is het 18,4 tot 21,2 jaar. Binnen een garantietermijn van tien jaar sluit de rekening pas onder circa €3.530.'
  - q: "Wat verandert er op 1-1-2027?"
    a: 'De saldering stopt volledig, in één keer. Er is geen afbouwpad: reeksen als 64/28/0 procent of 73/64/55/46 procent horen bij wetsvoorstellen die het niet hebben gehaald. Vanaf 1-1-2027 krijg je voor teruggeleverde stroom alleen nog de terugleververgoeding van je leverancier. Die is voor 2027 nog nergens gepubliceerd; wij rekenen met een aanname van €0,07 per kWh, expliciet gelabeld als aanname.'
  - q: "Hoe groot moet mijn batterij zijn?"
    a: 'Kijk naar wat je daadwerkelijk kunt verschuiven, niet naar je dak. In ons model haalt een batterij circa 150 volle cycli per jaar op zonoverschot, begrensd door je overschot en door wat je ''s avonds nog verbruikt. Een batterij van 10 kWh verschuift daarmee circa 1.500 kWh per jaar. Is je teruglevering kleiner dan dat, dan koop je capaciteit die stilstaat.'
  - q: "Werkt een batterij ook in de winter?"
    a: 'Voor zonverschuiving nauwelijks: in december is de opbrengst een fractie van die in juli en vult de batterij zich zelden. Wat in de winter wél kan, is netarbitrage op een dynamisch contract: laden op goedkope uren, ontladen op dure. Wij schatten dat op €80 per jaar bij 10 kWh, oftewel €8 per kWh capaciteit. Zonder dynamisch contract valt die component volledig weg.'
  - q: "Moet ik wachten tot batterijprijzen verder dalen?"
    a: 'Dat is een afweging, geen zekerheid — wij doen geen uitspraken over toekomstige prijzen. Wat wél vaststaat: elke maand die je in 2026 nog draait valt onder volledige saldering, dus in dat jaar levert een batterij vrijwel alleen arbitragewaarde op. De rekensom kantelt pas op 1-1-2027.'
  - q: "Tellen subsidies mee?"
    a: 'Nauwelijks. Er is geen landelijke subsidie op thuisbatterijen: de ISDE dekt voor woningeigenaren alleen isolatie, ventilatie (in combinatie met isolatie), (hybride) warmtepompen, zonneboilers, een warmtenetaansluiting en elektrisch koken. Sommige gemeenten of provincies hebben een eigen regeling; neem die alleen mee als je hem zwart-op-wit op de site van je eigen gemeente hebt gevonden. Btw-teruggaaf op de batterij is er voor particulieren niet.'
  - q: "Wat is een realistisch rendement?"
    a: 'Met de cashflows uit dit artikel komt de interne rentevoet over vijftien jaar uit op circa 6,7 procent bij een investering van €2.898, circa 3,9 procent bij €3.530 en negatief vanaf circa €4.850. Een thuisbatterij is dus geen belegging met een gegarandeerd rendement, maar een investering waarvan het resultaat volledig aan de inkoopprijs hangt. Dit is een modelberekening, geen financieel advies.'
  - q: "Mag ik dit aftrekken van de belasting?"
    a: 'Als particulier niet. Zakelijk kan de energie-investeringsaftrek (EIA) van toepassing zijn; die bedraagt in 2026 40 procent. Over een eventuele waardestijging van de woning door een thuisbatterij doen wij geen uitspraak: daar is geen publieke, controleerbare bron voor.'
---
*Disclosure: de twee links in dit artikel — naar EcoFlow en naar Anker Solix — zijn affiliate-links via het AWIN-netwerk: koop je daar iets, dan ontvangen wij mogelijk een commissie, zonder extra kosten voor jou. Sessy, Tibber en Frank Energie worden in de tekst genoemd maar niet commercieel gelinkt; met die partijen hebben wij geen commissierelatie. De berekeningen hieronder zijn gebaseerd op publieke EPEX-data, fabrikantspecificaties met peildatum en het feit dat de saldering per 1-1-2027 volledig stopt.*

Gaat een thuisbatterij geld opleveren, of doe je het uit principe? Dat is de vraag die telt, want het gaat om €1.600 tot €10.000. En het rekenwerk in offertes zit vaak twee fouten in: het rekent met een afbouwpad dat niet bestaat, en het telt dezelfde kilowattuur twee keer.

Dit artikel bevat één transparant rekenmodel, vier doorgerekende scenario's en een IRR die uit diezelfde cashflows volgt. De uitkomst is minder rooskleurig dan wat je in verkoopgesprekken hoort, en dat is precies het punt.

> **Kort antwoord:** De saldering stopt volledig op 1-1-2027. Vanaf dat moment is een batterij van 10 kWh in ons model €353 per jaar waard op een dynamisch contract. De terugverdientijd hangt daarna alleen nog aan wat je betaalt: 8,2 jaar bij €2.898, 18,4 tot 21,2 jaar bij €6.500 tot €7.500, bijna dertig jaar boven €10.000.

## Twee inkomsten, niet drie — en één telfout die overal terugkomt

Een batterij levert op twee manieren geld op. Veel calculators noemen er drie en tellen daarbij dezelfde kilowattuur dubbel.

### De telfout

De klassieke opzet is: (1) "je verhoogt je eigen verbruik met 1.980 kWh, dat is 1.980 × €0,26 = €515" en daarnaast (2) "je voorkomt saldering-verlies over diezelfde 1.980 kWh, dat is nog eens 1.980 × €0,19 = €376". Samen €891.

Dat is dubbeltelling. Het gaat om **dezelfde** kilowattuur, die je maar één keer kunt verzilveren. De juiste som is: die kWh levert je €0,26 op omdat je hem niet hoeft in te kopen, en kost je de terugleververgoeding die je misloopt omdat je hem niet teruglevert. Netto dus €0,26 − €0,07 = €0,19 per verschoven kWh, en niet €0,45. Correct je daarnaast voor het retourrendement van 90 procent, dan blijft er €0,182 over.

Bovendien geldt dat verschil **alleen vanaf 1-1-2027**. Zolang de saldering nog loopt, is teruggeleverde stroom net zoveel waard als afgenomen stroom en levert verschuiven vrijwel niets op.

### Inkomst 1: zonverschuiving (vanaf 1-1-2027)

Je slaat overdag overschot op en gebruikt het 's avonds zelf. Waarde per verschoven kWh: het leveringstarief minus de gemiste terugleververgoeding, gecorrigeerd voor het retourrendement.

### Inkomst 2: netarbitrage (alleen met een dynamisch contract)

In het winterhalfjaar, wanneer er geen zonoverschot is, kun je laden op goedkope uren en ontladen op dure. Dat vergt uurprijzen én automatische aansturing. Zie [dynamische energiecontracten en thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/) voor de strategie.

---

## Het rekenmodel

Dit is een **modelberekening met expliciete aannames**, geen prognose en geen advies. Peildatum 21 augustus 2026.

| Aanname | Waarde | Toelichting |
|---|---|---|
| Jaaropbrengst zonnepanelen | 900 kWh per kWp | Nederlands gemiddelde, zuid of oost-west |
| Direct eigen verbruik zonder batterij | 30% van de opbrengst | 20-25% als er overdag niemand thuis is, 40-50% met warmtepomp of EV die overdag afneemt |
| Leveringstarief stroom | **€0,26 per kWh** all-in incl. btw | Opgebouwd als (EPEX 2025 €0,105 + opslag-aanname €0,02 + energiebelasting €0,09161) × 1,21 |
| Terugleververgoeding vanaf 2027 | **€0,07 per kWh (aanname)** | Nog door geen enkele leverancier gepubliceerd; expliciet een aanname, geen tarief |
| Verschuifbaar volume batterij | capaciteit × 150 volle cycli per jaar | Begrensd door je overschot en door je avondverbruik. 10 kWh geeft circa 1.500 kWh per jaar |
| Retourrendement | 90% | Om 1.500 kWh te leveren laad je 1.667 kWh in |
| Netarbitrage | €8 per kWh capaciteit per jaar | Circa 100 extra wintercycli tegen €0,10 netto spreiding na omzetverliezen. Die spreiding is een marktgrootheid en hangt niet aan het all-in tarief. Alleen met dynamisch contract |
| Netbeheerkosten | buiten het model | Vast capaciteitstarief per jaar, verandert niet door een batterij |
| Degradatie | naar 80% restcapaciteit in 15 jaar, lineair | Conform de gangbare fabrieksgarantie |

**Basisformule per jaar, vanaf 1-1-2027:**

> waarde = (verschoven kWh × leveringstarief) − (ingeladen kWh × terugleververgoeding) + netarbitrage

Voor een batterij van 10 kWh: 1.500 × €0,26 − 1.667 × €0,07 + €80 = €390 − €117 + €80 = **€353 per jaar**. Bij een terugleververgoeding van €0,05 wordt dat €387, bij €0,10 wordt het €303.

### Zelf doorrekenen in zeven stappen

1. **Opwek** = kWp × 900 kWh. Bij noordligging of schaduw: × 700 tot 800.
2. **Direct eigen verbruik** = opwek × jouw fractie (30% als je het niet weet; haal je echte fractie uit je P1-data).
3. **Overschot** = opwek − direct eigen verbruik. **Afname van het net** = verbruik − direct eigen verbruik.
4. **Verschuifbaar** = het laagste van: capaciteit × 150, je overschot × 0,9, en je afname.
5. **Ingeladen** = verschuifbaar ÷ 0,9.
6. **Jaarwaarde** = verschuifbaar × €0,26 − ingeladen × €0,07, plus €8 per kWh capaciteit als je een dynamisch contract hebt.
7. **Terugverdientijd** = totale investering incl. btw en installatie ÷ jaarwaarde.

Wil je dit niet met de hand doen: de [saldering calculator 2027](/posts/saldering-calculator-2027-volledig/) rekent exact dit model door. Voor de bredere vergelijking, zie [thuisbatterij terugverdientijd berekenen](/posts/thuisbatterij-terugverdientijd-berekenen-2026/).

---

## Welke prijzen zijn publiek geverifieerd?

Alleen met een gepubliceerde prijs kun je een eerlijke ROI rekenen. Stand van zaken op 21-8-2026:

| Systeem | Capaciteit | Prijs incl. btw, excl. installatie | Bron |
|---|---|---|---|
| EcoFlow STREAM AC 5000 | 5 kWh, 3.000 W | €1.599 | nl.ecoflow.com |
| EcoFlow uitbreidingsaccu 5000 | +5 kWh | €1.299 | nl.ecoflow.com |
| Sessy | 5 kWh | €3.550 | fabrikant (Charged, Andelst) |
| Sessy | 10 kWh | €5.500 | fabrikant |
| Sessy Plus | 15 kWh | €9.400 | fabrikant |

Sessy rekent daarnaast €1.200 voor een noodstroom-basisinstallatie; laad- en ontlaadvermogen zijn 2,2 respectievelijk 1,7 kW en de fabrikant geeft 6.000+ cycli op.

Voor Marstek geldt dat de fabrikant maar één consumentenprijs publiceert (de Jupiter C Plus voor €599); voor de Venus- en E-lijn publiceert Marstek geen consumentenprijs, en de Nederlandse webshop staat op "coming soon". Wij nemen daarom geen Marstek-prijzen in dit model op. Datzelfde geldt voor Huawei, BYD en SolarEdge: die publiceren geen consumentenprijzen, alleen installateurs doen dat in een offerte.

Een tweede plug-in aanbieder met een Nederlandse winkel is Anker Solix. Op ankersolix.com/nl staat de Solarbank Max AC met 7 kWh en 3.500 W, uitbreidbaar tot 42 kWh (opgehaald 21-8-2026). Een vaste consumentenprijs publiceert Anker daar niet op de overzichtspagina — die staat per configuratie op de productpagina en wisselt met acties. Vul dus het bedrag in dat je op het bestelmoment ziet, en niet een actieprijs die inmiddels verlopen is.

<a href="https://go.duurzaamthuislab.nl/ecoflow" class="cta cta-affiliate" rel="sponsored nofollow noopener" target="_blank">Bekijk de actuele EcoFlow-prijzen</a>

<a href="https://go.duurzaamthuislab.nl/anker-solix" class="cta cta-affiliate" rel="sponsored nofollow noopener" target="_blank">Bekijk de actuele Anker Solix-prijzen</a>

---

## Vier doorgerekende scenario's

Alle vier vanaf 1-1-2027, met €0,26 all-in leveringstarief en de terugleververgoeding-aanname van €0,07, tenzij anders vermeld.

### Scenario A: klein huishouden, 5 kWh plug-in

- Verbruik 2.500 kWh · 3 kWp (2.700 kWh opwek)
- Direct eigen verbruik 810 kWh · overschot 1.890 kWh · afname 1.690 kWh
- Verschuifbaar: het laagste van 5 × 150 = 750, 1.890 × 0,9 = 1.701 en 1.690 → **750 kWh**
- Ingeladen: 833 kWh

**Jaarwaarde:** 750 × €0,26 − 833 × €0,07 = €195 − €58 = **€137**, plus €40 arbitrage met een dynamisch contract = **€177**.

**Terugverdientijd** bij €1.599 (EcoFlow STREAM AC 5000): €1.599 / €177 = **9,0 jaar**. Zonder dynamisch contract: 11,7 jaar.

Grensgeval, en het is de aanschafprijs die het kantelt: bij een vast systeem van €3.550 wordt dit 20,1 jaar.

### Scenario B: gemiddeld huishouden, 10 kWh

- Verbruik 3.500 kWh · 4,5 kWp (4.050 kWh opwek)
- Direct eigen verbruik 1.215 kWh · overschot 2.835 kWh · afname 2.285 kWh
- Verschuifbaar: het laagste van 1.500, 2.552 en 2.285 → **1.500 kWh**
- Ingeladen: 1.667 kWh

**Jaarwaarde:** 1.500 × €0,26 − 1.667 × €0,07 = €390 − €117 = **€273**, plus €80 arbitrage = **€353**.

| Investering | Systeem | Terugverdientijd |
|---|---|---|
| €2.898 | EcoFlow STREAM AC 5000 + uitbreidingsaccu, plug-in | 8,2 jaar |
| €5.500 | Sessy 10 kWh, excl. installatie | 15,6 jaar |
| €7.000 | Vast ingebouwd systeem incl. installatie | 19,8 jaar |
| €10.500 | 13,5 kWh all-in-one incl. installatie | 29,7 jaar |

De extra capaciteit boven 10 kWh helpt in dit profiel niet: het verschuifbare volume zit al tegen de grens van wat er 's zomers over is.

### Scenario C: warmtepomp en EV, 15 kWh

- Verbruik 7.500 kWh (warmtepomp 3.000 + EV 2.500 + huishouden 2.000) · 8 kWp (7.200 kWh opwek)
- Direct eigen verbruik 40% = 2.880 kWh (warmtepomp en EV nemen al overdag af) · overschot 4.320 kWh · afname 4.620 kWh
- Verschuifbaar: het laagste van 15 × 150 = 2.250, 3.888 en 4.620 → **2.250 kWh**
- Ingeladen: 2.500 kWh

**Jaarwaarde:** 2.250 × €0,26 − 2.500 × €0,07 = €585 − €175 = **€410**, plus €120 arbitrage = **€530**.

Dit is het gunstigste profiel van de vier, omdat er zowel veel overschot als veel avondverbruik is. Toch: bij een Sessy Plus 15 kWh van €9.400 excl. installatie is de terugverdientijd **17,7 jaar**. Bij drie gekoppelde EcoFlow-modules van samen 15 kWh (€1.599 + 2 × €1.299 = €4.197) is het **7,9 jaar**.

Ook hier is de conclusie dus niet "een batterij loont bij dit profiel", maar "bij dit profiel loont een goedkope batterij".

### Scenario D: geen dynamisch contract

Zelfde profiel als B, maar met een vast contract van €0,34 per kWh en dus geen arbitrage.

**Jaarwaarde:** 1.500 × €0,34 − 1.667 × €0,07 = €510 − €117 = **€393**.

Interessant detail: het hogere leveringstarief compenseert het wegvallen van de arbitrage ruim (€393 tegenover €353). Wie een duur vast contract heeft, verliest dus niets aan het missen van arbitrage — het tarief zelf weegt zwaarder. Wat een dynamisch contract oplevert is optionaliteit, niet een hoger rendement per definitie.

**Terugverdientijd** bij €5.500: 14,0 jaar. Bij €2.898: 7,4 jaar.

---

## IRR: wat het model over vijftien jaar oplevert

Terugverdientijd negeert de tijdswaarde van geld. Voor wie in rendement denkt, hier dezelfde cashflows uitgedrukt als interne rentevoet.

**Cashflow-aannames**, voor het profiel uit scenario B:
- Jaar 1 (2026): €80. De saldering loopt nog, dus alleen arbitrage telt mee
- Jaar 2 (2027): €353, daarna jaarlijks dalend met de degradatie tot €282 in jaar 16
- Restwaarde na 15 jaar: €0
- Geen onderhoudskosten meegerekend; zie de kanttekening hieronder

**Uitkomst:**

| Investering | Cumulatief na 15 jaar | Interne rentevoet |
|---|---|---|
| €2.898 (plug-in 10 kWh) | + €1.945 | circa 6,7% |
| €3.530 (grens voor 10 jaar terugverdientijd) | + €1.313 | circa 3,9% |
| €4.197 (3× EcoFlow-module, 15 kWh) | + €646 | circa 1,7% |
| €5.500 (Sessy 10 kWh, excl. installatie) | − €657 | circa −1,4% |
| €6.500 (Sessy 10 kWh + installatie) | − €1.657 | circa −3,3% |
| €7.000 (vast systeem incl. installatie) | − €2.157 | circa −4,0% |

De totale opbrengst over vijftien jaar bedraagt in dit model **€4.843**. Dat getal is het break-evenpunt: elke investering daarboven levert over vijftien jaar per saldo geld in. Let op: de €4.197-rij gaat over een systeem van 15 kWh en heeft dus een hogere jaarwaarde (€530); de IRR daar is niet met de andere rijen te vergelijken zonder dat mee te wegen.

**Kanttekeningen bij deze IRR.** Het model veronderstelt vijftien jaar lang een stabiel leveringstarief, een stabiele prijsspreiding en geen vervangings- of reparatiekosten. Een omvormer die na twaalf jaar vervangen moet worden (€600 tot €900) drukt het rendement, net als een eventuele premieopslag op de opstalverzekering. Vraag je verzekeraar wat een thuisbatterij in jouw polis doet; dat verschilt per maatschappij en wij noemen daar geen bedrag bij.

Wat deze tabel vooral laat zien: een thuisbatterij is geen belegging met een voorspelbaar rendement. Het is een investering waarvan de uitkomst bijna volledig aan de inkoopprijs hangt.

---

## Wanneer een batterij níet uitkomt

- **Weinig teruglevering.** Onder circa 1.200 kWh per jaar staat de batterij het grootste deel van het jaar stil en loopt de terugverdientijd hard op.
- **Weinig avondverbruik.** Kun je de batterij 's avonds niet leegtrekken, dan is de capaciteit die je koopt niet inzetbaar.
- **Zonnepanelen onder 2,5 kWp.** Te weinig overschot om de batterij te vullen.
- **Een systeem boven circa €3.530 als het je puur om rendement gaat.** Boven dat bedrag komt de terugverdientijd buiten de garantietermijn van tien jaar te liggen, en boven €4.843 komt hij over de volle vijftien jaar niet uit.
- **Verhuisplannen binnen vijf jaar.** Wat een batterij bij verkoop oplevert, is niet te onderbouwen met publieke data; ga er niet van uit dat je de restwaarde terugziet.
- **Geen P1-poort of geen slimme aansturing.** Zonder meetdata en sturing komt de arbitragecomponent niet van de grond.

Voor de randgevallen, zie [heeft een batterij na 2027 zin zonder zonnepanelen](/posts/batterij-na-2027-zonder-zonnepanelen-zin-2026/).

---

## Risico's in dit model

**Risico 1 — de terugleververgoeding valt anders uit.** Dit is de grootste onzekerheid, en de €0,07 waarmee wij rekenen is expliciet een aanname. Bij €0,05 stijgt de jaarwaarde in scenario B naar €387, bij €0,10 zakt hij naar €303. Zodra jouw leverancier voor 2027 een tarief publiceert, reken het model opnieuw door.

**Risico 2 — het leveringstarief daalt.** Bij €0,22 in plaats van €0,26 zakt de jaarwaarde in scenario B van €353 naar €293, en loopt de terugverdientijd bij €2.898 op naar 9,9 jaar.

**Risico 3 — terugleverkosten.** Rekent je leverancier vanaf 2027 terugleverkosten, dan valt een batterij juist gunstiger uit dan hier berekend, omdat je die post deels vermijdt. Welke leveranciers dat nu doen, houden wij bij op [terugleverkosten vergelijken](/terugleverkosten-vergelijken/). Voor 2027 is er nog niets gepubliceerd, dus het zit niet in het model.

**Risico 4 — technische levensduur.** LFP-batterijen halen volgens fabrieksopgave 6.000 cycli of meer tot 70 à 80 procent restcapaciteit. In dit model doet de batterij circa 250 cycli per jaar, dus die 6.000 zijn niet de beperkende factor. De garantietermijn in jaren is dat wel.

---

## Stappenplan

1. **Bereken je overschot** met de [saldering calculator 2027](/posts/saldering-calculator-2027-volledig/) of met de zeven stappen hierboven.
2. **Kies de capaciteit** op je verschuifbare volume, niet op je dakoppervlak. Capaciteit die je niet dagelijks vult, verdient niets terug.
3. **Vergelijk op prijs per kWh**, want dat is de variabele die de uitkomst bepaalt. Zie [Sessy versus Marstek](/posts/sessy-vs-marstek-vergelijking-2026/) en [10 kWh thuisbatterij vergelijking](/posts/thuisbatterij-10-kwh-vergelijking-2026/).
4. **Beslis over een dynamisch contract.** Zie [beste dynamisch contract met zonnepanelen](/posts/beste-dynamisch-contract-met-zonnepanelen-2026/) en onze [vergelijker van dynamische contracten](/dynamisch-energiecontract-vergelijken/). Tibber kost €5,99 per maand per energiesoort plus €0,0248 per kWh inkoopvergoeding; Frank Energie rekent een inkoopvergoeding én een terugleverstaffel en publiceert zijn vaste kosten niet.
5. **Vraag offertes op** en vul het werkelijke bedrag in het model in.
6. **Check je gemeente** op een eigen regeling; zie [thuisbatterij subsidie 2026 overzicht](/posts/thuisbatterij-subsidie-2026-overzicht/). Reken geen landelijke subsidie in.
7. **Installeer en monitor** — zie [thuisbatterij buiten versus binnen installeren](/posts/thuisbatterij-buiten-vs-binnen-installeren-2026/) — en controleer na een jaar of de verschoven kWh overeenkomen met de aanname van 150 cycli.

---

## Btw, ISDE en gemeentelijke regelingen

Een thuisbatterij is **niet ISDE-subsidiabel**. De ISDE voor woningeigenaren geldt volgens RVO uitsluitend voor isolatie, ventilatie (in combinatie met isolatie), (hybride) warmtepompen, zonneboilers, een aansluiting op een warmtenet en elektrisch koken. Batterijen, zonnepanelen en laadpalen staan er niet op. Sommige gemeenten hebben een eigen duurzaamheidssubsidie of -lening waar een batterij onder kan vallen; die regelingen wisselen per gemeente en per jaar, en sommige eisen een aanvraag vóór installatie. Check de actuele regeling op de site van je eigen gemeente vóór je tekent.

Op een thuisbatterij betaal je **21 procent btw**. Het 0-procentstarief voor zonnepanelen dekt volgens de Belastingdienst uitdrukkelijk niet de levering en installatie van een accupakket of thuisbatterij, ook niet als je de batterij samen met panelen koopt. Een Sessy van €5.500 bevat dus €954 aan btw. In specifieke gevallen kun je die btw terugvragen als je als btw-ondernemer stroom teruglevert; de Belastingdienst stelt daarbij voorwaarden, waaronder een energiemanagementsysteem en een dynamisch contract, en over de terugleververgoeding draag je dan 21 procent btw af. Behandel dat niet als standaardvoordeel: in onze modellen rekenen wij met de volledige prijs inclusief btw.

Over plaatsingseisen: er bestaat geen algemene eis in het Besluit bouwwerken leefomgeving (Bbl, sinds 1-1-2024 de opvolger van het Bouwbesluit) dat een batterij boven 5 kWh in een aparte ruimte moet staan. Wat er wél kan spelen, zijn voorwaarden van je eigen verzekeraar en de eisen die de fabrikant in de installatiehandleiding stelt. Vraag bij de offerte expliciet welke norm de installateur hanteert en welke documentatie je krijgt.

---

## Veelgemaakte fouten in ROI-berekeningen

1. **Rekenen met een afbouwpad.** Reeksen als 64/28/0 procent of 73/64/55/46 procent horen bij verworpen wetsvoorstellen. De saldering stopt in één keer op 1-1-2027. Wie met tussenstappen rekent, komt voor 2027 tot en met 2030 te gunstig uit.
2. **Dezelfde kWh dubbel tellen.** "Extra eigen verbruik" én "voorkomen saldering-verlies" over dezelfde kilowattuur optellen verdubbelt de uitkomst ten onrechte. Zie de uitleg bovenaan dit artikel.
3. **Rekenen met een eigen-verbruikfractie in plaats van met cycli.** "Eigen verbruik stijgt naar 85 procent" overschat wat een batterij in de winter kan. Reken met verschuifbaar volume: capaciteit × cycli, begrensd door overschot en avondverbruik.
4. **De inkoopvergoeding van je dynamische contract vergeten.** Tibber rekent €0,0248 per kWh bovenop de uurprijs, plus €5,99 per maand per energiesoort. Dat drukt de arbitragemarge en daarmee de €8 per kWh capaciteit waarmee wij rekenen.
5. **Subsidie inrekenen die niet bestaat.** De ISDE dekt geen thuisbatterijen. Een gemeentelijke regeling telt alleen mee als je hem zwart-op-wit hebt gevonden.
6. **Btw-teruggaaf inrekenen op de batterij.** Het 0-procentstarief geldt niet voor accupakketten, ook niet bij gelijktijdige aanschaf met panelen.
7. **Installatie en randkosten weglaten.** Een vast systeem heeft een installateur nodig; een plug-in systeem van 3.000 W mogelijk een aparte groep. Reken met de totaalprijs.
8. **Vervangingskosten negeren.** Een omvormer die na twaalf jaar aan vervanging toe is, hoort in de cashflow.

---

## Conclusie

De ROI van een thuisbatterij is in 2026 goed uit te rekenen, maar alleen als je twee dingen goed doet: rekenen met de harde stop op 1-1-2027 in plaats van met een afbouwpad, en dezelfde kilowattuur niet twee keer meetellen.

Doe je dat, dan komt de jaarwaarde voor een gangbaar profiel met 10 kWh uit op €353 met een dynamisch contract en €273 zonder. Dat betekent: rendabel binnen de garantietermijn bij een investering onder circa €3.530, en daarboven een investering die je vooral maakt voor onafhankelijkheid, noodstroom of het opvangen van de saldering-stop — niet voor het rendement.

Reken eerst met je eigen offertebedrag, koop daarna.

*Vragen over jouw berekening? Mail [info@duurzaamthuislab.nl](mailto:info@duurzaamthuislab.nl).*

---

## Gerelateerde artikelen

- [Saldering calculator 2027 volledig](/posts/saldering-calculator-2027-volledig/)
- [Saldering 2027 transitie planner](/posts/saldering-2027-transitie-planner/)
- [Thuisbatterij terugverdientijd berekenen 2026](/posts/thuisbatterij-terugverdientijd-berekenen-2026/)
- [Beste thuisbatterij Nederland 2026](/posts/beste-thuisbatterij-nederland-2026/)
- [Thuisbatterij prijs per kWh 2026](/posts/thuisbatterij-prijs-per-kwh-2026/)
- [Sessy vs Marstek vergelijking 2026](/posts/sessy-vs-marstek-vergelijking-2026/)
- [Dynamische energiecontracten thuisbatterij 2026](/posts/dynamische-energiecontracten-thuisbatterij-2026/)
- [Beste dynamisch contract met zonnepanelen 2026](/posts/beste-dynamisch-contract-met-zonnepanelen-2026/)
- [Thuisbatterij subsidie 2026 overzicht](/posts/thuisbatterij-subsidie-2026-overzicht/)

---

**Externe bron:** [RVO — ISDE voor woningeigenaren](https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren) — het officiële overzicht van welke maatregelen de ISDE wel en niet dekt (thuisbatterijen, zonnepanelen en laadpalen vallen er niet onder).
