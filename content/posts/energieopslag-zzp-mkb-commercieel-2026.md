---
title: 'Energieopslag voor zzp en mkb (2026): wanneer een zakelijke batterij rekenkundig uitkomt'
date: 2026-07-30 08:00:00+02:00
lastmod: '2026-08-21 08:00:00+02:00'
description: 'Zakelijke energieopslag doorgerekend: de drie business cases (zelfverbruik, arbitrage, piekafvlakking), wat EIA en KIA in 2026 werkelijk opleveren, en hoe je de omvang bepaalt op je eigen kwartierdata.'
draft: false
categories:
- thuisbatterijen
tags:
- ZZP
- MKB
- commercieel
- energieopslag
- EIA
keywords:
- energieopslag MKB
- thuisbatterij ZZP
- commerciële batterij
- batterij bedrijf
- EIA energieopslag
- batterij opslag onderneming
- industrial battery storage Nederland
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1518709268805-4e9042af2176&w=1200&output=webp&q=70
schema_type: Article
affiliate: false
faq:
- q: 'Is energieopslag rendabel voor zzp en mkb?'
  a: 'Vaker wel dan bij particulieren, om twee redenen: de energie-investeringsaftrek en de kleinschaligheidsinvesteringsaftrek verlagen de netto-investering, en zakelijke verbruikspatronen sluiten beter aan bij wat een batterij kan. In onze modelberekeningen op deze pagina komt de terugverdientijd uit tussen circa 3 en 7 jaar, maar dat zijn modellen: de uitkomst hangt volledig af van je eigen verbruiksprofiel, tarief en belastingpositie.'
- q: 'Wat is de EIA voor batterijopslag?'
  a: 'De energie-investeringsaftrek is in 2026 40% extra aftrek van de winst, bovenop de normale afschrijving. Voorwaarde is dat het bedrijfsmiddel op de Energielijst van RVO staat onder een geldige code, en dat je de investering binnen 3 maanden na de besteldatum aanmeldt bij RVO. Die termijn is fataal.'
- q: 'Welke batterij past bij een zakelijke toepassing?'
  a: 'Dat bepaalt de schaal, niet het merk. Tot enkele tientallen kWh werk je met modulaire systemen van het type dat ook in woningen wordt toegepast; daarboven kom je bij rack-opstellingen met een aparte omvormer- en EMS-laag; boven de honderden kWh bij containeropstellingen met netbeheerdersafstemming. Vraag altijd of het aangeboden systeem onder een geldige code op de Energielijst valt — dat bepaalt of de EIA van toepassing is.'
- q: 'Levert handelen op de spotmarkt iets op voor het mkb?'
  a: 'Alleen met een dynamisch contract en voldoende prijsspreiding. De opbrengst is het product van je bruikbare capaciteit, het aantal cycli per dag en het verschil tussen de goedkoopste en duurste uren, minus rendementsverlies en netkosten. Reken dat door op je eigen kwartierdata en op de prijshistorie van een heel jaar, niet op een gunstige week.'
- q: 'Hoe bepaal ik de juiste capaciteit?'
  a: 'Op je kwartierdata uit de slimme meter, over minimaal een paar representatieve weken. Kijk naar hoeveel kWh je per dag daadwerkelijk kunt verplaatsen — dus het overschot dat je nu terugleveert plus de afname in de dure uren. Een batterij die niet elke dag rondgaat, verdient zich niet terug.'
- q: 'Is netcongestie een reden om een batterij te overwegen?'
  a: 'Het kan een reden zijn, maar het is geen algemene regel. In gebieden met transportschaarste zijn nieuwe of zwaardere aansluitingen niet altijd op korte termijn beschikbaar, en bieden netbeheerders alternatieve contractvormen aan. Check de actuele capaciteitskaart van de netbeheerders en vraag je eigen netbeheerder wat er op jouw aansluitadres mogelijk is.'
---

*Disclosure: dit artikel bevat geen affiliate- of commissielinks. Genoemde merken en systemen zijn voorbeelden ter illustratie, geen aanbeveling en geen betaalde plaatsing.*

Voor een particulier is een thuisbatterij vooral een rekensom over saldering en zelfverbruik. Voor een onderneming ligt het anders: er is geen saldering te missen, de investering is fiscaal aftrekbaar, en het verbruikspatroon overdag sluit vaak beter aan bij wat een batterij kan. Dat maakt zakelijke opslag eerder rendabel — maar niet automatisch.

