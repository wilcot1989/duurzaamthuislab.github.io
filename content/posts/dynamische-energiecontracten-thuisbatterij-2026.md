---
title: Dynamische Energiecontracten + Thuisbatterij
date: 2026-04-02 12:00:00+01:00
lastmod: '2026-08-21 08:00:00+02:00'
description: Hoe een thuisbatterij en een dynamisch energiecontract samenwerken in 2026 — het mechanisme, de leverancierstarieven en een narekenbare modelberekening.
categories:
- thuisbatterijen
tags:
- dynamisch energiecontract
- thuisbatterij
- energie arbitrage
- slim laden
- tibber
- zonneplan
- ANWB energie
- dynamische tarieven
keywords:
- dynamisch energiecontract thuisbatterij
- geld verdienen thuisbatterij
- energie arbitrage
- slim laden thuisbatterij
- dynamisch tarief batterij
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1589276534126-adef63a95e05&w=1200&output=webp&q=70
faq:
- q: 'Wat is een dynamisch energiecontract?'
  a: 'Bij een dynamisch energiecontract betaal je per uur een wisselende prijs voor stroom, gebaseerd op de day-ahead marktprijs. Bij veel wind of zon is stroom goedkoop of zelfs negatief; bij hoge vraag op koude windstille avonden is stroom duur. Je profiteert door verbruik te verschuiven naar goedkope uren.'
- q: 'Hoeveel kun je besparen met een dynamisch contract en thuisbatterij?'
  a: 'In onze modelberekening met een batterij van 10 kWh levert het opslaan van eigen zonnestroom circa 385 euro per jaar op en handelen op prijsverschillen circa 130 tot 235 euro per jaar. Na aftrek van de vaste contractkosten van circa 72 euro komt het model uit op circa 445 tot 550 euro per jaar. De uitkomst hangt volledig af van de prijsspreiding in dat jaar en van je eigen verbruikspatroon.'
- q: 'Welke dynamische energieleveranciers zijn er in Nederland?'
  a: 'Onder meer Tibber, Zonneplan, ANWB Energie, easyEnergy, Frank Energie, Vandebron, EnergyZero en Eneco. Tarieven en vaste kosten verschillen sterk en wijzigen regelmatig; controleer ze op de tarievenpagina van de leverancier voordat je kiest.'
- q: 'Kan elke thuisbatterij automatisch laden en ontladen op dynamische tarieven?'
  a: 'Nee. Je hebt een energiemanagementsysteem nodig dat de batterij aanstuurt op basis van de uurprijzen. Sommige batterijen doen dat via het eigen platform van de fabrikant of via een integratie met de app van de leverancier; andere alleen via huisautomatisering zoals Home Assistant.'
- q: 'Is het legaal om stroom uit je thuisbatterij terug te leveren aan het net?'
  a: 'Ja, dat mag. Je ontvangt de terugleververgoeding van je leverancier. Let op: die vergoeding ligt doorgaans lager dan de afnameprijs, omdat je over afname wel energiebelasting en btw betaalt en over teruglevering niet. Zelf verbruiken is daarom vrijwel altijd voordeliger dan terugleveren.'
- q: 'Wat is energie-arbitrage?'
  a: 'Stroom inkopen wanneer de uurprijs laag is, opslaan in je thuisbatterij en gebruiken wanneer de prijs hoog is. Het prijsverschil is je opbrengst. Omdat energiebelasting en btw op beide momenten gelijk zijn, is de winst per kWh gelijk aan het verschil in marktprijs maal 1,21, min de laad- en ontlaadverliezen.'
- q: 'Heb ik zonnepanelen nodig voor energie-arbitrage?'
  a: 'Nee, arbitrage werkt ook zonder zonnepanelen: je laadt dan uitsluitend op goedkope uren van het net. De combinatie van zonnepanelen, thuisbatterij en dynamisch contract levert wel het hoogste totaal op, omdat er dan twee opbrengstbronnen zijn.'
schema_type: Article
---
Een thuisbatterij gekoppeld aan een dynamisch energiecontract kan op twee manieren geld opleveren: door zonnestroom op te slaan voor eigen gebruik én door te handelen op prijsverschillen — laden als de uurprijs laag is, ontladen als hij hoog is. In dit artikel leggen we uit hoe dat mechanisme werkt, welke leverancierstarieven publiek zijn en wat het volgens een narekenbare modelberekening oplevert.

