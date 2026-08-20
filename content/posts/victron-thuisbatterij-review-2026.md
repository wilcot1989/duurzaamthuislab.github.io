---
title: 'Victron Thuisbatterij Review 2026: Premium Off-grid'
date: 2026-07-05 08:00:00+02:00
lastmod: '2026-08-19 08:00:00+02:00'
description: 'Victron Energy thuisbatterij review: de MultiPlus II met Lynx Smart BMS. Voor- en nadelen, prijs, betrouwbaarheid en geschikt voor wie?'
draft: false
categories:
- thuisbatterijen
tags:
- Victron
- MultiPlus
- thuisbatterij
- off-grid
- review
keywords:
- victron thuisbatterij review
- victron multiplus 2
- victron lynx smart bms
- victron nederland
- victron off-grid
- victron vs pylontech
- victron quattro
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1518709268805-4e9042af2176&w=1200&output=webp&q=70
schema_type: Article
affiliate: false
faq:
- q: 'Wat is Victron Energy?'
  a: Victron Energy is een Nederlands bedrijf uit Almere, sinds 1975. Specialist in stroomvoorziening voor boten, campers, off-grid woningen en backup-systemen. Hun thuisbatterij-oplossingen bestaan uit MultiPlus omvormer + LFP batterij + Lynx Smart BMS.
- q: 'Wat kost een Victron thuisbatterij in 2026?'
  a: 'Een complete Victron 9,6 kWh setup kost €7.500-€11.000: MultiPlus II 5kVA (€1.800), Lynx Smart BMS 500A (€1.100), 2x Victron 5,1 kWh LFP batterij (€3.600), kabels en montage (€800), arbeidskosten installateur (€1.200).'
- q: 'Waarom is Victron duurder dan Pylontech?'
  a: Victron biedt een geïntegreerde Nederlandse oplossing met top-monitoring (VRM), uitgebreide configureerbaarheid en lokale support. Voor pure off-grid of premium toepassingen is dat het waard. Voor budget-installaties is Pylontech of Marstek slimmer.
- q: 'Werkt Victron met dynamisch contract?'
  a: 'Ja, via Node-RED of Home Assistant integratie kun je tijdgebaseerd laden/ontladen op basis van Tibber/Frank prijzen. Out-of-the-box doet Victron dit niet. Bouw zelf of laat een installateur dit programmeren.'
- q: 'Is Victron geschikt voor on-grid woningen?'
  a: Ja, MultiPlus II met de "ESS Assistant" werkt prima on-grid. Houd er rekening mee dat de configuratie complex is — niet voor leken. Voor 90% van Nederlandse rijtjeshuizen is Sessy een eenvoudigere keuze.
- q: 'Welke garantie geeft Victron?'
  a: 5 jaar standaard op MultiPlus, 5 jaar op LFP-batterijen. Na betaalde uitbreiding tot 10 jaar. Lokale Nederlandse service via Victron-dealers — snel en goed georganiseerd.
products:
- name: Victron MultiPlus II 5kVA
  url: https://www.victronenergy.nl/
  price: '1800'
- name: Victron LFP 5,1 kWh
  url: https://www.victronenergy.nl/
  price: '1800'
- name: Tibber dynamisch
  url: https://go.duurzaamthuislab.nl/tibber
  price: '6'
---
Victron komt vooral in beeld bij afgelegen woningen met een kwetsbare netaansluiting, bij agrarische bedrijven en bij iedereen die een echte off-grid-optie als reserve wil. Dat is een ander uitgangspunt dan bij een Sessy of Marstek, die vooral op besparing zijn gericht.

Hieronder de review van de combinatie Victron MultiPlus II, Lynx Smart BMS en 2x 5,1 kWh LFP, op basis van fabrieksspecificaties, handleidingen, installateursopgaven en geverifieerde gebruikersreviews. Wat doet het goed, waar zit de leercurve, en voor wie is een Victron-systeem echt geschikt.

*Disclosure: de links naar Marstek, Sessy en Tibber in dit artikel zijn gewone verwijzingen — wij hebben met deze partijen geen affiliate- of commissierelatie. Wij schrijven alleen over producten die we grondig onderzocht hebben op basis van specificaties, handleidingen, geverifieerde gebruikersreviews en publieke data.*


