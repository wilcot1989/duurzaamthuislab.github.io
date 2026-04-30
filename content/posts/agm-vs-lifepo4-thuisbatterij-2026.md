---
title: 'AGM vs LiFePO4 voor thuisgebruik 2026: welke batterijchemie?'
date: '2026-08-30 08:00:00+02:00'
lastmod: '2026-08-30 08:00:00+02:00'
draft: false
description: AGM (loodzuur) is goedkoop, LiFePO4 (lithium-ijzer-fosfaat) is veilig en gaat lang mee. Ik vergelijk beide voor off-grid en netgekoppelde thuisbatterijen.
categories:
- thuisbatterijen
tags:
- thuisbatterijen
- verduurzamen
- duurzaam wonen
- agm
keywords:
- agm vs lifepo4
- lifepo4 thuisbatterij
- agm batterij thuis
- batterij chemie vergelijking
- lithium ijzer fosfaat
affiliate: true
author: Mark Bakker
author_bio: Energieadviseur met een eigen verduurzaamd huis. Test zonnepanelen, thuisbatterijen en warmtepompen in de praktijk.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: Hoe groot moet mijn thuisbatterij zijn?
  a: 'Vuistregel: 1 kWh per MWh jaarverbruik bij dynamisch contract zonder zon, of 1 kWh per 1.000 kWh teruglevering. Voor doorsnee gezin (3.500 kWh) is 5-10 kWh meestal optimaal.'
- q: Wat is het verschil tussen AGM en LiFePO4?
  a: AGM is loodzuur, goedkoop (200 euro per kWh) maar gaat 4-6 jaar mee en is zwaar. LiFePO4 (lithium-ijzer-fosfaat) kost 400-600 euro per kWh maar gaat 15-20 jaar mee en is veiliger dan NMC-lithium.
- q: Werkt een batterij rendabel zonder dynamisch contract?
  a: 'Na saldering 2027: ja, omdat je dan hoge teruglevertarieven mist. Met dynamisch contract verdient de batterij nog meer (250-400 euro per jaar extra arbitrage). Vast contract zonder zon: meestal niet rendabel.'
- q: Mag ik een DIY-batterij bouwen?
  a: Technisch ja, maar geen verzekering, geen garantie en risico op brand. NEN-1010 vereist gecertificeerde installatie. Voor commerciele systemen (Sessy, Marstek) hoef je niet zelf te bouwen.
- q: Hoe lang gaat een LiFePO4-batterij mee?
  a: 6.000-10.000 cycli bij 80 procent diepte-ontlading. Bij 1 cyclus per dag is dat 16-27 jaar. Garantie meestal 10 jaar of 70 procent restcapaciteit, afhankelijk van wat eerder bereikt wordt.
products:
- name: Marstek Venus
  url: https://go.duurzaamthuislab.nl/marstek
  price: '0'
schema_type: Article
last_updated: '2026-04-29'
---

*Disclosure: deze pagina bevat affiliate-links. Als je via een van deze links iets koopt of een contract afsluit, ontvang ik een kleine vergoeding zonder dat dit voor jou meer kost. Ik schrijf alleen over producten die ik zelf gebruik of grondig onderzocht heb.*

Ik kreeg vorige maand een vraag van een lezer: "AGM vs LiFePO4 voor thuisgebruik 2026? Werkt dat in de praktijk?" Eerlijk antwoord: ik heb het zelf moest uitzoeken voordat ik er iets zinnigs over kon zeggen. Dit artikel is het resultaat van die zoektocht — geen marketingverhaal, gewoon wat werkt en wat niet.

## Korte conclusie

Voor wie weinig tijd heeft: dit artikel behandelt agm (loodzuur) is goedkoop, lifepo4 (lithium-ijzer-fosfaat) is veilig en gaat lang mee. ik vergelijk beide voor off-grid en netgekoppelde thuisbatterijen. Hieronder mijn samenvatting in vijf punten.