*Disclosure: wij hebben geen affiliate- of commissierelatie met Tibber, Frank Energie, ANWB Energie of Zonneplan (stand augustus 2026) en ontvangen geen vergoeding als je via onze links overstapt. De links naar deze leveranciers zijn gewone verwijzingen.*

💡 *Niet zeker over de stop van de saldering per 1 januari 2027? Lees de [Saldering 2027 transitie-planner](/posts/saldering-2027-transitie-planner/).*

> **Kort antwoord:** de combinatie van een thuisbatterij en een dynamisch contract levert in onze modelberekening circa 445 tot 550 euro per jaar op bij een batterij van 10 kWh — opgebouwd uit circa 385 euro aan opgeslagen zonnestroom en circa 130 tot 235 euro aan handelen op prijsverschillen, min circa 72 euro vaste contractkosten. Bij een investering van 5.500 euro komt de terugverdientijd daarmee op circa 10 tot 12,5 jaar. Alle aannames staan verderop in dit artikel.

## De tarieven waarmee we rekenen

| Invoerwaarde | Waarde | Bron / peildatum |
|---|---|---|
| Day-ahead jaargemiddelde 2025 | 0,105 euro/kWh | marktdata 2025 |
| Negatieve uren 2025 | 212 uur | marktdata 2025 |
| Duurste uur 2025 | 0,63 euro/kWh (20-1-2025, 17:00) | marktdata 2025 |
| Energiebelasting stroom 2026 | 0,09161 euro/kWh excl. btw (0,11085 incl.) | Belastingdienst-tarieven 2026, aug 2026 |
| Tibber | 5,99 euro/mnd **per energiesoort** + 0,0248 euro/kWh | tibber.com, aug 2026 |
| Frank Energie | rekent inkoopvergoeding én terugleverstaffel (sinds 1-6-2025); vaste kosten: publiceert geen consumentenprijs | frankenergie.nl, aug 2026 |
| ANWB Energie | inkoopkosten 0,018 euro/kWh | anwb.nl, aug 2026 |
| Zonneplan | tarieven staan op de eigen tarievenpagina; wij nemen geen bedrag over dat wij niet konden verifieren | — |
| Opslag-aanname in het model | 0,02 euro/kWh | eigen aanname |
| Dynamisch all-in bij het jaargemiddelde | 0,26 euro/kWh = (0,105 + 0,02 + 0,09161) x 1,21 | eigen model |
| Terugleververgoeding 2027 | 0,07 euro/kWh (**aanname**, niet gepubliceerd) | eigen model |

De **ODE bestaat sinds 2023 niet meer** als aparte post op je rekening; die is opgegaan in de energiebelasting. De netbeheerkosten zijn een vast jaarbedrag per aansluiting en veranderen niet door je contractvorm of door een batterij.

## Waarom batterij plus dynamisch meer doet dan elk afzonderlijk

Zonder batterij bepaalt het toeval wanneer je goedkoop inkoopt: je bent afhankelijk van wanneer je thuis bent en wanneer je panelen produceren. Met een batterij kies je zelf het moment van inkoop en van verbruik. Dat is precies de reden dat de twee elkaar versterken:

| Setup | Wat het oplevert |
|---|---|
| Alleen zonnepanelen | Waarde van eigen opwek, tot 1-1-2027 nog verrekend via saldering |
| Alleen dynamisch contract | Voordeel op het deel van je verbruik dat je kunt verschuiven |
| Zonnepanelen + dynamisch | Bovenstaande twee, plus teruglevering tegen de uurprijs |
| Zonnepanelen + batterij + vast contract | Eigen zonnestroom 's avonds gebruiken in plaats van terugleveren |
| **Zonnepanelen + batterij + dynamisch** | **Beide bronnen tegelijk: opslag én handelen op prijsverschillen** |

Wij zetten er bewust geen euro-bandbreedtes bij: die zouden per situatie zo ver uiteenlopen dat ze niets zeggen. De doorrekening voor één concreet profiel staat verderop onder "Rekenvoorbeeld".

## Seizoenspatroon: twee opbrengstbronnen die elkaar afwisselen