Dit artikel zet de drie business cases uit elkaar, geeft de fiscale bedragen zoals de Belastingdienst en RVO ze publiceren (opgehaald 21 augustus 2026), en laat met **modelberekeningen** zien waar de uitkomst op omslaat. Alle bedragen in de rekenvoorbeelden zijn aannames, geen weergave van bestaande klanten.

## Waarom de rekensom zakelijk anders loopt

| Aspect | Particulier | Zzp / mkb |
|---|---|---|
| Saldering | Stopt volledig per 1-1-2027 | Niet van toepassing op zakelijke aansluitingen |
| Btw op de batterij | 21%, niet terugvorderbaar | 21%, terug te vragen voor het zakelijke deel |
| EIA | Nee | Ja, 40% in 2026 — mits op de Energielijst |
| KIA | Nee | Ja, 28% binnen de schijf |
| Tariefstructuur | Leveringstarief + netbeheer vast | Vaak ook een vermogens- of capaciteitscomponent |
| Verbruikspiek | 's Avonds | Vaak overdag, synchroon met de zonproductie |

Die laatste rij snijdt twee kanten op: verbruik dat samenvalt met de zonproductie is goed nieuws voor je zelfverbruik, maar het betekent ook dat een batterij minder toe te voegen heeft dan bij een huishouden dat 's avonds piekt. Dat is precies waarom de omvang op eigen data bepaald moet worden.

## Drie business cases

### 1. Zelfverbruik verhogen bij eigen zonnepanelen

Je hebt panelen op de loods of het kantoor, en je levert midden op de dag terug tegen een lage vergoeding — vaak met terugleverkosten erbovenop. De batterij verschuift dat overschot naar de randen van de dag.

**Wanneer dit werkt:** als er daadwerkelijk een structureel overschot is dat 's avonds of de volgende ochtend verbruikt wordt. Bij een bedrijf dat in het weekend dicht is, staat de batterij twee van de zeven dagen stil — dat halveert het aantal cycli en dus het rendement.

### 2. Arbitrage op de dagmarkt

Met een dynamisch contract laad je in de goedkope uren en ontlaad je in de dure. De jaaropbrengst is grofweg:

> bruikbare capaciteit (kWh) × cycli per jaar × gemiddeld prijsverschil per kWh × retourrendement − netkosten over de geladen energie

De twee getallen waar dit op vastloopt zijn het **aantal cycli** (praktisch één tot twee per dag, en alleen op dagen dat het prijsverschil groot genoeg is) en het **prijsverschil**. Ter kalibratie: het EPEX-jaargemiddelde over 2025 lag op € 0,105/kWh, met 212 uren met een negatieve prijs en één uur van € 0,63 (20 januari 2025, 17:00). De spreiding is er dus, maar niet elke dag even groot. Reken door op een volledig jaar aan prijsdata, niet op een gunstige winterweek.

Vergeet in de sommen de **energiebelasting** niet: die bedraagt in 2026 € 0,09161 per kWh exclusief btw (€ 0,11085 inclusief) op elektriciteit en betaal je over wat je uit het net haalt om te laden.

### 3. Piekafvlakking

Bij een grootverbruikaansluiting betaal je niet alleen voor kWh maar ook voor **vermogen**: het gecontracteerde of gemeten transportvermogen in kW. Een batterij die tijdens korte pieken bijspringt, kan dat gecontracteerde vermogen omlaag brengen.

Dit is vaak de minst zichtbare en meest onderschatte post. De opbrengst hangt volledig af van je aansluitcategorie en de tarieven van jouw netbeheerder — die staan in de tarievenlijst van de netbeheerder en verschillen per regio. Vraag je netbeheerder wat een lager gecontracteerd vermogen concreet scheelt voordat je hier een bedrag voor inboekt.

## De fiscale kant, met de bedragen van 2026

### EIA — energie-investeringsaftrek

- **40%** van de investeringskosten extra aftrekbaar van de winst, bovenop de normale afschrijving (percentage 2026, RVO).
- Alleen voor bedrijfsmiddelen die onder een geldige code op de **Energielijst** van RVO staan. Vraag je leverancier om de code en controleer die zelf.
- **Aanmelden binnen 3 maanden na de besteldatum** via het eLoket van RVO. Niet vanaf de offerte, factuur of installatie — vanaf de besteldatum. Te laat is definitief te laat.
- Er geldt een minimum investeringsbedrag per melding; controleer het actuele bedrag bij RVO.