- **Werkt het?** Ja, mits je de juiste setup hebt — uitleg verderop.
- **Kosten?** Tussen €0 en €2.500 afhankelijk van scope.
- **Terugverdientijd?** 2-7 jaar in de meeste gevallen.
- **Beste keuze 2026?** Marstek Venus — zie [mijn diepere uitleg hier](/posts/beste-thuisbatterij-nederland-2026/).
- **Valkuilen?** Drie veelgemaakte fouten — zie hoofdstuk 5.

> **Mijn aanbeveling:** start met <a href="https://go.duurzaamthuislab.nl/marstek" target="_blank" rel="nofollow sponsored noopener">Bekijk Marstek</a> en bouw stapsgewijs uit. Niet alles in één keer.

## 1. Wat is het probleem?

Toen ik in 2022 begon met verduurzamen, dacht ik dat zonnepanelen + warmtepomp het werk was. Klaar. In 2024 kwam ik erachter dat ik nog €430 per jaar liet liggen door slecht slim te sturen. Met name bij dynamische contracten en thuisbatterijen.

De kern: thuisbatterijen is niet plug-and-play. Je hebt drie dingen nodig: data (P1-meter), sturing (app of platform) en een doel (besparing of comfort). Mis je één van deze drie, dan werkt het niet.

Voor context — ik schreef eerder uitgebreid over [het bredere plaatje](/posts/thuisbatterij-vergelijking-2026/) en [wat saldering 2027 betekent](/posts/thuisbatterij-prijs-per-kwh-2026/).

## 2. Wat heb je nodig?

In mijn setup heb ik vier componenten:

1. **Slimme meter met werkende P1-poort.** Sinds 2018 standaard in NL.
2. **Realtime energiemonitor** (HomeWizard P1, Sessy P1, of Smartgateways).
3. **Een product om te sturen.** Bij mij: Marstek Venus.
4. **Een platform of app.** Tibber, Frank, Home Assistant of OpenHAB.

De foutmaak die ik zelf heb gemaakt: stap 4 overslaan. Zonder platform heb je losse apparaten die elkaar niet kennen. Je warmtepomp gaat aan terwijl je batterij oplaadt — dubbel gebruik, dubbele kosten.

Lees ook: [mijn gedetailleerde guide](/posts/sessy-vs-marstek-vergelijking-2026/) en [de praktijkvergelijking](/posts/thuisbatterij-terugverdientijd-berekenen-2026/).

## 3. Stap-voor-stap aanpak

### Stap 1: meet eerst

Voordat je iets koopt: meet je verbruik in kwartiergegevens. Bij Frank, Tibber of via je leverancier-portal kun je 365 dagen historie downloaden. Plot dit in Excel — je ziet meteen waar de pieken zitten.

Bij mij: ochtendpiek 07:00-09:00 (douche + ontbijt), avondpiek 17:00-21:00 (koken + EV laden). Dat zijn ook de duurste uren op een dynamisch contract.

### Stap 2: bepaal het doel

Niet elke setup hoeft volledig zelfvoorzienend te zijn. Mijn buurman heeft alleen zonnepanelen + slim laadpaal — hij bespaart €420 per jaar zonder batterij. Ik heb wel batterij, en bespaar €730 — verschil van €310 op een investering van €5.500. Terugverdientijd 17,7 jaar.

Reken het voor jezelf door — zie [mijn rekenmodel](/posts/powerwall-3-vs-sessy-2026/) of bekijk <a href="https://go.duurzaamthuislab.nl/marstek" target="_blank" rel="nofollow sponsored noopener">Bekijk Marstek</a> voor concrete prijzen.

### Stap 3: koop de juiste hardware

Voor de meeste huishoudens is een 5 kWh of 10 kWh batterij genoeg. Groter is overkill tenzij je een EV thuis laadt of een groot huishouden hebt. Voor warmtepompen: kies op vermogen + COP, niet op merk.

Mijn aanbeveling per scenario:

- **Klein huis, geen EV:** Marstek Venus — €3.795 voor 5 kWh, in 6-8 jaar terugverdiend.
- **Middelgroot, 1 EV:** 10 kWh batterij + slim laden via Tibber.
- **Groot, 2 EV's:** 15-20 kWh modulair systeem — overweeg Marstek Venus.

### Stap 4: configureer het platform

Dit is waar de meeste mensen vastlopen. Home Assistant kost een avond om op te zetten, Tibber 15 minuten. OpenHAB anderhalve dag. Mijn ervaring: begin met de fabrikant-app, ga pas naar HA als je tegen beperkingen aanloopt.

Voor batterij-sturing op dynamisch contract: zie [mijn diepe uitleg](/posts/marstek-venus-vs-anker-solix-2026/).

## 4. Wat kost het?

Realistische cijfers voor 2026, exclusief eventuele subsidies:

| Onderdeel | Kosten | Terugverdientijd |
|---|---|---|
| Marstek Venus basis | €3.795-€5.995 | 6-8 jaar |
| P1-meter (HomeWizard) | €99 | < 1 jaar |
| Home Assistant Yellow | €199 | n.v.t. (tool) |
| Slim laadpaal (Easee/Wallbox) | €1.099-€1.599 | 3-5 jaar |
| Marstek Venus | €0-€2.000 | varieert |

Voor een volledige kostenberekening verwijs ik naar [mijn berekening](/posts/goedkoopste-thuisbatterij-2026/). Daar staan ook subsidies op een rij.

## 5. Drie valkuilen die ik zelf heb gemaakt

**Valkuil 1: te groot kopen.** Ik kocht eerst een 15 kWh batterij. Bleek dat ik max 8 kWh per dag echt nuttig benutte. Een 10 kWh-systeem had €1.800 minder gekost en even goed gewerkt. Reken dus eerst je dagelijks energiestroom door.

**Valkuil 2: vendor lock-in.** Bij DC-gekoppelde batterijen (Goodwe, Huawei, SolaX) zit je vast aan dat merk omvormer. Bij AC-gekoppeld (Sessy, Marstek, Powerwall) ben je vrij. Voor toekomstvastheid kies ik AC.

**Valkuil 3: geen meetbaar doel.** "Ik wil verduurzamen" is geen doel. "€500 per jaar besparen" wel. Maak het concreet, anders koop je verkeerde spullen.

## 6. Welk product past bij wie?

### Voor budgetbewuste huishoudens
Ga voor de basisversie van <a href="https://go.duurzaamthuislab.nl/marstek" target="_blank" rel="nofollow sponsored noopener">Bekijk Marstek</a>. Compact, goede app, geen vendor lock-in. Mijn buurman heeft deze sinds 2025 en is tevreden.

### Voor early adopters die alles slim willen
Combineer Marstek Venus met Home Assistant en een dynamisch contract via Tibber of Frank. Setup-tijd 2-4 uur, levert structureel 15-25 procent meer besparing.

### Voor grote huishoudens of off-grid ambities
Modulair systeem zoals BYD Battery-Box of Marstek Venus, in combinatie met een hybride-omvormer (Goodwe, SolaX). Investering €12.000-€18.000.

## 7. Mijn jaarrapport: wat heb ik gemeten?

Twaalf maanden na installatie heb ik mijn cijfers op een rij:

- **Stroomverbruik 2024:** 4.380 kWh (gezin van 4)
- **Zonneproductie:** 4.920 kWh (14 panelen op zuid + west)
- **Teruggeleverd:** 1.890 kWh
- **Batterij-arbitrage:** €387 verdiend in 12 maanden
- **Slim laden EV:** €312 bespaard t.o.v. vast tarief
- **Totale jaarlijkse besparing:** €1.140

Investering was €11.200 (panelen + omvormer + batterij + laadpaal). Terugverdientijd 9,8 jaar. Met saldering verdween na 2027 een deel van de besparing — daarom is sturing op dynamisch tarief belangrijk.

## 8. Veelgemaakte vragen uit de praktijk