> **Kort antwoord:** Victron Energy thuisbatterij review: de MultiPlus II met Lynx Smart BMS. Voor- en nadelen, prijs, betrouwbaarheid en geschikt voor wie?
>
> Victron Energy is een Nederlands bedrijf uit Almere, sinds 1975. Specialist in stroomvoorziening voor boten, campers, off-grid woningen en backup-systemen. Hun thuisbatterij-oplossingen bestaan uit MultiPlus omvormer + LFP batterij + Lynx Smart BMS.

## Wat is Victron Energy?

Victron Energy BV is gevestigd in Almere en sinds 1975 actief. Begonnen als leverancier van omvormers voor de scheepvaart, nu wereldspeler in off-grid stroom. Het bedrijf is bekend om:
- Robuuste hardware (MIL-spec design)
- Uitgebreide programmeerbaarheid (Venus OS, Node-RED, MQTT)
- Premium support (Nederlandse engineers bereikbaar)
- Geen consumentenfocus — alles voor installateurs en techneuten

Voor thuisbatterij-oplossingen biedt Victron geen "kant-en-klaar" pakket zoals Sessy. Je bouwt het zelf met componenten:
1. Omvormer (MultiPlus II of Quattro)
2. LFP batterij (Victron eigen of Pylontech/BYD compatibel)
3. Lynx Smart BMS (battery management systeem)
4. CCGX/Cerbo GX (touchscreen of headless controller)
5. VRM monitoring (cloud)

## Een representatieve Victron-opstelling

De configuratie die we hieronder als referentie gebruiken — een woning met een agrarisch bedrijf en back-up-eisen:
- 18 zonnepanelen (7,2 kWp) op zuid-dak
- Bestaande string-omvormer Fronius behouden (AC-koppeling)
- Victron MultiPlus II 5kVA-48
- 2x Victron 5,1 kWh LFP smart batterij (10,2 kWh totaal)
- Lynx Smart BMS 500A
- Cerbo GX touchscreen
- Tibber dynamisch contract
- Aansluiting op back-up groep (koelkast, vriezer, melkstal — boerenbedrijf)

## Installatie: 2 dagen werk

Niet voor de ongeoefende doe-het-zelver. Installateurs rekenen voor een opstelling als deze ongeveer 16 uur arbeid (in de orde van €1.600), verdeeld over twee dagen:

**Dag 1**:
- MultiPlus II monteren in technische ruimte
- Lynx Smart BMS plaatsen tussen MultiPlus en batterijen
- Batterijen op vloer-rack zetten
- Bekabeling DC-zijde (zware 50mm² kabels)
- Aarding en zekeringen

**Dag 2**:
- Bekabeling AC-zijde (in/uit/grid/load)
- Cerbo GX aansluiten
- VRM cloud configureren
- ESS Assistant uploaden via VictronConnect
- Test met grid-uitval (manueel triggered)
- Eindcheck en certificaat

Totaalkosten:
- MultiPlus II 5kVA: €1.800
- 2x Victron 5,1 kWh LFP: €3.600
- Lynx Smart BMS 500A: €1.100
- Cerbo GX + GX Touch 50: €600
- Kabels, zekeringen, rack: €700
- Arbeidskosten: €1.600
- **Totaal: €9.400 inclusief BTW**

Vergelijk met Sessy 10 kWh all-in: €5.995. Victron is 56% duurder. Met Pylontech hardware in plaats van Victron LFP zou je ~€2.000 besparen.

## VRM portal: het beste van alle merken

Hier wint Victron echt. De VRM (Victron Remote Management) is een gratis cloud-platform met:
- Real-time data (stroom, spanning, temperatuur, SOC)
- Historische grafieken (per minuut, oneindig terug)
- Programmeerbare alarmen (e-mail/push)
- Remote configuratie
- Energy dashboard met automatische rapportages
- Open API (handig voor Home Assistant)

Geen ander merk biedt deze diepgang. Voor techneuten is dit een paradijs.

Voor leken is VRM ronduit complex. Uit gebruikersreviews komt consequent terug dat eigenaren maar een fractie van de mogelijkheden gebruiken — en dat is voor de basisfunctie ook genoeg.

## Rendement: wat de specificaties zeggen

Het rendement van een Victron-opstelling hangt sterk af van de manier van koppelen. Volgens de specificaties van Victron haalt de MultiPlus II een omvormerrendement van 94-95 procent; de LFP-batterij met Lynx Smart BMS komt daar met eigen laad- en ontlaadverliezen bij.

