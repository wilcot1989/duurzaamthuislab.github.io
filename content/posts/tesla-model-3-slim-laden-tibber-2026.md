---
title: 'Tesla Model 3 slim laden met Tibber: koppeling, schema en opbrengst'
date: '2026-08-08 08:00:00+02:00'
lastmod: '2026-08-21 08:00:00+02:00'
draft: false
description: Een Tesla Model 3 laten laden op de goedkoopste uren van een dynamisch contract. Hoe de koppeling met Tibber werkt, hoe je een laadschema op day-ahead-prijzen bouwt en wat het per jaar oplevert.
categories:
- elektrisch-rijden
tags:
- elektrisch-rijden
- verduurzamen
- duurzaam wonen
- tesla
keywords:
- tesla slim laden
- tesla model 3 tibber
- tesla dynamisch tarief
- tesla api laden
- goedkoop laden tesla
affiliate: true
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: 'Hoeveel scheelt slim laden per kWh?'
  a: 'Minder dan vaak wordt gesuggereerd. Onze modelaanname voor laden in de nachtelijke daluren is €0,220 per kWh all-in, tegenover €0,26 per kWh als je ongestuurd over de dag verdeeld laadt. Dat is ongeveer 4 cent per kWh. Het voordeel zit dus niet in de prijs per kWh maar in het jaarvolume: bij 3.000 kWh thuisladen is dat circa €120 per jaar.'
- q: 'Hoe koppel je een Tesla aan Tibber?'
  a: 'Via drie routes. Je koppelt je Tesla-account in de Tibber-app zodat Tibber de laadsessies plant; je laat de wallbox plannen (die kent de prijzen via zijn eigen koppeling) en zet in de auto alleen een laadlimiet; of je stuurt zelf via Home Assistant of EVCC. De autorisatie-eisen van Tesla voor koppelingen van derden zijn de afgelopen jaren gewijzigd, dus check bij je leverancier wat op dit moment ondersteund is.'
- q: 'Moet de auto of de laadpaal het schema bepalen?'
  a: 'Eén van de twee, nooit beide. Staat er zowel in de Tesla-app als in de laadpaal een schema, dan blokkeren ze elkaar: de auto wacht op zijn venster terwijl de paal al vrijgeeft, of omgekeerd. Kies de partij die de prijsdata heeft en zet de andere op ongelimiteerd.'
- q: 'Kan de auto te leeg blijven door prijssturing?'
  a: 'Ja, als je alleen op prijs stuurt. Stel altijd een ondergrens met deadline in: bijvoorbeeld minimaal 60 procent om 07:00, ongeacht de prijs. Bij meerdaagse hoge prijzen laadt een puur prijsgestuurd schema anders bijna niet.'
- q: 'Heb ik een dynamisch contract nodig?'
  a: 'Voor prijssturing wel. Op een vast contract is elk uur even duur en valt er niets te verschuiven; dan blijft alleen laden op eigen zonnestroom over. Reken bij een dynamisch contract ook de vaste kosten mee: Tibber rekent €5,99 per maand per energiesoort plus €0,0248 per kWh inkoopvergoeding.'
products:
- name: HomeWizard P1-meter
  url: https://go.duurzaamthuislab.nl/homewizard
  price: '24.95'
schema_type: Article
last_updated: '2026-08-21'
---
*Disclosure: de link naar HomeWizard in dit artikel is een affiliate-link (via Daisycon); koop je daarvia, dan ontvangen wij mogelijk een commissie, zonder extra kosten voor jou. Met Tibber en Tesla hebben wij géén commissie- of affiliaterelatie — aan die links verdienen wij niets. Tarieven Tibber: tibber.com. HomeWizard-prijs: homewizard.com, prijspeil augustus 2026.*

> **Kort antwoord:** je laat de Tesla Model 3 thuis laden in de uren met de laagste day-ahead-prijs, met één partij die het schema bepaalt (de Tibber-app, de wallbox of je eigen sturing) en een ondergrens met deadline zodat de auto nooit te leeg staat. Het voordeel per kWh is klein — in ons model circa 4 cent — maar op een jaarvolume van duizenden kWh loopt dat op tot honderden euro's.

## Wat er precies gestuurd wordt

Slim laden klinkt ingewikkelder dan het is. Er zijn maar drie schakelaars:

1. **Wanneer** er stroom naar de auto gaat (het laadvenster).
2. **Hoe hard** er geladen wordt (het laadvermogen, in ampère per fase).
3. **Tot hoeveel** procent (de laadlimiet in de auto).

Prijssturing verandert alleen de eerste. De prijs per uur komt van de day-ahead-veiling: elke dag rond het middaguur worden de uurprijzen voor de volgende dag bekend. Wie die prijzen kent, kan een laadsessie van vier uur precies in de vier goedkoopste uren van de nacht leggen.