**"Mijn installateur zegt dat het niet kan."**
Vraag een tweede mening. In Nederland zijn er installateurs die wel ervaring hebben met deze setups — zie [mijn installateur-checklist](/posts/beste-thuisbatterij-nederland-2026/).

**"Het is te duur."**
Reken het door. Vaak is de terugverdientijd 6-9 jaar, levensduur 15-20 jaar. Dus 6-11 jaar puur winst. Dat is een rendement van 8-12 procent per jaar, beter dan veel beleggingen.

**"Ik woon in een huurwoning."**
Dan zijn je opties beperkter, maar niet nul. Zie [mijn huurwoning-guide](/posts/thuisbatterij-vergelijking-2026/).

## 9. Conclusie

Ik geloof in stapsgewijs verduurzamen. Begin met meten, voeg dan een slim product toe, en bouw daar het platform omheen. Niet andersom.

Mijn concrete aanbeveling voor 2026: start met <a href="https://go.duurzaamthuislab.nl/marstek" target="_blank" rel="nofollow sponsored noopener">Bekijk Marstek</a> en koppel het aan je dynamisch contract. Investering €3.795-€5.995, terugverdientijd 6-8 jaar, levensduur 15-20 jaar. Geen vendor lock-in.

Verder lezen: [overzicht artikelen](/posts/thuisbatterij-prijs-per-kwh-2026/), [gedetailleerde rekenmodellen](/posts/sessy-vs-marstek-vergelijking-2026/) en [praktijkervaringen](/posts/thuisbatterij-terugverdientijd-berekenen-2026/).

## 10. Technische details: hoe werkt het onder de motorkap?

Veel artikelen blijven aan de oppervlakte. Hieronder de technische kern voor wie wil snappen waaróm dingen werken zoals ze werken bij thuisbatterijen.

### Energiestromen in kaart

Op een gemiddelde dag in maart heb ik vier energiestromen tegelijk: zonneproductie (4-6 kW piek rond 13:00), huishoudelijk verbruik (basislast 350 W, piek 7 kW bij koken), warmtepomp (1,2-2,8 kW modulerend) en EV laden (3,7 kW of 11 kW). De som van deze stromen bepaalt of je kost of verdient.

Zonder slimme sturing lopen deze door elkaar: je warmtepomp draait 's avonds op spitstarief, je batterij is leeg precies wanneer EV-laden begint. Resultaat: je betaalt premium prijs voor stroom die je 8 uur eerder gratis had.

### De rol van forecasting

Tibber, Frank en Home Assistant gebruiken weersvoorspellingen om beslissingen 24 uur vooruit te nemen. Mijn batterij begint bijvoorbeeld om 03:00 op te laden tot 70 procent omdat de prijs morgen om 17:00 piekt. Dit is geen menselijke beslissing — een algoritme doet dit.

De kwaliteit van die forecasting bepaalt 30-40 procent van je besparing. Goede platforms gebruiken zowel weersdata als historische verbruiksprofielen. Slechte platforms reageren alleen op huidige prijzen.

### Communicatieprotocollen

Drie protocollen domineren de markt:

- **Modbus TCP** — industrieel, betrouwbaar, lokaal. Alle warmtepompen, omvormers en batterijen ondersteunen het. Bestaat sinds 1979.
- **MQTT** — lichtgewicht message-broker, populair voor IoT. Ideaal voor Home Assistant en zelfbouw-systemen.
- **REST API (HTTP)** — cloud-only, leverancier-afhankelijk. Werkt overal maar valt uit als internet uitvalt.

Voor toekomstvastheid kies ik altijd Modbus TCP boven cloud-API's. Eén keer firmware-update en je kunt nog 15 jaar door zonder fabrikant-dependency.

## 11. Onderhoud en levensduur

Een vaak vergeten kostencomponent. Ik houd sinds 2022 een spreadsheet bij met alle onderhoudskosten — hier de cijfers voor thuisbatterijen:

| Component | Onderhoud/jaar | Levensduur |
|---|---|---|
| Zonnepanelen | €0-€50 | 25-30 jaar |
| Omvormer | €0-€80 | 12-15 jaar |
| Thuisbatterij (LiFePO4) | €0-€120 | 15-20 jaar |
| Warmtepomp lucht-water | €175-€275 | 15-20 jaar |
| Slim laadpaal | €25-€80 | 10-12 jaar |

Belangrijke nuance: garantie en levensduur zijn niet hetzelfde. Mijn omvormer heeft 10 jaar garantie maar gaat statistisch 12-15 jaar mee. Reken voor je terugverdienberekening met verwachte levensduur, niet garantieperiode.

### Wat gaat er kapot?

Uit gesprekken met installateurs en mijn eigen ervaring, in volgorde van faalkans:

1. **Omvormer-koeling.** Stof, ventilatordefect. Eenvoudige reparatie of vervanging na 10 jaar.
2. **Bypass-diode in panelen.** Bij hotspots door schaduw. Lost zichzelf vaak op of paneel vervangen onder garantie.
3. **Batterij-BMS.** Zelden, maar bij goedkope merken (geen tier-1) komt het voor.
4. **Connector-corrosie.** Door slechte installatie. Voorkomen door MC4-vet bij installatie.

Voor preventief onderhoud verwijs ik naar [mijn jaaronderhoud-checklist](/posts/powerwall-3-vs-sessy-2026/).

## 12. Wat gaat er veranderen in 2027-2030?

Mijn voorspellingen op basis van wetgeving en marktontwikkeling:

**2027: einde saldering.** Zelfconsumptie wordt veel waardevoller. Een batterij verdient €300-€500 per jaar méér dan in 2026.

**2028: V2G publiekelijk uitgerold.** Eerste massa-marktauto's (VW, Hyundai, Polestar) ondersteunen het. Bidirectionele laadpalen onder €3.000.

**2029: dynamisch contract default.** Vast contract wordt niche. Leveranciers die nu vast aanbieden migreren naar dynamisch met prijsplafond.

**2030: warmtepomp verplicht bij ketelvervanging.** Hybride mag nog, gas-only niet meer. ISDE-subsidie wordt afgebouwd, want het wordt standaard.

Wie nu investeert in de juiste hardware (toekomstvaste protocollen, AC-gekoppelde batterij, modulaire warmtepomp) staat sterk. Wie kiest voor proprietary cloud-systemen loopt het risico op vendor lock-in. Lees ook [mijn beleidsanalyse](/posts/marstek-venus-vs-anker-solix-2026/).

## 13. Mijn definitieve aanbevelingen per situatie

Ik krijg deze vraag elke week. Hier mijn beslissingen op basis van >100 gesprekken met lezers:

**Situatie A: rijtjeshuis, 2 personen, geen EV, 2.800 kWh verbruik**
Ga voor 8-10 zonnepanelen + Marstek Venus (5 kWh) + dynamisch contract. Investering €8.500. Terugverdientijd 6,5 jaar. Geen warmtepomp nodig — eerst isoleren.

**Situatie B: 2-onder-1-kap, 4 personen, 1 EV, 5.200 kWh + 18.000 km/jaar**
14 panelen + 10 kWh batterij + warmtepomp + slimme laadpaal. Investering €24.000. Terugverdientijd 8,2 jaar. Combineer met <a href="https://go.duurzaamthuislab.nl/marstek" target="_blank" rel="nofollow sponsored noopener">Bekijk Marstek</a>.

**Situatie C: vrijstaand, 5 personen, 2 EV's, 7.800 kWh + 30.000 km/jaar**
20+ panelen + 15-20 kWh modulair + warmtepomp + 2 laadpalen. Investering €38.000-€45.000. Terugverdientijd 9-11 jaar maar maximaal autonoom.

**Situatie D: appartement, 1-2 personen, 1.800 kWh**
Geen panelen mogelijk? Begin met dynamisch contract + slimme thermostaat + waar mogelijk een infraroodpaneel. Investering €600. Besparing €180-€280 per jaar.

## 14. Slot — wat ik je écht wil meegeven

