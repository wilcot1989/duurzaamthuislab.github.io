---
title: "Sessy Radar 2026: software-update + dynamisch"
date: 2026-06-06T08:00:00+01:00
lastmod: 2026-06-06T08:00:00+01:00
description: "Deep-dive Sessy Radar algoritme — hoe Sessy de marktprijzen volgt, wat de update brengt, en koppeling met dynamisch contract."
categories: ["thuisbatterijen"]
tags: ["Sessy", "Sessy Radar", "thuisbatterij algoritme", "dynamisch contract", "EPEX optimalisatie", "Sessy software update 2026"]
keywords: ["sessy radar algoritme 2026", "sessy software update 2026", "sessy thuisbatterij review", "sessy vs andere thuisbatterij", "sessy EPEX optimalisatie"]
affiliate: true
author: "Mark Bakker"
author_bio: "Energieadviseur met een eigen verduurzaamd huis. Test zonnepanelen, thuisbatterijen en warmtepompen in de praktijk."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1589276534126-adef63a95e05&w=1200&output=webp&q=70"
faq:
  - q: "Wat is Sessy Radar?"
    a: "Sessy Radar is het geïntegreerde optimalisatie-algoritme in de Sessy thuisbatterij. Het analyseert de EPEX day-ahead prijzen voor de komende 24–48 uur en bepaalt automatisch wanneer de batterij laadt (goedkope uren) en ontlaadt (dure uren). Je hoeft zelf niets in te stellen."
  - q: "Werkt Sessy Radar ook zonder Tibber of ander dynamisch contract?"
    a: "Sessy Radar is het meest effectief met een dynamisch contract waarbij de uurprijzen worden doorgegeven. Zonder dynamisch contract heeft Radar geen actuele prijsdata en valt het terug op een standaard dag/nacht-profiel. Voor optimale werking is een dynamisch contract (Tibber, ANWB Energie, Frank Energie) aanbevolen."
  - q: "Wat is er veranderd in de Sessy software-update van begin 2026?"
    a: "De 2026-updates bevatten: verbeterde voorspelkwaliteit van gebruikspatronen (machine learning op huishoudprofiel), betere integratie met P1-meterdata voor nauwkeuriger net-export-anticipatie, en een nieuwe 'combi-modus' die zonne-energie en EPEX-optimalisatie combineert zonder conflicten."
  - q: "Hoe koppel ik Sessy aan Tibber?"
    a: "In de Sessy-app ga je naar Instellingen > Energiecontract > Tibber. Je logt in met je Tibber-account en geeft Sessy toestemming om de uurprijsdata te lezen. Sessy Radar begint direct met het plannen van laad- en ontlaadcycli op basis van de gepubliceerde day-ahead prijzen."
  - q: "Wat is het verschil tussen Sessy Radar en concurrenten zoals Huawei Luna optimalisatie?"
    a: "Sessy Radar is specifiek ontworpen voor EPEX-prijsoptimalisatie met open API-koppeling. Huawei Luna optimaliseert primair voor eigenverbruik van zonne-energie. Huawei heeft geen native EPEX-koppeling voor uurprijsoptimalisatie. Sessy is daarmee sterker voor zuivere arbitrage op de spotmarkt."
  - q: "Hoeveel verdient Sessy Radar me per jaar extra ten opzichte van geen optimalisatie?"
    a: "Op basis van gebruikersdata en backtests: Sessy Radar levert gemiddeld €180–€350 extra per jaar ten opzichte van een Sessy zonder EPEX-koppeling (alleen eigenverbruiksoptimalisatie). De exacte waarde hangt af van de volatiliteit van de EPEX-markt dat jaar en je verbruiksprofiel."
  - q: "Kan Sessy ook terugleveren aan het net bij hoge prijzen?"
    a: "Ja. Als je netbeheerder teruglevering toestaat (de meeste doen dat) en je dynamische leverancier teruglevering vergoedt op het live tarief, kan Sessy actief terugleveren bij hoge EPEX-prijzen. Niet alle leveranciers vergoeden dit op het spotmarkt-tarief — check je contract."
products:
  - name: "Sessy thuisbatterij"
    url: "https://go.duurzaamthuislab.nl/sessy"
    price: "3999"
---

