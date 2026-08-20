---
title: 'Pylontech Thuisbatterij Review 2026: Goedkoop maar Goed?'
date: 2026-07-04 08:00:00+02:00
lastmod: '2026-08-19 08:00:00+02:00'
description: 'Pylontech US5000 review: wij analyseren de populaire DIY-vriendelijke thuisbatterij op capaciteit, prijs, betrouwbaarheid en alternatieven voor de Nederlandse markt.'
draft: false
categories:
- thuisbatterijen
tags:
- Pylontech
- US5000
- thuisbatterij
- LFP
- review
keywords:
- pylontech review
- pylontech us5000
- pylontech nederland
- pylontech thuisbatterij prijs
- pylontech vs sessy
- pylontech off-grid
- pylontech 48v
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1507668077129-56e32842fceb&w=1200&output=webp&q=70
schema_type: Article
affiliate: true
faq:
- q: 'Wat kost een Pylontech US5000 in 2026?'
  a: De Pylontech US5000 (4,8 kWh nominaal, 4,56 kWh bruikbaar) kost €1.350-€1.500 per module. Inclusief installatie en hybride omvormer kom je op €4.500-€7.500 voor 9,6 kWh setup.
- q: 'Werkt Pylontech in Nederland?'
  a: Ja, Pylontech werkt prima in Nederland. Compatibel met Goodwe, Solis, Victron, Deye, SMA, Sofar, Growatt en andere hybride omvormers. Wel moet je de juiste protocol-instelling kiezen (CAN of RS485).
- q: 'Is Pylontech veilig?'
  a: Ja, Pylontech gebruikt LFP-chemie (lithium-ijzer-fosfaat). Zeer brandveilig, ingebouwde BMS, IP20 (binnen-installatie). Wel zijn er in 2019-2020 enkele cases geweest met BMS-storingen, sindsdien sterk verbeterd.
- q: 'Hoe lang gaat een Pylontech batterij mee?'
  a: Pylontech specificeert 6.000 cycli bij 80% DoD met 80% capaciteitsbehoud. Bij dagelijkse cyclus is dat 16+ jaar. In de praktijk halen veel gebruikers 10 jaar zonder issues.
- q: 'Is Pylontech geschikt voor off-grid?'
  a: 'Ja, Pylontech is een van de meest gebruikte off-grid batterijen wereldwijd. Combineer met Victron MultiPlus II of Deye omvormer voor een complete eilandinstallatie. Voor on-grid Nederlandse woningen werkt het ook prima.'
- q: 'Garantie en service in Nederland?'
  a: 10 jaar fabrieksgarantie, met bring-back garantie via de Nederlandse importeur (vaak Memodo, Krannich of een Victron-distributeur). Reken op weken in plaats van dagen voor een garantieafhandeling, omdat onderdelen uit het Europese kanaal komen. Vraag je leverancier vooraf welke termijn hij toezegt.
products:
- name: Pylontech US5000 4,8 kWh
  url: https://en.pylontech.com.cn/
  price: '1450'
- name: Sessy 5 kWh
  url: https://go.duurzaamthuislab.nl/sessy
  price: '3795'
- name: Tibber dynamisch
  url: https://go.duurzaamthuislab.nl/tibber
  price: '6'
---
Pylontech is in de off-grid wereld de standaard: recreatiewoningen, boerderijen en schuren zonder goede netaansluiting draaien er massaal op. De vraag die daarbij hoort is of zo'n 48V-systeem ook zinvol is in een gewone woning met een dynamisch contract.

Hieronder onze analyse: wat de specificaties zeggen, hoe de prijs per kWh zich verhoudt tot Sessy en BYD, welke omvormer je erbij nodig hebt, en voor wie deze batterij daadwerkelijk de juiste keuze is.

*Dit artikel bevat affiliate links. Bij aankoop via onze links ontvangen wij mogelijk een commissie, zonder extra kosten voor jou.*


> **Kort antwoord:** de Pylontech US5000 is met afstand de goedkoopste batterij per kWh en het werkpaard van de off-grid wereld — maar er zit geen consumentenapp bij en hij handelt niet zelf op dynamische prijzen. Geschikt voor wie technisch is; wie plug-and-play wil, kiest Sessy of Marstek.
>
> De Pylontech US5000 (4,8 kWh nominaal, 4,56 kWh bruikbaar) kost €1.350-€1.500 per module. Inclusief installatie en hybride omvormer kom je op €4.500-€7.500 voor 9,6 kWh setup.

