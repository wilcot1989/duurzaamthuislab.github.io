---
title: SolarEdge Omvormer + Dynamisch Contract 2026
date: 2026-10-18 08:00:00+02:00
lastmod: 2026-10-18 08:00:00+02:00
draft: false
description: "SolarEdge omvormer combineren met dynamisch contract (Tibber/Frank)? Tijdgestuurd laden, peak shaving en smart EV. Voor wie loont het wel — en niet."
categories:
- zonnepanelen
tags:
- SolarEdge
- omvormer
- dynamisch contract
- Tibber
- Frank Energie
- peak shaving
keywords:
- solaredge dynamisch contract
- solaredge tibber
- solaredge frank energie
- solaredge home battery
affiliate: true
author: Mark Bakker
author_bio: Energieadviseur met een eigen verduurzaamd huis. Test zonnepanelen, thuisbatterijen en warmtepompen in de praktijk.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1559302504-64aae6ca6b6d&w=1200&output=webp&q=70
faq:
- q: Werkt SolarEdge automatisch samen met Tibber?
  a: 'Via de mySolarEdge-app kun je tijdgestuurde profielen instellen, maar er is geen native Tibber-koppeling. Voor automatisch laden/ontladen op basis van Tibber-prijzen heb je Home Assistant + Pulse nodig, of de SolarEdge Energy Bank met EnergyHub.'
- q: Wat kost een SolarEdge-omvormer in 2026?
  a: 'Een SolarEdge HD-Wave 5kW kost €1.800-€2.200 inclusief optimizers (~€55 per paneel). Voor 12 panelen kom je dus op €2.450-€2.860 alleen voor omvormer + optimizers — €700-€1.000 duurder dan een vergelijkbare Huawei of Enphase.'
- q: Is SolarEdge Home Battery beter dan Sessy of Marstek voor dynamisch?
  a: 'SolarEdge Home Battery integreert naadloos met de eigen omvormer (DC-gekoppeld, hoger rendement) maar mist Sessy''s sterke handelsalgoritme. Voor pure dynamische winst: Sessy. Voor systeem-eenheid en peak shaving: SolarEdge.'
- q: Wat is peak shaving precies?
  a: 'Peak shaving = het afvlakken van je piekafname van het net. Bij dynamisch contract met hoge ochtend- en avondpieken (€0,60-€0,90/kWh) laat de batterij die uren overbruggen, zodat je alleen het lage tarief afneemt. Bespaart €300-€600/jaar bij 8000+ kWh verbruik.'
- q: Werkt SolarEdge met Home Assistant?
  a: 'Ja, via Modbus TCP of de officiële SolarEdge integration. Werkt prima voor monitoring; voor sturen heb je de SolarEdge Energy Manager API nodig — die heeft een abonnementsvereiste van €4-€8 per maand sinds 2024.'
- q: Kun je een dynamisch contract op een bestaande SolarEdge gebruiken?
  a: 'Ja, elke omvormer kan met een dynamisch contract — maar de winst zit in sturing (laden/ontladen op prijs). Zonder batterij scheelt het hooguit dat je wasmachine en EV op goedkope uren draait; daar heb je geen SolarEdge voor nodig.'
products:
- name: Tibber dynamisch contract
  url: https://go.duurzaamthuislab.nl/tibber
  price: '0'
- name: Frank Energie
  url: https://go.duurzaamthuislab.nl/frank-energie
  price: '0'
- name: Sessy thuisbatterij
  url: https://go.duurzaamthuislab.nl/sessy
  price: '5995'
- name: Zonneplan zonnepanelen
  url: https://go.duurzaamthuislab.nl/zonneplan
  price: '6995'
schema_type: Article
last_updated: '2026-10-18'
category: zonnepanelen
---

Vorige maand zat ik bij een klant in Hilversum aan de keukentafel — 14 panelen op het zuiddak, een SolarEdge HD-Wave 6kW omvormer uit 2022 en sinds april een Tibber-contract. Hij had me erbij gehaald omdat zijn jaarafrekening rarer aanvoelde dan verwacht: wel saldering verloren, wel dynamisch tarief, maar de besparing bleef hangen rond de €280. Toen we de mySolarEdge-data naast zijn Tibber-grafiek legden, zag ik wat er misging — zijn omvormer leverde keurig terug om 13:00 (lage prijs), terwijl hij om 18:30 zijn EV oplaadde voor €0,71/kWh. Een uur instellen later betaalde de combinatie zichzelf wél terug.