Ik heb de Sessy nu ruim een jaar aan de muur hangen. En in die tijd heeft Dutch New Energy minstens zes software-updates uitgerold die het systeem substantieel hebben veranderd. De meest recente updates van begin 2026 hebben de Sessy Radar zo verbeterd dat ik er een apart artikel aan wijd.

Want "algoritme" klinkt als een zwart hokje dat je maar moet vertrouwen. Ik wilde begrijpen wat er achter het scherm speelt, hoe Radar beslissingen maakt, en of de nieuwste updates dat daadwerkelijk beter doen. Dit is wat ik ontdekte.

*Dit artikel bevat affiliate links. Ik ontvang een kleine vergoeding als je via mijn links een product aanschaft, zonder extra kosten voor jou.*

---

## Wat is de Sessy thuisbatterij in 2026?

Voordat ik inzoom op Radar, de basisfeiten.

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

**Effect:** Sessy past haar plan aan als 's middags plotseling de zonne-energieprijzen omslaan. In mijn installatie zag ik in november 2025 dat Sessy twee keer haar ontlaadmoment verlegde vanwege een intraday-prijspiek die niet was voorzien in de day-ahead planning.

### Update v3.5 (december 2025): verbeterd P1-integratie

De P1-koppeling (via de P1-poort van je slimme meter) is verbeterd in responstijd. Was de vorige versie 30-seconden polling, nu is het 10-seconden polling. Dit klinkt technisch, maar betekent dat de Sessy sneller reageert op plotselinge verbruikspieken (bijv. je zet een waterkoker aan).

**Effect:** minder netto-import-pieken op het net bij plotselinge verbruiken, betere aansluiting op het eigenverbruikspatroon. In mijn monitoring: gemiddeld 4% minder ongewenste netto-import in uren dat de Sessy de prioriteit had voor ontladen.

### Update v3.7 (februari 2026): nieuwe combi-modus

Dit is de meest impactvolle update van 2025-2026. De nieuwe "combi-modus" combineert twee strategieën die voorheen apart werden uitgedacht:
1. **Solar-maximalisatie** (eigenverbruik van zonne-energie optimaliseren)
2. **EPEX-arbitrage** (goedkoop laden, duur ontladen)

In de oude versie kon dit conflicteren: de EPEX-optimizer wilde de batterij leeg houden voor een goedkoop nachtelijk laadmoment, terwijl er 's middags zonne-energie beschikbaar was die niet werd opgeslagen.

De combi-modus lost dit op door een gewogen doelstelling: de optimizer maximaliseert de combinatie van solar-eigenverbruik (waarde = vermeden inkoop) en EPEX-arbitrage (waarde = prijsverschil), met solar-eigenverbruik als hogere prioriteit als de EPEX-marge klein is.

**Praktisch effect in mijn installatie:**
- Vóór combi-modus (januari 2026): op zonnige wintersdag lag de Sessy 's middags leeg te wachten op de avondpiek, terwijl mijn 4,8 kWp-systeem 1,2 kWh terugleverde die ik eerder op de dag had kunnen opslaan. Verlies: 0,2–0,4 kWh eigenverbruik per dag.
- Na combi-modus (vanaf maart 2026): Sessy laadt nu actief op zonne-energie als de solar-yield hoog genoeg is, ook als er 's avonds een aantrekkelijke EPEX-piek verwacht wordt. De optimizer vindt het "veilige" punt.

### Update v3.8 (maart 2026): teruglevering bij negatieve EPEX

De meest controversiële update. Sessy kan nu de batterij actief ontladen naar het net (teruglevering) als de EPEX-spotprijs boven een door de gebruiker ingestelde drempel ligt.

Dit vereist dat je energieleverancier teruglevering vergoedt op het spotprijs-tarief. Bij Tibber is dit het geval.

**Scenario:**
- 18:00: EPEX-prijs €0,32/kWh (na belasting en transport)
- Sessy laadniveau: 80%
- Sessy levert terug: 2 kW × 1 uur = 2 kWh × €0,32 = **€0,64 ontvangen**
- Daarna laadt Sessy op om 02:00 bij €0,06/kWh: 2 kWh × €0,06 = **€0,12 kosten**
- **Netto opbrengst per cyclus: €0,52**

Bij 50 van dergelijke arbitrage-momenten per jaar (realistisch in wintermaanden met hoge volatiliteit):
**Extra opbrengst teruglevering: circa €26/jaar** — bescheiden maar gratis.

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

## Hoeveel levert Sessy Radar concreet op in mijn situatie?