Wat je *niet* verandert: het totale aantal kWh dat je laadt. Slim laden maakt stroom niet minder, alleen goedkoper per kWh.

## Drie routes om het te koppelen

**Route 1 — de auto koppelen in de app van je leverancier.** Je verbindt je Tesla-account met de Tibber-app; Tibber ziet de laadstatus en de gewenste limiet en start en stopt het laden zelf. Voordeel: werkt ook zonder slimme laadpaal, want de auto zelf is het schakelpunt. Nadeel: je bent afhankelijk van de koppeling tussen leverancier en autofabrikant. Tesla heeft de voorwaarden voor toegang van derden tot de auto in de loop der jaren gewijzigd; check wat op dit moment ondersteund wordt voordat je hier je hele opzet op bouwt.

**Route 2 — de laadpaal laten plannen.** Een slimme wallbox met een koppeling naar prijsdata (via je leverancier, via OCPP-backend of via een eigen integratie) bepaalt het venster. In de auto zet je dan alleen een laadlimiet en verder niets. Voordeel: onafhankelijk van de auto-API en werkt met elke auto. Nadeel: de paal weet niet wat de accu doet, dus het regelt grover.

**Route 3 — zelf sturen via Home Assistant of EVCC.** Je haalt de prijzen binnen als entiteit en schrijft zelf de logica: start laden als de prijs onder het daggemiddelde min een marge zit, stop bij de deadline-SoC. Meeste vrijheid, meeste onderhoud. Zie [het YAML-stappenplan voor Home Assistant](/posts/home-assistant-warmtepomp-integratie-2026/) voor de opzet van de prijsentiteit; die is identiek voor een auto.

Wat je in geen geval doet: routes combineren. Twee schedulers die elkaar tegenwerken is de meest gemelde oorzaak van "hij heeft vannacht niet geladen".

## Een laadschema op day-ahead-prijzen bouwen

Het schema dat in de praktijk werkt, bestaat uit vier regels:

1. **Bepaal het benodigde volume, niet het venster.** Je hebt bijvoorbeeld 30 kWh nodig voor morgen. Bij 11 kW laden is dat bijna drie uur. Geef die drie uur op als benodigde laadtijd en laat de scheduler zelf de goedkoopste drie uur kiezen.
2. **Zet een deadline met minimum-SoC.** Bijvoorbeeld: minimaal 60 procent om 07:00, ongeacht de prijs. Dit is de belangrijkste regel van het hele artikel.
3. **Laad in één blok, niet in dipjes.** Een scheduler die het laden opdeelt in blokjes van een half uur, verliest per opstart een beetje energie aan het conditioneren van de accu en aan de communicatie. Geef een minimale blokduur op als je systeem dat ondersteunt.
4. **Reken met een bovengrens voor dagelijks laden.** Voor de accu is dagelijks tot 80 procent laden vriendelijker dan tot 100 procent; Tesla zelf adviseert 100 procent te bewaren voor lange ritten. Dat is een vendoradvies uit de handleiding, geen meting van ons.

Zit je op route 3, dan is de kern van de automatisering: sorteer de uurprijzen van vannacht, neem de N goedkoopste uren waarin je het benodigde volume kwijt kunt, en schrijf een override als de deadline-SoC in gevaar komt.

## Wat het oplevert: modelberekening

Onderstaande cijfers zijn een **modelberekening met gelabelde aannames**, geen meting aan een eigen auto.

Uitgangspunten:

- Verbruik 18-20 kWh per 100 km, dus 3.000 kWh thuisladen bij circa 15.000 km per jaar dat je thuis laadt.
- Laadverlies (auto plus paal) circa 5 procent; dat betekent dat je iets meer inkoopt dan er in de accu komt.
- **Ongestuurd laden**, verdeeld over de dag: €0,26 per kWh all-in. Dat bedrag is opgebouwd uit de EPEX-prijs van gemiddeld €0,105 per kWh (jaargemiddelde 2025, inclusief btw), energiebelasting €0,11085 per kWh (tarief 2026, inclusief btw) en €0,044 per kWh aan inkoopvergoeding en omgeslagen vaste kosten — dat laatste is een gelabelde aanname.
- **Gestuurd nachtladen:** €0,220 per kWh all-in. Ook een aanname, gebaseerd op de gemiddelde afslag van de nachtelijke daluren op het daggemiddelde; wij hebben dit niet gemeten.

| Scenario | Prijs per kWh | 3.000 kWh per jaar | 6.000 kWh per jaar |
|---|---|---|---|
| Ongestuurd, dynamisch contract | €0,26 (aanname) | €780 | €1.560 |
| Gestuurd nachtladen, dynamisch | €0,220 (aanname) | €660 | €1.320 |
| Vast contract, referentie | €0,32 (aanname) | €960 | €1.920 |