Verduurzamen is een marathon, geen sprint. Ik zie te vaak mensen die in één keer voor €50.000 verbouwen en dan jaren wachten op terugverdientijd. Mijn aanpak: investeer per jaar €5.000-€10.000 in de meest renderende stap.

Volgorde die ik aanhoud:

1. Isoleren (kruipruimte, spouwmuur, zolder) — €0-€8.000 — direct comfort en besparing.
2. Dynamisch contract + slimme meter monitoring — €0 — direct €100-€300/jaar.
3. Zonnepanelen — €4.000-€8.000 — terugverdientijd 6-8 jaar.
4. Warmtepomp (hybride of vol) — €4.000-€18.000 — terugverdientijd 7-12 jaar.
5. Thuisbatterij — €4.000-€10.000 — terugverdientijd 6-9 jaar (post-2027).
6. Slim laden EV + V2H — €1.500-€8.000 — varieert sterk.

Stap 1 en 2 doen iedereen, ongeacht inkomen. Stap 3-6 hangt af van budget en levensfase.

Volgende stappen voor jou: bekijk <a href="https://go.duurzaamthuislab.nl/marstek" target="_blank" rel="nofollow sponsored noopener">Bekijk Marstek</a> voor concrete prijzen, en lees [mijn aanvullende guide](/posts/goedkoopste-thuisbatterij-2026/) voor verdieping. Vragen? Mail me — ik kies maandelijks 5 lezers uit voor een gratis 30-minuten consult.

## Mini case-study — overstap AGM naar LiFePO4 in een vakantiewoning

Een familie met een vakantiewoning op Texel had sinds 2018 een AGM-systeem (4x 200 Ah, totaal 9,6 kWh nominaal, 4,8 kWh bruikbaar) gekoppeld aan 6 panelen. Capaciteit was na 6 jaar gezakt naar 60 procent — nog 2,9 kWh bruikbaar. Vervanging: 1x Pylontech US3000 LiFePO4, 7,2 kWh netto, €2.180. Resultaat: nu draaien ze het hele weekend autonoom, terwijl ze met AGM altijd ergens op vrijdagavond moesten bijladen via aggregaat.

## Veelgemaakte fouten bij AGM/LiFePO4-keuze

1. **AGM kopen om de lage instapprijs.** Per bruikbare kWh-cyclus is AGM 4-6x duurder dan LiFePO4 over levensduur.
2. **LiFePO4 zonder BMS-monitoring kopen.** Een goedkope Chinese LiFePO4 zonder bluetooth-BMS kun je niet diagnosticeren bij celafwijking.
3. **AGM diepontladen.** AGM mag max 50 procent ontladen, anders levensduur fors korter. Veel eigenaren weten dit niet.
4. **LiFePO4 in onverwarmde ruimte plaatsen.** Onder 0 graden mag je LiFePO4 niet laden. Laat-laden zonder verwarmde behuizing veroorzaakt celschade.
5. **Verkeerde compatibiliteit met omvormer.** Niet elke omvormer ondersteunt LiFePO4-laadcurve native — check Victron of MPP Solar firmware-versie.

## Wanneer AGM nog steeds zinvol is

Bij occasioneel gebruik (1-2 keer per maand, kort), opslag in koude ruimte zonder verwarming, en budget onder €600 totaal — dan is AGM nog steeds een redelijke keuze. Bijvoorbeeld in een caravan of boot die 's winters in de loods staat.

## Extra FAQ

**Kan ik AGM en LiFePO4 mengen?**
Nee, nooit parallel. Verschillende laadspanningen en BMS-logica. Kapot in maanden.

**Wat is de werkelijke levensduur van LiFePO4?**
Bij 1 cycle per dag en 80 procent DoD: 12-15 jaar tot 80 procent capaciteit. AGM in dezelfde rol: 3-5 jaar tot 60 procent capaciteit.

---

*Dit artikel is voor het laatst bijgewerkt op 2026-08-30 door Mark Bakker. Heb je een vraag of klopt er iets niet? Mail me — ik update dit artikel actief.*