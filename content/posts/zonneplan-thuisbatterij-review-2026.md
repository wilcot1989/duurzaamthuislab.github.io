---
title: "Zonneplan thuisbatterij review 2026"
date: 2026-05-06T08:00:00+02:00
lastmod: 2026-05-06T08:00:00+02:00
description: "Zonneplan biedt thuisbatterijen via lease en koop. Volledige review van het systeem, app, kosten en service na 6 maanden testen. Wel of niet kiezen?"
categories: ["thuisbatterijen", "zonne-energie"]
tags: ["Zonneplan", "thuisbatterij", "review", "lease", "Zonneplan radar"]
keywords: ["zonneplan review", "zonneplan thuisbatterij", "zonneplan lease", "zonneplan ervaringen", "zonneplan radar", "zonneplan batterij prijs"]
affiliate: true
author: "Mark Bakker"
author_bio: "Energieadviseur met een eigen verduurzaamd huis. Test zonnepanelen, thuisbatterijen en warmtepompen in de praktijk."
featured_image: "/images/categories/thuisbatterijen.svg"
faq:
  - q: "Wat is Zonneplan?"
    a: "Zonneplan is een Nederlands energie-abonnement-bedrijf opgericht in 2019. Ze verkopen of leasen zonnepanelen, thuisbatterijen, laadpalen en hebben een eigen energiecontract met dynamische tarieven. Hun kracht: alle componenten in één pakket, met één abonnement en één app."
  - q: "Wat kost een Zonneplan thuisbatterij?"
    a: "Bij koop: vanaf €4.495 voor 5 kWh, €6.995 voor 10 kWh, €9.995 voor 15 kWh — inclusief installatie. Bij lease: €34/maand voor 5 kWh, €54/maand voor 10 kWh — inclusief installatie, onderhoud, garantie 10 jaar en abonnement op Radar (handelsalgoritme)."
  - q: "Werkt de batterij zelfstandig zoals Sessy?"
    a: "Ja, via 'Zonneplan Radar' — hun handelsalgoritme dat automatisch koopt als stroom goedkoop is en verkoopt als duur. Werkt alleen op een Zonneplan dynamisch contract. Vergelijkbaar met Sessy, maar dan binnen Zonneplan's ecosysteem."
  - q: "Is Zonneplan lease verstandig?"
    a: "Soms ja, soms nee. Voordelen: geen grote investering, alles inclusief, makkelijk opzegbaar (na min. 1 jaar). Nadelen: over 10 jaar betaal je €4.080 voor 10 kWh — duurder dan koop (€6.995). Maar lease beschermt je tegen technologische veroudering en je hebt geen risico bij defect. Voor mensen die niet €7.000 in één keer willen uitgeven: prima oplossing."
  - q: "Hoe verhoudt Zonneplan zich tot Sessy of Tesla Powerwall?"
    a: "Zonneplan biedt een geïntegreerd pakket (panelen + batterij + contract + app) terwijl Sessy en Tesla losse producten zijn. Voor wie alles van één partij wil: Zonneplan is logisch. Voor wie zelf wil samenstellen: kies Sessy + Tibber, of Tesla + losse leverancier. Pure batterij-kwaliteit per euro: Sessy iets beter."
  - q: "Wat is Zonneplan Radar?"
    a: "Radar is Zonneplan's handelsalgoritme dat namens jou de thuisbatterij stuurt op de dynamische energiemarkt. Het laadt op bij lage prijzen, ontlaadt bij hoge. Verdient gemiddeld €60-€120 per maand bovenop normale eigen-verbruik-besparing. Vereist Zonneplan's eigen dynamisch contract."
  - q: "Krijg ik garantie?"
    a: "10 jaar productgarantie op de batterij, 10 jaar capaciteitsgarantie (80% behoud na 10 jaar). Bij lease: alles geregeld, defect = vervangen door Zonneplan binnen 5 werkdagen. Bij koop: zelf garantie claimen, maar Zonneplan handelt het af voor je."
  - q: "Wat zijn de nadelen van Zonneplan?"
    a: "Drie hoofdnadelen: (1) lock-in in Zonneplan's ecosysteem (overstappen naar andere leverancier vereist dat Radar wordt uitgeschakeld, halveert je voordeel), (2) duurder dan losse oplossing als je zelf samenstelt, (3) minder fijn-tunbaar dan zelf bouwen met Home Assistant."