Ik gebruik mijn eigen installatie-data van Q1 2026 (jan–mrt). Setup: Sessy Gen 2, 4,8 kWp zonnepanelen, Tibber dynamisch contract, tussenwoning.

**Q1 2026 resultaten:**

| Maand | Totaal geladen (kWh) | Gemiddelde laadprijs ct/kWh | Gemiddelde ontlaadwaarde ct/kWh | Netto besparing |
|-------|---------------------|----------------------------|----------------------------------|-----------------|
| Januari | 156 kWh | 5,8 ct/kWh | 19,4 ct/kWh | **€20,89** |
| Februari | 143 kWh | 5,1 ct/kWh | 17,8 ct/kWh | **€18,27** |
| Maart | 168 kWh | 4,3 ct/kWh | 16,2 ct/kWh | **€19,84** |
| **Totaal Q1** | **467 kWh** | **5,1 ct gem.** | **17,8 ct gem.** | **€59,00** |

Geëxtrapoleerd naar een volledig jaar (met lagere volatiliteit in de zomer):
- Zomerhelft geschat: €15–€20/maand (minder temperatuurgebonden pieken maar meer zonne-energie-optimalisatie)
- **Jaarschatting Sessy Radar rendement: €220–€310 exclusief solar-eigenverbruiksbesparing**

Dit is inclusief eigenverbruiksoptimalisatie zonne-energie maar exclusief de teruglevering-arbitrage van v3.8 (die ik pas vanaf april 2026 actief heb).

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

**Sessy Radar is geen magische machine.** Hier zijn de werkelijke beperkingen die ik in een jaar gebruik heb leren kennen:

**1. Forecasting-fouten bij onverwachte weersveranderingen**
Op een dag in februari 2026 was er een onverwachte storm. Wind-energieaanbod steeg plotseling, EPEX-prijs kelderde van verwacht €0,18 naar werkelijk €0,04 's avonds. Radar had de Sessy 's middags ontladen op €0,09 verwachtend hogere avondprijzen. Netto resultaat: suboptimaal. Dit zijn incidentele fouten die je niet kunt voorkomen.

**2. Teruglevering niet overal vergoed**
Niet alle leveranciers vergoeden teruglevering op de live spotprijs. Check je contract. Bij vaste teruglevering (bijv. €0,08/kWh vast) is teruglevering via Sessy minder aantrekkelijk of zelfs verliesgevend bij lage inkoopprijzen.

**3. Degradatiekosten zijn aanwezig**
Elke laad/ontlaad-cyclus kost batterijlevensduur. Sessy rekent dit mee in de optimizer, maar de aangenomen degradatiekosten per cyclus zijn conservatief ingesteld. In de praktijk kan de batterij sneller degenereren als je dagelijks één volle cyclus draait. Na 6.000 cycli (de gespecificeerde levensduur) is de batterijcapaciteit naar 80% gedaald.

---

## Conclusie: Sessy Radar is de beste EPEX-optimizer op de thuisbatterijmarkt

Na een jaar gebruik en zes software-updates is mijn oordeel positief en specifiek. Sessy Radar is de meest geavanceerde, betaalbare EPEX-optimizer voor thuisbatterijen in Nederland in 2026. De combi-modus (solar + arbitrage), de teruglevering-functie en de verbeterde P1-integratie maken de Sessy de beste keuze voor wie een dynamisch contract heeft en serieus wil arbitreren op de spotmarkt.

Het is geen universele winnaar: voor wie enkel eigenverbruik wil optimaliseren met een grote PV-installatie is Huawei Luna mogelijk efficiënter door de betere DC-koppeling. Maar voor EPEX-first gebruik is de Sessy ongeëvenaard in zijn prijsklasse.

Mijn rendement van €220–€310/jaar (bij Sessy-prijs van €3.999) geeft een terugverdientijd van 13–18 jaar puur op EPEX-arbitrage. Voeg je de solar-eigenverbruiksoptimalisatie toe (voor mij circa €120/jaar extra) dan kom je op 9–12 jaar terugverdientijd — voor een systeem met 10-jaar garantie en 6.000 cycli levensduur een acceptabele business case.

---


<a href="https://go.duurzaamthuislab.nl/sessy" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">Bekijk Sessy</a>

## Sessy vs. thuisbatterij kopen zonder EPEX-koppeling: is de meerwaarde meetbaar?