De twee opbrengstbronnen bewegen tegengesteld door het jaar:

- **Zomer (mei-augustus):** veel zonproductie, dus veel te bufferen. Tegelijk is de prijsspreiding op de markt in die maanden vaak beperkt. Opslag levert dan het meeste op, handelen het minste.
- **Winter (november-februari):** nauwelijks zonproductie, dus weinig te bufferen uit eigen opwek. Maar juist dan is de spreiding groot: koude, windstille dagen geven forse avondpieken, terwijl winderige nachten zeer lage of negatieve prijzen kennen. Handelen levert dan het meeste op.
- **Voorjaar en najaar:** beide bronnen dragen bij, in wisselende verhouding.

Praktisch gevolg: één of twee maanden meten geeft geen betrouwbaar beeld van het jaarrendement. Daar heb je een volledig kalenderjaar voor nodig.

## Welke batterijen werken met welke leverancier

| Batterij | Aansturing via eigen platform | Via huisautomatisering |
|---|---|---|
| Huawei Luna 2000 | ja, eigen app | ja |
| Sessy | ja, open API | ja |
| Marstek | beperkt | ja |
| Tesla Powerwall 3 | beperkt | ja, complex |
| EcoFlow PowerOcean | beperkt | ja |
| BYD Battery-Box | via omvormer | ja |

Welke leverancier welke batterij rechtstreeks aanstuurt, wisselt: integraties worden toegevoegd en verdwijnen weer. Controleer dat vóór aankoop bij zowel de batterijfabrikant als de leverancier, in plaats van op een tabel in een artikel te vertrouwen. Wij nemen hier geen integratieclaims per leverancier over die wij niet in de documentatie van beide partijen konden terugvinden.

## Wat is een dynamisch energiecontract?

| Aspect | Vast contract | Dynamisch contract |
|---|---|---|
| Prijs per kWh | vast tarief voor de looptijd | wisselt per uur |
| Prijsbasis | afgesproken bij afsluiten | day-ahead marktprijs |
| Goedkoopste momenten | altijd dezelfde prijs | 's nachts en midden op de dag bij veel zon of wind |
| Duurste momenten | altijd dezelfde prijs | 17:00-21:00 en koude windstille dagen |
| Risico | bij de leverancier | bij jou |
| Besparingspotentieel | beperkt | afhankelijk van hoeveel je kunt verschuiven |

De prijs die je op een dynamisch contract per kWh betaalt is: (marktprijs + opslag + energiebelasting) x 1,21. Bij het jaargemiddelde van 2025 en de opslag-aanname van 0,02 euro/kWh komt dat uit op circa **0,26 euro/kWh**. In het duurste uur van 2025 (0,63 euro/kWh marktprijs) was dat circa 0,90 euro/kWh; in een uur met een marktprijs van 0,02 euro nog altijd circa 0,16 euro/kWh, omdat belasting en btw doorlopen.

## Energie-arbitrage: het mechanisme

1. **Laden** wanneer de uurprijs laag is (nacht, of middag bij veel zon)
2. **Ontladen** wanneer de prijs hoog is (avondpiek)
3. Het **prijsverschil** is je opbrengst

Een belangrijk detail dat vaak wordt gemist: **energiebelasting en btw betaal je op beide momenten**, dus die vallen tegen elkaar weg. De winst per kWh is daardoor gelijk aan het verschil in *marktprijs* maal 1,21, verminderd met de laad- en ontlaadverliezen van de batterij.

Ter illustratie een dagpatroon (geen gemeten dag, maar een typisch verloop):

| Tijd | Marktprijs (indicatief) | Actie thuisbatterij |
|---|---|---|
| 02:00-06:00 | laag | laden vanuit het net |
| 08:00-16:00 | laag tot midden | laden vanuit zonnepanelen |
| 17:00-21:00 | hoog | ontladen voor eigen gebruik |
| 22:00-01:00 | midden | standby of licht laden |

Rekenvoorbeeld per cyclus, met een aangenomen bruikbaar verschil in marktprijs van 0,12 euro/kWh: 0,12 x 1,21 = 0,145 euro per kWh. Bij een batterij van 10 kWh en 90% rendement is dat 10 x 0,9 x 0,145 = **circa 1,31 euro per volledige cyclus**. De actuele uurprijzen van vandaag en morgen staan op onze [stroomprijzenpagina](/stroomprijzen/); daar zie je zelf hoe groot het verschil op een gegeven dag is.

