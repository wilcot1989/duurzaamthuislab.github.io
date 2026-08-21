---
title: 'Dynamisch contract + thuisbatterij: rekenmodel besparing 2026'
date: '2026-09-09 08:00:00+02:00'
lastmod: '2026-08-21 08:00:00+02:00'
draft: false
description: Wat levert een 10 kWh thuisbatterij op een dynamisch contract op? Een transparant rekenmodel met EPEX-spreads, belastingen en degradatie — alle aannames expliciet.
categories:
- energiecontracten
tags:
- energiecontracten
- verduurzamen
- duurzaam wonen
- dynamisch
keywords:
- dynamisch contract batterij
- tibber sessy besparing
- frank batterij rekenmodel
- dynamisch tarief arbitrage
- batterij verdienmodel
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: 'Wat is een terugleverstaffel?'
  a: 'Een tariefsysteem waarbij je leverancier terugleverkosten in rekening brengt die oplopen naarmate je meer teruglevert. De schijven en bedragen verschillen per leverancier en per contract; kijk voor jouw situatie in het tarievenblad van je eigen leverancier, want er is geen landelijk vastgestelde staffel.'
- q: 'Rekenen Tibber en Frank Energie terugleverkosten?'
  a: 'Tibber rekent een vaste maandprijs per energiesoort plus een inkoopvergoeding per kWh en geen aparte terugleverstaffel. Frank Energie rekent sinds 1 juni 2025 naast de inkoopvergoeding wél een terugleverstaffel. Wie veel teruglevert, moet die staffel dus in de vergelijking meenemen en niet aannemen dat dynamisch automatisch staffelvrij is.'
- q: 'Hoe werkt de prijsvorming op de day-ahead-markt?'
  a: 'Elke dag wordt in de vroege middag een veiling gehouden voor de 24 uren van de volgende dag. Vraag en aanbod bepalen per uur de prijs. Negatieve prijzen ontstaan als er veel zon en wind is en weinig vraag; in 2025 waren er 212 uren met een negatieve prijs.'
- q: 'Wanneer is dynamisch goedkoper dan vast?'
  a: 'Bij verbruik buiten piekuren (18:00-22:00) en/of zonnepanelen + batterij. Voor laagverbruikers zonder slimme apparaten kan vast voordeliger zijn.'
- q: 'Heb ik een slimme meter nodig?'
  a: 'Voor dynamisch contract: ja, met kwartiergegevens. Bijna alle Nederlandse meters sinds 2018 voldoen. Check via de meterstand-app of je P1-poort werkt.'
schema_type: Article
---
*Disclosure: de links naar Sessy en Tibber in dit artikel zijn gewone verwijzingen — wij hebben met deze partijen geen affiliate- of commissierelatie en ontvangen voor dit artikel van geen enkele partij een vergoeding. Wij vergelijken op basis van specificaties, tarievenbladen en publieke data.*

Of een thuisbatterij op een dynamisch contract loont, hangt volledig af van je verbruiksprofiel en van de prijsspreads op de EPEX-markt. Daarom bouwen we hieronder een rekenmodel waarin elke aanname zichtbaar is, zodat je hem met jouw eigen cijfers kunt narekenen.


> **Kort antwoord:** Een 10 kWh thuisbatterij op een dynamisch contract verdient geld via twee kanalen: arbitrage (goedkoop laden, duur ontladen) en zelfconsumptie van zonnestroom. Hoeveel dat oplevert, bepalen de EPEX-spread, de energiebelasting en de vermogenslimiet van je omvormer.
>
> Neem in de vergelijking ook de terugleverkosten mee: Tibber rekent geen aparte terugleverstaffel, Frank Energie sinds 1 juni 2025 wel. Dat verschil kan bij veel teruglevering zwaarder wegen dan het verschil in vaste kosten.

## Korte conclusie

Voor wie weinig tijd heeft, de samenvatting in vijf punten:

- **Werkt het?** Ja, maar de opbrengst is bescheiden ten opzichte van de investering — uitleg verderop.
- **Wat levert een batterij op?** In ons model, na het einde van de saldering: circa €177 per jaar bij 5 kWh, €353 bij 10 kWh en €530 bij 15 kWh. Dat zijn gelabelde aannames, geen metingen.
- **Terugverdientijd?** Bij marktprijzen van €3.550 (5 kWh) tot €5.500 (10 kWh) komt het model uit op ongeveer achttien tot ruim twintig jaar — dus voorbij de verwachte levensduur.
- **Wat is de dominante variabele?** Niet het merk, maar hoeveel kWh je per dag daadwerkelijk kunt verschuiven en welk prijsverschil daartegenover staat.
- **Valkuilen?** Vijf rekenfouten — zie de sectie "Veelgemaakte fouten in het rekenmodel".

> **Onze inschatting:** begin met een dynamisch contract en meting, en beslis pas daarna over hardware. Zonder een half jaar eigen kwartierdata is elke terugverdienberekening een aanname.

## 1. Wat is het probleem?

Zonnepanelen en een warmtepomp leveren op zichzelf besparing op, maar zonder sturing loopt er geld weg: de warmtepomp draait op de duurste uren en de batterij is leeg precies wanneer de prijs piekt. Bij een dynamisch contract wordt dat direct zichtbaar in je rekening.

De kern: een dynamisch contract is niet plug-and-play. Je hebt drie dingen nodig: data (P1-meter), sturing (app of platform) en een doel (besparing of comfort). Mis je één van deze drie, dan blijft het rendement achter.

Voor context — zie ook [het bredere plaatje](/posts/frank-energie-vs-tibber-2026/) en [wat het einde van saldering betekent](/posts/tibber-review-ervaringen-2026/).

## 2. Wat heb je nodig?

Vier componenten:

1. **Slimme meter met werkende P1-poort.** Sinds 2018 standaard in NL.
2. **Realtime energiemonitor** (HomeWizard P1, Sessy P1, of Smartgateways).
3. **Een apparaat om te sturen** (batterij, laadpaal, warmtepomp).
4. **Een platform of app.** Tibber, Frank, Home Assistant of OpenHAB.

De fout die je hierbij wilt vermijden: stap 4 overslaan. Zonder platform heb je losse apparaten die elkaar niet kennen. Je warmtepomp gaat aan terwijl je batterij oplaadt — dubbel gebruik, dubbele kosten.

