---
title: 'Dynamisch contract + thuisbatterij: rekenmodel besparing 2026'
date: '2026-09-09 08:00:00+02:00'
lastmod: '2026-08-20 08:00:00+02:00'
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
- q: Wat is een terugleverstaffel?
  a: Een prijssysteem waarbij je hoger tarief voor teruglevering betaalt naarmate je meer teruglevert. Bijvoorbeeld 0-1.500 kWh gratis, 1.501-3.000 kWh kost 6 cent per kWh extra.
- q: Welke leverancier heeft de laagste terugleverkosten in 2026?
  a: Frank Energie en Tibber rekenen geen extra staffel — je krijgt direct de spot-prijs. Vast-contract leveranciers (Eneco, Vattenfall) rekenen volgens hun tarievenbladen 9-15 cent per kWh staffel boven 2.500 kWh.
- q: Hoe werkt EPEX spot prijsvorming?
  a: EPEX (European Power Exchange) houdt elke dag om 12:00 een veiling voor de 24 uren van de volgende dag. Vraag en aanbod bepalen de uurprijs. Negatieve prijzen ontstaan bij overschot zon/wind en weinig vraag.
- q: Wanneer is dynamisch goedkoper dan vast?
  a: Bij verbruik buiten piekuren (18:00-22:00) en/of zonnepanelen + batterij. Voor laagverbruikers zonder slimme apparaten kan vast voordeliger zijn.
- q: Heb ik een slimme meter nodig?
  a: 'Voor dynamisch contract: ja, met kwartiergegevens. Bijna alle Nederlandse meters sinds 2018 voldoen. Check via de meterstand-app of je P1-poort werkt.'
products:
- name: Tibber
  url: https://go.duurzaamthuislab.nl/tibber
  price: '0'
- name: Sessy thuisbatterij
  url: https://go.duurzaamthuislab.nl/sessy
  price: '0'
schema_type: Article
last_updated: '2026-08-19'
---
*Disclosure: de links naar Sessy en Tibber in dit artikel zijn gewone verwijzingen — wij hebben met deze partijen geen affiliate- of commissierelatie. Wij vergelijken op basis van specificaties, tarievenbladen, geverifieerde gebruikersreviews en publieke data.*

"Dynamisch contract plus thuisbatterij — werkt dat in de praktijk?" is een van de meestgestelde vragen over energiecontracten. Het antwoord hangt volledig af van je verbruikprofiel en van de prijsspreads op de EPEX-markt. Daarom bouwen we hieronder een rekenmodel waarin elke aanname zichtbaar is, zodat je hem met jouw eigen cijfers kunt narekenen.


> **Kort antwoord:** Een 10 kWh thuisbatterij op een dynamisch contract verdient geld via twee kanalen: arbitrage (goedkoop laden, duur ontladen) en zelfconsumptie van zonnestroom. Hoeveel dat oplevert, bepalen de EPEX-spread, de energiebelasting en de vermogenslimiet van je omvormer.
>
> Een terugleverstaffel is een prijssysteem waarbij je een hoger tarief voor teruglevering betaalt naarmate je meer teruglevert. Bijvoorbeeld 0-1.500 kWh gratis, 1.501-3.000 kWh kost 6 cent per kWh extra.

## Korte conclusie

Voor wie weinig tijd heeft, de samenvatting in vijf punten:

- **Werkt het?** Ja, mits je verbruikprofiel en installatie het toelaten — uitleg verderop.
- **Kosten?** Tussen €0 en €2.500 aan randapparatuur, plus de batterij zelf.
- **Terugverdientijd?** In de meeste rekenvoorbeelden 2-7 jaar, sterk afhankelijk van de spread.
- **Beste keuze 2026?** Zie de [vergelijking van dynamische contracten](/posts/dynamische-energiecontracten-vergelijking-2026/).
- **Valkuilen?** Vijf rekenfouten — zie hoofdstuk 5 en de sectie over het rekenmodel.

> **Onze inschatting:** begin met een dynamisch contract en meting, en bouw daarna stapsgewijs uit. <a href="https://go.duurzaamthuislab.nl/tibber" target="_blank" rel="nofollow sponsored noopener">Bekijk Tibber</a>.

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

De fout die het vaakst terugkomt in gebruikersforums: stap 4 overslaan. Zonder platform heb je losse apparaten die elkaar niet kennen. Je warmtepomp gaat aan terwijl je batterij oplaadt — dubbel gebruik, dubbele kosten.