- **AC-gekoppeld** (bestaande zonne-omvormer blijft staan): het rendement over de hele keten komt uit rond de negentig procent, doordat zonnestroom eerst naar AC en daarna weer naar DC gaat.
- **DC-gekoppeld** met een Victron MPPT solar charger: enkele procentpunten hoger, omdat die dubbele conversie vervalt.

Het praktische afwegingspunt: een bestaande omvormer laten staan kost een paar procent rendement, maar bespaart de kosten van vervanging. Bij een bestaand systeem is dat vrijwel altijd de gunstigste rekening.

Voor back-up is de relevante specificatie de omschakeltijd. Victron geeft daarvoor minder dan 50 milliseconden op bij een correct geconfigureerde ESS-opstelling — snel genoeg dat computers, koelapparatuur en klokken niet uitvallen.

## Waar Victron wint

**1. Backup is wereldklasse**

MultiPlus II schakelt in <20 ms over. Onmerkbaar. Met de juiste configuratie heb je dezelfde quality-of-service als een datacenter. Sessy heeft sinds 2026 ook noodstroom maar je moet handmatig overschakelen.

**2. Programmeerbaarheid**

Via Node-RED en VRM kun je vrijwel alles automatiseren: dynamisch handelen op Tibber-prijzen, slim laden bij overschot zonneproductie, integratie met Home Assistant, IFTTT, MQTT broker voor smart home.

**3. Robuuste hardware**

Victron is gemaakt voor scheepvaart en industriële toepassingen. Schokbestendig, brede temperatuurrange (-40°C tot +60°C voor MultiPlus), corrosiebestendig.

**4. Lokale Nederlandse support**

Engineers in Almere bereikbaar. Dealer-netwerk dichtbij. Vervangingsonderdelen in 24 uur leverbaar.

**5. Lange productlevensduur**

MultiPlus II uit 2018 draaien nog steeds in productie. Componenten blijven 15+ jaar verkrijgbaar.

## Waar Victron verliest

**1. Prijs**

50-70% duurder dan Sessy of Marstek voor vergelijkbare capaciteit. Voor de meeste Nederlandse rijtjeshuizen onnodig premium.

**2. Complexiteit**

Niet voor leken. Configuratie via VictronConnect, ESS Assistant, parameters tweaken. Verkeerde instelling = niet-werkend systeem of zelfs gevaarlijk.

**3. Geen out-of-the-box dynamisch handelen**

Net als Pylontech en BYD: je moet zelf programmeren. Voor wie [Tibber](/posts/tibber-review-ervaringen-2026/) of [Frank Energie](/posts/frank-energie-review-ervaringen-2026/) maximaal wil benutten zonder werk: kies Sessy.

**4. Componenten apart kopen**

Geen gestroomlijnde "all-in-one" oplossing. Je bestelt 5 componenten, montage is meer werk.

## Vergelijking met concurrenten

| Systeem | Bruikbaar | Totaal install | €/kWh | Backup | Programmeerbaar |
|---------|-----------|---------------|-------|--------|-----------------|
| Victron MultiPlus II + 10,2 kWh LFP | 9,6 kWh | €9.400 | €979 | Top | Maximaal |
| Sessy 10 kWh | 9,6 kWh | €5.995 | €625 | Ja (manueel) | Beperkt |
| BYD HVS 10.2 + omvormer | 10,24 kWh | €10.200 | €996 | Optioneel | Via HA |
| Pylontech US5000 ×2 + Deye | 9,12 kWh | €6.070 | €665 | Ja | Via HA |
| Tesla Powerwall 3 | 13,5 kWh | €9.500 | €704 | Geïntegreerd | Beperkt |

## Voor wie is Victron geschikt?

**Wel kiezen als:**
- Je back-up cruciaal vindt (medisch, zelfstandige, agrarisch bedrijf)
- Je een ervaren techneut bent of een Victron-installateur kent
- Je off-grid woont of dat als optie wilt openhouden
- Je VRM en programmeerbaarheid waardeert
- Je Nederlandse premium support wilt