## Twee opbrengstbronnen naast elkaar

### Bron 1: zonnestroom opslaan

Overdag opgewekte stroom opslaan en 's avonds zelf verbruiken. De waarde hiervan stijgt zodra de **salderingsregeling per 1 januari 2027 volledig stopt**: vanaf dat moment levert teruggeleverde stroom niet meer je afnametarief op, maar alleen de terugleververgoeding uit je contract. Het verschil tussen die twee is precies wat je met opslag bespaart.

### Bron 2: handelen op prijsverschillen

Laden op goedkope uren en ontladen op dure uren, ook op dagen dat je panelen weinig produceren. Dit werkt naast de zonne-opslag en benut de batterij in de wintermaanden.

## Rekenvoorbeeld: het verdienmodel uitgewerkt

Dit is een modelberekening, geen meting. De aannames:

- **Thuisbatterij:** 10 kWh bruikbaar, rendement 90%
- **Zonnepanelen:** circa 4.500 Wp
- **Investering:** 5.500 euro inclusief installatie en 21% btw (geen rijkssubsidie beschikbaar)
- **Jaarverbruik:** 3.500 kWh
- **Afnameprijs dynamisch:** 0,26 euro/kWh all-in (jaargemiddelde 2025 + opslag-aanname 0,02 + energiebelasting 2026 + btw)
- **Terugleververgoeding:** 0,07 euro/kWh (aanname; niet gepubliceerd en per contract verschillend)
- **Bruikbaar verschil in marktprijs voor handelen:** 0,12 euro/kWh (aanname)
- **Vaste contractkosten:** 71,88 euro per jaar (Tibber, 5,99 euro per maand voor één energiesoort)
- **Situatie:** na 1 januari 2027, dus zonder saldering

**Bron 1 — zonnestroom opslaan:** 2.250 kWh per jaar door de batterij, maal 90% rendement = 2.025 kWh die je zelf verbruikt in plaats van terug te leveren. Waarde per kWh: 0,26 − 0,07 = 0,19 euro. Opbrengst: 2.025 x 0,19 = **385 euro per jaar**.

**Bron 2 — handelen op prijsverschillen:** 100 volledige cycli per jaar naast de zonne-opslag, 10 kWh per cyclus, 90% rendement, 0,145 euro voordeel per kWh: 100 x 10 x 0,9 x 0,145 = **131 euro per jaar**. In een jaar met veel prijsspreiding en 180 bruikbare cycli: **235 euro per jaar**.

| Component | Conservatief | Gunstig jaar |
|---|---|---|
| Zonnestroom opslaan | 385 euro | 385 euro |
| Handelen op prijsverschillen | 131 euro | 235 euro |
| Vaste kosten dynamisch contract | −72 euro | −72 euro |
| **Netto per jaar** | **444 euro** | **548 euro** |
| **Terugverdientijd bij 5.500 euro** | **circa 12,4 jaar** | **circa 10,0 jaar** |

Voor een thuisbatterij bestaat geen ISDE-subsidie, dus reken met de volledige investering inclusief 21% btw. Vervang de aannames door je eigen cijfers — vooral het investeringsbedrag en de aangenomen prijsspreiding hebben grote invloed op de uitkomst.

## Welke dynamische leveranciers zijn geschikt?

| Leverancier | Vaste kosten per maand | Inkoopvergoeding per kWh | Peildatum |
|---|---|---|---|
| Tibber | 5,99 euro **per energiesoort** | 0,0248 euro | aug 2026 |
| Frank Energie | publiceert geen consumentenprijs | rekent een inkoopvergoeding; bedrag niet publiek. Terugleverstaffel sinds 1-6-2025 | aug 2026 |
| ANWB Energie | geen eenduidig servicebedrag gepubliceerd | 0,018 euro | aug 2026 |
| Zonneplan | zie tarievenpagina leverancier | zie tarievenpagina leverancier | — |

Let op de betekenis van "per energiesoort" bij Tibber: neem je zowel stroom als gas af, dan betaal je die 5,99 euro twee keer. Over een eventueel prijsdempingsmechanisme bij ANWB doen wij geen uitspraak; wij hebben dat niet in de voorwaarden kunnen verifieren. Het actuele overzicht van aanbieders staat in onze [vergelijker dynamische energiecontracten](/dynamisch-energiecontract-vergelijken/).

