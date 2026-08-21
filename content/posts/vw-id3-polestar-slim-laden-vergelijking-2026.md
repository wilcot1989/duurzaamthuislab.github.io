---
title: 'VW ID.3 vs Polestar 2: slim laden op een dynamisch contract vergeleken'
date: '2026-08-10 08:00:00+02:00'
lastmod: '2026-08-21 08:00:00+02:00'
draft: false
description: ID.3 of Polestar 2 thuis slim laden op een dynamisch contract? We vergelijken beide auto's op laadvermogen, planningsmogelijkheden en te verwachten besparing, op basis van specificaties en documentatie.
categories:
- elektrisch-rijden
tags:
- elektrisch-rijden
- verduurzamen
- duurzaam wonen
- id3
keywords:
- id3 slim laden
- polestar 2 slim laden
- tibber id3
- frank energie polestar
- ev dynamisch laden vergelijking
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: 'Maakt de auto veel verschil voor slim laden?'
  a: 'Minder dan de laadpaal en het contract. Zowel de ID.3 als de Polestar 2 laadt thuis op wisselstroom met maximaal 11 kW; dat bepaalt hoeveel kWh je in een goedkoop venster kwijt kunt. Het verschil zit in hoe fijnmazig je het schema kunt plannen en hoe betrouwbaar de koppeling met een app van derden is — niet in het rendement van de accu.'
- q: 'Kan een laadprijs van 12 cent per kWh?'
  a: 'Nee, niet all-in. Alleen de energiebelasting is in 2026 al €0,11085 per kWh inclusief btw, en daar komt de marktprijs plus de inkoopvergoeding en vaste kosten van je leverancier bij. Een all-in prijs van 12 cent kan alleen in uren met een zeer lage of negatieve marktprijs, niet als jaargemiddelde. Wij rekenen met €0,220 per kWh voor gestuurd nachtladen — en dat is al een gunstige aanname.'
- q: 'Wie moet het laadschema bepalen: de auto of de laadpaal?'
  a: 'Eén van de twee. Staat er in de auto-app én in de laadpaal een venster, dan blokkeren ze elkaar en laadt de auto soms helemaal niet. Onze voorkeur is de laadpaal of een eigen sturing via Home Assistant of EVCC: die kent de prijzen en is niet afhankelijk van de API-voorwaarden van de autofabrikant.'
- q: 'Ondersteunt de Polestar 2 vehicle-to-load?'
  a: 'Op de Nederlandse Polestar-pagina''s van de Polestar 2 en de Polestar 3 staat op 21 augustus 2026 niets over vehicle-to-load of bidirectioneel laden. Wij kunnen die functie dus niet bevestigen en noemen hem daarom niet als eigenschap. Claims op forums en in vergelijkingsartikelen lopen op dit punt uiteen; ga alleen af op de officiële specificatie van jouw exacte modeljaar.'
- q: 'Heb ik voor slim laden een thuisbatterij nodig?'
  a: 'Nee. Een EV is voor prijssturing zelf al het grootste verschuifbare verbruik in huis; een batterij is een aparte investering met een eigen terugverdientijd. Reken die twee nooit door elkaar. En een energieleverancier is geen batterij — een dynamisch contract verschuift alleen het moment waarop je inkoopt.'
schema_type: Article
last_updated: '2026-08-21'
---
*Disclosure: dit artikel bevat geen affiliate-links. Met Volkswagen, Polestar, Tibber en Frank Energie hebben wij géén commissie- of affiliaterelatie en aan de vermeldingen in dit artikel verdienen wij niets. De autospecificaties komen van de Nederlandse merkpagina's (polestar.com/nl en volkswagen.nl), opgehaald op 21 augustus 2026. Tarieven Tibber: tibber.com. Frank Energie rekent naast een inkoopvergoeding ook een terugleverstaffel (per 1 juni 2025); de vaste kosten publiceert Frank niet.*

> **Kort antwoord:** voor slim laden zijn de ID.3 en de Polestar 2 vergelijkbaar: beide laden thuis met maximaal 11 kW wisselstroom, en dat is wat bepaalt hoeveel kWh je in een goedkoop venster kwijt kunt. Het verschil zit in de planning: de ID.3 werkt met vaste laadvensters in de eigen app, de Polestar 2 heeft een directere koppeling met sturing van derden. Wie de laadpaal of een eigen automatisering laat plannen, maakt dat verschil grotendeels irrelevant.