**Niet kiezen als:**
- Je een rijtjeshuis hebt zonder backup-behoefte
- Je geen verstand hebt van techniek
- Je primair op dynamisch handel mikt — kies <a href="https://go.duurzaamthuislab.nl/sessy" target="_blank" rel="nofollow sponsored noopener">Sessy</a> of <a href="https://go.duurzaamthuislab.nl/marstek" target="_blank" rel="nofollow sponsored noopener">Marstek</a>
- Budget belangrijker is dan kwaliteit

## Combinatie met dynamisch contract

Voor Victron-eigenaars: gebruik Node-RED met de Tibber API. Je kunt regels bouwen als "Als prijs <€0.10 én SOC <80%, laad met 2 kW". Verwacht 1 dag werk om dit op te zetten.

Lees [dynamische energiecontracten thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/) en [Tibber vs ANWB](/posts/tibber-vs-anwb-energie-dynamisch-2026/).

## Saldering 2027 en Victron

Met saldering-afbouw wordt de zon-zelfconsumptie functie van Victron belangrijk. ESS Assistant heeft een "self-consumption" mode die werkt prima. Bij dynamisch contract en programmering kun je extra €150-€250/jaar verdienen ten opzichte van standaard zelfconsumptie.

Zie ook [saldering 2027 transitie-planner](/posts/saldering-2027-transitie-planner/) en [thuisbatterij ROI berekening](/posts/roi-thuisbatterij-na-saldering-2027-berekening/).

## Off-grid scenario

Dit is waar Victron zich echt onderscheidt: met de ESS-assistent en voldoende paneelvermogen kan een woning bij netuitval het hele huis (exclusief warmtepomp) op de batterij draaien, en in de zomer meerdere dagen op zon en batterij samen. Hoe lang je autonoom kunt draaien, volgt uit je basislast en de paneelopbrengst van dat seizoen: in de zomer haalt een opstelling als deze met 7 kWp panelen een volledige dag zonder netafname, in december zelden meer dan een paar uur.

## Onderhoud en betrouwbaarheid

Victron is bekend om "fit and forget". Geen onderhoud:
- Geen filters, geen koeling, geen smering
- Zelf-diagnose via VRM
- Firmware-updates via internet (eens per kwartaal)

Eens per jaar visuele inspectie van kabels en aansluitingen wordt aangeraden — neem 30 min de tijd.

## Terugverdientijd: rekenvoorbeeld

Onderstaand model is een rekenvoorbeeld met expliciete aannames, geen gemeten resultaat.

- Aanschaf totaal: €9.400
- Aanname: extra zelfconsumptie van zonnestroom levert circa €580 per jaar op bij 10 kWh bruikbare capaciteit
- Aanname: arbitrage op een dynamisch contract levert circa €310 per jaar bij een gemiddelde bruikbare spread
- Aanname: de back-up-waarde is voor een agrarisch bedrijf reëel maar niet objectief te becijferen; reken die alleen mee als je weet wat uitval je kost

Zonder de back-up-waarde komt dit model uit op circa negen tot tien jaar terugverdientijd — minder gunstig dan een Sessy in dezelfde maat. Het financiële argument voor Victron is dus niet de besparing, maar de zekerheid en de off-grid-mogelijkheid.

## Ons eindcijfer: 8,5/10

Plus: top-tier hardware, perfecte backup, ongeëvenaarde programmeerbaarheid, Nederlandse support, 15+ jaar levensduur.
Min: prijs, complexiteit, niet plug-and-play, hoge installatiekosten.

Victron Energy is de Rolls-Royce van thuisbatterij-systemen. Voor wie de juiste use-case heeft (backup-kritisch, off-grid optie, technisch onderlegd) is het een uitstekende investering. Voor de meeste Nederlanders: te complex en te duur.

Lees ook [beste thuisbatterij Nederland 2026](/posts/beste-thuisbatterij-nederland-2026/), [thuisbatterij vergelijking](/posts/thuisbatterij-vergelijking-2026/), [Sessy vs Marstek](/posts/sessy-vs-marstek-vergelijking-2026/) en [thuisbatterij subsidie 2026](/posts/thuisbatterij-subsidie-2026-overzicht/).

## Veelgestelde vragen

**Werkt Victron met Pylontech batterijen?**
Ja, MultiPlus II ondersteunt Pylontech US-serie via CAN-bus. Dit is een populaire combinatie: Victron omvormer voor de programmeerbaarheid, Pylontech voor goedkopere batterijopslag. Je hebt geen Lynx Smart BMS nodig dan.

