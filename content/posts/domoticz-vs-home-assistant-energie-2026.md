---
title: 'Domoticz vs Home Assistant: welke is beter voor energie 2026?'
date: '2026-08-03 08:00:00+02:00'
lastmod: '2026-08-21 08:00:00+02:00'
draft: false
description: Domoticz of Home Assistant voor energiebeheer? Wij vergelijken installatie, hardware-eisen, P1/DSMR- en Modbus-koppelingen, dynamische tarieven, het energiedashboard en het onderhoud.
categories:
- smart-home
tags:
- smart-home
- verduurzamen
- duurzaam wonen
- domoticz
keywords:
- domoticz vs home assistant
- beste smart home platform energie
- ha vs domoticz
- domoticz p1 meter
- home assistant energy dashboard
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: 'Wat is het grootste verschil tussen Domoticz en Home Assistant?'
  a: 'Domoticz is een compacte C++-applicatie die je als één programma installeert en die met weinig rekenkracht toe kan. Home Assistant is een Python-platform met een eigen add-on-ecosysteem, een veel langere integratielijst en een ingebouwd energiedashboard, maar het vraagt structureel meer rekenkracht en schijf-I/O.'
- q: 'Kan Domoticz een P1-meter uitlezen?'
  a: 'Ja. Domoticz heeft een ingebouwd hardware-type voor de P1 slimme meter, zowel via een USB-kabel op de meter als via een netwerk-leesbril. Home Assistant doet hetzelfde via de DSMR-integratie of via de lokale API van een netwerk-P1-module. Op dit punt is er inhoudelijk geen verschil.'
- q: 'Welk platform is beter voor een dynamisch energiecontract?'
  a: 'Home Assistant, omdat het energiedashboard uur- en dagprijzen naast je verbruik kan zetten en er kant-en-klare integraties voor dagvooruitprijzen bestaan. In Domoticz kan het ook, maar je bouwt de prijsopvraag en de kostenberekening zelf met een script of een dummy-sensor.'
- q: 'Kan ik een omvormer of thuisbatterij via Modbus sturen?'
  a: 'In beide platforms wel. Home Assistant heeft een generieke Modbus-integratie waarin je registers in de configuratie vastlegt; Domoticz heeft geen kern-Modbus-ondersteuning en werkt met een plug-in of een tussenlaag die de registers naar MQTT publiceert. Controleer altijd eerst in de handleiding van het apparaat welke registers de fabrikant vrijgeeft.'
- q: 'Welke hardware heb ik minimaal nodig?'
  a: 'Voor Domoticz is een Raspberry Pi 3 met een paar tientallen apparaten in de praktijk nog werkbaar. Voor Home Assistant is een Raspberry Pi 4 of 5 met SSD of een kleine x86-mini-pc de praktische ondergrens; op een SD-kaart met veel historie loopt de database vast of raakt de kaart versleten.'
- q: 'Kan ik van Domoticz naar Home Assistant overstappen zonder alles opnieuw te doen?'
  a: 'Niet automatisch. Er is geen importroute die apparaten, automatiseringen en historie meeneemt. Je koppelt de apparaten opnieuw, herschrijft de automatiseringen en bouwt het dashboard opnieuw op. Laat de oude installatie draaien tot de nieuwe stabiel is.'
schema_type: Article
---
*Dit artikel bevat geen affiliate- of commissielinks. Wij vergelijken op basis van de officiële documentatie van beide projecten en van wat gebruikers in publieke forums rapporteren; wij ontvangen van geen van beide projecten een vergoeding.*

Domoticz en Home Assistant zijn beide gratis, open source en draaien op hardware die je in een meterkast kunt hangen. Toch pakken ze energiebeheer fundamenteel anders aan. Hieronder de vergelijking op de punten die voor stroom, gas, zon en batterij daadwerkelijk verschil maken: installatie, hardware-eisen, P1- en Modbus-koppelingen, dynamische tarieven, het energiedashboard en het onderhoud op langere termijn.

