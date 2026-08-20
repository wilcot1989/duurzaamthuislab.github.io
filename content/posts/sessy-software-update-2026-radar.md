---
title: 'Sessy Radar 2026: software-update + dynamisch'
date: 2026-06-06 08:00:00+01:00
lastmod: '2026-08-20 08:00:00+02:00'
description: Deep-dive Sessy Radar algoritme — hoe Sessy de marktprijzen volgt, wat de update brengt, en koppeling met dynamisch contract.
categories:
- thuisbatterijen
tags:
- Sessy
- Sessy Radar
- thuisbatterij algoritme
- dynamisch contract
- EPEX optimalisatie
- Sessy software update 2026
keywords:
- sessy radar algoritme 2026
- sessy software update 2026
- sessy thuisbatterij review
- sessy vs andere thuisbatterij
- sessy EPEX optimalisatie
affiliate: true
author: Wilco Terlouw
author_bio: Oprichter van DuurzaamThuisLab. Schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1589276534126-adef63a95e05&w=1200&output=webp&q=70
faq:
- q: Wat is Sessy Radar?
  a: Sessy Radar is het geïntegreerde optimalisatie-algoritme in de Sessy thuisbatterij. Het analyseert de EPEX day-ahead prijzen voor de komende 24–48 uur en bepaalt automatisch wanneer de batterij laadt (goedkope uren) en ontlaadt (dure uren). Je hoeft zelf niets in te stellen.
- q: Werkt Sessy Radar ook zonder Tibber of ander dynamisch contract?
  a: Sessy Radar is het meest effectief met een dynamisch contract waarbij de uurprijzen worden doorgegeven. Zonder dynamisch contract heeft Radar geen actuele prijsdata en valt het terug op een standaard dag/nacht-profiel. Voor optimale werking is een dynamisch contract (Tibber, ANWB Energie, Frank Energie) aanbevolen.
- q: Wat is er veranderd in de Sessy software-update van begin 2026?
  a: 'De 2026-updates bevatten: verbeterde voorspelkwaliteit van gebruikspatronen (machine learning op huishoudprofiel), betere integratie met P1-meterdata voor nauwkeuriger net-export-anticipatie, en een nieuwe ''combi-modus'' die zonne-energie en EPEX-optimalisatie combineert zonder conflicten.'
- q: Hoe koppel ik Sessy aan Tibber?
  a: In de Sessy-app ga je naar Instellingen > Energiecontract > Tibber. Je logt in met je Tibber-account en geeft Sessy toestemming om de uurprijsdata te lezen. Sessy Radar begint direct met het plannen van laad- en ontlaadcycli op basis van de gepubliceerde day-ahead prijzen.
- q: Wat is het verschil tussen Sessy Radar en concurrenten zoals Huawei Luna optimalisatie?
  a: Sessy Radar is specifiek ontworpen voor EPEX-prijsoptimalisatie met open API-koppeling. Huawei Luna optimaliseert primair voor eigenverbruik van zonne-energie. Huawei heeft geen native EPEX-koppeling voor uurprijsoptimalisatie. Sessy is daarmee sterker voor zuivere arbitrage op de spotmarkt.
- q: Hoeveel verdient Sessy Radar me per jaar extra ten opzichte van geen optimalisatie?
  a: 'Een modelberekening met 4,2 kWh bruikbare capaciteit per cyclus, circa 200 productieve cycli per jaar en een all-in prijsverschil van €0,10 tot €0,18 per kWh komt uit op ruwweg €85 tot €190 per jaar uit zuivere EPEX-arbitrage, bovenop de besparing uit eigenverbruik van zonnestroom. De werkelijke opbrengst hangt sterk af van de volatiliteit van de EPEX-markt in dat jaar en van je verbruiksprofiel.'
- q: Kan Sessy ook terugleveren aan het net bij hoge prijzen?
  a: Ja. Als je netbeheerder teruglevering toestaat (de meeste doen dat) en je dynamische leverancier teruglevering vergoedt op het live tarief, kan Sessy actief terugleveren bij hoge EPEX-prijzen. Niet alle leveranciers vergoeden dit op het spotmarkt-tarief — check je contract.