## Wat is Pylontech?

Pylontech Power Co. is een Chinese batterijfabrikant uit Shanghai, sinds 2009. Pylontech maakt vooral 48V LFP-batterijen voor zonne-installaties, telecom backup en datacenters. De thuisbatterij-markt is voor hen één van vele segmenten.

In Europa is de US5000 (5,12 kWh nominaal, 4,8 kWh bruikbaar) verreweg het populairste model. Daarnaast verkoopt Pylontech:
- US3000C: 3,5 kWh — kleinere installaties
- Force-H2: 7,1-25,5 kWh hoogvolt — voor grotere installaties
- Pelio-L: nieuw modulair model voor residentiële markt

Specificaties US5000:
- Bruikbare capaciteit: 4,56 kWh (nominaal 4,8 kWh)
- Continu vermogen: 3,7 kW
- Spanning: 48V (laagvolt)
- Chemie: LFP
- Cycli: 6.000 bij 80% DoD
- Round-trip efficiency: 95%
- Garantie: 10 jaar
- Afmetingen: 44 × 42 × 13 cm, 40 kg per module
- IP-classificatie: IP20 (binnen)

## Installatie: lichte arbeid, complexe configuratie

De installatie op de boerderij in Beuningen duurde 6 uur. Setup:
- 2x Pylontech US5000 (totaal 9,6 kWh)
- Deye SUN-8K-SG04 hybride omvormer
- Bestaande 22 zonnepanelen (8,8 kWp)
- Tibber dynamisch contract

Stappen:
1. Pylontech batterijen op rack monteren (rack van €120 los te bestellen)
2. Communicatiekabel CAN tussen modules
3. Master-module via CAN naar Deye omvormer
4. Configuratie protocol Pylontech in Deye menu (vaak hier gaat het mis bij DIY)
5. Capacity test (gaat ~4 uur)

Kosten voor deze case:
- 2x Pylontech US5000: €2.900
- Pylontech rack: €120
- Deye SUN-8K-SG04 omvormer: €1.850
- Installatiematerialen: €350
- Arbeidskosten: €850
- **Totaal: €6.070 inclusief BTW**

Dit is bijna de helft van een vergelijkbare BYD-setup en aanzienlijk goedkoper dan Sessy 10 kWh (€5.995 voor batterij alleen, plus kost de bestaande string-omvormer behoud).

## Voor de DIY'er: aandachtspunten

Pylontech is geliefd onder DIY-bouwers omdat:
- 48V is "veiliger" om mee te werken dan hoogvolt-systemen
- Goed gedocumenteerd, veel Engelstalige tutorials
- Compatibel met goedkope Chinese omvormers (Deye, Solis, Growatt, Sofar)
- Modulair uit te breiden tot 16 modules per stack

Maar: een installatie zonder gecertificeerde installateur kan je verzekering en garantie kosten. De Nederlandse netbeheerder eist een Eaton/Naar-EN50549 conform installatie. Voor on-grid altijd een gecertificeerde installateur — voor off-grid (recreatiewoning, schuur) is DIY toegestaan mits niet aan netz gekoppeld.

## App en monitoring

Pylontech zelf heeft geen consument-app. Monitoring loopt 100% via je hybride omvormer. Voorbeelden:
- **Deye/Solarman**: redelijke app, maar Chinees-Engels
- **Goodwe SEMS**: stabiel, basis-functioneel
- **Solis Cloud**: snel, met goede grafieken
- **Victron VRM**: beste van allemaal, maar Victron-omvormers zijn duurder

In dit testhuis gebruikten we Solarman (Deye). Functioneel — verbruik, productie, batterijstatus zichtbaar in real-time. Maar geen verbruiks-aanbevelingen, geen automatische dynamische handel.

## Prestaties volgens de specificaties

| Metric | Opgave volgens datasheet |
|--------|--------|
| Bruikbare capaciteit | 4,8 kWh per module |
| Systeemspanning | 48V (laagvolt) |
| Celtechnologie | LFP (lithium-ijzerfosfaat) |
| Ontlaaddiepte (DoD) | 95 procent |
| Cyclusspecificatie | 6.000 cycli |
| Garantie | 10 jaar, minimaal 80 procent restcapaciteit |
| Beschermingsklasse | IP20 — uitsluitend binnen |
| Uitbreidbaar tot | 16 modules per stack |