<div class="cta cta-affiliate">
<strong>Tibber bekijken</strong><br>
Tibber rekent 5,99 euro per maand per energiesoort plus 0,0248 euro per kWh inkoopvergoeding (peildatum augustus 2026) en is maandelijks opzegbaar. Wij ontvangen geen vergoeding als je overstapt.<br>
<a href="https://go.duurzaamthuislab.nl/tibber" rel="noopener nofollow">Naar Tibber</a>
</div>

## Welke thuisbatterijen ondersteunen slim laden?

Je hebt een systeem nodig dat:

1. **Externe aansturing accepteert** (via API, Modbus of een integratieplatform)
2. **Laad- en ontlaadtijden kan inplannen** op basis van prijssignalen
3. **Samenwerkt** met je leverancier of met een huisautomatiseringssysteem

De Huawei Luna 2000 en de SolarEdge Home Battery bieden aansturing via het eigen platform van de fabrikant; de Sessy heeft een open API. Vrijwel elk merk is daarnaast via Home Assistant aan te sturen op basis van de uurprijzen, met de kanttekening dat dat technische kennis en instelwerk vraagt.

Lees meer in onze [Huawei Luna 2000 review](/posts/huawei-luna-2000-review-2026/) en in het overzicht van de [beste thuisbatterijen 2026](/posts/beste-thuisbatterij-nederland-2026/).

## Stap voor stap aan de slag

**Stap 1 — check je situatie:** hoeveel Wp aan panelen heb je, welke omvormer, wat is je jaarverbruik en heb je een slimme meter met werkende P1-poort?

**Stap 2 — kies een batterij** die past bij je omvormer en die externe aansturing ondersteunt. Reken eerst je avondpiekverbruik uit voordat je een capaciteit kiest.

**Stap 3 — laat installeren en check lokale regelingen.** Vraag minimaal drie offertes aan. Voor thuisbatterijen bestaat geen ISDE-subsidie; sommige gemeenten en provincies hebben een eigen regeling, en die eisen bijna altijd aanvraag vóór installatie. Zie onze [subsidiegids](/posts/zonnepanelen-subsidie-nederland-2026/).

**Stap 4 — stap over naar een dynamisch contract.** De overstap duurt doorgaans enkele weken. Controleer de opzegvoorwaarden van je huidige contract.

**Stap 5 — stel de sturing in**, via het platform van je batterij, de app van je leverancier of huisautomatisering.

**Stap 6 — monitor en stel bij.** De eerste maanden gaan op aan finetunen.

## Risico's en aandachtspunten

**Prijzen kunnen hoog oplopen.** Op koude, windstille dagen loopt de uurprijs op; het duurste uur van 2025 kostte 0,63 euro/kWh kale marktprijs, oftewel circa 0,90 euro/kWh all-in. Staat je batterij op zo'n moment leeg, dan betaal je het volle tarief. Een goed ingestelde sturing laadt daarom vooruit.

**Niet elke dag is winstgevend.** Op dagen met een vlak prijsverloop levert handelen niets op. De opbrengst zit in het jaargemiddelde.

**Complexiteit.** Sturing op uurprijzen instellen vraagt technische affiniteit, zeker via huisautomatisering.

**Batterijslijtage.** Elke extra cyclus draagt bij aan slijtage. Bij LiFePO4-cellen met duizenden cycli is dat beheersbaar, maar het hoort in de berekening thuis.

## Veelgemaakte fouten

**Fout 1: batterij zonder energiemanagementsysteem.** Zonder koppeling aan de uurprijzen laadt en ontlaadt de batterij alleen op eigen opwek, en mis je de handelsopbrengst volledig.

**Fout 2: te kleine batterij voor het profiel.** Bij een huishouden met warmtepomp en elektrische auto raakt een kleine batterij 's avonds leeg voordat de piek voorbij is.

**Fout 3: standaard volledig laden en ontladen.** Ondiepe cycli sparen de batterij. Een laadlimiet van 90% en een ontlaadminimum van 10% kost je bruikbare capaciteit maar verlengt de levensduur; hoeveel precies verschilt per fabrikant — kijk in de garantievoorwaarden.