products:
- name: Sessy thuisbatterij
  url: https://go.duurzaamthuislab.nl/sessy
  price: '3999'
schema_type: Article
---
De Sessy is een van de weinige thuisbatterijen die je in Nederland kunt kopen met een ingebouwde koppeling aan de EPEX-uurprijzen. Dutch New Energy rolde tussen najaar 2025 en voorjaar 2026 een reeks firmware-updates uit die het optimalisatie-algoritme — Sessy Radar — op belangrijke punten hebben veranderd. Genoeg reden voor een apart artikel.

Want "algoritme" klinkt als een zwarte doos die je maar moet vertrouwen. In dit artikel leggen we uit wat Radar volgens de documentatie van Dutch New Energy doet, welke beslissingen het per uur neemt, wat de updates concreet toevoegen en wat dat volgens modelberekeningen kan opleveren. Basis: de release-informatie en handleiding van Sessy, publieke EPEX-data, leveranciersvoorwaarden en geverifieerde gebruikersreviews.

*Dit artikel bevat affiliate links. Wij ontvangen een vergoeding als je via onze links een product aanschaft, zonder extra kosten voor jou.*

---


> **Kort antwoord:** Deep-dive Sessy Radar algoritme — hoe Sessy de marktprijzen volgt, wat de update brengt, en koppeling met dynamisch contract.
>
> Sessy Radar is het geïntegreerde optimalisatie-algoritme in de Sessy thuisbatterij. Het analyseert de EPEX day-ahead prijzen voor de komende 24–48 uur en bepaalt automatisch wanneer de batterij laadt (goedkope uren) en ontlaadt (dure uren). Je hoeft zelf niets in te stellen.

## Wat is de Sessy thuisbatterij in 2026?

Eerst de basisfeiten, voordat we inzoomen op Radar.

De Sessy is een Nederlandse thuisbatterij, ontwikkeld door Dutch New Energy (onderdeel van Featurespace/Seeder labs, gevestigd in Amsterdam). De Sessy is ontworpen als een betaalbare maar intelligente thuisbatterij specifiek voor de Nederlandse markt — met EPEX-koppeling als onderscheidend kenmerk dat bij de meeste concurrenten ontbreekt of later is toegevoegd.

**Technische specs 2026 (Sessy Gen 2):**
| Spec | Waarde |
|------|--------|
| Capaciteit | 5 kWh bruikbaar |
| Laad/ontlaad-vermogen | 3 kW |
| Round-trip efficiency | 92–94% |
| Batterijchemie | LFP (LiFePO4) |
| Levensduur cycli | 6.000 cycli tot 80% |
| Garantie | 10 jaar |
| Gewicht | 59 kg |
| Afmetingen | 58 × 24 × 52 cm (wand) |
| Connectiviteit | Wifi, P1-poort |
| Prijs 2026 | **€3.999** |

