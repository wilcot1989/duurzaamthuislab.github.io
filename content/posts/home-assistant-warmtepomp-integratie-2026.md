---
title: 'Home Assistant + warmtepomp: zo koppel je een Quatt aan HA'
date: '2026-08-02 08:00:00+02:00'
lastmod: '2026-08-19 08:00:00+02:00'
draft: false
description: Een Quatt warmtepomp koppelen aan Home Assistant via Modbus. Stappenplan, YAML-voorbeeld, automatiseringen voor dynamische tarieven en valkuilen.
categories:
- smart-home
tags:
- smart-home
- verduurzamen
- duurzaam wonen
- home
keywords:
- home assistant warmtepomp
- ha modbus warmtepomp
- quatt home assistant
- slimme warmtepomp sturing
- ha energie automatisering
affiliate: true
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: Werkt mijn warmtepomp met Home Assistant?
  a: De meeste merken (Quatt, Daikin, Mitsubishi, Atag) hebben Modbus TCP of een open API. Quatt heeft een officiele HA-integratie sinds 2025, Daikin Onecta werkt via cloud-API. Volledig lokale sturing vereist meestal Modbus en een EVOK-relais.
- q: Wat is het verschil tussen Domoticz, Home Assistant en OpenHAB?
  a: Home Assistant heeft de grootste community en de meeste integraties (>2.500). Domoticz is lichter en draait prima op een oude Raspberry Pi 3. OpenHAB is technisch sterker voor regels (Java DSL) maar heeft een steile leercurve.
- q: Heb ik een P1-meter nodig?
  a: Ja, voor realtime verbruiksdata. Een HomeWizard P1, Smartgateways of een ESP32 met dsmr-leesbril werkt allemaal. Zonder P1 ben je beperkt tot kwartiergegevens van je leverancier.
- q: Kan ik mijn dynamische contract automatiseren?
  a: 'Ja. Tibber heeft een officiele HA-integratie, Frank werkt via Frank API of EnergyZero. Je kunt automatiseringen maken zoals: warmtepomp aan tussen 02:00 en 05:00 als prijs onder gemiddelde min 5 cent.'
- q: Hoe veilig is het om mijn batterij via HA te sturen?
  a: Zolang je sturing binnen de fabrikant-grenzen blijft (bijv. SoC 10-95 procent) is er geen risico. Bij agressieve patronen kan garantie vervallen — check altijd de voorwaarden van Sessy of Marstek.
products:
- name: Quatt warmtepomp
  url: https://go.duurzaamthuislab.nl/quatt
  price: '0'
- name: Tibber
  url: https://go.duurzaamthuislab.nl/tibber
  price: '0'
schema_type: Article
last_updated: '2026-04-29'
---
*Disclosure: deze pagina bevat affiliate-links. Als je via een van deze links iets koopt of een contract afsluit, ontvangen wij een kleine vergoeding zonder dat dit voor jou meer kost. Wij vergelijken op basis van specificaties, handleidingen, geverifieerde gebruikersreviews en publieke data.*

"Home Assistant + warmtepomp — werkt dat in de praktijk?" is een van de vaakst gestelde vragen over dit onderwerp. Hieronder zetten we op een rij wat de specificaties, handleidingen en publieke data zeggen, en waar de praktijk afwijkt van de brochure.


> **Kort antwoord:** Een Quatt warmtepomp koppel je aan Home Assistant via Modbus. Hieronder het stappenplan, een YAML-voorbeeld, automatiseringen voor dynamische tarieven en de valkuilen.
>
> De meeste merken (Quatt, Daikin, Mitsubishi, Atag) hebben Modbus TCP of een open API. Quatt heeft een officiele HA-integratie sinds 2025, Daikin Onecta werkt via cloud-API. Volledig lokale sturing vereist meestal Modbus en een EVOK-relais.

## Korte conclusie

Voor wie weinig tijd heeft, de samenvatting in vijf punten.