**Fout 4: aannemen dat leverancier en batterij samenwerken.** Controleer de integratie vóór aankoop bij beide partijen.

**Fout 5: rekenen met een subsidie die niet bestaat.** De ISDE voor woningeigenaren dekt isolatie, ventilatie, (hybride) warmtepompen, zonneboilers, een warmtenetaansluiting en elektrisch koken — geen thuisbatterijen, geen zonnepanelen en geen laadpalen. Kijk in plaats daarvan naar een gemeentelijke of provinciale regeling, en vraag die aan vóór installatie.

## Wettelijk kader 2026

**Geen ISDE-subsidie op thuisbatterijen.** De ISDE dekt volgens RVO uitsluitend isolatie, ventilatie in combinatie met isolatie, (hybride) warmtepompen, zonneboilers, een aansluiting op een warmtenet en elektrisch koken.

**Btw op een thuisbatterij: 21%.** Het 0%-tarief geldt alleen voor zonnepanelen en wat direct nodig is om ze te laten werken: kabels, montagemateriaal, optimizers, omvormers en aanpassingen aan meterkast en dak. Een accupakket valt daar uitdrukkelijk buiten, ook als je het samen met de panelen koopt. In specifieke gevallen kun je btw terugvragen als btw-ondernemer; de Belastingdienst stelt daarbij voorwaarden. Reken daar niet standaard op.

**Anti-eilandbeveiliging.** Elke netgekoppelde batterij schakelt bij netuitval automatisch af. Wil je noodstroom, dan heb je extra hardware nodig; de kosten daarvan vraag je op bij je installateur.

**Terugleveren van batterijstroom** aan het net mag; je ontvangt de terugleververgoeding van je leverancier. Bij incidenteel gebruik is dat een particuliere activiteit. Wie systematisch en bedrijfsmatig handelt, kan fiscaal anders worden behandeld — vraag dat na bij je boekhouder.

## Je eigen opbrengst bijhouden

Omdat het jaarrendement zo sterk afhangt van de marktspreiding in een specifiek jaar, is er maar één betrouwbare manier om te weten wat jouw systeem oplevert: zelf meten over minimaal twaalf maanden.

**Wat je nodig hebt:** de laad- en ontlaadhoeveelheden per dag uit het platform van je batterij, de uurprijzen uit de app van je leverancier, en je eigen verbruiks- en teruglevercijfers uit de P1-uitlezing.

**Hoe je de twee bronnen scheidt:**

- **Zonne-opslag:** de kWh uit eigen opwek die je via de batterij zelf verbruikte, maal het verschil tussen afnameprijs en terugleververgoeding op dat moment.
- **Handelen:** de kWh die je bij een lage prijs uit het net laadde en later verbruikte in plaats van dure netstroom, maal het prijsverschil maal 1,21, min de rondgangsverliezen van de batterij.

Controleer in de eerste weken dagelijks of de sturing echt op de goedkoopste uren laadt en niet op een vast tijdschema. Verkeerd ingestelde laadvensters zijn de meest genoemde oorzaak van een tegenvallende opbrengst.

## Conclusie

Een thuisbatterij op een dynamisch contract heeft twee opbrengstbronnen die elkaar door het jaar heen afwisselen. In onze modelberekening met een batterij van 10 kWh komt dat neer op circa 445 tot 550 euro per jaar en een terugverdientijd van circa 10 tot 12,5 jaar bij een investering van 5.500 euro — zonder rijkssubsidie, want die is er voor batterijen niet, en met 21% btw op de accu.

Of dat voor jou uitkomt, hangt af van drie dingen die je zelf moet invullen: je investeringsbedrag, hoeveel zonnestroom je werkelijk door de batterij stuurt, en hoe groot de prijsspreiding in jouw jaar is.

Lees ook [thuisbatterij terugverdientijd berekenen](/posts/thuisbatterij-terugverdientijd-berekenen-2026/) en [wat de stop van de saldering betekent](/posts/salderingsregeling-afbouw-wat-betekent-het-2026/).

---

**Externe bron:** [RVO — ISDE voor woningeigenaren](https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren) — het officiële overzicht van welke maatregelen de ISDE wel en niet dekt.