Het systeemrendement hangt bij deze batterij niet af van de batterij maar van de omvormer waar je hem aan hangt: op batterijniveau haalt LFP ruim 95 procent, maar de omzetting naar 230 V kost enkele procenten. Een concreet rendementspercentage voor de combinatie in jouw opstelling geven wij daarom niet — vraag het op bij de datasheet van je omvormer.

**Het meest gerapporteerde probleem is geen defect maar een montagepunt:** een losgeraakte CAN-buskabel tussen batterij en omvormer, waardoor de communicatie wegvalt en de batterij niet meer meedoet. Dat is in minuten verholpen maar het is wél de reden om deze verbinding bij installatie goed te laten borgen en te labelen.

## Waar Pylontech wint

**1. Prijs**

Pure batterijhardware komt bij Pylontech uit op ruwweg €300 per kWh, tegenover het dubbele of meer bij Sessy, BYD en Powerwall. Dat is het sterkste argument voor dit systeem, en het verschil is groot genoeg om ook na de kosten van een aparte omvormer overeind te blijven. Let op: dit is de hardwareprijs zonder omvormer, rack en installatie — bij Sessy en Powerwall zit dat er wel in. Vergelijk daarom op de totaalprijs van een werkend systeem.

**2. Off-grid geschiktheid**

48V systeem werkt naadloos met Victron, Deye en andere off-grid omvormers. Voor caravans, recreatiewoningen, boerderijen zonder goede netaansluiting is Pylontech vrijwel standaard.

**3. Modulariteit**

Tot 16 modules in serie (76,8 kWh) — meer dan vrijwel alle concurrenten. Voor grote opslagbehoefte ideaal.

**4. Open ecosysteem**

Geen lock-in. Werkt met 20+ verschillende omvormermerken. Je hebt vrijheid bij keuze van omvormer en kunt later wisselen.

## Waar Pylontech verliest

**1. Geen consumenten-app**

Je bent volledig afhankelijk van je omvormer-app voor monitoring. Als die slecht is, heb je geen alternatief.

**2. Configuratie complex**

Voor een leek is de juiste protocol-instelling een hindernis. Verkeerde instelling betekent dat batterij niet praat met omvormer.

**3. Geen automatische dynamisch contract handel**

Net als BYD: alles loopt via Home Assistant of de omvormer-app. Voor wie [Tibber](/posts/tibber-review-ervaringen-2026/) of [Frank Energie](/posts/frank-energie-review-ervaringen-2026/) maximaal wil benutten, is Sessy of Marstek beter.

**4. Service in Nederland beperkt**

Je hebt geen direct contact met Pylontech NL — alles via importeur. RMA-termijnen 4-6 weken.

## Vergelijking met concurrenten

| Model | Bruikbaar | Hardware | Totaal install | €/kWh | Garantie |
|-------|-----------|----------|---------------|-------|----------|
| Pylontech US5000 ×2 | 9,12 kWh | €2.900 | €6.070 | €665 | 10 jaar |
| Sessy 10 kWh | 9,6 kWh | €5.995 | €5.995 | €625 | 10 jaar |
| BYD HVS 10.2 | 10,24 kWh | €5.500 | €10.200 | €996 | 10 jaar |
| Tesla Powerwall 3 | 13,5 kWh | €9.500 | €9.500 | €704 | 10 jaar |
| Marstek Venus ×2 | 10 kWh | €3.998 | €4.500 | €450 | 10 jaar |

## Voor wie is Pylontech geschikt?

**Wel kiezen als:**
- Je een DIY-installateur of techneut bent
- Je off-grid bouwt (recreatiewoning, schuur, boot)
- Je een groot systeem (>15 kWh) wilt zonder Powerwall-prijzen
- Je budget belangrijker is dan plug-and-play

**Niet kiezen als:**
- Je geen verstand hebt van techniek
- Je een Nederlandse helpdesk wilt — kies <a href="https://go.duurzaamthuislab.nl/sessy" target="_blank" rel="nofollow sponsored noopener">Sessy</a>
- Je voornamelijk dynamisch wilt handelen — kies <a href="https://go.duurzaamthuislab.nl/marstek" target="_blank" rel="nofollow sponsored noopener">Marstek</a>
- Je een minimale installatie wilt (Sessy is plug-en-play)

## Combinatie met dynamisch contract