> **Kort antwoord:** wil je één plek waar verbruik, opbrengst, gas en uurprijzen naast elkaar staan en waar je op prijs kunt sturen, dan is Home Assistant het sterkere platform — het energiedashboard en de integratielijst zijn daarvoor gebouwd. Wil je vooral betrouwbaar en zuinig een P1-meter, een paar schakelaars en wat sensoren loggen op bestaande hardware, dan doet Domoticz dat met een fractie van de rekenkracht en het onderhoud.

## 1. Twee verschillende ontwerpkeuzes

Domoticz is één programma, geschreven in C++, met een SQLite-database en een webinterface. Je installeert het, kiest onder *Setup → Hardware* een apparaattype en klaar. Alles wat het platform kan, zit in die ene binary; uitbreiden gebeurt met Python-plug-ins of met scripts (Lua, dzVents, bash) die op events reageren.

Home Assistant is een Python-platform waarin elke koppeling een aparte integratie is. Daarnaast draait er in de gangbare installatievorm (Home Assistant OS) een supervisor met add-ons: Mosquitto, InfluxDB, Node-RED, ESPHome. Het aantal officiële integraties is een orde van grootte groter dan wat Domoticz aan hardwaretypes kent — het exacte aantal verschuift per release, dus kijk op de integratiepagina van home-assistant.io in plaats van op een getal in een artikel.

Dat verschil in architectuur verklaart bijna alles wat volgt. Domoticz is klein en stabiel omdat het weinig doet. Home Assistant kan veel meer omdat er veel meer in beweging is — en dat betekent ook meer updates, meer breaking changes en meer hardware.

## 2. Installatie en hardware-eisen

| | Domoticz | Home Assistant |
|---|---|---|
| Gangbare installatievorm | pakket of Docker-container op een bestaande Linux-machine | Home Assistant OS op eigen hardware, of container op Linux |
| Database | SQLite, één bestand | SQLite (standaard) of externe database, plus recorder-instellingen |
| Praktische ondergrens hardware | Raspberry Pi 3, SD-kaart nog werkbaar | Raspberry Pi 4 of 5 met SSD, of x86-mini-pc |
| Configuratie | volledig via de webinterface | webinterface, met YAML voor de zwaardere onderdelen |
| Add-on-ecosysteem | geen; plug-ins en scripts | supervisor met add-ons (MQTT-broker, database, Node-RED) |

De hardware-eis is de belangrijkste praktische scheidslijn. Home Assistant houdt standaard alle sensorwaarden in een recorder-database bij, en energiesensoren die elke paar seconden een nieuwe waarde leveren laten die database snel groeien. Op een SD-kaart is dat een dubbel probleem: traag én slijtage. Domoticz schrijft veel minder weg en overleeft daarom jaren op precies dezelfde hardware.

Stroomverbruik als modelberekening, met de all-in prijs van €0,26/kWh die wij op deze site als rekenconstante gebruiken: een Raspberry Pi met SSD in de orde van 4 W kost ongeveer 35 kWh en dus circa €9 per jaar; een kleine mini-pc in de orde van 12 W komt op ruim 100 kWh en circa €27 per jaar. Het zijn schattingen op basis van typische verbruikswaarden, geen metingen — maar de conclusie houdt: het verschil in energierekening is klein ten opzichte van wat sturing kan opleveren.

## 3. De P1-meter uitlezen

Dit is voor energiebeheer de belangrijkste koppeling, en hier zijn de platforms verrassend gelijkwaardig.

**Domoticz** heeft *P1 Smart Meter* als ingebouwd hardwaretype, in twee varianten: seriële USB-kabel rechtstreeks op de P1-poort van de meter, of een netwerkverbinding naar een leesbril die de DSMR-telegrammen over TCP doorstuurt. Je krijgt automatisch tellers voor levering, teruglevering, actueel vermogen en gas.