**[Bekijk Sessy thuisbatterij](https://go.duurzaamthuislab.nl/sessy)**

---

## Sessy Radar: het algoritme uitgelegd

### Hoe werkt Radar op hoofdlijnen?

Sessy Radar is een multi-step optimalisatie-algoritme dat dagelijks meerdere malen draait. De kern is een lineair programmeringsprobleem: gegeven de EPEX-prijsdata voor de komende 24 uur, de huidige batterijlading, het verwachte verbruiksprofiel en de beschikbare capaciteit — bepaal het optimale laad- en ontlaad-schema dat de netto energiekosten minimaliseert.

Dit klinkt simpel maar bevat meerdere lagen van complexiteit.

### Stap 1: Dataverzameling (elk uur vernieuwd)

Radar trekt realtime de volgende inputs:
- **EPEX day-ahead prijzen** voor de komende 24–48 uur (gepubliceerd om 12:00 voor de volgende dag)
- **P1-meterdata** (als je een P1-poort hebt) — realtime nettoverbruik en zonne-energieproductie
- **Sessy-app-data** — huidig laadniveau, batterijgezondheid, temperatuur

### Stap 2: Verbruiksprofielschatting

Hier zit de machine learning component. Sessy leert na 2–4 weken gebruik jouw huishoudprofiel: wanneer gebruik jij typisch veel stroom, wanneer weinig? Wanneer zijn je zonnepanelen actief?

De 2026-update heeft deze voorspelmodule aanzienlijk verbeterd. Het systeem gebruikt nu een rolling window van 14 dagen historische data (was 7 dagen in 2024) en weegt weekdagen en weekenden apart. Dit resulteerde intern in 8–12% betere voorspelnauwkeurigheid in de beta-tests voor de update.

**Praktisch effect:** de Sessy verspreidt de laadmomenten beter over meerdere goedkope uren in plaats van één groot blok, waardoor de batterij soepeler aansluit op je werkelijke verbruikspatroon.

### Stap 3: Optimalisatie

Gegeven de inputs berekent Radar per uur of het beter is om:
- **Te laden** (net → batterij) bij lage prijs
- **Te ontladen** (batterij → huis) bij hoge prijs, zodat minder van het net wordt afgenomen
- **Terug te leveren** (batterij → net) als je leverancier dat vergoedt op spotprijs
- **Niets te doen** (als prijzen gemiddeld zijn en batterij al vol/leeg is)

De optimalisatie houdt rekening met:
- **Round-trip efficiency** (laden + ontladen = 92–94% efficiënt, de rest is warmteverlies)
- **Degradatiekosten** — elke cyclus slijt de batterij een kleine fractie; de optimizer rekent dit mee (verwachte vervangingskosten gedeeld door levensduurcycli)
- **Minimum State of Charge (SoC)** — Radar houdt standaard 10% reserve aan als noodstroom buffer
- **Temperatuurcompensatie** — bij koud weer (winternacht) daalt de capaciteit licht; het algoritme compenseert

### Stap 4: Uitvoering en monitoring

Na het plannen stuurt Radar opdrachten naar de laad/ontlaad-controller van de Sessy. De planning wordt elk uur herberekend op basis van nieuwe EPEX-data en actueel verbruik. Dit is "rolling optimization" — het plan is nooit definitief maar past zich continue aan.

---

## De 2026 software-updates: wat er concreet veranderd is

Dutch New Energy heeft in de periode oktober 2025 – maart 2026 vier significante firmware-updates uitgebracht.

### Update v3.4 (oktober 2025): intraday marktkoppeling

Naast day-ahead data (prijzen voor morgen) kan Sessy nu ook intraday EPEX-data (prijzen voor de komende uren op dezelfde dag) gebruiken als referentie. In de praktijk zijn de meeste afwijkingen tussen day-ahead en intraday beperkt (<8%), maar bij onverwachte weersveranderingen (plotse bewolking bij voorspelde zonnige dag) kan de intraday prijs significant afwijken.

**Effect:** Sessy kan haar plan aanpassen als de prijsverwachting binnen de dag omslaat, bijvoorbeeld bij onverwachte bewolking of een plotselinge windpiek. Gebruikers melden dat het geplande ontlaadmoment daardoor soms een of twee uur opschuift ten opzichte van de oorspronkelijke day-ahead planning.

### Update v3.5 (december 2025): verbeterd P1-integratie

De P1-koppeling (via de P1-poort van je slimme meter) is verbeterd in responstijd. Was de vorige versie 30-seconden polling, nu is het 10-seconden polling. Dit klinkt technisch, maar betekent dat de Sessy sneller reageert op plotselinge verbruikspieken (bijv. je zet een waterkoker aan).

**Effect:** minder netto-importpieken bij plotselinge verbruiken en een betere aansluiting op het eigenverbruikspatroon. Een exact percentage verbetering is niet publiek gedocumenteerd; wij noemen daarom geen cijfer.

### Update v3.7 (februari 2026): nieuwe combi-modus

Dit is de meest impactvolle update van 2025-2026. De nieuwe "combi-modus" combineert twee strategieën die voorheen apart werden uitgedacht:
1. **Solar-maximalisatie** (eigenverbruik van zonne-energie optimaliseren)
2. **EPEX-arbitrage** (goedkoop laden, duur ontladen)

In de oude versie kon dit conflicteren: de EPEX-optimizer wilde de batterij leeg houden voor een goedkoop nachtelijk laadmoment, terwijl er 's middags zonne-energie beschikbaar was die niet werd opgeslagen.

De combi-modus lost dit op door een gewogen doelstelling: de optimizer maximaliseert de combinatie van solar-eigenverbruik (waarde = vermeden inkoop) en EPEX-arbitrage (waarde = prijsverschil), met solar-eigenverbruik als hogere prioriteit als de EPEX-marge klein is.

**Wat dat praktisch betekent:**
- Vóór de combi-modus kon een batterij op een zonnige winterdag 's middags leeg blijven wachten op de avondpiek, terwijl er op datzelfde moment zonnestroom werd teruggeleverd die opgeslagen had kunnen worden. Dat is precies de klacht die in gebruikersreviews van de oudere firmware terugkomt.
- Met de combi-modus laadt de batterij ook op zonne-energie wanneer de opbrengst voldoende is, óók als er 's avonds een aantrekkelijke EPEX-piek in de planning staat. De optimizer weegt beide waarden tegen elkaar af in plaats van één strategie te laten winnen.

### Update v3.8 (maart 2026): teruglevering bij negatieve EPEX

De meest controversiële update. Sessy kan nu de batterij actief ontladen naar het net (teruglevering) als de EPEX-spotprijs boven een door de gebruiker ingestelde drempel ligt.

Dit vereist dat je energieleverancier teruglevering vergoedt op het spotprijs-tarief. Bij Tibber is dit het geval.

**Rekenvoorbeeld (modelberekening met deze aannames):**
- 18:00: EPEX-prijs €0,32/kWh (na belasting en transport)
- Sessy laadniveau: 80%
- Sessy levert terug: 2 kW × 1 uur = 2 kWh × €0,32 = **€0,64 ontvangen**
- Daarna laadt Sessy op om 02:00 bij €0,06/kWh: 2 kWh × €0,06 = **€0,12 kosten**
- **Netto opbrengst per cyclus: €0,52**

Bij 50 van dergelijke momenten per jaar — plausibel in wintermaanden met hoge volatiliteit — komt het model uit op **circa €26 per jaar extra**. Bescheiden dus, maar het kost je niets extra behalve wat batterijcycli.

**Aandachtspunt:** niet alle netbeheerders staan onbeperkt teruglevering toe. Controleer of jouw netbeheerder terugleveren via batterij toestaat en of je leverancier het op spotprijs-tarief vergoedt.

---

## Sessy Radar vs. concurrenten: eerlijke vergelijking

De EPEX-optimalisatie van Sessy is haar grootste onderscheidende eigenschap. Maar hoe verhoudt dit zich tot concurrenten?

| Thuisbatterij | EPEX-koppeling | Eigenverbruiksoptimalisatie | P1-integratie | Teruglevering spotprijs |
|--------------|---------------|---------------------------|---------------|------------------------|
| **Sessy** | ✅ Volledig | ✅ Combi-modus | ✅ 10 sec polling | ✅ (v3.8) |
| **Huawei Luna** | ❌ (alleen eigenverbruik) | ✅ Excellent | ✅ Via FusionSolar | ❌ Geen native |
| **VARTA Element** | ❌ | ✅ Goed | ✅ Via EMS | ❌ |
| **Sonnen eco** | Beperkt (vaste tariefvensters) | ✅ Goed | ✅ | ❌ |
| **Enphase IQ Battery** | ❌ | ✅ Via Enlighten | ✅ | ❌ |
| **SolarEdge Home** | ❌ | ✅ Via SolarEdge API | ✅ | ❌ |

Sessy is in 2026 de enige betaalbare thuisbatterij in Nederland met native EPEX day-ahead koppeling én teruglevering op spotprijs. Dit is haar sterkste argument.

**Wanneer kies je Sessy Radar boven Huawei Luna?**
- Je hebt een dynamisch contract (Tibber, Frank Energie) en wil EPEX-arbitrage
- Zonnepanelen zijn kleiner (<4 kWp) — eigenverbruiksoptimalisatie is dan minder dominant
- Je wil actief arbitreren, ook zonder zonnepanelen

**Wanneer kies je Huawei Luna boven Sessy?**
- Je hebt een Huawei SUN2000 omvormer (naadloze DC-koppeling)
- Grote zonnepaneelinstallatie (>6 kWp) — eigenverbruik is dan al voldoende arbitrage
- Je wil de beste monitoring-app van de markt

---

## Wat kan Sessy Radar opleveren? Een modelberekening

Onderstaande berekening is een model met expliciete aannames, geen meting aan een bestaande installatie. Uitgangspunt: Sessy Gen 2 (5 kWh bruikbaar), een tussenwoning met circa 4,8 kWp zonnepanelen en een dynamisch contract waarbij de uurprijzen worden doorgegeven.

**Aannames:**
- Bruikbare arbitragecapaciteit per cyclus: 5 kWh, minus 10% minimum-SoC-reserve en circa 7% rondgangsverlies → effectief circa 4,2 kWh per cyclus.
- Bruikbaar prijsverschil (all-in, dus inclusief energiebelasting en btw) tussen het laadmoment en het vermeden afnamemoment: gemiddeld €0,10-€0,14/kWh. In de winter is de spread groter, in de zomer kleiner.
- Aantal cycli waarop arbitrage daadwerkelijk iets oplevert: circa 200 per jaar. Op vlakke prijsdagen levert een cyclus niets op en slaat de optimizer die over.

**Uitkomst:**
- Per productieve cyclus: 4,2 kWh × €0,10 tot €0,14 = **€0,42 tot €0,59**
- Op jaarbasis: 200 × €0,42 tot €0,59 = **circa €85 tot €120 per jaar** uit zuivere EPEX-arbitrage

Reken je met een ruimere spread (€0,18/kWh gemiddeld, realistisch in een winter met veel volatiliteit) en 250 productieve cycli, dan komt het model uit rond €190 per jaar. De bandbreedte is dus breed, en dat is inherent: de opbrengst is een functie van de marktvolatiliteit in dat specifieke jaar, en die is niet vooraf bekend.

De opbrengst uit solar-eigenverbruik komt hier bovenop en is een andere rekensom: die hangt af van je zonproductie, je verbruikspatroon en het verschil tussen afnameprijs en terugleververgoeding — zie ons artikel over de [terugverdientijd van een thuisbatterij](/posts/thuisbatterij-terugverdientijd-berekenen-2026/).

---

## Praktische setup: Sessy Radar correct configureren

### Stap 1: Koppel je dynamische leverancier

In de Sessy-app (Instellingen → Energiecontract):
- Kies Tibber, Frank Energie of ANWB Energie
- Autoriseer de Sessy-app om uurprijsdata te lezen via OAuth
- Sessy begint direct met optimaliseren op basis van dag-ahead data

### Stap 2: Koppel je P1-meter

Verbind een HomeWizard P1-meter of vergelijkbare P1-reader via de Sessy-app. Dit geeft Sessy realtime inzicht in je nettoverbruik, waardoor de eigenverbruiksoptimalisatie nauwkeuriger is.

Kosten P1-meter: €30–€49 (HomeWizard, DSMR-reader).

### Stap 3: Stel minimum SoC in

Standaard houdt Sessy 10% in reserve. Als je de Sessy ook als noodstroom wil gebruiken bij stroomstoring, stel dan een hogere minimum-SoC in (bijv. 20–30%). Dit verlaagt de effectieve arbitrage-capaciteit licht maar geeft buffer.

### Stap 4: Activeer teruglevering (v3.8)

Ga naar Instellingen → Geavanceerd → Teruglevering naar net. Stel een drempelprijs in boven welke Sessy mag terugleveren. Beginadvies: start bij €0,28/kWh om te zien hoe vaak dit in jouw situatie voorkomt.

### Stap 5: Monitor en bijsturen

In de Sessy-app zie je per dag het laad-/ontlaad-schema, de gerealiseerde prijzen en de berekende besparing. Controleer de eerste twee weken of het schema logisch aansluit op jouw gebruiksprofiel. Correcties zijn mogelijk via "Gebruiksprofiel overschrijven."

---

## Beperkingen en eerlijke kanttekeningen

**Sessy Radar is geen magische machine.** Dit zijn de structurele beperkingen van dit type optimalisatie:

**1. Forecasting-fouten bij onverwachte weersveranderingen**
Radar plant op basis van verwachtingen. Slaat het weer om — een onverwachte storm levert plotseling veel windenergie, waardoor de avondprijs juist keldert in plaats van piekt — dan blijkt een eerder ontlaadbesluit achteraf suboptimaal. Dit is inherent aan optimaliseren op een voorspelling en niet met software op te lossen; het gaat om incidentele dagen, niet om een structureel verlies.

**2. Teruglevering niet overal vergoed**
Niet alle leveranciers vergoeden teruglevering op de live spotprijs. Check je contract. Bij vaste teruglevering (bijv. €0,08/kWh vast) is teruglevering via Sessy minder aantrekkelijk of zelfs verliesgevend bij lage inkoopprijzen.

**3. Degradatiekosten zijn aanwezig**
Elke laad/ontlaad-cyclus kost batterijlevensduur. Sessy rekent dit mee in de optimizer, maar de aangenomen degradatiekosten per cyclus zijn conservatief ingesteld. In de praktijk kan de batterij sneller degenereren als je dagelijks één volle cyclus draait. Na 6.000 cycli (de gespecificeerde levensduur) is de batterijcapaciteit naar 80% gedaald.

---

## Conclusie: Sessy Radar is de beste EPEX-optimizer op de thuisbatterijmarkt

Op basis van de functievergelijking hierboven is ons redactionele oordeel positief en specifiek: Sessy Radar is in 2026 de meest complete EPEX-optimizer in deze prijsklasse op de Nederlandse thuisbatterijmarkt. De combi-modus (solar + arbitrage), de teruglevering-functie en de verbeterde P1-integratie maken de Sessy de beste keuze voor wie een dynamisch contract heeft en serieus wil arbitreren op de spotmarkt.

Het is geen universele winnaar: voor wie enkel eigenverbruik wil optimaliseren met een grote PV-installatie is Huawei Luna mogelijk efficiënter door de betere DC-koppeling. Maar voor EPEX-first gebruik is de Sessy ongeëvenaard in zijn prijsklasse.

Wel een kanttekening bij het rendement: op de modelmatige €85 tot €190 per jaar uit pure EPEX-arbitrage is een Sessy van €3.999 niet terug te verdienen — dat zou 20 jaar of meer duren. De business case draait daarom op de combinatie: arbitrage plus de besparing op eigenverbruik van zonnestroom, die na de afbouw van de saldering flink zwaarder gaat wegen. Zie de paragraaf hieronder over 2027.

---


<a href="https://go.duurzaamthuislab.nl/sessy" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">Bekijk Sessy</a>

## Wat voegt de EPEX-koppeling toe boven pure eigenverbruiksoptimalisatie?

Dit is de kernvraag bij de Sessy, want een batterij zonder EPEX-koppeling optimaliseert alleen op eigenverbruik van zonnestroom. Onderstaande vergelijking is een modelberekening voor het winterkwartaal, de periode waarin het verschil het grootst is.

**Aannames voor een winterkwartaal (januari-maart), 4,8 kWp PV, 5 kWh batterij:**

*Zonder EPEX-koppeling (alleen eigenverbruik):* de zonproductie is in deze maanden laag, dus er is weinig om te bufferen. Bij circa 90 kWh die je in het kwartaal via de batterij zelf verbruikt in plaats van teruglevert, en een waardeverschil van circa €0,24/kWh tussen afname en teruglevering, komt dat op **circa €22 in het kwartaal**.

*Met EPEX-koppeling:* de batterij kan daarnaast dagelijks een netcyclus draaien op het prijsverschil tussen nacht en avondpiek. Bij circa 70 productieve cycli in een winterkwartaal, 4,2 kWh effectief per cyclus en een all-in spread van €0,12/kWh: **circa €35 extra in het kwartaal**.

**Modelmatig verschil: de EPEX-koppeling voegt in een winterkwartaal ruwweg €35 toe** — meer dan een verdubbeling van de kwartaalwaarde. Over een heel jaar is het verschil relatief kleiner, omdat de zomer juist het omgekeerde patroon geeft: veel eigenverbruikswaarde, lage volatiliteit. Wie geen dynamisch contract heeft of niet wil, laat deze component volledig liggen — dan is de meerwaarde van Radar boven een gewone batterij beperkt tot de eigenverbruiksoptimalisatie die de concurrentie ook biedt.

---

## Veelgestelde vragen van Sessy-gebruikers

**"Mijn Sessy laadt niet in de nacht terwijl de EPEX-prijs laag was — waarom?"**

Sessy Radar kijkt niet alleen naar de huidige prijs maar naar de geoptimaliseerde spread over de komende 24 uur. Als er 's ochtends vroeg een nog lagere prijs wordt verwacht, kan Radar besluiten te wachten. Ook: als de batterij al deels vol is, is het niet altijd optimaal om extra te laden op een lage prijs als er de volgende dag geen hoge piekprijs wordt verwacht.

**"De Sessy-app toont een negatieve besparing deze week — is dat normaal?"**

De besparing in de app is berekend op basis van wat er zonder de batterij gekost zou hebben. In weken met weinig EPEX-volatiliteit en weinig zonne-energie is de besparing inderdaad klein of zelfs negatief — dat is normaal en zegt weinig over het jaarresultaat. Beoordeel de opbrengst daarom nooit op een week of maand, maar over minimaal een volledig jaar.

**"Kan ik Sessy ook handmatig overschrijven?"**

Ja. In de Sessy-app kun je via "Manueel instellen" de batterij forceren te laden of ontladen op een moment dat jij kiest. Na het handmatige commando valt de Sessy terug op automatische Radar-planning.

---

## Sessy in 2027: de saldering-afbouw als businessgeval

De salderingsregeling vervalt per 2027. Dit verandert de waarde van een thuisbatterij fundamenteel.

Zolang je kunt salderen, is elke teruggeleverde kWh vrijwel evenveel waard als een afgenomen kWh — en dan verdient een batterij weinig terug. Verdwijnt de saldering, dan ontstaat er een gat tussen wat je voor teruglevering krijgt en wat je voor afname betaalt. Precies dat gat is de waarde die een batterij kan oogsten.

**Modelberekening voor de situatie na 2027 (aannames: PV 4,8 kWp, 5 kWh batterij, afnameprijs €0,28/kWh, terugleververgoeding €0,05/kWh):**

- Zonnestroom die je zonder batterij zou terugleveren en met batterij zelf verbruikt: circa 1.100 kWh per jaar
- Waardeverschil per kWh: €0,28 − €0,05 = €0,23
- Extra jaarwaarde eigenverbruik: 1.100 × €0,23 = **circa €250**
- Plus EPEX-arbitrage volgens de eerdere modelberekening: **€85 tot €190**
- **Totaal modelmatig: circa €335 tot €440 per jaar**

Bij een aanschafprijs van €3.999 komt dat neer op een terugverdientijd van ruwweg negen tot twaalf jaar — een lange horizon, maar wel binnen de opgegeven levensduur van 6.000 cycli en met tien jaar garantie. De richting is in ieder geval duidelijk: de business case van een thuisbatterij wordt beter naarmate de saldering verder afbouwt, niet slechter. Alle bedragen hierboven zijn modelmatig en staan of vallen met de energieprijzen en terugleververgoeding die dan gelden.

**[Bekijk Sessy thuisbatterij](https://go.duurzaamthuislab.nl/sessy)**

## Gerelateerde artikelen

- [Huawei Luna vs Tesla Powerwall vs Sessy 2026](/posts/huawei-luna-vs-tesla-powerwall-vs-sessy-2026/)
- [Sessy review 2026: eerlijke test van de Nederlandse](/posts/sessy-review-thuisbatterij-nederland/)
- [Thuisbatterij Zonder Zonnepanelen: Heeft Het Zin in 2027?](/posts/batterij-na-2027-zonder-zonnepanelen-zin-2026/)
- [Beste 10 kWh thuisbatterij 2026: vergelijking 7 topmerken](/posts/thuisbatterij-10-kwh-vergelijking-2026/)
- [Thuisbatterij binnen of buiten plaatsen: veilig 2026](/posts/thuisbatterij-buiten-vs-binnen-installeren-2026/)

---

**Externe bron:** [RVO — ISDE-subsidie info](https://www.rvo.nl/subsidies-financiering/isde) — onafhankelijke informatie over dit onderwerp.