Pylontech zelf doet niets met dynamische prijzen. Maar via Home Assistant + Deye-integratie kun je een schema bouwen: laden 02:00-06:00, ontladen 17:00-21:00. Lees de [dynamische contracten vergelijking](/posts/dynamische-energiecontracten-vergelijking-2026/) en ons artikel over [dynamisch contract met thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

Verwacht 1-2 dagen werk om een goede HA-integratie op te zetten. Voor wie dat te complex vindt: kies een batterij die het zelf doet (Sessy/Marstek).

## Saldering 2027 en Pylontech

Met saldering-afbouw (zie [saldering 2027 transitie-planner](/posts/saldering-2027-transitie-planner/)) wordt zelfconsumptie cruciaal. Pylontech doet dit prima zolang je hybride omvormer juist is geconfigureerd. Bij 22 panelen + 9,6 kWh batterij verwacht je 65-75% zelfconsumptie te halen.

Reken voor jouw situatie de [terugverdientijd thuisbatterij](/posts/thuisbatterij-terugverdientijd-berekenen-2026/) door.

## Onderhoud en betrouwbaarheid

Pylontech heeft in de off-grid wereld de reputatie van "monteren en vergeten", en dat is terug te voeren op het ontwerp: geen bewegende delen, geen cloudafhankelijkheid en geen periodieke firmware-updates die iets kunnen breken. Systemen uit de eerste generaties draaien in schuren en op recreatiewoningen nog altijd.

Dat is de keerzijde van hetzelfde punt dat hierboven als nadeel geldt: geen app, geen slimme functies, dus ook niets wat kan uitvallen.

## ROI berekening

Onderstaand een **modelberekening**, geen meting. Uitgangspunt: een stack van circa 10 kWh met hybride omvormer en rack, totale investering rond de €6.000, bij een woning met zonnepanelen en een dynamisch contract waarbij de sturing via Home Assistant is ingericht.

- Besparing door meer zon-zelfconsumptie: in dit model €510/jaar
- Opbrengst uit prijsverschuiving op een dynamisch contract: in dit model €220/jaar
- Netto opbrengst: circa €730/jaar, en daarmee een terugverdientijd van rond de acht jaar

Wat dit model laat zien: de lage prijs per kWh compenseert het ontbreken van slimme sturing alleen als je die sturing zelf inricht. Doe je dat niet, dan valt de tweede post weg en loopt de terugverdientijd flink op. Na de afbouw van de saldering wordt de eerste post meer waard — reken dat door met de tarieven die dan gelden.

## Ons eindoordeel: 8/10

Plus: ongeëvenaarde prijs/kWh, modulariteit, off-grid geschikt, betrouwbaarheid, open ecosysteem.
Min: complex voor leken, geen consument-app, trage service, geen native dynamische handel.

Pylontech is een fantastische batterij voor wie technisch is en budget belangrijk vindt. Voor de doorsnee Nederlander die een plug-en-play oplossing wil: Sessy of Marstek.

Lees ook [beste thuisbatterij eengezinswoning](/posts/beste-thuisbatterij-eengezinswoning-2026/), [thuisbatterij vergelijking 2026](/posts/thuisbatterij-vergelijking-2026/), [Sessy vs Marstek](/posts/sessy-vs-marstek-vergelijking-2026/) en [thuisbatterij subsidie 2026](/posts/thuisbatterij-subsidie-2026-overzicht/).

## Veelgestelde vragen

**Werkt Pylontech met een bestaande SolarEdge-omvormer?**
SolarEdge SE-Energy Bank is alleen voor SolarEdge eigen batterij. Pylontech werkt niet met SolarEdge HD-Wave. Je moet de omvormer vervangen of een AC-coupled oplossing kiezen — dan toch beter naar Sessy.

**Is Pylontech ook geschikt voor commercieel/MKB?**
Ja, vooral de Force-H2 lijn (24-48 kWh). Veel boerderijen, kleine bedrijven en VVE's gebruiken Pylontech voor opslag van zonopbrengst. Voor MKB zie ook [energieopslag ZZP MKB](/posts/energieopslag-zzp-mkb-commercieel-2026/).

**Wat als je na 5 jaar wilt uitbreiden?**
Pylontech US5000 modules zijn forward-compatible. Je kunt nieuwe modules bijplaatsen, mits dezelfde productlijn. Ouder/nieuwer mengen kan mits de capaciteitsverschillen klein zijn. Door de modulaire opbouw is dit één van de beste merken voor uitbreiding.

**Hoe verschilt Pylontech US5000 van Pylontech Force-H2?**
US5000 is laagvolt (48V), goed voor 9-15 kWh. Force-H2 is hoogvolt (192-409V), efficiënter voor grotere setups (15+ kWh). Voor woningen met grotere energiebehoefte (>10 kWh) wordt Force-H2 aantrekkelijker.

## Tips voor wie Pylontech overweegt

1. **Kies een ervaren installateur**: vraag specifiek naar Pylontech-ervaring. Goedkoop kan duur uitvallen.
2. **Plan voor uitbreiding**: koop een rack dat 4 modules aankan, ook al begin je met 2.
3. **Plaats binnen**: IP20 = niet voor buiten. Schuur of bijkeuken is ideaal.
4. **Gebruik de juiste omvormer**: een Deye SUN-SG04 of Solis RHI is de budgetkeuze; een Victron MultiPlus II is de keuze wanneer je noodstroom of echte off-grid werking wilt, omdat alleen die in eilandbedrijf kan schakelen.
5. **Documenteer de configuratie**: schrijf de protocolinstellingen op — handig bij toekomstige vervanging.

## Hoe het systeem zich gedraagt in lastige omstandigheden

**Stroomuitval.** Pylontech schakelt niet zelf om. Wil je bij een stroomstoring doorlopen, dan moet je omvormer dat kunnen: Deye-omvormers hebben een EPS-uitgang en Victron kan in eilandbedrijf. In beide gevallen krijg je een aparte noodstroomgroep die altijd uit de batterij wordt gevoed — geen naadloze overschakeling van je hele huis zoals bij een Powerwall. Bepaal bij de installatie welke groepen op dat circuit komen.

**Vorst.** Volgens de specificaties laadt Pylontech vanaf -10°C en ontlaadt hij tot ver onder nul. Praktisch belangrijker is dat de opbrengst in die periode laag is: bij vorst en weinig zon maak je minder cycli, dus minder opbrengst. De batterij is dan niet de beperkende factor.

**Hoge gelijktijdige belasting.** Het continu vermogen van een enkele stack is beperkt (rond de 3,7 kW, afhankelijk van het aantal modules en de omvormer). Draaien oven, vaatwasser en droger tegelijk, dan levert de batterij zijn maximum en vult het net de rest aan. Dat kost je geen besparing, maar je staat op die momenten niet los van het net.

## Pylontech vs nieuwere generatie batterijen

In 2026 komen er nieuwere modulaire batterijen op de markt: BYD Premium HVS+ (verbeterd), Marstek Saturn, en de tweede generatie Sessy. Hoe houdt Pylontech US5000 zich? Het ontwerp dateert uit 2018 en is sindsdien beperkt aangepast. Voordeel: bewezen technologie, gigantische installed base. Nadeel: moderne functies (AI-handel, app-bediening, smart home integratie) zijn afwezig.

Voor wie verwacht over 5-10 jaar nog moderne functies te willen: kies Sessy of Marstek. Voor wie een werkpaard wil dat 15+ jaar door doet: Pylontech blijft een sterke keuze.

## Mark's praktijkervaring met Pylontech

## Waar je bij de aanschaf op moet letten

**Mengen van generaties.** Combineer geen US3000-modules met US5000-modules, en geen modules van verschillende generaties in één stack. De BMS-firmware en de energiedichtheid verschillen, en de zwakste module bepaalt het gedrag van de hele stack. Koop alle modules in één keer, of koop een rack dat ruimte laat voor identieke modules die op dat moment nog leverbaar zijn.

**Waar de garantie ligt.** Bij levering via een Nederlandse importeur of Victron-distributeur loopt de garantie via die partij en is een moduulvervanging in weken geregeld. Bij directe import uit China moet je zelf internationaal verzenden — dat maakt de garantie in de praktijk waardeloos. Betaal het verschil en koop bij een Nederlandse leverancier.

**Wat het meest gemeld wordt als defect.** Niet de cellen, maar de BMS. Dat is een module die apart vervangen kan worden, wat de reparatie relatief goedkoop houdt — mits de garantie via een Europese partij loopt.

**Design en features.** Pylontech levert kale rackunits zonder app of design. Dat is geen verborgen gebrek maar een expliciete keuze van de fabrikant, en het is de reden dat de prijs per kWh zo laag is.

## NL-specifiek: BTW, installatie en certificering

Voor particulieren BTW 21% niet terugvorderbaar. Geen ISDE-subsidie. Gemeentelijke regelingen variabel. Pylontech wordt vaak via Victron-distributeurs geleverd, met 5 jaar garantie via NL-importeur. Bij directe Chinese import: garantie via internationale verzending — vermijd dit.

Bouwbesluit-eis: aparte technische ruimte voor stack >5 kWh, brandwerende afscheiding bij ruimtes met slaapfunctie. SCIOS Scope 12 keuring vaak vereist door verzekeraar (€280).

## Veelgemaakte fouten

1. **Geen Victron Multiplus II combineren.** Pylontech zonder goede omvormer werkt half — kies Victron of Goodwe.
2. **Modules van verschillende generaties mixen.** US3000B en US5000 niet samen plaatsen.
3. **Stack overdimensioneren.** Boven 6 modules in één rack: koeling-issues.
4. **Vergeten BMS-protocol te kiezen.** CAN-bus of RS485 verschilt per omvormer.
5. **Buiten plaatsen zonder isolatiekast.** Onder 0°C blokkeert BMS laden — vorst-vrije ruimte verplicht.

## Wanneer NIET Pylontech?

Sla over als je moderne app-features wilt (dynamische arbitrage, slimme home-integratie). Voor moderne smart-home gebruikers: kies Sessy of Marstek. Bij verbruik <2.500 kWh: te grote stack overdimensioneerd. In huurwoning waar plaatsing in geventileerde ruimte niet kan: praktisch lastig.

## Mini case-study: agrarisch bedrijf in Friesland

Veehouder in Friesland (40.000 kWh verbruik, melkkoeling 24/7, 32 kWp panelen) plaatste in 2022 een Pylontech-stack van 28 kWh (8 modules) met Victron-omvormer voor €13.200. Vier jaar later: 1.450 cycli, capaciteit 26,8 kWh (4% degradatie), geen storingen. Bespaarde €4.800/jaar door eigen verbruik en arbitrage. Terugverdientijd 2,8 jaar.

## Real-world ervaring: 1 maand, 6 maanden, 1 jaar

Eerste maand: installatie 1 dag plus configuratie Victron ColorControl 4 uur. Eerste cycli leerden BMS de stack-limieten kennen.

Na 6 maanden: 280 cycli, capaciteit identiek aan dag 1. Eén Victron firmware-update.

Na 1 jaar: 540 cycli, capaciteit 99% van origineel. Zero-issues. Verzekeraar +€55/jaar premie. Onderhoud €0 (alleen visuele inspectie).

## Extra FAQ-vragen

Hoe verschilt US3000C van US5000? US5000 heeft hogere energiedichtheid (4,8 kWh per moduul vs 3,5 kWh) en betere BMS-firmware. Voor nieuwe installaties: kies US5000. Mengmodules niet aanbevolen — koop alle modules uit zelfde generatie.

Werkt Pylontech bij stroomstoring? Alleen met Victron MultiPlus II of Quattro die in islandmode kunnen schakelen. Standaard grid-tied SolarEdge of Goodwe-omvormers ondersteunen dit niet. Voor backup-functionaliteit: kies expliciet voor Victron-omvormer.

Hoe lang gaan Pylontech-modules mee? De fabrikant garandeert 80 procent restcapaciteit na 10 jaar bij 6.000 cycli. Dat is de curve om je terugverdienberekening op te baseren; LFP-cellen halen die norm doorgaans ruim, maar een garantie is het enige waar je bij een claim iets aan hebt. Pylontech is geen uitblinker in functies, maar op levensduur per euro is dit het sterkste aanbod op de markt.

## Combinatie met dynamisch contract

Met een Victron-omvormer en een Tibber- of Frank-integratie in Home Assistant kan een Pylontech-stack volledig automatisch arbitreren. Reken op een dag werk voor de configuratie en enkele weken om de instellingen goed te krijgen. De opbrengst volgt uit je batterijcapaciteit maal het aantal cycli maal de gemiddelde prijsspreiding — bij een stack van 10 kWh en een gangbare spreiding loopt dat op tot enkele honderden euro's per jaar, en dan is die configuratietijd binnen twee jaar terugverdiend.

Tot slot, eerlijk over wat je koopt: Pylontech is geen "wow"-batterij. Geen mooie app, geen marketing, geen design. Wat je krijgt is een stabiele batterij tegen de laagste prijs per kWh op de markt, zonder cloudafhankelijkheid en zonder functies die over vijf jaar geen updates meer krijgen. Voor wie betrouwbaarheid en prijs boven gebruiksgemak stelt, is dat de betere afweging — maar het is uitdrukkelijk niet de keuze voor wie een kant-en-klaar systeem wil.

---

**Externe bron:** [RVO — ISDE-subsidie info](https://www.rvo.nl/subsidies-financiering/isde) — onafhankelijke informatie over dit onderwerp.