**Home Assistant** heeft de DSMR-integratie voor exact dezelfde twee routes, plus aparte integraties voor netwerk-P1-modules die een eigen lokale API aanbieden. Die laatste route is de eenvoudigste: je vult een IP-adres in en de sensoren verschijnen.

Twee aandachtspunten die voor beide gelden:

- De P1-poort levert één telegram per seconde in de nieuwere DSMR-versies, en in oudere meters per tien seconden. Dat bepaalt hoe fijnmazig je kunt sturen — niet je software.
- Een meter kan maar één P1-verbinding tegelijk aan. Wil je zowel je platform als een aparte energiemonitor of de app van je leverancier voeden, dan heb je een splitter of een leesbril nodig die het telegram doorgeeft aan meerdere afnemers.

Meer over de hardwarekant: [de vergelijking van P1-energiemonitors](/posts/beste-energiemonitor-p1-meter-2026/).

## 4. Omvormer, warmtepomp en batterij: Modbus en MQTT

Wie niet alleen wil meten maar ook sturen, komt vroeg of laat bij Modbus TCP uit. Vrijwel elke hybride omvormer, thuisbatterij en lucht-waterwarmtepomp heeft een Modbus-interface; welke registers de fabrikant vrijgeeft, staat in de installatie- of Modbus-handleiding van dat specifieke model. Zoek dat document op vóór je hardware koopt — het bepaalt wat je überhaupt kunt uitlezen en schrijven.

**Home Assistant** heeft een generieke Modbus-integratie. Je definieert in YAML per register een sensor of een schakelaar, met adres, datatype en schaalfactor. Voor de bekendste merken bestaan daarnaast kant-en-klare integraties of HACS-projecten die de registerkaart al hebben ingevuld.

**Domoticz** heeft geen Modbus in de kern. De gangbare route is een tussenlaag die Modbus naar MQTT vertaalt en de waarden als dummy-devices in Domoticz zet. Dat werkt, maar het is een extra component die je zelf moet onderhouden.

Voor MQTT zijn beide platforms goed uitgerust: Domoticz heeft MQTT-client- en MQTT-autodiscovery-hardwaretypes, Home Assistant heeft de MQTT-integratie met discovery. Zelfbouwsensoren op ESP-basis werken in beide even goed.

Praktisch advies: geef bij nieuwe hardware voorrang aan apparaten met een gedocumenteerde lokale interface (Modbus TCP of een lokale HTTP-API) boven apparaten die alleen via de cloud van de fabrikant te bereiken zijn. Een cloud-API kan worden uitgezet of achter een abonnement worden gezet; een Modbus-register blijft doen wat het doet. Zie ook [de Modbus-route voor warmtepompen](/posts/home-assistant-warmtepomp-integratie-2026/).

## 5. Dynamische tarieven en sturen op prijs

Hier loopt Home Assistant duidelijk voor.

Het **energiedashboard** van Home Assistant is expliciet gebouwd voor deze use case. Je wijst per categorie een sensor aan — netlevering, teruglevering, zonneproductie, gas, batterij, individuele apparaten — en je kunt aan de levering- en teruglevercategorie een prijsentiteit koppelen. Vul daar een dagvooruitprijs in en het dashboard rekent per uur je werkelijke kosten en opbrengsten uit. Voor de dagvooruitprijzen zijn er integraties die de uurprijzen van de day-ahead-markt ophalen; sommige leveranciers hebben daarnaast een eigen integratie voor klanten.

Op die prijsentiteit bouw je vervolgens automatiseringen: laad de batterij in de goedkoopste uren van het aankomende venster, zet de boiler aan als de prijs onder het daggemiddelde minus een marge zakt, stel het laden van de auto uit tot na de avondpiek. Omdat de prijzen als attribuut met een volledig uurlijstje beschikbaar zijn, kun je vooruit plannen in plaats van alleen reageren op de huidige prijs — dat is het verschil tussen een goede en een matige besparing.