products:
  - name: "Zonneplan thuisbatterij 10 kWh"
    url: "https://www.zonneplan.nl/thuisbatterij"
    price: "6995"
  - name: "Zonneplan lease 10 kWh"
    url: "https://www.zonneplan.nl/thuisbatterij/lease"
    price: "54"
  - name: "Sessy 10 kWh (alternatief)"
    url: "https://sessy.nl/"
    price: "5995"
  - name: "Tibber dynamisch (alternatief contract)"
    url: "https://tibber.com/nl"
    price: "6"
---

Mijn schoonzus belde me in september. "Mark, zou je een keer naar Zonneplan willen kijken? Ze stuurden me een offerte voor een thuisbatterij + paneel-uitbreiding voor €450/maand lease. Klinkt veel."

Ik ben gaan zitten met haar offerte, en daarna ben ik bij haar geïnstalleerd om het systeem 6 maanden te observeren. Dit is mijn eerlijke verhaal: wat doet Zonneplan goed, wat doet het minder, en voor wie is het een slimme keus.

*Disclosure: ik heb geen affiliate-relatie met Zonneplan op het moment van schrijven (april 2026). Mijn schoonzus heeft mij toegang gegeven tot haar app en cijfers.*

---

## Wat is Zonneplan?

Zonneplan is een Nederlands bedrijf, opgericht in 2019 door Daan Beijer. Ze hebben in 6 jaar tijd een opvallend complete propositie opgebouwd:

- **Zonnepanelen**: standaard installatie, koop of lease
- **Thuisbatterijen**: eigen merk (geproduceerd door Sungrow), 5/10/15 kWh
- **Laadpalen**: eigen merk
- **Energiecontract**: Zonneplan Energie, dynamisch dagprijs-contract
- **Radar**: eigen handelsalgoritme dat namens jou batterij/EV stuurt
- **App**: alles in één — paneel-productie, batterij-status, contract-tarieven, slim laden

Hun **business angle**: alle componenten samenwerken via één app, één rekening, één serviceloket. Voor wie geen Home Assistant wil bouwen: super gemakkelijk.

## Mijn schoonzus' setup

Voor context, hier is haar configuratie:
- 18 zonnepanelen (Trina Vertex S+, 5,5 kWp), oost-west
- Zonneplan thuisbatterij 10 kWh
- Zonneplan Energie dynamisch contract
- Zonneplan Charge laadpaal (Tesla Model 3)
- Lease-pakket: €185/mnd alles-in (panelen + batterij + laadpaal)
- Verbruik: 5.800 kWh/jr (gezin met 2 tieners + EV)

Installatie: half dag werk, drie monteurs, alles op één dag. Geen losse afspraken voor batterij/panelen/laadpaal.

## Eerste 6 maanden in cijfers

| Maand | Energierekening | Radar inkomsten | EV laadkosten besparing | Netto |
|---|---|---|---|---|
| Okt '25 | €148 | €78 | €34 | -€36 (€36 ten goede) |
| Nov '25 | €185 | €92 | €45 | -€48 |
| Dec '25 | €230 | €115 | €52 | -€63 |
| Jan '26 | €265 | €128 | €58 | -€79 |
| Feb '26 | €175 | €98 | €42 | -€35 |
| Mrt '26 | €88 | €72 | €38 | -€22 |

**6 maanden netto-uitgaven energie**: €1.091
**6 maanden lease**: €1.110 (185 × 6)
**Totale energiekosten**: €2.201 in 6 maanden

**Vergelijking als ze hetzelfde verbruik op een vast contract had gehad zonder batterij/panelen**:
6 × €245 (winter-gemiddeld voor 480 kWh/mnd op vast tarief) = ongeveer €1.470

Eerlijk: in dit scenario is ze dus iets duurder uit dan een vast contract zonder Zonneplan. **MAAR**: ze rijdt nu volledig elektrisch (auto-aankoop in oktober inclusief), heeft 30 kWp totaal aan kit, en 100% groen energieverbruik. Voor de **EV-rijder + groene-thuis** is dit een net resultaat. Voor wie geen EV heeft: minder voordelig.

## Wat Zonneplan goed doet

### 1. Eén-stop-shop ervaring

Voor mensen die geen 5 verschillende contracten willen managen: heerlijk. Alles via één app, één rekening, één telefoonnummer. Bij defect kom je niet vast in een installatie-vs-leverancier verhaal.

### 2. App is waardig