## Waar het verschil werkelijk zit

Bij slim laden gaat het om één vraag: hoeveel van je laadvolume kun je in de goedkoopste uren leggen? Daarvoor zijn drie eigenschappen bepalend, en de accucapaciteit staat daar niet bij.

**1. Laadvermogen thuis.** Beide auto's laden op wisselstroom met maximaal 11 kW (3 fasen × 16 A). Dat betekent circa 11 kWh per uur, dus een laadsessie van 30 kWh past in bijna drie uur — ruim binnen een nachtelijk daluur-venster. Heb je thuis maar één fase (max 3,7 kW), dan duurt diezelfde 30 kWh ruim acht uur en past het níet meer in het goedkoopste blok. Dan is je netaansluiting de beperkende factor, niet de auto.

**2. Hoe fijnmazig het schema is.** De ID.3 plant via de eigen app met laadvensters: je geeft een tijdvak op en de auto laadt daarbinnen. De Polestar 2 draait op Android Automotive en heeft een directere koppeling met laadsturing van derden. Praktisch gevolg: bij de ID.3 stel je vaker een vast nachtvenster in, bij de Polestar kun je gemakkelijker meebewegen met de uurprijzen.

**3. Betrouwbaarheid van de koppeling.** Dit is het punt dat de meeste ergernis oplevert en dat in geen specificatieblad staat. Koppelingen tussen energie-apps en autofabrikanten lopen via API's waarvan de voorwaarden veranderen. Voor beide merken bestaan community-integraties voor Home Assistant; die zijn niet door de fabrikant ondersteund en kunnen breken bij een app-update. Wil je zekerheid, dan stuur je op de laadpaal — die verandert niet ineens zijn API.

## Wat wij niet kunnen bevestigen

Op de Nederlandse Polestar-pagina's van de Polestar 2 en de Polestar 3 staat op 21 augustus 2026 **niets** over vehicle-to-load, vehicle-to-home of bidirectioneel laden. Elders wordt V2L wel als eigenschap van een van beide modellen genoemd, en die claims spreken elkaar tegen. Wij nemen die functie daarom niet op in deze vergelijking. Voor de ID.3 geldt hetzelfde: bidirectioneel laden is geen gepubliceerde eigenschap van dit model.

Wat V2H en V2G in Nederland op dit moment wél en niet kunnen, staat in [ons artikel over bidirectioneel laden](/posts/v2h-v2g-thuisbatterij-2026/).

## Vergelijking op de punten die voor laden uitmaken

| | VW ID.3 | Polestar 2 |
|---|---|---|
| Laadvermogen AC thuis | tot 11 kW (3 fasen) | tot 11 kW (3 fasen) |
| Planning in de auto | laadvensters in de merkapp | laadschema, Android Automotive |
| Koppeling met sturing van derden | via de merkapp of de laadpaal | directer, plus laadpaalroute |
| Home Assistant | alleen community-integratie, niet fabrikant-ondersteund | alleen community-integratie, niet fabrikant-ondersteund |
| Preconditioning plannen | ja | ja |
| Bidirectioneel laden | niet gepubliceerd | niet gepubliceerd (zie hierboven) |

Bewust weggelaten: abonnementsprijzen van de merkapps en prijzen van bidirectionele laders. Die bedragen wisselen per land en per aanbieding en wij hebben er geen bron met peildatum voor. Liever geen bedrag dan een bedrag dat niet klopt.

## Wat het oplevert: modelberekening

Onderstaande cijfers zijn een **modelberekening met gelabelde aannames**, geen meting.

Uitgangspunten: twee huishoudens met dezelfde 11 kW-wallbox en hetzelfde dynamische contract, circa 17.000 km per jaar waarvan het grootste deel thuis geladen wordt. Bij 18-20 kWh per 100 km komt dat neer op ongeveer 3.000 kWh thuisladen per jaar.

- **Ongestuurd laden**, verdeeld over de dag: €0,26 per kWh all-in. Opbouw: EPEX-jaargemiddelde 2025 €0,105 per kWh (inclusief btw) + energiebelasting €0,11085 per kWh (2026, inclusief btw) + €0,044 per kWh inkoopvergoeding en omgeslagen vaste kosten — dat laatste is een gelabelde aanname.
- **Gestuurd nachtladen:** €0,220 per kWh all-in (aanname, geen meting).
- **Vast contract als referentie:** €0,32 per kWh all-in (aanname).