In **Domoticz** kan hetzelfde, maar je bouwt de onderdelen zelf: een script dat de uurprijzen ophaalt en in een dummy-sensor of een tekstvariabele zet, en een dzVents- of Lua-script dat daarop schakelt. Voor wie graag scripts schrijft is dat prima; voor wie een dashboard wil dat kosten en opbrengsten netjes optelt, is het veel handwerk.

Let bij het inrichten op één ding dat vaak fout gaat: de beursprijs is niet je tarief. Bij je leverancier komen energiebelasting, btw en een inkoopvergoeding bovenop de inkoopprijs, en aan de terugleverzijde krijg je die belastingcomponent niet terug. Reken in je automatiseringen met je eigen all-in tarief, niet met de kale uurprijs — anders lijkt verschuiven aantrekkelijker dan het is. Zie [het rekenmodel voor een batterij op een dynamisch contract](/posts/dynamisch-contract-met-batterij-rekenmodel-2026/).

## 6. Dashboards en historie

Domoticz levert per apparaat standaardgrafieken op dag-, maand- en jaarniveau. Ze zijn functioneel en je hoeft er niets voor te doen, maar samenstellen wat jij wil zien is beperkt.

Home Assistant heeft naast het energiedashboard een vrij indeelbaar dashboard met kaarten; voor fijnmazige grafieken gebruiken veel mensen een grafiekkaart uit de community-store. Dat is krachtiger, maar het is ook de plek waar de meeste tijd in gaat zitten en waar een update van een community-component je dashboard kan breken.

Voor langetermijnhistorie geldt in beide gevallen: zet een backup in. Home Assistant houdt naast de recorder-database langetermijnstatistieken per uur bij, waardoor het energiedashboard jaren terug kan kijken zonder dat de database onbeheersbaar groeit. Domoticz comprimeert historie zelf naar dag- en maandwaarden. Verlies van de database betekent in beide systemen verlies van je historie — en dat is precies het gegeven waarmee je over vijf jaar wil aantonen wat een maatregel heeft opgeleverd.

## 7. Onderhoud en updates

Dit is de post die mensen bij de keuze systematisch onderschatten.

| | Domoticz | Home Assistant |
|---|---|---|
| Releasetempo | rustig; stabiele versies met lange tussenpauzes | maandelijkse feature-release, plus patch-releases |
| Breaking changes | zeldzaam | komen voor; per release gedocumenteerd |
| Backup | database- en configuratiebestand kopiëren | ingebouwde snapshot van configuratie en add-ons |
| Community-uitbreidingen | plug-ins en scripts | add-ons en een community-store |
| Onderhoud per jaar | laag | reken op enkele uren, meer bij veel community-componenten |

Home Assistant vraagt om iemand die af en toe de release-notes leest. Wie een jaar niet update en dan in één keer doorspringt, loopt tegen opgestapelde wijzigingen aan. Domoticz vraagt vrijwel niets, maar geeft je ook geen nieuwe integraties.

Twee vaste aanraders, ongeacht je keuze: draai van SSD in plaats van SD-kaart, en zet automatische backups aan naar een plek buiten het apparaat.

## 8. Overstappen van Domoticz naar Home Assistant

De meest voorkomende reden om over te stappen is een ontbrekende integratie: een laadpaal, een dynamische leverancier of een batterij waarvoor Home Assistant een officiële koppeling heeft en Domoticz geen hardwaretype.

Wat de overstap volgens de documentatie van beide projecten praktisch betekent:

- Sensoren en apparaten koppel je opnieuw. Er is geen automatische importroute van Domoticz naar Home Assistant.
- Automatiseringen (Domoticz-events, Lua- of dzVents-scripts) herschrijf je naar Home Assistant-automatiseringen of YAML.
- Het dashboard bouw je opnieuw op.
- Historie gaat niet mee. Wil je die bewaren, exporteer dan eerst je Domoticz-grafieken naar CSV.
- Home Assistant vraagt structureel meer rekenkracht en schijf-I/O. Draait je Domoticz op een Pi 3, dan hoort nieuwe hardware bij het overstapbudget.