Lees ook: [de gedetailleerde guide](/posts/frank-energie-review-ervaringen-2026/) en [de praktijkvergelijking](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

## 3. Stap-voor-stap aanpak

### Stap 1: meet eerst

Voordat je iets koopt: breng je verbruik in kwartiergegevens in kaart. Bij Frank, Tibber of via je leverancier-portal kun je 365 dagen historie downloaden. Plot dit in een spreadsheet — dan zie je meteen waar de pieken zitten.

In een gemiddeld gezinsprofiel liggen die pieken rond 07:00-09:00 (douche en ontbijt) en 17:00-21:00 (koken en EV-laden). Dat zijn ook de duurste uren op een dynamisch contract.

### Stap 2: bepaal het doel

Niet elke setup hoeft volledig zelfvoorzienend te zijn. Zonnepanelen plus slim laden zonder batterij levert al een groot deel van de winst; de batterij voegt daar arbitrage en meer zelfconsumptie aan toe. Of dat extra bedrag de investering rechtvaardigt, is precies wat het rekenmodel hieronder uitwijst.

Reken het voor jezelf door — zie [het rekenmodel voor zonnepanelen](/posts/beste-dynamisch-contract-met-zonnepanelen-2026/) of bekijk <a href="https://go.duurzaamthuislab.nl/sessy" target="_blank" rel="nofollow sponsored noopener">Bekijk Sessy</a> voor actuele prijzen.

### Stap 3: koop de juiste hardware

Voor de meeste huishoudens is een 5 kWh of 10 kWh batterij genoeg. Groter is zelden nuttig tenzij je een EV thuis laadt of een groot huishouden hebt. Voor warmtepompen: kies op vermogen en COP, niet op merk.

Onze inschatting per scenario:

- **Klein huis, geen EV:** 5 kWh batterij — vaak de kortste terugverdientijd per euro investering.
- **Middelgroot, 1 EV:** 10 kWh batterij plus slim laden.
- **Groot, 2 EV's:** 15-20 kWh modulair systeem.

### Stap 4: configureer het platform

Dit is waar de meeste mensen vastlopen. Volgens de documentatie en gebruikerservaringen is een fabrikant-app in een kwartier ingericht, Home Assistant kost een avond en OpenHAB nog aanzienlijk meer. Onze aanbeveling: begin met de fabrikant-app en stap pas over op Home Assistant als je tegen beperkingen aanloopt.

Voor batterij-sturing op dynamisch contract: zie [de uitleg over terugleverkosten](/posts/terugleverkosten-zonnepanelen-2026/).

## 4. Wat kost het?

Indicatieve marktprijzen voor 2026, inclusief btw en zonder subsidie. Reken op de batterij met 21% btw: het 0%-tarief voor zonnepanelen dekt volgens de Belastingdienst uitdrukkelijk niet de levering en installatie van een accupakket of thuisbatterij, en de ISDE dekt voor woningeigenaren geen batterijopslag.

| Onderdeel | Kosten | Terugverdientijd |
|---|---|---|
| Thuisbatterij 5-10 kWh | circa €3.550-€5.500 (prijspeil aug 2026, Sessy als referentie via sessy.nl; andere merken wijken af — zie vendorsites) | 6-8 jaar (modelberekening) |
| P1-meter (HomeWizard) | €99 | < 1 jaar |
| Home Assistant Yellow | €199 | n.v.t. (tool) |
| Slimme laadpaal (Easee/Wallbox) | €1.099-€1.599 | 3-5 jaar |
| Extra sturing/accessoires | €0-€2.000 | varieert |

Voor een volledige kostenberekening: zie [de vergelijking dynamisch versus vast](/posts/dynamisch-vs-vast-contract-2026/).

## 5. Drie valkuilen bij de aanschaf

**Valkuil 1: te groot kopen.** Een batterij die groter is dan je dagelijkse nuttige doorzet, staat een deel van het jaar stil. Bereken eerst hoeveel kWh je per dag daadwerkelijk kunt verschuiven; dat is bijna altijd minder dan de nominale capaciteit.

**Valkuil 2: vendor lock-in.** Bij DC-gekoppelde batterijen (Goodwe, Huawei, SolaX) zit je vast aan de omvormer van dat merk. Bij AC-gekoppeld (Sessy, Marstek, Powerwall) ben je vrij. Voor toekomstvastheid heeft AC onze voorkeur.

**Valkuil 3: geen meetbaar doel.** "Ik wil verduurzamen" is geen doel. "€500 per jaar besparen" wel. Maak het concreet, anders koop je verkeerde spullen.

## 6. Welk product past bij wie?

### Voor budgetbewuste huishoudens
Een compacte AC-gekoppelde batterij met een goede app en zonder vendor lock-in. <a href="https://go.duurzaamthuislab.nl/tibber" target="_blank" rel="nofollow sponsored noopener">Bekijk Tibber</a> voor het contract dat de sturing mogelijk maakt.

### Voor wie alles wil automatiseren
Combineer de batterij met Home Assistant en een dynamisch contract via Tibber of Frank. Setup-tijd volgens de documentatie 2-4 uur; je krijgt er fijnmazigere sturing voor terug dan met alleen de fabrikant-app.

### Voor grote huishoudens of off-grid ambities
Modulair systeem zoals BYD Battery-Box of Sessy thuisbatterij, in combinatie met een hybride-omvormer (Goodwe, SolaX). Investering in deze klasse loopt op tot €12.000-€18.000.

## 7. Het rekenmodel: rekenvoorbeeld voor een gezinswoning

Onderstaand voorbeeld is een rekenvoorbeeld met expliciete aannames — geen meting. Vul je eigen cijfers in en de uitkomst verandert mee.

Aannames:

- **Stroomverbruik:** 4.380 kWh per jaar (gezin van 4)
- **Zonneproductie:** 4.920 kWh (14 panelen, zuid en west)
- **Teruglevering zonder batterij:** 1.890 kWh
- **Batterij:** 10 kWh, AC-gekoppeld, 5 kW omvormer
- **Gemiddelde bruikbare dag-spread:** €0,18/kWh na belasting
- **Nuttige doorzet:** 1,2 cycli per dag, 300 dagen per jaar

Uitkomst van het model:

- Arbitrage: 10 kWh × 1,2 × 300 × €0,18 × 0,88 rendement ≈ €570 bruto
- Minus maandfee dynamisch contract (€5,99/maand): −€72
- Extra zelfconsumptie zonnestroom: afhankelijk van salderingsregime, in dit voorbeeld €150-€300

Bij een investering van circa €5.500 komt de terugverdientijd in dit voorbeeld op 8 tot 10 jaar. Verlaag de spread naar €0,12/kWh en het wordt 12 jaar of meer; verhoog hem naar €0,24/kWh en het zakt richting 6 jaar. De spread is dus de dominante variabele, en die kun je niet vooraf vastzetten.

## 8. Veelgestelde vragen uit de praktijk

**"Mijn installateur zegt dat het niet kan."**
Vraag een tweede mening. Er zijn installateurs met ervaring met deze setups — zie [de installateur-checklist](/posts/dynamische-energiecontracten-vergelijking-2026/).

**"Het is te duur."**
Reken het door met je eigen cijfers. In veel rekenvoorbeelden ligt de terugverdientijd op 6-9 jaar bij een verwachte levensduur van 15-20 jaar. Wat dat als rendement betekent, hangt af van de spread en de restwaarde — behandel het als een schatting met een brede marge, niet als een gegarandeerd rendement.

**"Ik woon in een huurwoning."**
Dan zijn je opties beperkter, maar niet nul. Zie [de vergelijking van leveranciers](/posts/frank-energie-vs-tibber-2026/).

## 9. Conclusie

Stapsgewijs verduurzamen werkt beter dan alles in één keer: begin met meten, voeg dan sturing toe, en bouw daar het platform omheen. Niet andersom.

Voor 2026 is de logische eerste stap een dynamisch contract met goede data-ontsluiting: <a href="https://go.duurzaamthuislab.nl/tibber" target="_blank" rel="nofollow sponsored noopener">Bekijk Tibber</a>. De batterij komt daarna, als je verbruikprofiel bekend is.

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

Een vaak vergeten kostencomponent. Indicatieve bedragen op basis van onderhoudscontracten en fabrikantopgaven:

| Component | Onderhoud/jaar | Levensduur |
|---|---|---|
| Zonnepanelen | €0-€50 | 25-30 jaar |
| Omvormer | €0-€80 | 12-15 jaar |
| Thuisbatterij (LiFePO4) | €0-€120 | 15-20 jaar |
| Warmtepomp lucht-water | €175-€275 | 15-20 jaar |
| Slimme laadpaal | €25-€80 | 10-12 jaar |

Belangrijke nuance: garantie en levensduur zijn niet hetzelfde. Een omvormer met 10 jaar garantie gaat volgens fabrikantopgaven doorgaans 12-15 jaar mee. Reken voor je terugverdienberekening met verwachte levensduur, niet met de garantieperiode.

### Wat gaat er kapot?

De faalmodi die installateurs en fabrikant-servicedocumentatie het vaakst noemen, ongeveer in volgorde van frequentie:

1. **Omvormer-koeling.** Stof, ventilatordefect. Eenvoudige reparatie of vervanging na circa 10 jaar.
2. **Bypass-diode in panelen.** Bij hotspots door schaduw. Vaak paneelvervanging onder garantie.
3. **Batterij-BMS.** Zelden, maar bij goedkopere merken komt het voor.
4. **Connector-corrosie.** Door slechte installatie. Te voorkomen met MC4-vet bij montage.

Voor preventief onderhoud: zie [de jaaronderhoud-checklist](/posts/beste-dynamisch-contract-met-zonnepanelen-2026/).

## 12. Wat gaat er veranderen in 2027-2030?

Onze verwachting op basis van wetgeving en marktontwikkeling — geen zekerheden:

**2027: einde saldering.** Zelfconsumptie wordt waardevoller; het verdienmodel van een batterij verschuift van teruglevering naar eigen gebruik en arbitrage.

**2028: bredere V2G-uitrol.** De eerste massamarktauto's ondersteunen bidirectioneel laden; verwachting is dat bidirectionele laadpalen in prijs dalen.

**2029: dynamisch contract als norm.** Vaste contracten worden waarschijnlijk nichés, mogelijk in de vorm van dynamisch met prijsplafond.

**2030: strengere eisen bij ketelvervanging.** De richting van beleid is hybride of volledig elektrisch; hoe de regels exact luiden, hangt af van besluitvorming die nog loopt.

Wie nu investeert in toekomstvaste hardware (open protocollen, AC-gekoppelde batterij, modulaire warmtepomp) staat sterker dan wie kiest voor gesloten cloud-systemen. Lees ook [de beleidsanalyse](/posts/terugleverkosten-zonnepanelen-2026/).

## 13. Rekenvoorbeelden per situatie

Vier fictieve rekenvoorbeelden met expliciete aannames. Bedragen zijn marktprijsindicaties, terugverdientijden volgen uit het model in hoofdstuk 7.

**Situatie A: rijtjeshuis, 2 personen, geen EV, 2.800 kWh verbruik**
8-10 zonnepanelen, 5 kWh batterij, dynamisch contract. Investering circa €8.500, terugverdientijd in het model 6-8 jaar. Warmtepomp nog niet aan de orde — eerst isoleren.

**Situatie B: 2-onder-1-kap, 4 personen, 1 EV, 5.200 kWh + 18.000 km/jaar**
14 panelen, 10 kWh batterij, warmtepomp, slimme laadpaal. Investering circa €24.000, terugverdientijd 8-10 jaar. Combineer met <a href="https://go.duurzaamthuislab.nl/sessy" target="_blank" rel="nofollow sponsored noopener">Bekijk Sessy</a>.

**Situatie C: vrijstaand, 5 personen, 2 EV's, 7.800 kWh + 30.000 km/jaar**
20+ panelen, 15-20 kWh modulair, warmtepomp, 2 laadpalen. Investering €38.000-€45.000, terugverdientijd 9-11 jaar bij maximale autonomie.

**Situatie D: appartement, 1-2 personen, 1.800 kWh**
Geen panelen mogelijk? Begin met dynamisch contract, slimme thermostaat en waar mogelijk lokale elektrische bijverwarming. Investering circa €600, besparing in het model €180-€280 per jaar.

## 14. Slot

Verduurzamen is een marathon, geen sprint. Alles in één keer verbouwen levert een lange wachttijd op je terugverdientijd op; per jaar de meest renderende stap zetten werkt beter.

De volgorde die in vrijwel elk rekenmodel het beste uitpakt:

1. Isoleren (kruipruimte, spouwmuur, zolder) — €0-€8.000 — direct comfort en besparing.
2. Dynamisch contract plus monitoring — €0-€100 — direct €100-€300 per jaar.
3. Zonnepanelen — €4.000-€8.000 — terugverdientijd 6-8 jaar.
4. Warmtepomp (hybride of vol) — €4.000-€18.000 — terugverdientijd 7-12 jaar.
5. Thuisbatterij — €4.000-€10.000 — terugverdientijd 6-9 jaar in de meeste modellen.
6. Slim laden EV en V2H — €1.500-€8.000 — varieert sterk.

Stap 1 en 2 zijn voor vrijwel iedereen zinvol. Stap 3-6 hangt af van budget en levensfase.

Volgende stap: bekijk <a href="https://go.duurzaamthuislab.nl/tibber" target="_blank" rel="nofollow sponsored noopener">Bekijk Tibber</a> voor actuele voorwaarden, en lees [de vergelijking dynamisch versus vast](/posts/dynamisch-vs-vast-contract-2026/) voor verdieping.

## Rekenvoorbeeld: 5 kWh batterij bij een gezinswoning

Een tweede rekenvoorbeeld, kleiner gedimensioneerd (fictief, aannames expliciet):

Verbruik 4.100 kWh per jaar, zonneproductie 5.200 kWh, EV-laden 6.500 kWh extra, batterij 5 kWh AC-gekoppeld. Bij een gemiddelde bruikbare spread van €0,20/kWh en 1,3 cycli per dag komt de arbitragewinst op circa €400 per jaar; extra zelfconsumptie levert in dit profiel €250-€350. Bij een investering van €2.890 inclusief 21% btw — er is geen btw-teruggaaf of subsidie op de batterij verondersteld — is de terugverdientijd in dit model 4 tot 5 jaar.

De les uit dit voorbeeld: bij een klein systeem met een hoog verbruik is de batterij vrijwel altijd volledig benut, waardoor het rendement per kWh capaciteit hoger uitvalt dan bij een grote batterij die maar deels wordt gebruikt.

## Veelgemaakte fouten in het rekenmodel

1. **Spreads te conservatief of te optimistisch inschatten.** Modellen rekenen vaak met een vaste gemiddelde spread. Kijk in de EPEX- of ENTSO-E-historie van je eigen jaar hoe de top-bottom spread zich werkelijk gedroeg en reken met een bandbreedte, niet met één getal.
2. **Cycle-degradatie negeren.** Fabrikanten geven voor LiFePO4 doorgaans 6.000 tot 10.000 cycli tot 70-80% restcapaciteit. Neem het degradatiepad uit het datasheet mee in je NPV-berekening.
3. **Energiebelasting vergeten.** Op importzijde betaal je energiebelasting per kWh, op exportzijde krijg je die niet terug. Spreads moeten dus na belasting worden gerekend.
4. **Maandfee niet opnemen.** Een fee van €5,99 per maand is €72 per jaar en drukt de nettowinst.
5. **Vermogen-cap negeren.** Een 5 kWh batterij met 2,5 kW omvormer laadt in één uur maximaal 2,5 kWh. Korte prijs-dips kun je daarmee niet volledig benutten.

## Wanneer arbitrage niet rendabel is

Heb je een vast contract zonder switchmogelijkheid de komende 18 maanden? Dan start je rekenmodel pas bij het einde van dat contract — dat schuift de terugverdientijd met dezelfde periode op.

Woon je in een gebied met netcongestie en afspraken over curtailment? Dan kan je batterij niet vrij terugleveren en vallen de arbitrage-inkomsten lager uit; hoeveel precies, hangt af van de voorwaarden van je netbeheerder.

## Extra FAQ

**Welke API gebruik ik voor live EPEX-prijzen?**
ENTSO-E (gratis, met vertraging) of de Tibber GraphQL-API (gratis voor klanten, dag-vooruitprijzen). Voor automatisering werken EVCC of Home Assistant met een prijs-integratie het soepelst.

**Hoe vaak moet ik mijn rekenmodel updaten?**
Minimaal elk half jaar. EPEX-prijzen schommelen seizoensgebonden en een andere gemiddelde spread verandert de rendementsberekening aanzienlijk.

---

*Dit artikel is voor het laatst bijgewerkt op 2026-08-19 door de redactie. Klopt er iets niet? Laat het ons weten — wij houden dit artikel actief bij.*

---

**Externe bron:** [RVO — ISDE voor woningeigenaren](https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren) — het officiële overzicht van wat de ISDE wel en niet dekt (thuisbatterijen vallen er niet onder).