Wat 40% aftrek waard is, hangt af van je belastingtarief. Bij vennootschapsbelasting van 25,8% levert 40% aftrek effectief circa 10,3% van de investering op. Bij een IB-ondernemer in het toptarief ligt dat hoger. Dat verschil is groot genoeg om de business case te kantelen — reken met jóuw tarief.

### KIA — kleinschaligheidsinvesteringsaftrek

De tabel van de Belastingdienst voor 2026 (opgehaald 21 augustus 2026):

| Investeringsbedrag in het boekjaar | KIA-aftrek |
|---|---|
| Tot en met € 2.900 | 0% |
| € 2.901 t/m € 71.683 | 28% van het investeringsbedrag |
| € 71.684 t/m € 132.746 | € 20.072 (vast bedrag) |
| € 132.747 t/m € 398.236 | € 20.072 min 7,56% van het bedrag boven € 132.746 |
| Meer dan € 398.236 | 0% |

De KIA is cumuleerbaar met de EIA op dezelfde investering.

### MIA en Vamil

Werken met een eigen lijst (de Milieulijst) en eigen codes. Of een opslagsysteem daar onder valt, verschilt per jaar en per uitvoering. Controleer het per investering; ga er niet vanuit.

### Btw

Op de levering en installatie van een batterij geldt **21% btw**. Het nultarief voor zonnepanelen dekt het accupakket uitdrukkelijk niet, ook niet bij gelijktijdige aanschaf. Bij zakelijk gebruik vraag je die btw als voorbelasting terug via de aangifte; over een eventueel privédeel niet. Reken de EIA en KIA dus over het bedrag **exclusief** btw.

## Modelberekening 1: metaalbedrijf met 24 kWp op de loods

**Aannames** (modelberekening, geen bestaand bedrijf): 80 panelen van in totaal 24 kWp, 38.000 kWh verbruik per jaar, een 30 kWh batterijsysteem voor € 18.500 exclusief btw inclusief installatie, dynamisch contract, IB-ondernemer met een marginaal tarief van 49,5%, investering valt volledig onder een geldige EIA-code.

| Post | Bedrag |
|---|---|
| Investering exclusief btw | € 18.500 |
| Btw (21%, terugvorderbaar bij zakelijk gebruik) | € 3.885 — cash-neutraal |
| EIA-aftrek 40% | € 7.400 → belastingeffect ± € 3.663 |
| KIA-aftrek 28% | € 5.180 → belastingeffect ± € 2.564 |
| **Netto investering na fiscaal effect** | **± € 12.273** |

Aangenomen jaarlijkse opbrengst: € 1.800 uit hoger zelfverbruik, € 1.700 uit arbitrage, € 700 uit lager gecontracteerd vermogen — samen € 4.200. Rekenkundige terugverdientijd: **circa 2,9 jaar**.

De gevoeligheid zit hier bijna volledig in die € 4.200. Halveert de arbitrageopbrengst omdat de spreiding tegenvalt, dan loopt de terugverdientijd op naar ruim vier jaar. De fiscale voordelen zijn bovendien **eenmalig** en alleen te verzilveren bij voldoende winst.

## Modelberekening 2: zzp'er met thuiskantoor

**Aannames:** 40% zakelijk gebruik, 6.000 kWh verbruik per jaar, 12 zonnepanelen, een Sessy van 10 kWh (fabrikantprijs € 5.500 inclusief btw, exclusief installatie, peildatum 20 augustus 2026).

- Zakelijk deel (40%): € 2.200 inclusief btw, oftewel € 1.818 exclusief.
- Btw over het zakelijke deel (± € 382) terug te vragen; over het privédeel niet.
- EIA over het zakelijke deel: 40% × € 1.818 = € 727 → belastingeffect bij 49,5% ± € 360.
- KIA: € 1.818 valt ruim onder de drempel van € 2.901 — alleen te benutten door in hetzelfde boekjaar andere bedrijfsmiddelen aan te schaffen.
- Effectieve zakelijke kosten: ± € 1.458.