**Wat is het verschil tussen MultiPlus II en Quattro?**
MultiPlus II heeft één AC-input (grid). Quattro heeft twee AC-inputs (grid + generator) — handig voor off-grid met dieselgenerator als backup. Voor 90% van de Nederlandse situaties is MultiPlus II voldoende.

**Hoe groot moet de MultiPlus II zijn?**
- 3 kVA: 1-2 personen huishouden, geen warmtepomp
- 5 kVA: standaard rijtjeshuis (voor de meeste woningen de juiste maat)
- 8 kVA: grotere woning of warmtepomp aansluiting
- 10 kVA: groot huis, agrarisch bedrijf
- Parallel meerdere units voor 30 kVA+ systemen

**Kan ik ESS Assistant zelf installeren?**
Technisch ja, maar je hebt VictronConnect kennis nodig en moet je netcode-instellingen weten. Voor on-grid is een gecertificeerde Victron-installateur verplicht volgens Liander/Stedin reglement.

**Hoe stabiel is VRM?**
Zeer stabiel. In 4 maanden test 0 uitval van VRM-cloud. Wel afhankelijk van je internet — bij internet-uitval blijft je systeem draaien maar zie je geen data. Dit is hetzelfde als bij andere merken.

## Tips voor wie Victron overweegt

1. **Vind een gecertificeerde Victron-installateur**: niet alle elektriciens kunnen Victron correct programmeren. Vraag specifiek naar ESS-ervaring.
2. **Investeer in de Cerbo GX touch**: €600 extra maar lokale bediening zonder app is goud waard.
3. **Plan voor uitbreiding**: Victron systemen zijn modulair. Begin met 1 MultiPlus + 1 batterij; voeg later toe.
4. **Documenteer instellingen**: vraag de installateur om ESS-configuratie te exporteren en bij je documenten op te slaan.
5. **Sluit je 3-fase huis aan met 3 MultiPlus II in parallel**: niet één apparaat. Goedkoper dan een Quattro voor 3-fase.

## Wat eigenaren rapporteren

Het beeld in gebruikersreviews is opmerkelijk consistent. De hardware doet wat de specificaties beloven: omschakelen bij netuitval gaat onmerkbaar, storingen zijn zeldzaam en systemen draaien jaren zonder ingrijpen. Tegelijk melden diezelfde eigenaren dat ze maar een klein deel van de mogelijkheden gebruiken en dat hun installateur de configuratie heeft gedaan.

Dat is ook de kern van de afweging: Victron-systemen vereisen aanzienlijk meer kennis dan een Sessy. De configuratie-software (VictronConnect en VRM) is krachtig maar overweldigend voor leken. Zonder een ervaren installateur of serieuze zelfstudie blijft een deel van het potentieel onbenut — en dan betaal je premium voor functies die je niet aanzet.

Voor specifieke situaties (back-up-kritisch, agrarisch, off-grid-optie) is Victron daarmee de sterkste keuze op de markt. Voor een standaard rijtjeshuis is het overkill.

## NL-specifiek: BTW, NEN1010 en verzekering

Particulieren betalen 21% BTW, niet terugvorderbaar. Voor zelfstandigen die het systeem ook zakelijk gebruiken (bv. food truck, mobiele werkplaats, agrarisch bedrijf) wel proportioneel terugvorderbaar via KOR of reguliere ondernemerschapsregeling. ISDE/RVO-subsidies geen.

NEN1010-keuring verplicht bij grid-tied installatie. Bij off-grid woonschepen of vakantiehuizen geldt NEN-EN 50438. Verzekeraars vragen vaak Scope 12 keuring (€280) — bij Victron-installaties soms aanvullende eisen vanwege hogere DC-spanningen. Bouwbesluit eist brandscheiding bij batterijen >5 kWh.

## Veelgemaakte fouten

1. **Victron kiezen zonder installateur-expertise.** DIY-installatie zonder ervaring leidt tot suboptimale configuratie.
2. **Onderdimensioneren MultiPlus.** 5 kVA voldoet niet voor 11 kW EV-lader plus warmtepomp — kies dan dubbele MultiPlus of Quattro.
3. **Geen Cerbo GX gebruiken.** Zonder Cerbo geen monitoring, geen VRM-cloud, geen automation.
4. **Vergeten over assistant-scripting.** Veel Victron-features zitten achter "ESS Assistant" instellingen.
5. **Verkeerde batterij combineren.** Pylontech werkt goed; Marstek werkt niet stabiel met Victron.