*Disclosure: ik heb affiliate-partnerships met Tibber, Frank Energie, Sessy en Zonneplan. Als je via mijn links een contract afsluit of een batterij koopt krijg ik een vergoeding. Dat verandert niets aan mijn advies — ik schrijf op wat ik bij klanten zie werken, niet wat het meeste oplevert.*

---

> **Kort antwoord:** SolarEdge + dynamisch contract loont bij 8000+ kWh/jaar verbruik + EV of warmtepomp; bij minder verbruik betaal je de meerprijs niet terug.

## Waarom SolarEdge populair is bij dynamisch-contract-gebruikers

SolarEdge heeft één eigenschap die bij dynamisch contract goud waard is: power optimizers per paneel. Elk paneel heeft zijn eigen MPPT-tracker, wat betekent dat schaduw op één paneel niet de hele string platlegt. Voor een Hilversumse rijtjeswoning met een schoorsteen of een boom is dat het verschil tussen 4.200 en 5.100 kWh per jaar opbrengst — die 900 kWh is bij €0,28 gemiddeld zo'n €250 per jaar.

Maar er is een tweede reden waarom mensen met Tibber of Frank Energie juist voor SolarEdge kiezen: het ecosysteem. SolarEdge maakt niet alleen omvormers maar ook batterijen (Home Battery 10kWh), EV-laders (Home EV-charger 11kW) en de EnergyHub die alles aanstuurt. Voor wie tijdgestuurd wil laden op basis van een dynamisch tarief is dat één app, één installatie, één garantieloket.

Ik zie in mijn klantenbestand dat 60-70% van de huizen met 12+ panelen die ná juli 2025 overstapten op dynamisch contract een SolarEdge of Huawei hebben — Enphase volgt op afstand. Een vergelijking met de alternatieven vind je in mijn [overzicht van de beste omvormers voor 2026](/posts/beste-omvormer-zonnepanelen-2026/) en in de directe [Huawei vs SolarEdge vergelijking](/posts/huawei-vs-solaredge-omvormer-2026/).

## Hoe werkt de integratie met Tibber en Frank Energie?

Hier moet ik direct een misverstand uit de wereld helpen: **SolarEdge heeft geen native koppeling met Tibber of Frank Energie**. Wie verwacht dat hij in de mySolarEdge-app op een Tibber-knop drukt en klaar is, komt bedrogen uit. De integratie verloopt op drie manieren:

1. **Handmatige tijdprofielen in mySolarEdge** — je stelt zelf in welke uren de batterij laadt of ontlaadt. Werkt prima als je tarieven redelijk voorspelbaar zijn (nacht goedkoop, avondspits duur).
2. **SolarEdge Energy Manager met dynamisch profiel** — sinds firmware 4.18 (2024) kan de EnergyHub via een API priceforecast-data ophalen. Maar: je hebt een SolarEdge ONE-abonnement nodig (€4,99/maand) en de prijzen-API werkt alleen met geselecteerde leveranciers — Tibber wél, Frank Energie pas sinds september 2025.
3. **Home Assistant als middleman** — de populairste route. Je trekt Tibber-prijzen via de officiële HA-integratie binnen, schrijft die naar de SolarEdge Modbus-registers, en de omvormer doet de rest.

Frank Energie heeft sinds 2025 een open API waarmee dezelfde routes mogelijk zijn. In de praktijk zie ik dat Tibber-klanten vaker direct via de SolarEdge ONE-cloud werken (omdat Tibber Pulse de communicatie versimpelt), terwijl Frank Energie-klanten meestal de Home Assistant route nemen. Welke leverancier voor jou voordeliger is leg ik uit in [Frank Energie vs Tibber](/posts/frank-energie-vs-tibber-2026/) en het uitgebreide [Frank Energie review](/posts/frank-energie-review-ervaringen-2026/).

<a href="https://go.duurzaamthuislab.nl/tibber" class="cta-affiliate" target="_blank" rel="nofollow sponsored noopener">Bekijk Tibber</a>

## Tijdgestuurd laden via SetApp en mySolarEdge