Bij een aangenomen zakelijke besparing van € 270 per jaar komt de rekenkundige terugverdientijd op **circa 5,4 jaar** — voor het zakelijke deel alleen. Voor de vermogensetikettering van dit soort gemengd gebruik: zie [zonnepanelen als zzp'er met kantoor aan huis](/posts/zzp-zonnepanelen-kantoor-aan-huis-2026/).

## Modelberekening 3: waarom overdimensioneren duur uitpakt

**Aannames:** autogaragebedrijf, 480 m² werkplaats, 38.000 kWh per jaar, 24 kWp aan panelen, bedrijfsprofiel van 7 tot 18 uur op werkdagen, gesloten in het weekend. Beide varianten gerekend inclusief EIA en KIA.

| Variant | Investering (excl. btw) | Benutting | Rekenkundige terugverdientijd |
|---|---|---|---|
| 30 kWh systeem | € 19.800 | Beperkt: capaciteit zelden volledig benut door weekendsluiting | ± 9,5 jaar |
| 15 kWh systeem + EMS (laadpaal en klimaat meegestuurd) | € 11.200 | Aanzienlijk hoger: de capaciteit gaat dagelijks rond | ± 6,2 jaar |

De les uit dit model: bij zakelijke opslag is "groter is beter" zelden waar. Wat telt is het aantal volledige cycli per jaar, en dat wordt bepaald door je dagprofiel — niet door je jaartotaal. Laat een installateur daarom altijd doorrekenen op je **kwartierdata uit de slimme meter**.

## De omvang bepalen: waar je op moet letten

1. **Haal je kwartierdata op** bij je leverancier of netbeheerder, over minimaal enkele representatieve weken (bij voorkeur een heel jaar).
2. **Bepaal het verplaatsbare volume per dag**: het overschot dat nu wordt teruggeleverd, plus de afname in de duurste uren.
3. **Tel de dagen** waarop dat volume er daadwerkelijk is. Weekendsluiting, vakantiestops en seizoenspatronen halveren zomaar het aantal bruikbare cycli.
4. **Kijk naar vermogen, niet alleen capaciteit.** Voor piekafvlakking is het laad- en ontlaadvermogen in kW bepalend, niet de kWh.
5. **Reken retourrendement mee.** Een deel van wat je laadt komt er niet uit; dat verlies betaal je wel, inclusief energiebelasting.

## Systeemkeuze: wat er te kiezen valt

Wij noemen bewust geen prijstabel per merk: zakelijke opstellingen worden vrijwel altijd op maat samengesteld en de prijs hangt af van omvormerkeuze, EMS, installatie en netbeheerdersafstemming. Wat wel houdbaar is, is de indeling naar schaal:

- **Tot enkele tientallen kWh.** Modulaire systemen van het type dat ook in woningen wordt toegepast, gestapeld tot de gewenste capaciteit. Vaak het snelst te realiseren.
- **Enkele tientallen tot ± 200 kWh.** Rack-opstellingen met een aparte omvormer- en EMS-laag, doorgaans gebouwd door een systeemintegrator. Zie voor de componentkant onze reviews van [Victron](/posts/victron-thuisbatterij-review-2026/), [Pylontech](/posts/pylontech-thuisbatterij-review-2026/) en [BYD Battery-Box](/posts/byd-battery-box-review-2026/).
- **Boven ± 200 kWh.** Containeropstellingen, met netbeheerdersafstemming en een aanzienlijk langere doorlooptijd.

Vraag bij elke offerte drie dingen op schrift: de **Energielijst-code** (bepaalt de EIA), de **garantietermijn en het gegarandeerde aantal cycli of doorzet in MWh**, en het **laad- en ontlaadvermogen in kW** — niet alleen de kWh.

## Een EMS is geen luxe

Bij zakelijke opslag is een energiemanagementsysteem geen extraatje maar de voorwaarde waaronder de business case werkt. Het stuurt laden en ontladen op basis van verbruik, productie, tarief en — als je die hebt — laadpalen en klimaatinstallatie. Zonder die coördinatie laad je op het verkeerde moment en mis je precies de pieken die je wilde afvlakken.

Neem bij de offerte-aanvraag expliciet op wat het EMS aanstuurt, welke datakoppelingen het heeft (P1, omvormer, laadpalen) en of je bij de data kunt om achteraf te controleren of het doet wat is beloofd.

## Netcongestie: nuance in plaats van vuistregel

In delen van Nederland is er transportschaarste. Dat kan betekenen dat een zwaardere aansluiting of een grotere terugleverpositie niet op korte termijn beschikbaar is, en netbeheerders bieden dan alternatieve contractvormen aan — bijvoorbeeld contracten met een tijdgebonden of beperkt transportvermogen, waarbij een batterij helpt om binnen de afgesproken grenzen te blijven.

Maar dat is iets anders dan "je krijgt geen panelen aangesloten zonder batterij". Wat er op jouw aansluitadres speelt, staat op de capaciteitskaart van de netbeheerders en kun je bij je eigen netbeheerder navragen. Doe dat vóór je een systeem bestelt: het antwoord bepaalt zowel de omvang als de doorlooptijd.

## Grotere projecten en SDE++

Voor grootschalige opstellingen wordt vaak naar de SDE++ gekeken. Welke categorieën in een bepaalde openstellingsronde meedoen, tegen welke basisbedragen en onder welke voorwaarden, verschilt per ronde. Controleer dat bij RVO op het moment dat je aanvraagt — bedragen uit een eerdere ronde zeggen niets over de volgende.

## Vijf fouten die het rendement slopen

1. **Te groot dimensioneren.** Capaciteit die niet dagelijks rondgaat, verdient zich niet terug. Match op het dagprofiel, niet op het jaartotaal.
2. **De EIA-termijn missen.** Drie maanden na de besteldatum. Dit is de duurste administratieve fout die je op dit dossier kunt maken.
3. **Rekenen inclusief btw.** De btw komt bij zakelijk gebruik terug; reken EIA en KIA over het bedrag exclusief btw, anders overschat je het voordeel.
4. **Geen dynamisch contract.** Zonder prijsverschil per uur valt de arbitragecomponent volledig weg. Zie [dynamische energiecontracten vergeleken](/posts/dynamische-energiecontracten-vergelijking-2026/).
5. **Garantie op cycli niet naast het eigen gebruik leggen.** Een garantie van 6.000 cycli is bij één cyclus per dag ruim zestien jaar, maar bij anderhalve cyclus per dag nog geen elf. Reken de garantietermijn om naar jóuw gebruik.

## Wanneer een zakelijke batterij níet uitkomt

- **Vlak verbruiksprofiel zonder pieken.** Een kantoor van negen tot vijf zonder grote afnamepieken heeft weinig te verplaatsen.
- **Weinig cyclusdagen.** Seizoensbedrijven, weekendsluiting of lange productiestops verlagen het aantal cycli en daarmee direct de opbrengst.
- **Huurpand met korte resterende looptijd.** Een investering die je niet kunt meenemen en niet kunt afschrijven binnen de huurperiode, komt niet uit.
- **Onvoldoende winst.** EIA en KIA zijn aftrekposten. Zonder belastbare winst is er niets om ze tegen af te zetten.
- **Geen dynamisch contract en geen vermogenscomponent op de factuur.** Dan blijft alleen zelfverbruik over, en dat is zelden genoeg.

## Verzekering en veiligheid

Een zakelijke batterij hoort thuis in je opstal- of bedrijfsmiddelenpolis en roept aparte vragen op over opstelplaats en brandveiligheid. Vraag je verzekeraar schriftelijk of de installatie is opgenomen in de dekking en welke eisen aan opstelling en installatie worden gesteld — vóór de plaatsing, niet erna. De algemene lijn en de vragen die je moet stellen staan in [zonnepanelen en je opstalverzekering](/posts/zonnepanelen-verzekering-opstal-2026/).

## Conclusie

Zakelijke energieopslag komt eerder uit dan particuliere opslag, maar de reden daarvoor is fiscaal en niet magisch. Wat je concreet moet doen:

1. **Haal je kwartierdata op** en bepaal het verplaatsbare volume per dag.
2. **Regel eerst het contract**: zonder dynamisch tarief valt de arbitragecomponent weg.
3. **Check de Energielijst-code** bij de leverancier — die bepaalt of de EIA geldt.
4. **Meld binnen 3 maanden na de besteldatum** bij RVO.
5. **Plan investeringen binnen één boekjaar** om de KIA-drempel van € 2.901 te halen.
6. **Reken met jouw belastingtarief**, niet met het tarief uit een voorbeeld.
7. **Neem het EMS mee in de offerte** — zonder aansturing werkt de case niet.

Verder lezen: [thuisbatterij-vergelijking](/posts/thuisbatterij-vergelijking-2026/), [BYD Battery-Box review](/posts/byd-battery-box-review-2026/), [Pylontech review](/posts/pylontech-thuisbatterij-review-2026/), [Victron review](/posts/victron-thuisbatterij-review-2026/) en [zonnepanelen als zzp'er met kantoor aan huis](/posts/zzp-zonnepanelen-kantoor-aan-huis-2026/).

---

**Externe bronnen:** [RVO — energie-investeringsaftrek](https://www.rvo.nl/subsidies-financiering/eia/ondernemers), [Belastingdienst — kleinschaligheidsinvesteringsaftrek 2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026) en [RVO — SDE++](https://www.rvo.nl/subsidies-financiering/sde). Bedragen opgehaald op 21 augustus 2026.