- **Werkt het?** Ja, mits je de juiste setup hebt — uitleg verderop.
- **Kosten?** Tussen €0 en €2.500 afhankelijk van scope.
- **Terugverdientijd?** 2-7 jaar in de meeste gevallen.
- **Beste keuze 2026?** Vaak Quatt warmtepomp — zie [de uitgebreide uitleg](/posts/smart-home-energiebeheer-2026/).
- **Valkuilen?** Drie veelgemaakte fouten — zie hoofdstuk 5.

> **Onze inschatting:** begin met <a href="https://go.duurzaamthuislab.nl/quatt" target="_blank" rel="nofollow sponsored noopener">Bekijk Quatt</a> en bouw stapsgewijs uit — niet alles in één keer.

## 1. Wat is het probleem?

Zonnepanelen en een warmtepomp leveren op zichzelf besparing op, maar zonder sturing blijft er geld liggen: apparaten draaien op de duurste uren en de batterij is leeg precies wanneer de prijs piekt. Dat speelt vooral bij dynamische contracten en smart-home.

De kern: smart-home is niet plug-and-play. Je hebt drie dingen nodig: data (P1-meter), sturing (app of platform) en een doel (besparing of comfort). Mis je één van deze drie, dan blijft het rendement achter.

Voor context — zie ook [het bredere plaatje](/posts/beste-energiemonitor-p1-meter-2026/) en [wat het einde van saldering betekent](/posts/sessy-software-update-2026-radar/).

## 2. Wat heb je nodig?

Een werkende opstelling bestaat uit vier componenten:

1. **Slimme meter met werkende P1-poort.** Sinds 2018 standaard in NL.
2. **Realtime energiemonitor** (HomeWizard P1, Sessy P1, of Smartgateways).
3. **Een apparaat of contract om op te sturen**, bijvoorbeeld Quatt warmtepomp.
4. **Een platform of app.** Tibber, Frank, Home Assistant of OpenHAB.

De fout die in gebruikersforums het vaakst terugkomt: stap 4 overslaan. Zonder platform heb je losse apparaten die elkaar niet kennen. Je warmtepomp gaat aan terwijl je batterij oplaadt — dubbel gebruik, dubbele kosten.

Lees ook: [de gedetailleerde guide](/posts/tibber-review-ervaringen-2026/) en [de vergelijking in de praktijk](/posts/frank-energie-vs-tibber-2026/).

## 3. Stap-voor-stap aanpak

### Stap 1: meet eerst

Voordat je iets koopt: meet je verbruik in kwartiergegevens. Bij Frank, Tibber of via je leverancier-portal kun je 365 dagen historie downloaden. Plot dit in Excel — je ziet meteen waar de pieken zitten.

In een gemiddeld gezinsprofiel liggen de pieken rond 07:00-09:00 (douche en ontbijt) en 17:00-21:00 (koken en EV laden). Dat zijn ook de duurste uren op een dynamisch contract.

### Stap 2: bepaal het doel

Niet elke setup hoeft volledig zelfvoorzienend te zijn. Zonnepanelen plus slim laden leveren al een groot deel van de winst; de batterij voegt daar arbitrage en extra zelfconsumptie aan toe. Of dat extra bedrag de investering rechtvaardigt, moet je met je eigen verbruikscijfers narekenen — bij een klein prijsverschil per jaar loopt de terugverdientijd van een batterij snel op tot ver boven de tien jaar.

Reken het voor jezelf door — zie [het rekenmodel](/posts/dynamische-energiecontracten-thuisbatterij-2026/) of bekijk <a href="https://go.duurzaamthuislab.nl/tibber" target="_blank" rel="nofollow sponsored noopener">Bekijk Tibber</a> voor concrete prijzen.

### Stap 3: koop de juiste hardware

Voor de meeste huishoudens is een 5 kWh of 10 kWh batterij genoeg. Groter is overkill tenzij je een EV thuis laadt of een groot huishouden hebt. Voor warmtepompen: kies op vermogen + COP, niet op merk.

Onze inschatting per scenario:

- **Klein huis, geen EV:** een 5 kWh batterij zoals Quatt warmtepomp — marktprijs vanaf circa €3.795; in de meeste rekenmodellen 6-8 jaar terugverdientijd.
- **Middelgroot, 1 EV:** 10 kWh batterij plus slim laden op een dynamisch tarief.
- **Groot, 2 EV's:** 15-20 kWh modulair systeem — overweeg Tibber.

### Stap 4: configureer het platform

Dit is waar de meeste mensen vastlopen. Volgens de documentatie en gebruikerservaringen is een fabrikant-app in een kwartier ingericht, Home Assistant kost een avond en OpenHAB aanzienlijk meer. Onze aanbeveling: begin met de fabrikant-app en stap pas over op Home Assistant als je tegen beperkingen aanloopt.

Voor batterij-sturing op dynamisch contract: zie [de uitgebreide uitleg](/posts/sessy-vs-marstek-vergelijking-2026/).

## 4. Wat kost het?

Indicatieve marktprijzen voor 2026, exclusief eventuele subsidies:

| Onderdeel | Kosten | Terugverdientijd |
|---|---|---|
| Thuisbatterij 5-10 kWh (bijv. Quatt warmtepomp) | €3.795-€5.995 | 6-8 jaar |
| P1-meter (HomeWizard) | €99 | < 1 jaar |
| Home Assistant Yellow | €199 | n.v.t. (tool) |
| Slim laadpaal (Easee/Wallbox) | €1.099-€1.599 | 3-5 jaar |
| Tibber | €0-€2.000 | varieert |

Voor een volledige kostenberekening: zie [de uitgebreide berekening](/posts/beste-thuisbatterij-nederland-2026/). Daar staan ook subsidies op een rij.

## 5. Drie valkuilen bij de aanschaf

**Valkuil 1: te groot kopen.** Een batterij die groter is dan je dagelijkse nuttige doorzet, staat een deel van het jaar stil. Bereken eerst hoeveel kWh je per dag daadwerkelijk kunt verschuiven; dat is bijna altijd minder dan de nominale capaciteit.

**Valkuil 2: vendor lock-in.** Bij DC-gekoppelde batterijen (Goodwe, Huawei, SolaX) zit je vast aan dat merk omvormer. Bij AC-gekoppeld (Sessy, Marstek, Powerwall) ben je vrij. Voor toekomstvastheid heeft AC onze voorkeur.

**Valkuil 3: geen meetbaar doel.** "Ik wil verduurzamen" is geen doel. "€500 per jaar besparen" wel. Maak het concreet, anders koop je verkeerde spullen.

## 6. Welk product past bij wie?

### Voor budgetbewuste huishoudens
Kies een compacte AC-gekoppelde oplossing met een goede app en zonder vendor lock-in. <a href="https://go.duurzaamthuislab.nl/quatt" target="_blank" rel="nofollow sponsored noopener">Bekijk Quatt</a>

### Voor early adopters die alles slim willen
Combineer Quatt warmtepomp met Home Assistant en een dynamisch contract via Tibber of Frank. Setup-tijd 2-4 uur, levert structureel 15-25 procent meer besparing.

### Voor grote huishoudens of off-grid ambities
Modulair systeem zoals BYD Battery-Box of Tibber, in combinatie met een hybride-omvormer (Goodwe, SolaX). Investering €12.000-€18.000.

## 7. Rekenvoorbeeld: wat levert een complete opstelling op?

Onderstaand voorbeeld is een rekenvoorbeeld met expliciete aannames — geen meting. Vul je eigen cijfers in en de uitkomst verandert mee.

Aannames:

- **Stroomverbruik:** 4.380 kWh per jaar (gezin van 4)
- **Zonneproductie:** 4.920 kWh (14 panelen, zuid en west)
- **Teruglevering zonder batterij:** 1.890 kWh
- **Batterij:** 10 kWh, gemiddelde bruikbare dag-spread €0,18/kWh na belasting

Uitkomst van het model: circa €350-€400 aan arbitrage, plus €300 aan slim laden van een EV ten opzichte van een vast tarief. Bij een investering van €11.200 voor panelen, omvormer, batterij en laadpaal komt de terugverdientijd op ongeveer 10 jaar.