Het verschil tussen ongestuurd en gestuurd is dus **circa €120 per jaar bij 3.000 kWh** en €240 bij 6.000 kWh. Dat is eerlijk gezegd bescheiden — 4 cent per kWh — maar het is wél geld dat je zonder extra hardware kunt pakken als je al een dynamisch contract hebt.

Twee dingen die je erbij moet rekenen voordat je conclusies trekt:

- **De vaste kosten van het dynamische contract.** Tibber rekent €5,99 per maand per energiesoort plus €0,0248 per kWh inkoopvergoeding. Op een huishouden met 4.500 kWh totaal verbruik is dat circa €72 aan abonnement plus circa €112 aan inkoopvergoeding per jaar. Die kosten maak je ook als je niet slim laadt — maar ze bepalen wel of dynamisch in totaal gunstiger is dan vast.
- **De referentie €0,32 voor een vast contract is een aanname en gevoelig.** Ligt het vaste tarief dat jij kunt krijgen op €0,28, dan verdwijnt een groot deel van het voordeel van dynamisch — ook mét slimme sturing. Vul je eigen aanbod in voordat je overstapt.

Reken het door met de werkelijke prijzen van jouw dagen: [de day-ahead-prijzen per uur](/stroomprijzen/) en [de historie sinds 2014](/stroomprijzen-historie/).

## Wat het kost

| Onderdeel | Kosten | Bron |
|---|---|---|
| HomeWizard P1-meter | €24,95 | homewizard.com, prijspeil aug 2026 |
| Tibber-abonnement | €5,99 per maand per energiesoort | tibber.com |
| Tibber-inkoopvergoeding | €0,0248 per kWh | tibber.com |
| Slimme wallbox 11 kW | prijzen verschillen sterk per merk en installatie — zie [het laadpaal-overzicht](/posts/beste-laadpaal-thuis-2026/) | — |
| Eigen sturing via Home Assistant/EVCC | software gratis, kost tijd | — |

Wat wij hier bewust **niet** in een kostentabel zetten: de prijs van een Tibber Pulse (niet publiek gepubliceerd), de abonnementskosten van externe Tesla-apps (variëren en veranderen) en een thuisbatterij. Een thuisbatterij hoort niet in een kostentabel over slim laden: dat is een aparte investering van een heel andere orde. Wat een Tesla Powerwall in Nederland kost, staat in [onze Powerwall-review](/posts/tesla-powerwall-review-nederland-2026/): een marktindicatie van €8.500-€9.500 — een andere orde van grootte dan de onderdelen in de tabel hierboven.

## Veelgemaakte fouten

1. **Twee schedulers tegelijk.** Auto én laadpaal een schema geven. Kies één.
2. **Alleen op prijs sturen, zonder deadline-SoC.** Bij een week met hoge prijzen sta je met een lege auto.
3. **Op een gewoon stopcontact laden.** Met circa 2 kW (10 A, 1 fase) duurt 30 kWh vijftien uur — dan past de laadsessie niet meer in de goedkope uren en verdwijnt het hele voordeel. Voor prijssturing wil je minimaal 7,4 kW.
4. **Preconditioning vergeten.** Het voorwarmen of koelen van de auto voor vertrek trekt stroom buiten je laadvenster, vaak precies in een duur ochtenduur.
5. **Laadverlies negeren in je berekening.** Je betaalt voor kWh aan de meter, niet voor kWh in de accu. Reken met enkele procenten verlies.
6. **Denken dat de spread altijd gelijk is.** In 2025 lag het EPEX-jaargemiddelde op €0,105 per kWh en waren er 212 uren met een negatieve prijs, maar het duurste uur kwam op €0,63 (20 januari 2025, 17:00). Die spreiding verschilt sterk per seizoen; een berekening op één maand zegt niets over het jaar.

## Wanneer slim laden de moeite niet is

Laad je minder dan een paar honderd kWh per jaar thuis — korte ritten, veel publiek laden, een leaseauto met laadpas — dan blijft het voordeel binnen de tientjes en weegt dat niet op tegen het opzetten en onderhouden. Heb je een vast contract, dan is er niets te verschuiven. En zit je in een appartement zonder eigen laadpunt, dan begint het verhaal bij [laden in een VvE](/posts/laadpaal-vve-installatie-2026/), niet bij prijssturing.

Verder lezen: [laadpalen thuis vergeleken](/posts/beste-laadpaal-thuis-2026/), [ID.3 en Polestar 2 slim laden](/posts/vw-id3-polestar-slim-laden-vergelijking-2026/) en [wat V2H en V2G in Nederland wel en niet kunnen](/posts/v2h-v2g-thuisbatterij-2026/).