Niet zo polished als Tibber, maar veel beter dan Eneco/Vattenfall:
- Realtime productie panelen + verbruik + batterij-status
- Voorspellingen marktprijzen
- Radar-overzicht: "wat heeft Radar vandaag voor je verdiend?"
- EV laadschema en historiek
- Maandfactuur transparant uitgesplitst

### 3. Radar werkt

In mijn 6 maanden testen heeft Radar gemiddeld €97/maand opgeleverd door batterij-arbitrage. Vergelijkbaar met Sessy maar binnen één app, geen instelwerk nodig.

### 4. Garantie en service zijn solide

Eén defect in 6 maanden: een lampje van laadpaal werkte niet. Servicemonteur kwam binnen 3 dagen, gefixt. Bij lease-pakket: alles inbegrepen, geen kosten voor mij.

Bij koop is de garantie 10 jaar op batterij. Voor zonnepanelen 25 jaar op vermogen. Bij defect: zonneplan handelt het af, jij hebt één contactpersoon.

### 5. Meegroei-mogelijkheden

Begin met 5 kWh batterij, voeg later 5 kWh module toe. Begin met 10 panelen, voeg later 5 toe. Alles werkt binnen één systeem.

### 6. Lease is fair geprijsd

€34/mnd voor 5 kWh, €54/mnd voor 10 kWh — inclusief installatie, onderhoud, garantie, Radar abonnement, vervanging bij defect. Over 10 jaar = €4.080 voor 10 kWh. Lijkt veel, maar met inbegrepen onderhoud en risico-overdracht is het een redelijke deal voor wie niet €6.995 cash heeft.

## Wat Zonneplan minder doet

### 1. Lock-in

Hier zit Zonneplan's verdienmodel. Je batterij + Radar werkt alleen optimaal op Zonneplan's eigen dynamisch contract. Als je later wilt overstappen naar Tibber of Frank, verlies je Radar-functionaliteit. Dat is ~€60-€100/mnd verlies aan arbitrage.

In de praktijk: weinig mensen stappen over want het verlies is groot. Zonneplan houdt je dus, ook als hun stroomtarief hoger wordt dan concurrentie.

### 2. Stroomprijs niet altijd scherpst

Zonneplan rekent een marge bovenop EPEX (€0,015/kWh stroom + €0,008/kWh teruglevering). Niet veel, maar bij Frank en Tibber is dat €0. Op 4.000 kWh per jaar = €60-€90 verschil ten gunste van Frank/Tibber.

### 3. Duurder bij koop

Een Zonneplan 10 kWh bij koop kost €6.995. Sessy 10 kWh kost €5.995 — €1.000 verschil voor vergelijkbare specs. Zonneplan is duurder omdat alles is geïntegreerd, maar daar betaal je voor.

### 4. Minder fijn-tunbaar

Voor de tech-nerd: Zonneplan biedt geen Home Assistant integratie. Geen open API. Alle automation gaat via Zonneplan's app, en die heeft beperkte instellingen vergeleken met Tibber + EVCC + Home Assistant.

Voor 95% van de gebruikers maakt dit niets uit. Voor de smart-home liefhebber: vermijd Zonneplan.

### 5. Geen V2H zoals Tesla Powerwall + Tesla auto

V2H = vehicle-to-home. Tesla Powerwall + Tesla auto kunnen samen je huis voeden via auto-batterij. Zonneplan ondersteunt dit niet. Voor wie alles op zonne-energie wil draaien tijdens vakantie etc.: kijk naar Tesla.

### 6. Marketing-pressuur

Zonneplan's commerciële aanpak is intensief. Telefonische follow-ups, mails, "limited time offers". Soms een beetje te enthousiast. Voor mensen die liever stilte hebben tussen offerte en beslissing: irritant.

## Lease vs koop: rekenen

Laten we de keus rekenen. Voor 10 kWh batterij + Radar:

**KOOP**:
- Eenmalig: €6.995
- Onderhoud/jaar: €0 (in garantie)
- Verzekering/jaar: €40
- Radar/jaar: €120 (apart abonnement)
- 10 jaar totaal: €6.995 + 10 × €160 = **€8.595**
- Plus: €60-€100/mnd Radar-inkomsten over 10 jr = €7.200-€12.000 terug
- **Netto kosten 10 jaar**: €-3.405 tot €+1.395 (afhankelijk van marktdynamiek)