Lees ook: [de gedetailleerde guide](/posts/frank-energie-review-ervaringen-2026/) en [de praktijkvergelijking](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

## 3. Stap-voor-stap aanpak

### Stap 1: meet eerst

Voordat je iets koopt: breng je verbruik in kwartiergegevens in kaart. Bij Frank, Tibber of via je leverancier-portal kun je 365 dagen historie downloaden. Plot dit in een spreadsheet — dan zie je meteen waar de pieken zitten.

In een gemiddeld gezinsprofiel liggen die pieken rond 07:00-09:00 (douche en ontbijt) en 17:00-21:00 (koken en EV-laden). Dat zijn ook de duurste uren op een dynamisch contract.

### Stap 2: bepaal het doel

Niet elke setup hoeft volledig zelfvoorzienend te zijn. Zonnepanelen plus slim laden zonder batterij levert al een groot deel van de winst; de batterij voegt daar arbitrage en meer zelfconsumptie aan toe. Of dat extra bedrag de investering rechtvaardigt, is precies wat het rekenmodel hieronder uitwijst.

Reken het voor jezelf door — zie [het rekenmodel voor zonnepanelen](/posts/beste-dynamisch-contract-met-zonnepanelen-2026/).

### Stap 3: koop de juiste hardware

Voor de meeste huishoudens is een 5 kWh of 10 kWh batterij genoeg. Groter is zelden nuttig tenzij je een EV thuis laadt of een groot huishouden hebt. Voor warmtepompen: kies op vermogen en COP, niet op merk.

Onze inschatting per scenario:

- **Klein huis, geen EV:** 5 kWh batterij — vaak de kortste terugverdientijd per euro investering.
- **Middelgroot, 1 EV:** 10 kWh batterij plus slim laden.
- **Groot, 2 EV's:** 15-20 kWh modulair systeem.

### Stap 4: configureer het platform

Hier gaat de meeste tijd zitten. Een fabrikant-app is volgens de installatiehandleidingen in minuten ingericht; voor Home Assistant met een prijsintegratie moet je op basis van de officiële documentatie op enkele uren rekenen, en voor OpenHAB op meer. Onze aanbeveling: begin met de fabrikant-app en stap pas over op Home Assistant als je tegen beperkingen aanloopt.

Voor batterij-sturing op dynamisch contract: zie [de uitleg over terugleverkosten](/posts/terugleverkosten-zonnepanelen-2026/).

## 4. Wat kost het?

Indicatieve marktprijzen voor 2026, inclusief btw en zonder subsidie. Reken op de batterij met 21% btw: het 0%-tarief voor zonnepanelen dekt volgens de Belastingdienst uitdrukkelijk niet de levering en installatie van een accupakket of thuisbatterij, en de ISDE dekt voor woningeigenaren geen batterijopslag.

| Onderdeel | Kosten | Terugverdientijd |
|---|---|---|
| Thuisbatterij 5-10 kWh | circa €3.550-€5.500 (prijspeil aug 2026, Sessy als referentie via sessy.nl; andere merken wijken af — zie vendorsites) | 18 tot ruim 20 jaar (modelberekening, zie hoofdstuk 7) |
| P1-meter (HomeWizard Wi-Fi P1) | €24,95 (vendorprijs homewizard.com, peildatum aug 2026) | < 1 jaar |
| Kleine server voor Home Assistant | prijs wisselt per model — zie vendorsite | n.v.t. (tool) |
| Slimme laadpaal | richtprijs Milieu Centraal €1.300-€2.200 all-in inclusief installatie; Easee, Wallbox en Alfen publiceren zelf geen consumentenprijs, dus vergelijk offertes | 3-5 jaar tegenover thuisladen op een vast contract (modelberekening) |
| Extra sturing/accessoires | €0-€2.000 | varieert |

Voor een volledige kostenberekening: zie [de vergelijking dynamisch versus vast](/posts/dynamisch-vs-vast-contract-2026/).

## 5. Drie valkuilen bij de aanschaf

**Valkuil 1: te groot kopen.** Een batterij die groter is dan je dagelijkse nuttige doorzet, staat een deel van het jaar stil. Bereken eerst hoeveel kWh je per dag daadwerkelijk kunt verschuiven; dat is bijna altijd minder dan de nominale capaciteit.

**Valkuil 2: vendor lock-in.** Bij DC-gekoppelde batterijen (Goodwe, Huawei, SolaX) zit je vast aan de omvormer van dat merk. Bij AC-gekoppeld (Sessy, Marstek, Powerwall) ben je vrij. Voor toekomstvastheid heeft AC onze voorkeur.

**Valkuil 3: geen meetbaar doel.** "Ik wil verduurzamen" is geen doel. "€500 per jaar besparen" wel. Maak het concreet, anders koop je verkeerde spullen.

## 6. Welk product past bij wie?

### Voor budgetbewuste huishoudens
Een compacte AC-gekoppelde batterij met een goede app en zonder vendor lock-in. Voor het contract dat de sturing mogelijk maakt: <a href="https://go.duurzaamthuislab.nl/tibber" class="cta cta-affiliate" target="_blank" rel="noopener nofollow">Bekijk Tibber</a>

### Voor wie alles wil automatiseren
Combineer de batterij met Home Assistant en een dynamisch contract via Tibber of Frank. Reken op enkele uren inrichtwerk op basis van de officiële documentatie; je krijgt er fijnmazigere sturing voor terug dan met alleen de fabrikant-app.

### Voor grote huishoudens of off-grid ambities
Modulair systeem zoals BYD Battery-Box of Sessy thuisbatterij, in combinatie met een hybride-omvormer (Goodwe, SolaX). Investering in deze klasse loopt op tot €12.000-€18.000.

## 7. Het rekenmodel: rekenvoorbeeld voor een gezinswoning

Onderstaand voorbeeld is een modelberekening met expliciete aannames — geen meting. Vul je eigen cijfers in en de uitkomst verandert mee.

**Aannames over de woning:**

- **Stroomverbruik:** 4.380 kWh per jaar (gezin van 4)
- **Zonneproductie:** 4.920 kWh (14 panelen, zuid en west)
- **Teruglevering zonder batterij:** 1.890 kWh
- **Batterij:** 10 kWh, AC-gekoppeld, 5 kW omvormer

**Aannames over de tarieven (de rekenconstanten van deze site, alle bedragen inclusief btw):**

- **All-in stroomprijs:** €0,26/kWh — opgebouwd uit een beursprijs van €0,105 (jaargemiddelde 2025, inclusief btw), energiebelasting €0,11085 en een gelabelde aanname van €0,044 voor inkoopopslag en de omslag van vaste kosten.
- **Terugleververgoeding vanaf 2027:** €0,07/kWh. Dit is een aanname: geen leverancier heeft een tarief voor na het einde van de saldering gepubliceerd.
- **Retourrendement batterij:** 90%.
- **Bruikbare zoncycli:** 150 per jaar. Meer cycli haal je alleen als er ook overschot is om ze mee te vullen.
- **Netarbitrage:** €8 per kWh capaciteit per jaar, en alleen op een dynamisch contract. Dit is onze eigen afleiding uit circa 100 wintercycli met €0,10 netto spreiding — een aanname, geen gemeten resultaat.

**Uitkomst van het model, geldig vanaf 2027 (het jaar waarin de saldering volledig stopt):**

1. Verschuifbaar volume = de kleinste van drie grenzen: capaciteit × 150 cycli (10 × 150 = 1.500 kWh), overschot × 0,9 (1.890 × 0,9 = 1.701 kWh) en de **netto-afname** die je nog kunt vervangen. Die laatste is hier bepalend: van 4.920 kWh zonneproductie gebruik je zonder batterij al 3.030 kWh direct zelf (4.920 − 1.890 teruglevering), dus blijft er 4.380 − 3.030 = **1.350 kWh** netafname over. Meer dan dat kun je niet vervangen, hoe groot de batterij ook is. De bindende grens is dus **1.350 kWh**.
2. Na retourrendement: 1.350 × 0,9 = **1.215 kWh** die je zelf gebruikt in plaats van teruglevert.
3. Waarde per kWh = €0,26 (niet inkopen) − €0,07 (niet terugleveren) = **€0,19**. Levert 1.215 × €0,19 = **€231**.
4. Netarbitrage: 10 kWh × €8 = **€80**.
5. **Totaal circa €311 per jaar** voor dit huishoudprofiel.

Ons sitebrede kengetal voor een 10 kWh batterij is €353 per jaar (5 kWh: €177, 15 kWh: €530). Dit profiel komt daar €42 onder, en dat is geen afrondingsverschil: in het kengetal is de capaciteitsgrens bepalend, hier de netto-afname. Dit huishouden verbruikt relatief weinig stroom naast een fors dak, waardoor er simpelweg minder netafname te vervangen is. Dat is precies waarom je dit model met je eigen cijfers moet vullen: het kengetal is het plafond, niet de uitkomst.

Let op wat er níet in staat: de vaste kosten van het dynamische contract zelf. Tibber rekent €5,99 per maand **per energiesoort** plus €0,0248/kWh inkoopvergoeding; met stroom en gas is dat €143,76 per jaar aan vaste kosten. Die kosten hoor je niet aan de batterij toe te rekenen — je maakt ze ook zonder batterij — maar ze bepalen wel of het contract als geheel gunstig uitpakt.

Bij een investering van circa €5.500 voor 10 kWh komt de terugverdientijd in dit model op **bijna achttien jaar**, tegenover een verwachte levensduur van 15-20 jaar. De cumulatieve opbrengst over tien jaar is in dit profiel €3.110 (met het sitebrede kengetal van €353 zou dat €3.530 zijn). Dat is de kern van dit artikel: op de aannames hierboven verdient een thuisbatterij zichzelf niet ruim terug, en de uitkomst is bovendien gevoelig voor twee getallen die niemand kent — de terugleververgoeding na 2027 en de spreiding op de dagmarkt.

## 8. Bezwaren die het vaakst terugkomen

**"Mijn installateur zegt dat het niet kan."**
Vraag een tweede mening. Er zijn installateurs met ervaring met deze setups — zie [de installateur-checklist](/posts/dynamische-energiecontracten-vergelijking-2026/).

**"Het is te duur."**
Dat is in ons model voor de batterij zelf een terecht bezwaar: de terugverdientijd komt uit op achttien tot ruim twintig jaar bij een verwachte levensduur van 15-20 jaar. De stappen die er wél snel uit komen zijn het dynamische contract met sturing (geen hardware nodig) en zonnepanelen. Reken het door met je eigen cijfers, en behandel de uitkomst als een schatting met een brede marge — niet als een rendement.

**"Ik woon in een huurwoning."**
Dan zijn je opties beperkter, maar niet nul. Zie [de vergelijking van leveranciers](/posts/frank-energie-vs-tibber-2026/).

## 9. Conclusie

Stapsgewijs verduurzamen werkt beter dan alles in één keer: begin met meten, voeg dan sturing toe, en bouw daar het platform omheen. Niet andersom.

Voor 2026 is de logische eerste stap een dynamisch contract met goede data-ontsluiting. De batterij komt daarna, als je verbruikprofiel bekend is — en dan pas met je eigen kwartierdata in het model hierboven.

Verder lezen: [overzicht Tibber](/posts/tibber-review-ervaringen-2026/), [rekenmodellen Frank Energie](/posts/frank-energie-review-ervaringen-2026/) en [dynamische contracten met thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

## 10. Technische details: hoe werkt het onder de motorkap?

### Energiestromen in kaart

Op een gemiddelde voorjaarsdag lopen er vier energiestromen door elkaar: zonneproductie (4-6 kW piek rond het middaguur), huishoudelijk verbruik (basislast rond 350 W, pieken tot 7 kW bij koken), warmtepomp (1,2-2,8 kW modulerend) en EV-laden (3,7 kW of 11 kW). De som van deze stromen bepaalt of je op dat moment kost of verdient.

Zonder slimme sturing lopen deze door elkaar: de warmtepomp draait 's avonds op piektarief, de batterij is leeg precies wanneer het EV-laden begint. Resultaat: je betaalt de piekprijs voor stroom die uren eerder bijna gratis was.

### De rol van forecasting

Tibber, Frank en Home Assistant gebruiken weersvoorspellingen en dag-vooruitprijzen om beslissingen 24 uur vooruit te nemen: laden om 03:00 tot 70% omdat de prijs de volgende dag om 17:00 piekt. Dat is een algoritmische beslissing, geen menselijke.

De kwaliteit van die forecasting bepaalt een aanzienlijk deel van je besparing. Goede platforms gebruiken zowel weersdata als historische verbruiksprofielen; simpele implementaties reageren alleen op de huidige prijs.

### Communicatieprotocollen

Drie protocollen domineren de markt:

- **Modbus TCP** — industrieel, betrouwbaar, lokaal. Vrijwel alle warmtepompen, omvormers en batterijen ondersteunen het.
- **MQTT** — lichtgewicht message-broker, populair voor IoT. Ideaal voor Home Assistant en zelfbouw-systemen.
- **REST API (HTTP)** — cloud-only, leverancier-afhankelijk. Werkt overal maar valt uit als internet uitvalt.

Voor toekomstvastheid verdient Modbus TCP de voorkeur boven cloud-API's: lokale besturing blijft werken als een fabrikant zijn cloud uitzet.

## 11. Onderhoud en levensduur

Een vaak vergeten kostencomponent. De bedragen hieronder zijn **gelabelde eigen indicaties** — er is geen publieke bron die onderhoudskosten per component op één peildatum vergelijkt. Vraag je installateur wat hij voor jouw installatie rekent en vervang deze getallen daardoor. De levensduren zijn de orde van grootte die fabrikanten in hun documentatie aanhouden:

| Component | Onderhoud/jaar | Levensduur |
|---|---|---|
| Zonnepanelen | €0-€50 | 25-30 jaar |
| Omvormer | €0-€80 | 12-15 jaar |
| Thuisbatterij (LiFePO4) | €0-€120 | 15-20 jaar |
| Warmtepomp lucht-water | €175-€275 | 15-20 jaar |
| Slimme laadpaal | €25-€80 | 10-12 jaar |

Belangrijke nuance: garantie en levensduur zijn niet hetzelfde. Een omvormer met 10 jaar garantie gaat volgens fabrikantopgaven doorgaans 12-15 jaar mee. Reken voor je terugverdienberekening met verwachte levensduur, niet met de garantieperiode.

### Wat gaat er kapot?

Vier faalmodi die in servicedocumentatie van fabrikanten terugkomen. Wij hebben geen bron die ze op frequentie rangschikt, dus lees dit als een lijst met aandachtspunten en niet als een rangorde:

1. **Omvormer-koeling.** Stof, ventilatordefect. Eenvoudige reparatie of vervanging na circa 10 jaar.
2. **Bypass-diode in panelen.** Bij hotspots door schaduw. Vaak paneelvervanging onder garantie.
3. **Batterij-BMS.** Het batterijmanagementsysteem is de elektronica die uitval kan geven zonder dat de cellen zelf defect zijn. Of dat bij het ene merk vaker gebeurt dan bij het andere, is niet publiek vastgelegd; kijk naar de garantietermijn op de elektronica in het datasheet.
4. **Connector-corrosie.** Door slechte installatie. Te voorkomen met MC4-vet bij montage.

Voor preventief onderhoud: zie [de jaaronderhoud-checklist](/posts/beste-dynamisch-contract-met-zonnepanelen-2026/).

## 12. Wat gaat er veranderen in 2027-2030?

Onze verwachting op basis van wetgeving en marktontwikkeling — geen zekerheden:

**2027: einde saldering.** Zelfconsumptie wordt waardevoller; het verdienmodel van een batterij verschuift van teruglevering naar eigen gebruik en arbitrage.

**2028: bredere V2G-uitrol.** De eerste massamarktauto's ondersteunen bidirectioneel laden; verwachting is dat bidirectionele laadpalen in prijs dalen.

**2029: dynamisch contract als norm.** Vaste contracten worden waarschijnlijk nichés, mogelijk in de vorm van dynamisch met prijsplafond.

**Ketelvervanging: geen verplichting.** De aangekondigde normering die bij ketelvervanging een hybride warmtepomp verplicht zou stellen, is ingetrokken — niet uitgesteld. Er is dus geen wettelijke einddatum voor de gasketel waarop je je investeringsplanning kunt baseren. Wat er wél verandert, is de prijsverhouding tussen gas en stroom; dat is de variabele om in de gaten te houden.

Wie nu investeert in toekomstvaste hardware (open protocollen, AC-gekoppelde batterij, modulaire warmtepomp) staat sterker dan wie kiest voor gesloten cloud-systemen. Lees ook [de beleidsanalyse](/posts/terugleverkosten-zonnepanelen-2026/).

## 13. Rekenvoorbeelden per situatie

Vier fictieve rekenvoorbeelden met expliciete aannames. Bedragen zijn marktprijsindicaties, terugverdientijden volgen uit het model in hoofdstuk 7.

**Situatie A: rijtjeshuis, 2 personen, geen EV, 2.800 kWh verbruik**
8-10 zonnepanelen, 5 kWh batterij, dynamisch contract. Investering circa €8.500 voor het geheel, waarvan €3.550 de batterij. De terugverdientijd van dat pakket wordt volledig gedragen door de panelen (in ons model 6-8 jaar); de batterij zelf komt in het model uit op ruim twintig jaar en verlengt de terugverdientijd van het geheel dus. Warmtepomp nog niet aan de orde — eerst isoleren.

**Situatie B: 2-onder-1-kap, 4 personen, 1 EV, 5.200 kWh + 18.000 km/jaar**
14 panelen, 10 kWh batterij, warmtepomp, slimme laadpaal. Investering circa €24.000. De terugverdientijd van het geheel wordt hier gedragen door de panelen en de warmtepomp, niet door de batterij; die laatste levert in het model circa €353 per jaar op een investering van €5.500.

**Situatie C: vrijstaand, 5 personen, 2 EV's, 7.800 kWh + 30.000 km/jaar**
20+ panelen, 15-20 kWh modulair, warmtepomp, 2 laadpalen. Investering €38.000-€45.000, terugverdientijd 9-11 jaar bij maximale autonomie.

**Situatie D: appartement, 1-2 personen, 1.800 kWh**
Geen panelen mogelijk? Begin met een dynamisch contract en een slimme thermostaat. Reken hier niet op grote bedragen: bij 1.800 kWh verbruik is er weinig te verschuiven. Lukt het om een derde van dat verbruik (600 kWh) naar uren te schuiven die €0,05 per kWh goedkoper zijn, dan gaat het om circa €30 per jaar — en daar gaan de vaste kosten van het dynamische contract nog van af. Een investeringsbedrag noemen wij hier niet: dat hangt volledig af van wat je al hebt.

## 14. Slot

Verduurzamen is een marathon, geen sprint. Alles in één keer verbouwen levert een lange wachttijd op je terugverdientijd op; per jaar de meest renderende stap zetten werkt beter.

De volgorde die in vrijwel elk rekenmodel het beste uitpakt:

1. Isoleren (kruipruimte, spouwmuur, zolder) — €0-€8.000 — direct comfort en besparing.
2. Dynamisch contract plus monitoring — €0-€100 — direct €100-€300 per jaar.
3. Zonnepanelen — €4.000-€8.000 — terugverdientijd 6-8 jaar.
4. Warmtepomp (hybride of vol) — €4.000-€18.000 — terugverdientijd 7-12 jaar.
5. Thuisbatterij — €4.000-€10.000 — terugverdientijd in ons model achttien tot ruim twintig jaar; dit is de stap met het slechtste rendement en de reden dat hij als vijfde staat.
6. Slim laden EV en V2H — €1.500-€8.000 — varieert sterk.

Stap 1 en 2 zijn voor vrijwel iedereen zinvol. Stap 3-6 hangt af van budget en levensfase.

Volgende stap: lees [de vergelijking dynamisch versus vast](/posts/dynamisch-vs-vast-contract-2026/) voor verdieping, en vul het model hierboven met je eigen kwartierdata.

## Rekenvoorbeeld: 5 kWh batterij bij een gezinswoning

Een tweede rekenvoorbeeld, kleiner gedimensioneerd (fictief, aannames expliciet):

Verbruik 4.100 kWh per jaar, zonneproductie 5.200 kWh, EV-laden 6.500 kWh extra, batterij 5 kWh AC-gekoppeld. Met dezelfde rekenconstanten als hierboven:

- Verschuifbaar volume = de kleinste van 5 × 150 = 750 kWh, het overschot × 0,9 en de jaarafname. Door het EV-laden is de afname hoog en het overschot beperkt, maar 750 kWh blijft hier de bindende grens.
- Na retourrendement: 750 × 0,9 = 675 kWh × €0,19 = €128.
- Netarbitrage: 5 × €8 = €40.
- **Totaal circa €168 per jaar** voor dit profiel. Ons sitebrede kengetal voor 5 kWh is €177; dat verschil van €9 komt doordat het kengetal met een iets ruimere doorzet rekent. Wij laten beide getallen staan in plaats van het ene naar het andere af te ronden.

De referentieprijs is €3.550 inclusief 21% btw voor een 5 kWh-systeem (Sessy als referentie, prijspeil augustus 2026 via sessy.nl, exclusief installatie). Er is geen btw-teruggaaf en geen subsidie op een thuisbatterij: het 0%-tarief geldt alleen voor zonnepanelen en direct noodzakelijke onderdelen, en de ISDE dekt geen batterijopslag. Dat maakt de terugverdientijd in dit model **ruim twintig jaar** — langer dan de verwachte levensduur.

De les uit dit voorbeeld is niet dat een kleine batterij beter rendeert. Het is dat een batterij die volledig benut wordt weliswaar het maximum uit zijn capaciteit haalt, maar dat het maximum bij 5 kWh simpelweg klein is: 750 kWh per jaar verschuiven is bij elk realistisch prijsverschil geen bedrag waarmee je €3.550 binnen de levensduur terugverdient. Wie op korte terugverdientijden rekent, moet naar isolatie en zonnepanelen kijken, niet naar opslag.

## Veelgemaakte fouten in het rekenmodel

1. **Spreads te conservatief of te optimistisch inschatten.** Modellen rekenen vaak met een vaste gemiddelde spread. Kijk in de EPEX- of ENTSO-E-historie van je eigen jaar hoe de top-bottom spread zich werkelijk gedroeg en reken met een bandbreedte, niet met één getal.
2. **Cycle-degradatie negeren.** Cyclusopgaven verschillen sterk per fabrikant en per meetdefinitie; Charged noemt voor de Sessy 6.000+ cycli (sessy.nl, opgehaald 21 augustus 2026). Neem het degradatiepad uit het datasheet van jóuw model mee in je berekening en gebruik geen algemeen getal, want de restcapaciteit waarbij dat aantal geldt verschilt per merk.
3. **Energiebelasting vergeten.** Op importzijde betaal je energiebelasting per kWh, op exportzijde krijg je die niet terug. Spreads moeten dus na belasting worden gerekend.
4. **Maandfee niet opnemen.** Een fee van €5,99 per maand is €72 per jaar en drukt de nettowinst.
5. **Vermogen-cap negeren.** Een 5 kWh batterij met 2,5 kW omvormer laadt in één uur maximaal 2,5 kWh. Korte prijs-dips kun je daarmee niet volledig benutten.

## Wanneer arbitrage niet rendabel is

Heb je een vast contract zonder switchmogelijkheid de komende 18 maanden? Dan start je rekenmodel pas bij het einde van dat contract — dat schuift de terugverdientijd met dezelfde periode op.

Woon je in een gebied met netcongestie en afspraken over curtailment? Dan kan je batterij niet vrij terugleveren en vallen de arbitrage-inkomsten lager uit; hoeveel precies, hangt af van de voorwaarden van je netbeheerder.

## Het model in de praktijk bijhouden

Voor live dagvooruitprijzen zijn er twee gangbare routes: het transparantieplatform van ENTSO-E, en de API van je eigen leverancier als die er een aanbiedt. Voor het automatisch laten meebewegen van apparaten werken EVCC of Home Assistant met een prijsintegratie het soepelst — zie [Domoticz vs Home Assistant](/posts/domoticz-vs-home-assistant-energie-2026/) voor de platformkeuze.

Werk het model minimaal elk half jaar bij. De beursprijs schommelt seizoensgebonden, en zodra leveranciers wél terugleververgoedingen voor na 2027 publiceren, vervalt de belangrijkste aanname in dit model en moet stap 3 opnieuw.

---

**Externe bron:** [RVO — ISDE voor woningeigenaren](https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren) — het officiële overzicht van wat de ISDE wel en niet dekt (thuisbatterijen vallen er niet onder).