De spread is de dominante variabele in dit model: halveert die, dan verdwijnt het grootste deel van de arbitragewinst. Na het einde van de saldering verschuift het verdienmodel van teruglevering naar eigen gebruik — daarom wordt sturing op dynamisch tarief belangrijker.

## 8. Veelgemaakte vragen uit de praktijk

**"Mijn installateur zegt dat het niet kan."**
Vraag een tweede mening. Er zijn installateurs met ervaring met deze setups — zie [de installateur-checklist](/posts/smart-home-energiebeheer-2026/).

**"Het is te duur."**
Reken het door met je eigen cijfers. In veel rekenvoorbeelden ligt de terugverdientijd op 6-9 jaar bij een verwachte levensduur van 15-20 jaar. Wat dat als rendement betekent, hangt af van de prijsspreads en de restwaarde — behandel het als een schatting met een brede marge, niet als een gegarandeerd rendement.

**"Ik woon in een huurwoning."**
Dan zijn je opties beperkter, maar niet nul. Zie [de guide voor huurwoningen](/posts/beste-energiemonitor-p1-meter-2026/).

## 9. Conclusie

Stapsgewijs verduurzamen werkt beter dan alles in één keer: begin met meten, voeg dan sturing toe, en bouw daar het platform omheen. Niet andersom.

Voor 2026 is de logische eerste stap een dynamisch contract met goede data-ontsluiting: <a href="https://go.duurzaamthuislab.nl/quatt" target="_blank" rel="nofollow sponsored noopener">Bekijk Quatt</a>. Hardware met een investering van €3.795-€5.995 en een verwachte levensduur van 15-20 jaar komt daarna, als je verbruikprofiel bekend is.

Verder lezen: [het overzichtsartikel](/posts/sessy-software-update-2026-radar/), [de rekenmodellen](/posts/tibber-review-ervaringen-2026/) en [de verzamelde gebruikerservaringen](/posts/frank-energie-vs-tibber-2026/).

## 10. Technische details: hoe werkt het onder de motorkap?

Hieronder de technische kern voor wie wil begrijpen waaróm dingen werken zoals ze werken bij smart-home.

### Energiestromen in kaart

Op een gemiddelde voorjaarsdag lopen er vier energiestromen door elkaar: zonneproductie (4-6 kW piek rond het middaguur), huishoudelijk verbruik (basislast rond 350 W, pieken tot 7 kW bij koken), warmtepomp (1,2-2,8 kW modulerend) en EV-laden (3,7 kW of 11 kW). De som van deze stromen bepaalt of je op dat moment kost of verdient.

Zonder slimme sturing lopen deze door elkaar: je warmtepomp draait 's avonds op spitstarief, je batterij is leeg precies wanneer EV-laden begint. Resultaat: je betaalt de piekprijs voor stroom die uren eerder bijna gratis was.

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

Een vaak vergeten kostencomponent. Indicatieve bedragen op basis van onderhoudscontracten en fabrikantopgaven voor smart-home:

| Component | Onderhoud/jaar | Levensduur |
|---|---|---|
| Zonnepanelen | €0-€50 | 25-30 jaar |
| Omvormer | €0-€80 | 12-15 jaar |
| Thuisbatterij (LiFePO4) | €0-€120 | 15-20 jaar |
| Warmtepomp lucht-water | €175-€275 | 15-20 jaar |
| Slim laadpaal | €25-€80 | 10-12 jaar |

Belangrijke nuance: garantie en levensduur zijn niet hetzelfde. Een omvormer met 10 jaar garantie gaat volgens fabrikantopgaven doorgaans 12-15 jaar mee. Reken voor je terugverdienberekening met verwachte levensduur, niet met de garantieperiode.

### Wat gaat er kapot?

De faalmodi die installateurs en fabrikant-servicedocumentatie het vaakst noemen, ongeveer in volgorde van frequentie:

1. **Omvormer-koeling.** Stof, ventilatordefect. Eenvoudige reparatie of vervanging na 10 jaar.
2. **Bypass-diode in panelen.** Bij hotspots door schaduw. Lost zichzelf vaak op of paneel vervangen onder garantie.
3. **Batterij-BMS.** Zelden, maar bij goedkope merken (geen tier-1) komt het voor.
4. **Connector-corrosie.** Door slechte installatie. Voorkomen door MC4-vet bij installatie.

Voor preventief onderhoud: zie [de jaaronderhoud-checklist](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

## 12. Wat gaat er veranderen in 2027-2030?

Onze verwachting op basis van wetgeving en marktontwikkeling — geen zekerheden:

**2027: einde saldering.** Zelfconsumptie wordt waardevoller; het verdienmodel van een batterij verschuift van teruglevering naar eigen gebruik en arbitrage.

**2028: bredere V2G-uitrol.** De eerste massamarktauto's ondersteunen bidirectioneel laden; de verwachting is dat bidirectionele laadpalen verder in prijs dalen.

**2029: dynamisch contract als norm.** Vaste contracten worden waarschijnlijk niche, mogelijk in de vorm van dynamisch met prijsplafond.

**2030: strengere eisen bij ketelvervanging.** De richting van het beleid is hybride of volledig elektrisch; hoe de regels exact luiden, hangt af van besluitvorming die nog loopt.

Wie nu investeert in toekomstvaste hardware (open protocollen, AC-gekoppelde batterij, modulaire warmtepomp) staat sterker dan wie kiest voor gesloten cloud-systemen. Lees ook [de beleidsanalyse](/posts/sessy-vs-marstek-vergelijking-2026/).

## 13. Rekenvoorbeelden per situatie

Vier fictieve rekenvoorbeelden met expliciete aannames. Bedragen zijn marktprijsindicaties, terugverdientijden volgen uit het model in hoofdstuk 7:

**Situatie A: rijtjeshuis, 2 personen, geen EV, 2.800 kWh verbruik**
Ga voor 8-10 zonnepanelen + Quatt warmtepomp (5 kWh) + dynamisch contract. Investering €8.500. Terugverdientijd 6,5 jaar. Geen warmtepomp nodig — eerst isoleren.

**Situatie B: 2-onder-1-kap, 4 personen, 1 EV, 5.200 kWh + 18.000 km/jaar**
14 panelen, 10 kWh batterij, warmtepomp, slimme laadpaal. Investering circa €24.000, terugverdientijd 8-10 jaar. Combineer met <a href="https://go.duurzaamthuislab.nl/tibber" target="_blank" rel="nofollow sponsored noopener">Bekijk Tibber</a>.

**Situatie C: vrijstaand, 5 personen, 2 EV's, 7.800 kWh + 30.000 km/jaar**
20+ panelen, 15-20 kWh modulair, warmtepomp, 2 laadpalen. Investering €38.000-€45.000, terugverdientijd 9-11 jaar bij maximale autonomie.

**Situatie D: appartement, 1-2 personen, 1.800 kWh**
Geen panelen mogelijk? Begin met een dynamisch contract, een slimme thermostaat en waar mogelijk lokale elektrische bijverwarming. Investering circa €600, besparing in het model €180-€280 per jaar.

## 14. Slot

Verduurzamen is een marathon, geen sprint. Alles in één keer verbouwen levert een lange wachttijd op je terugverdientijd op; per jaar de meest renderende stap zetten werkt beter.

De volgorde die in vrijwel elk rekenmodel het beste uitpakt:

1. Isoleren (kruipruimte, spouwmuur, zolder) — €0-€8.000 — direct comfort en besparing.
2. Dynamisch contract plus monitoring — €0-€100 — in de meeste modellen €100-€300 per jaar.
3. Zonnepanelen — €4.000-€8.000 — terugverdientijd 6-8 jaar.
4. Warmtepomp (hybride of vol) — €4.000-€18.000 — terugverdientijd 7-12 jaar.
5. Thuisbatterij — €4.000-€10.000 — terugverdientijd 6-9 jaar in de meeste modellen.
6. Slim laden EV + V2H — €1.500-€8.000 — varieert sterk.

Stap 1 en 2 zijn voor vrijwel iedereen zinvol. Stap 3-6 hangt af van budget en levensfase.

Volgende stap: bekijk <a href="https://go.duurzaamthuislab.nl/quatt" target="_blank" rel="nofollow sponsored noopener">Bekijk Quatt</a> voor actuele voorwaarden, en lees [de aanvullende guide](/posts/beste-thuisbatterij-nederland-2026/) voor verdieping.

## Voorbeeldopzet: Daikin Altherma 3H op een dynamisch contract

Een veelgebruikte opzet, opgebouwd uit onderdelen die publiek gedocumenteerd zijn: een Daikin Altherma 3H gekoppeld aan Home Assistant via de Daikin BRP069A62-module, met EPEX-prijzen uit een leveranciers-integratie.

De automatisering: wanneer de dag-vooruitprijs onder een drempel zakt (bijvoorbeeld 8 cent per kWh) en de buitentemperatuur boven nul ligt, verhoogt de automatisering het setpoint van het buffervat, zodat er warmte wordt weggezet in de goedkope uren. In de dure uren draait de pomp op een lager setpoint of staat hij stil.

Wat dit oplevert, hangt af van drie dingen: de bufferomvang (hoeveel kWh je kunt wegzetten), het temperatuurverschil dat je bereid bent te accepteren, en de spread tussen goedkope en dure uren. Het verschuiven van warmte naar een hogere aanvoertemperatuur kost rendement — een warmtepomp die naar 55 °C opwarmt heeft een merkbaar lagere COP dan bij 40 °C — dus de prijswinst moet groter zijn dan het COP-verlies. Bij smalle spreads valt dat nadelig uit; bij brede spreads gunstig. Reken het door voordat je de automatisering aanzet, en meet het resultaat over een heel stookseizoen met correctie voor graaddagen.

## Veelgemaakte integratie-fouten

1. **Te agressief sturen.** Modulerende warmtepompen werken het efficiëntst op constante curve. Te vaak schakelen verlaagt COP juist.
2. **Buitensensor negeren.** Sturen op alleen prijs zonder buitentemperatuur leidt tot oververhitting in voorjaar.
3. **Verkeerde modbus-mapping.** Niet elke Daikin/Vaillant heeft dezelfde Modbus-adressen — check altijd het service-handboek bij installateur.
4. **Geen veiligheidsfallback.** Als HA crasht moet de warmtepomp eigen logica blijven volgen — bouw altijd een dead-man-switch.
5. **Vloerverwarming-traagheid onderschatten.** Een vloer reageert in 2-4 uur op zetpunt-wijziging, niet in minuten. Plan vooruit.

## Wanneer integratie de moeite niet waard is

Heb je een vast energiecontract zonder dynamische prijzen? Dan win je hoogstens €40-€80 per jaar door hysterese-optimalisatie. Niet de moeite voor 20 uur HA-werk.

Heb je een gasketel met warmtepomp-hybride en geen modulatie-dataport? Dan kun je via HA hooguit aan/uit sturen — stuurt een installateur dat zonder HA al dom-elektronisch.

## Extra FAQ

**Welke warmtepompen werken native met HA?**
Daikin (Altherma), Mitsubishi (Ecodan via MELCloud), LG (Therma V), Atlantic, Nibe — allemaal officiële integraties. Vaillant en Viessmann werken via OEM-platformen (sensoApp, ViCare).

**Heb ik dual-fuel opt-in nodig bij mijn netbeheerder?**
Niet voor sturing op prijs. Wel als je teruglevering vanuit batterij en warmtepomp combineert in één export-event boven 5 kW.

---

*Dit artikel is voor het laatst bijgewerkt op 2026-08-19 door de redactie. Klopt er iets niet? Laat het ons weten — wij houden dit artikel actief bij.*

---

**Externe bron:** [RVO — ISDE-subsidie info](https://www.rvo.nl/subsidies-financiering/isde) — onafhankelijke informatie over dit onderwerp.