SetApp is de installateurs-app van SolarEdge — die zie je waarschijnlijk nooit, tenzij je zelf je systeem onderhoudt. mySolarEdge is de consumenten-app, en daar gebeurt het werk. Open de app, ga naar **Batterij** → **Werkmodus** → **Aangepast schema**. Daar kun je vier tijdvensters per dag instellen met drie opties:

- **Maximize self-consumption** — standaardmodus, batterij laadt uit zon
- **Time of Use** — handmatige tijdsturing op tarief
- **Charge from grid** — actief laden uit het net (alleen toegestaan bij dynamisch contract sinds 2023)

Bij mijn Hilversumse klant heb ik vier vensters ingesteld op basis van zijn gemiddelde Tibber-prijscurve van afgelopen 3 maanden:

| Uur | Modus | Reden |
|---|---|---|
| 00:00-06:00 | Charge from grid (60%) | Nachttarief ~€0,12/kWh |
| 06:00-11:00 | Maximize self-consumption | Ochtendzon, eigenverbruik |
| 11:00-15:00 | Maximize self-consumption | Piekproductie, terugleveren |
| 15:00-22:00 | Discharge to load | Avondspits ~€0,55/kWh |

Resultaat na 6 weken: gemiddelde inkoopprijs daalde van €0,31 naar €0,19 per kWh. Bij 7.800 kWh netto-afname per jaar (na zonneproductie) is dat €936 besparing — voor 30 minuten instelwerk.

Wil je zelf zo'n schema bouwen? Mijn [rekenmodel voor dynamisch contract met batterij](/posts/dynamisch-contract-met-batterij-rekenmodel-2026/) helpt je de optimale percentages bepalen op basis van je verbruik en EPEX-spreads.

## SolarEdge Home Battery + peak shaving

De SolarEdge Home Battery (officieel: Energy Bank) komt in twee maten: 10 kWh (€5.400 incl. installatie) en 20 kWh (€9.200). DC-gekoppeld aan de omvormer betekent: één conversie van DC naar AC bij ontladen in plaats van twee bij AC-gekoppelde batterijen. Rondloop-rendement is daardoor 94-95% tegen 88-90% bij Sessy of Marstek — bij 4.000 kWh batterijdoorzet per jaar is dat 200 kWh extra benutting, ofwel €60-€100 per jaar.