Reken bij enkele tientallen sensoren op een avond tot een dag werk, en houd de oude installatie draaiend tot de nieuwe stabiel is. Een tussenvorm die goed werkt: laat Domoticz de bestaande hardware uitlezen en publiceer alles via MQTT naar Home Assistant. Zo migreer je stap voor stap. Permanent twee systemen naast elkaar draaien is af te raden — twee keer updaten, twee dashboards, twee logbestanden.

## 9. Veelgemaakte fouten in de keuze

1. **Hardware onderschatten.** Home Assistant met energiesensoren op een Pi 3 met SD-kaart wordt traag en frustrerend. Pi 4 of 5 met SSD, of een mini-pc.
2. **Domoticz afschrijven om de interface.** Onder de motorkap is Domoticz licht en stabiel. Voor een P1-meter, wat schakelaars en een handvol sensoren is het een uitstekende keuze die jaren vergeten in de meterkast kan hangen.
3. **Community-componenten verwarren met kernfunctionaliteit.** Veel Home Assistant-tutorials gebruiken onderdelen uit de community-store. Die zijn niet gebonden aan het releaseproces van het project; bij een update kan zo'n component stilvallen.
4. **Geen backups instellen.** Een corrupte SD-kaart kost je in beide systemen al je historie.
5. **Meteen met YAML beginnen.** Beide platforms hebben interfacegestuurde flows. Leer eerst wat het platform zelf kan voordat je gaat programmeren.
6. **Sturen zonder doel.** Meten is de eerste stap, maar een dashboard bespaart niets. Bepaal welk apparaat je wil verschuiven en op welk signaal, anders bouw je een mooi paneel zonder resultaat.

## 10. Wanneer je geen van beide nodig hebt

Heb je alleen zonnepanelen, een dynamisch contract en een elektrische auto? Dan doet EVCC — open source, licht, gericht op laden op zon en prijs — wat nodig is zonder een volledige home-automation-stack. Het draait op zeer bescheiden hardware.

Wil je uitsluitend monitoren zonder te sturen? Dan is een netwerk-P1-module met de eigen app van de fabrikant genoeg. Je hebt direct grafieken en er is geen platform om te onderhouden. De grens ligt bij het moment waarop je op basis van die data iets wil aan- of uitzetten — dan heb je een platform nodig.

## 11. Conclusie: welke voor wie

**Kies Home Assistant** als energie het doel is en je op prijs wil sturen: het energiedashboard, de prijsintegraties, de generieke Modbus-integratie en de lengte van de integratielijst maken het geheel dat je anders zelf in scripts bouwt. Voorwaarde is dat je bereid bent in fatsoenlijke hardware te investeren en een paar keer per jaar release-notes te lezen.

**Kies Domoticz** als je een bestaande, werkende installatie hebt, of als je doel meten en eenvoudig schakelen is op zuinige hardware met minimaal onderhoud. Het is geen tweede keus — het is een ander uitgangspunt.

**Kies OpenHAB** als je een sterke regelengine wil en je niet laat afschrikken door een stevige leercurve. Voor wie specifiek zonnepanelen en een batterij wil sturen: [openHAB voor zonnepanelen en batterijsturing](/posts/openhab-zonnepanelen-batterij-sturing-2026/).

Wat je ook kiest: begin bij de P1-meter, laat een paar weken draaien, en beslis daarna welk apparaat je gaat verschuiven. Die volgorde levert meer op dan een dashboard dat op dag één alles laat zien.

---

**Externe bronnen:** de integratiedocumentatie van [Home Assistant](https://www.home-assistant.io/integrations/) en de hardware- en scriptdocumentatie van [Domoticz](https://www.domoticz.com/wiki/Main_Page) — beide geraadpleegd op 21 augustus 2026.