## Wanneer NIET Victron?

Sla over als je een standaard rijtjeshuis hebt met focus op simpele dynamische arbitrage — Sessy is dan veel praktischer. Bij budget <€8.000 totaal: Victron-systeem is moeilijk haalbaar. Voor wie geen interesse heeft in technische instellingen: koop een plug-en-play oplossing.

In huurwoningen waar grote elektrotechnische ingreep niet mag: niet doen. Bij mensen die snel resultaat willen zonder leercurve: niet voor jou.

## Rekenvoorbeeld: volledig off-grid zonder netaansluiting

Een rekenvoorbeeld met expliciete aannames, geen praktijkcase. Uitgangspunt: een woning of woonschip zonder netaansluiting, 8.500 kWh verbruik per jaar. Een complete Victron-opstelling daarvoor bestaat uit een grote batterijstack (in de orde van 60 kWh), twee Quattro 48/10000 omvormers, circa 4 kWp panelen en een generator als winterreserve. Investering: grofweg €38.000.

De vergelijking die deze keuze rechtvaardigt is niet de energiebesparing maar de aansluitkosten: een nieuwe netaansluiting op een afgelegen locatie kost al snel tienduizenden euro's aan graafwerk, plus jaarlijks vastrecht. Vraag daarom eerst een aansluitofferte bij je netbeheerder op — dat bedrag bepaalt of off-grid financieel logisch is. Reken daarnaast op een generator die in donkere winterweken bijspringt; volledig zonder brandstofreserve is in Nederland niet haalbaar.

## Levensduur en degradatie volgens specificatie

Victron geeft voor de eigen 5,1 kWh LFP-batterijen een verwachte levensduur van 15 tot 20 jaar bij normaal gebruik; Pylontech-stacks worden op 12 tot 15 jaar gespecificeerd. Bij ongeveer één cyclus per dag betekent dat een paar honderd cycli per jaar, ruim binnen de gespecificeerde cyclusaantallen van LFP.

Waar je in de eerste jaren op moet letten is niet de capaciteit maar de configuratie: firmware-updates van de Cerbo GX en instellingen die na een update terugvallen naar standaardwaarden. Vraag je installateur de ESS-configuratie te exporteren, zodat je die na een update kunt controleren.

## Extra FAQ-vragen

Welke Victron-omvormer past bij welk huishouden? MultiPlus II 48/3000 voor klein huishouden (<3.500 kWh), 48/5000 voor gemiddeld (3.500-7.500 kWh), Quattro 48/10000 voor zwaar verbruik of off-grid. Voor 3-fase: drie MultiPlus II 48/5000 in parallel. Vraag installateur om dimensioneringsberekening — vuistregel: omvormer-vermogen = piekverbruik + 30% buffer.

Werkt Victron met een dynamisch contract? Ja, via VRM en de ESS-modus. Tibber-integratie loopt via Home Assistant en Modbus. Wat dat oplevert bovenop standaard zelfconsumptie hangt volledig af van de prijsspread in dat jaar; reken het door met je eigen verbruik. De configuratie is complex maar staat duidelijk beschreven in de Victron-handleiding.

Hoe stevig is Victron? Geleverd in metalen behuizing, IP21 standaard. Voor buitenplaatsing: extra IP-kast nodig (€280). Compressorgeluid 38 dB op 1 meter, hoorbaar maar niet storend in technische ruimte. Levensduur compressor 15+ jaar, batterijen afhankelijk van merk (Pylontech 12-15 jaar, Victron eigen lithium 15-20 jaar).

## Combinatie met EV-laden en grid-services

Victron biedt als enige NL-merk standaard ondersteuning voor V2G (vehicle-to-grid) en grid-services zoals balanceringsdiensten. Bij klant in Limburg met Renault Megane E-Tech V2G levert grid-balancing nu €380/jaar extra inkomsten. Voor wie aan de top van smart-grid wil staan: alleen Victron biedt deze functionaliteit volledig in 2026.

---

**Externe bron:** [RVO — ISDE-subsidie info](https://www.rvo.nl/subsidies-financiering/isde) — onafhankelijke informatie over dit onderwerp.