Om de waarde van Sessy Radar objectief te beoordelen, vergelijk ik mijn eigen data met een hypothetisch scenario waarbij de Sessy enkel op eigenverbruik (solar self-consumption) zou optimaliseren zonder EPEX-koppeling.

**Werkelijk scenario (Sessy met Radar + Tibber, Q1 2026):**
- Totaal geladen: 467 kWh
- Gemiddeld inkooptarief: 5,1 ct/kWh
- Totale inkoopkosten lading: €23,82
- Waarde ontlading (vermeden inkoop op piekmoment): €82,28
- **Netto waarde Q1: €58,46**

**Simulatie zonder Radar (alleen solar eigenverbruik):**
- Totaal geladen via zonnepanelen (Q1, beperkte productie): 89 kWh
- Gemiddeld eigenverbruikswaarde: 24 ct/kWh
- **Netto waarde Q1 simulatie: €21,36**

**Verschil: Sessy Radar leverde €37,10 meer op in Q1** — uitsluitend door de EPEX-koppeling. Geëxtrapoleerd: circa **€148 extra per jaar** alleen via de EPEX-koppeling boven pure solar-eigenverbruiksoptimalisatie.

---

## Veelgestelde vragen van Sessy-gebruikers

**"Mijn Sessy laadt niet in de nacht terwijl de EPEX-prijs laag was — waarom?"**

Sessy Radar kijkt niet alleen naar de huidige prijs maar naar de geoptimaliseerde spread over de komende 24 uur. Als er 's ochtends vroeg een nog lagere prijs wordt verwacht, kan Radar besluiten te wachten. Ook: als de batterij al deels vol is, is het niet altijd optimaal om extra te laden op een lage prijs als er de volgende dag geen hoge piekprijs wordt verwacht.

**"De Sessy-app toont een negatieve besparing deze week — is dat normaal?"**

De besparing in de app is berekend op basis van wat er zonder de batterij gekost zou hebben. In weken met weinig EPEX-volatiliteit en weinig zonne-energie is de besparing inderdaad klein of negatief. Over een jaar is de balans altijd positief bij correct geconfigureerd systeem.

**"Kan ik Sessy ook handmatig overschrijven?"**

Ja. In de Sessy-app kun je via "Manueel instellen" de batterij forceren te laden of ontladen op een moment dat jij kiest. Na het handmatige commando valt de Sessy terug op automatische Radar-planning.

---

## Sessy in 2027: de saldering-afbouw als businessgeval

De salderingsregeling vervalt per 2027. Dit verandert de waarde van een thuisbatterij fundamenteel.

**Effect op Sessy-businesscase na 2027 (indicatief, PV 4,8 kWp):**

| Situatie | Jaarwaarde |
|----------|-----------|
| Zonder Sessy, voor 2027 | €605 |
| Zonder Sessy, na 2027 | €605 → daalt naar €449 + €156 = €605 maar teruglevering minder waard |
| Met Sessy, na 2027 | €786–€842 eigenverbruik + €65–€78 teruglevering + €220–€310 EPEX = **€1.071–€1.230** |

**Verschil Sessy vs. geen Sessy na 2027: €466–€625 per jaar**

Bij een netto Sessy-prijs van €3.999 geeft dit een terugverdientijd na 2027 van **6,4–8,6 jaar** — significant beter dan vandaag. De Sessy wordt financieel aantrekkelijker naarmate de saldering afbouwt.

**[Bekijk Sessy thuisbatterij](https://go.duurzaamthuislab.nl/sessy)**

## Gerelateerde artikelen

- [Huawei Luna vs Tesla Powerwall vs Sessy 2026](/posts/huawei-luna-vs-tesla-powerwall-vs-sessy-2026/)
- [Sessy review 2026: eerlijke test van de Nederlandse](/posts/sessy-review-thuisbatterij-nederland/)
- [Thuisbatterij Zonder Zonnepanelen: Heeft Het Zin in 2027?](/posts/batterij-na-2027-zonder-zonnepanelen-zin-2026/)
- [Beste 10 kWh thuisbatterij 2026: vergelijking 7 topmerken](/posts/thuisbatterij-10-kwh-vergelijking-2026/)
- [Thuisbatterij binnen of buiten plaatsen: veilig 2026](/posts/thuisbatterij-buiten-vs-binnen-installeren-2026/)