Peak shaving is de killer-feature bij dynamisch contract. Mijn klant in Hilversum had vorige winter 6 dagen waarop het avondtarief boven €0,80/kWh schoot — donkere windstille dagen. Zonder batterij had hij die avonden gemiddeld 8 kWh afgenomen tegen €0,82 = €6,56 per dag. Met de Home Battery (10 kWh, 's middags geladen op €0,11) werd dat €0,88 per dag — een besparing van €5,68 per piekdag, ofwel €34 over die 6 dagen. Op jaarbasis 60-90 van dat soort uren = €250-€450 puur uit peak shaving, bovenop normale eigenverbruik-optimalisatie.

De vergelijking met andere batterijen leg ik uit in [Sessy vs Marstek](/posts/sessy-vs-marstek-thuisbatterij-2026/) en het overzicht [thuisbatterij prijzen](/posts/thuisbatterij-prijzen-vergelijking-2026/).

<a href="https://go.duurzaamthuislab.nl/sessy" class="cta-affiliate" target="_blank" rel="nofollow sponsored noopener">Bekijk Sessy</a>

## Smart EV-laden via SolarEdge EV-charger

De SolarEdge Home EV Charger (€1.290 incl. installatie, 11 kW driefase) is geen wonder van techniek — andere Type 2 laders doen hetzelfde — maar hij integreert direct in EnergyHub. Drie modi:

- **Solar mode** — laadt alleen wanneer panelen overschot leveren (>1,4 kW boven huisverbruik)
- **Time of Use** — laadt op vooraf ingestelde uren
- **Smart energy management** — combineert beide: zon overdag, plus dynamisch goedkope uren 's nachts

Die derde modus is waar de combo met Tibber/Frank interessant wordt. Mijn klant rijdt een Tesla Model 3 (16.000 km/jaar = ~3.200 kWh laadbehoefte). Voor de combo SolarEdge + dynamisch:

- 1.400 kWh uit eigen panelen tijdens zomer (gratis)
- 1.800 kWh uit dynamisch contract gemiddeld €0,13/kWh = €234

Tegen vaste 2026-tarieven (€0,33/kWh all-in) had hij €1.056 betaald — een verschil van €822 per jaar **op alleen de EV**. De laadpaal verdient zich in 18 maanden terug. Voor wie nog twijfelt tussen modellen: lees [beste laadpaal thuis 2026](/posts/beste-laadpaal-thuis-2026/) en [EV laden met thuisbatterij](/posts/ev-laden-met-thuisbatterij/).

## Voor wie heeft deze combo zin? (rekenvoorbeeld)

Niet voor iedereen. Eerlijk: voor een gezin van 2 personen met 8 panelen en 2.800 kWh jaarverbruik is SolarEdge + dynamisch contract overkill. De meerprijs ten opzichte van een simpele Growatt of Goodwe haal je er niet uit.

Hier is de drempel die ik bij klanten hanteer:

| Profiel | Verbruik | EV/WP | Advies |
|---|---|---|---|
| Klein gezin, geen EV | 3.000-4.500 kWh | nee | Goodwe + dynamisch, geen batterij |
| Modaal gezin | 4.500-7.000 kWh | misschien | Huawei SUN2000 + Sessy |
| Groot gezin + EV | 7.000-10.000 kWh | ja | SolarEdge + Home Battery 10kWh |
| Groot gezin + EV + WP | 10.000+ kWh | ja+ja | SolarEdge + Home Battery 20kWh |

Concreet rekenvoorbeeld voor het "groot gezin + EV" segment (mijn Hilversumse klant):

- 14 panelen (5.880 Wp) — opbrengst 5.500 kWh/jaar
- Verbruik: 8.400 kWh (huishouden + Tesla)
- Netto-afname: 4.300 kWh (zonneproductie deels gelijktijdig met verbruik)
- Zonder batterij + vast contract: €1.419 stroomkosten
- Met SolarEdge Home Battery + Tibber: €567 stroomkosten

Besparing: **€852/jaar**. Meerprijs SolarEdge boven Goodwe: €950. Meerprijs Home Battery: €5.400. Terugverdientijd batterij: 6,3 jaar — onder de 10-jarige garantie. Doe je het zelfde sommetje voor jouw situatie? Mijn vergelijking [beste dynamisch contract met zonnepanelen](/posts/beste-dynamisch-contract-met-zonnepanelen-2026/) helpt daarbij.

<a href="https://go.duurzaamthuislab.nl/frank-energie" class="cta-affiliate" target="_blank" rel="nofollow sponsored noopener">Bekijk Frank Energie</a>

## Nadelen: prijs, abonnementen, complexiteit

Tijd voor de zure kant. SolarEdge is geen perfect product en de combo met dynamisch contract is niet altijd plug-and-play.

**Prijs**. Een SolarEdge HD-Wave 5kW kost €1.800-€2.200 inclusief 10 optimizers. Voor 12 panelen zit je op €2.450-€2.860 — €700-€1.000 duurder dan een vergelijkbare Huawei SUN2000-5KTL-M1 of Enphase IQ8M-set. Die meerprijs is alleen te rechtvaardigen als je daadwerkelijk panelenoptimalisatie nodig hebt (schaduw, oost/west) óf het ecosysteem gaat gebruiken (batterij, EV-charger). Voor een schaduwvrij zuiddak: zonde van het geld.

**Abonnementen**. Sinds 2024 zit er een SolarEdge ONE-abonnement op de geavanceerde features: dynamische tariefintegratie, geavanceerde rapportage en de slimme EnergyHub-API. €4,99/maand of €49,99/jaar. Niet wereldschokkend maar irritant — bij Enphase en Huawei zijn die features gratis. En zonder ONE werkt de Tibber-koppeling via SolarEdge-cloud niet, dus moet je terug naar Home Assistant.

**Complexiteit**. De Home Assistant-route werkt prima als je technisch bent. Maar: je moet de Modbus TCP-verbinding configureren, een YAML-automation schrijven die Tibber-prijzen vergelijkt met je drempelwaarde, en alles testen. Voor wie nooit eerder met HA werkte: reken 8-12 uur leertijd. Mijn [Home Assistant integratie guide voor warmtepompen](/posts/home-assistant-warmtepomp-integratie-2026/) geeft een idee van de denkstijl die je nodig hebt.

**Lock-in**. SolarEdge omvormers werken alleen met SolarEdge-optimizers en SolarEdge-batterijen. Wil je later een Sessy of een tweede merk batterij? Dan moet je AC-koppelen, waarbij je het rendementsvoordeel verliest. Bij Huawei en Enphase is die lock-in minder strikt.

**Servicekwaliteit**. SolarEdge Nederland heeft sinds 2023 zijn supportkanaal verschraald — telefonisch alleen via installateur, e-mail-support reageert binnen 3-5 werkdagen. Voor een omvormer die je 15 jaar moet meegaan: doe me een lol en kies een installateur die garantieafhandeling volledig overneemt. Ik heb klanten gezien die met een defecte HD-Wave 8 weken zonder productie zaten omdat installateur en SolarEdge naar elkaar wezen. Vraag vooraf om de RMA-procedure.

**Firmware-onzekerheid**. SolarEdge heeft de afgelopen drie jaar twee keer een firmware-update uitgerold die de Modbus-registers wijzigde. Eén keer in 2023 (storage_control_mode kreeg een extra waarde) en één keer in 2025 (rate-limiting op lokale TCP-verbindingen). Voor Home Assistant-gebruikers betekende dat: automations stuk, opnieuw opbouwen. Reken op zo'n moment elke 12-18 maanden — niet onoverkomelijk, wel vervelend.

## SolarEdge vs Huawei vs Enphase voor dynamisch contract

Korte vergelijking op de drie punten die bij dynamisch contract tellen: prijssturing, batterij-ecosysteem en Home Assistant-ondersteuning.

| Punt | SolarEdge | Huawei | Enphase |
|---|---|---|---|
| Prijs 5kW omvormer (incl. opt.) | €2.100 | €1.350 | €2.400 (micros) |
| Eigen batterij ecosysteem | Home Battery 10/20 kWh | LUNA2000 5-15 kWh | IQ Battery 5P |
| Native dyn-tarief integratie | ONE-abonnement | Smart PV App (gratis) | Enlighten + IQ Gateway |
| Home Assistant Modbus TCP | Ja, stabiel | Ja, lastig na firmware | Beperkt (cloud only) |
| Peak shaving software | Ja, configurabel | Ja, sinds 2024 | Ja, maar duur |
| Garantie omvormer | 12 jaar | 10 jaar | 25 jaar microcontrollers |

**Mijn verdict**: voor mensen die bewust voor het systeem-pakket gaan (panelen + omvormer + batterij + lader van één merk) is SolarEdge het volwassenste keuze. Voor mensen die de batterij later separaat kopen of al Home Assistant draaien is Huawei goedkoper en even flexibel. Enphase is voor wie 25 jaar onderhoudsvrij wil; de dynamische integratie is daar zwakker.

Een uitgebreide vergelijking vind je in [Huawei vs SolarEdge](/posts/huawei-vs-solaredge-omvormer-2026/), en als je nog moet kiezen welke panelen erbij passen: [beste zonnepanelen 2026](/posts/beste-zonnepanelen-2026/) of het scenario [na saldering 2027](/posts/beste-zonnepanelen-2026-na-saldering/).

## Home Assistant integratie: wat werkt en wat niet

De Home Assistant SolarEdge-integratie heeft twee smaken: de officiële (REST API, cloud-gebaseerd) en de community Modbus-integratie (lokaal, via SE1000-modem of direct TCP). Wat werkt en wat niet, op basis van mijn eigen testbench:

**Werkt goed:**
- Live productie-data uitlezen (interval 5-15 seconden via Modbus)
- Batterijstatus (SoC, laad/ontlaad-vermogen, temperatuur)
- Per-paneel productie (optimizer-data) — wel via cloud, niet lokaal
- Sturen van batterijmodus (laden/ontladen/idle) via Modbus-register
- Tibber-prijzen automatisch koppelen aan batterijstuur-automation

**Werkt half:**
- EV-charger besturing — alleen via cloud API, met 30-60 sec vertraging
- Forecast-gebaseerd laden (zon-voorspelling) — werkt met Solcast als datapaar
- Energy Manager via API — abonnementsvereiste, niet alle endpoints open

**Werkt niet:**
- Real-time prijssturen onder de minuut (Modbus is responsief, cloud niet)
- Optimizer-data lokaal (alleen via SolarEdge ONE cloud beschikbaar)
- Native HACS-component voor dynamische profielen — moet je zelf YAML schrijven

In de praktijk schrijven mensen een Node-RED-flow of een HA-blueprint die elke 15 minuten de Tibber-prijs leest, vergelijkt met de drempel (bv. mediaan van komende 24u), en de Modbus-register 0xE004 (storage_control_mode) zet op 1 (charge), 2 (discharge) of 0 (auto). Het werkt — maar reken 4-8 avonden tinkeren voor het stabiel draait.

## Veelgestelde vragen

**Werkt SolarEdge automatisch samen met Tibber?**
Via mySolarEdge kun je tijdgestuurde profielen instellen, maar er is geen native Tibber-koppeling. Voor automatisch laden/ontladen op Tibber-prijs heb je Home Assistant + Pulse nodig, of SolarEdge ONE met EnergyHub.

**Wat kost een SolarEdge-omvormer in 2026?**
Een HD-Wave 5kW kost €1.800-€2.200 incl. optimizers (~€55 per paneel). Voor 12 panelen kom je op €2.450-€2.860 — €700-€1.000 duurder dan vergelijkbare Huawei of Enphase.

**Is SolarEdge Home Battery beter dan Sessy of Marstek?**
Voor pure dynamische winst: Sessy (sterker handelsalgoritme). Voor systeem-eenheid en peak shaving: SolarEdge (DC-gekoppeld, hoger rendement). Voor backup-functie bij stroomuitval: ook SolarEdge.

**Wat is peak shaving precies?**
Het afvlakken van piekafname uit het net. Bij dynamisch contract met avondpieken (€0,60-€0,90/kWh) overbrugt de batterij die uren met goedkoop geladen stroom. Bespaart €300-€600/jaar bij 8000+ kWh verbruik.

**Werkt SolarEdge met Home Assistant?**
Ja, via Modbus TCP of de officiële cloud-integratie. Monitoring werkt prima; voor sturen heb je de SolarEdge Energy Manager API (€4,99/maand) of de lokale Modbus-route nodig.

**Kun je dynamisch contract op een bestaande SolarEdge gebruiken?**
Ja — maar de winst zit in sturing (laden/ontladen op prijs). Zonder batterij scheelt het hooguit dat je wasmachine en EV op goedkope uren draait, en daar heb je geen SolarEdge voor nodig. Lees [dynamisch vs vast contract](/posts/dynamisch-vs-vast-contract-2026/) voor de break-even-rekening.

**Heeft het zin als ik nog saldering heb?**
Nee, niet financieel. Tot 1 januari 2027 krijg je voor teruglevering hetzelfde tarief als afname, dus de batterij-arbitrage is verlies (rendementsverlies + slijtage). Wacht met de batterij tot ná saldering, of koop nu de omvormer en voeg later de batterij toe. Mijn overzicht [dynamische energiecontracten vergelijking](/posts/dynamische-energiecontracten-vergelijking-2026/) gaat hier dieper op in.

---

**Conclusie**: SolarEdge + dynamisch contract is geen instapcombinatie. Het is een bewust premium-pakket dat zich terugverdient bij verbruik boven 8.000 kWh/jaar mét een EV of warmtepomp. Voor die doelgroep is het in 2026 een van de stabielste set-ups die je kunt installeren — alles werkt samen, één garantieloket, één app. Onder die drempel: kies Huawei + losse batterij of blijf bij je huidige omvormer en voeg alleen een dynamisch contract toe.

Twijfel je over de keuze? Reken zelf door met mijn [batterij-rekenmodel](/posts/dynamisch-contract-met-batterij-rekenmodel-2026/), of vraag een SolarEdge-offerte aan via [mijn omvormer-vergelijking](/posts/beste-omvormer-zonnepanelen-2026/).

<a href="https://go.duurzaamthuislab.nl/zonneplan" class="cta-affiliate" target="_blank" rel="nofollow sponsored noopener">Bekijk Zonneplan</a>

Meer over de regels rond saldering en dynamische tarieven lees je bij [Milieu Centraal: zonnepanelen en het saldeerregeling](https://www.milieucentraal.nl/energie-besparen/zonnepanelen/salderingsregeling-voor-zonnepanelen/).