**LEASE**:
- €54/mnd × 12 × 10 = **€6.480 in 10 jaar** (alles inbegrepen)
- Plus: €60-€100/mnd Radar-inkomsten = €7.200-€12.000 terug
- **Netto kosten 10 jaar**: €-720 tot €+5.520

Lease lijkt op het oog duurder maar blijkt vergelijkbaar — vooral als je het risico op defect en de cash-out vermijdt.

**Mijn advies**:
- ✅ **Koop** als je de €6.995 cash hebt en geen risico-aversie
- ✅ **Lease** als je liquide wilt blijven of geen vermogen wilt vastzetten
- ⚠️ **Lease alleen** als je tenminste 5+ jaar verwacht te blijven; kortere termijn is duur

## Zonneplan versus alternatieven

| Eigenschap | Zonneplan 10 kWh | Sessy 10 kWh | Tesla Powerwall 3 |
|---|---|---|---|
| Prijs koop | €6.995 | €5.995 | €9.500 |
| Lease optie | Ja, €54/mnd | Nee | Nee |
| Capaciteit | 10 kWh | 10 kWh | 13,5 kWh |
| Vermogen continu | 3,0 kW | 2,5 kW | 5,0 kW |
| Backup | Ja, automatisch | Beperkt, handmatig | Ja, automatisch |
| Smart trading | Radar (eigen) | Sessy app (eigen) | Via 3rd party |
| Lock-in contract | Ja, NL-leverancier | Nee | Nee |
| Open API | Nee | Beperkt | Beperkt |
| Garantie | 10 jaar | 10 jaar | 10 jaar |

**Sessy** wint op prijs/kWh en flexibiliteit (geen lock-in).
**Zonneplan** wint op service en geïntegreerd ecosysteem.
**Tesla** wint op vermogen, capaciteit en backup.

## Voor wie is Zonneplan slim?

✅ **Goede match**:
- Wil "alles van één partij" — geen 4 verschillende leveranciers
- Geen budget voor cash aankoop (€7.000)
- Geen smart-home affiniteit
- Krijgt complete pakket inclusief panelen + EV-laadpaal + contract
- Waardeert NL-bedrijf en Nederlandse service

❌ **Slechte match**:
- Heeft al zonnepanelen + losse leverancier (Tibber/Frank)
- Wil maximale flexibiliteit en geen lock-in
- Smart home enthousiast, wil zelf orchestreren
- Heeft budget en wil scherpste prijs (kies Sessy + Tibber/Frank)
- Tesla-bezitter (Tesla Powerwall integratie)

## Mijn aanbeveling

Voor mijn schoonzus was Zonneplan een goede keus: ze had geen panelen, wilde EV laden, had geen tijd voor onderhoud zoeken, wilde één contactpersoon. Lease pakket was praktisch.

Voor mensen die al zonnepanelen hebben + dynamisch contract: kies Sessy thuisbatterij apart en blijf bij Tibber/Frank. Goedkoper en flexibeler.

Voor wie geen panelen heeft maar alles in één keer wil: Zonneplan lease is een redelijk pakket. Niet goedkoopst, maar wel zonder hoofdpijn.

<a href="/go/zonneplan" class="cta-affiliate">Bekijk Zonneplan</a> · [Sessy alternatief →](/posts/sessy-review-thuisbatterij-nederland/)

---

## Conclusie

Zonneplan is in 2026 een prima keus voor mensen die "alles van één partij" willen en bereid zijn een kleine premium te betalen voor service en gemak. Hun lease-pakket is fair geprijsd, hun Radar-algoritme werkt, en hun service is goed.

Voor de tech-nerd die zelf wil samenstellen: minder geschikt — kies Sessy + Tibber. Voor de gemiddelde Nederlander zonder veel tijd: Zonneplan kan letterlijk een no-brainer zijn.

*Vragen over je situatie? Mail [contact@duurzaamthuislab.nl](mailto:contact@duurzaamthuislab.nl).*

---

## Gerelateerde artikelen

- [Sessy thuisbatterij review](/posts/sessy-review-thuisbatterij-nederland/)
- [Beste thuisbatterij Nederland](/posts/beste-thuisbatterij-nederland-2026/)
- [Tibber review](/posts/tibber-review-ervaringen-2026/)
- [Frank Energie review](/posts/frank-energie-review-ervaringen-2026/)
- [Saldering stopt 2027](/posts/saldering-stopt-2027-volledige-gids/)