| Scenario | Prijs per kWh | 3.000 kWh per jaar |
|---|---|---|
| Vast contract | €0,32 (aanname) | €960 |
| Dynamisch, ongestuurd | €0,26 (aanname) | €780 |
| Dynamisch, gestuurd nachtladen | €0,220 (aanname) | €660 |

Het verschil tussen ongestuurd en gestuurd is dus circa **€120 per jaar** — ongeveer 4 cent per kWh. Dat is de eerlijke orde van grootte. Een "gemiddelde laadprijs van 12 cent per kWh", zoals eerder in dit artikel stond, kan niet: de energiebelasting alléén is al €0,11085 per kWh inclusief btw.

En het verschil tussen de twee auto's? Dat zit in het deel van je laadvolume dat je in de goedkoopste uren krijgt. Kan de ene auto 90 procent van het volume in het goedkoopste blok leggen en de andere 75 procent, dan scheelt dat bij 3.000 kWh en een spread van 4 cent ongeveer **€18 per jaar**. Dat is geen argument om een auto op te kiezen. Kies op prijs, ruimte en rijeigenschappen; regel het slim laden daarna met de laadpaal.

Reken het door met de werkelijke prijzen van jouw dagen: [de day-ahead-prijzen per uur](/stroomprijzen/).

## Zo zet je het op

1. **Kies één scheduler.** Laadpaal óf auto óf eigen sturing. Zet de andere twee op ongelimiteerd.
2. **Geef benodigde kWh op, niet een tijdvak.** Dan kan de scheduler zelf de goedkoopste uren kiezen.
3. **Stel een deadline met minimum-SoC in.** Bijvoorbeeld minimaal 60 procent om 07:00, ongeacht de prijs.
4. **Zet preconditioning binnen het laadvenster.** Voorwarmen terwijl de auto nog aan de paal hangt kost geen accu en valt binnen je goedkope uren.
5. **Controleer met een P1-meter of het klopt.** Zonder meting weet je niet of de sessie werkelijk in de goedkope uren lag. Zie [P1-meters vergeleken](/posts/beste-energiemonitor-p1-meter-2026/).
6. **Check je aansluiting.** Eén fase of een groep die maar 16 A trekt maakt elke slimme planning zinloos, omdat de sessie te lang duurt.

## Veelgemaakte fouten

1. **Twee schedulers tegelijk.** Auto en laadpaal die elkaar tegenwerken. De meest gemelde oorzaak van "hij heeft niet geladen".
2. **Vertrouwen op een community-integratie voor kritieke sturing.** Werkt vaak prima, maar breekt bij een app-update van de fabrikant. Zorg dat je auto ook zonder die koppeling geladen raakt.
3. **Preconditioning buiten het venster.** Een auto die om 07:45 gaat voorwarmen, trekt stroom in een van de duurste uren van de dag.
4. **Rekenen met de kale marktprijs.** De prijs die je in prijs-apps ziet, is doorgaans exclusief energiebelasting en inkoopvergoeding. Je werkelijke prijs is fors hoger.
5. **Een leverancier voor een batterij aanzien.** Een dynamisch contract verschuift het moment van inkoop; het slaat niets op. Een energieleverancier hoort niet in een lijstje met batterijsystemen.

## Wanneer slim laden marginaal blijft

Rij je weinig, of laad je het grootste deel publiek of op het werk, dan blijft het voordeel op je thuislaadvolume klein: bij 800 kWh per jaar en 4 cent verschil praat je over ruim €30. De investering in een slimme laadpaal en een dynamisch contract verdien je daarmee niet terug. Heb je een vast contract, dan valt er per uur niets te verschuiven en blijft alleen laden op eigen zonnestroom over.

Verder lezen: [Tesla Model 3 slim laden met Tibber](/posts/tesla-model-3-slim-laden-tibber-2026/), [laadpalen thuis vergeleken](/posts/beste-laadpaal-thuis-2026/) en [Frank Energie en Tibber vergeleken](/posts/frank-energie-vs-tibber-2026/).
