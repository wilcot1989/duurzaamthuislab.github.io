---
title: 'Dynamische stroomprijzen per uur in 2026: goedkoopste'
date: 2026-05-26 08:00:00+01:00
lastmod: 2026-08-21 08:00:00+02:00
description: 'Hoe lopen de uurprijzen op de day-ahead-markt uiteen, en wat levert het op om verbruik te verschuiven? De cijfers over 2025, de opbouw van je eindtarief en een narekenbare modelberekening.'
categories:
- energie
tags:
- dynamische prijzen
- EPEX
- thuisbatterij
- Tibber
- uurprijzen
- spotmarkt
- energiekosten
keywords:
- dynamische stroomprijzen uur 2026
- EPEX spotprijs gemiddeld
- goedkoopste uren stroom
- thuisbatterij dynamisch contract
- tibber uurprijzen
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: Welke uren zijn gemiddeld het goedkoopst?
  a: 'Structureel zijn dat de nachtelijke uren, grofweg tussen 01:00 en 06:00, en op zonnige dagen het midden van de dag wanneer er veel zonnestroom op het net staat. Het zijn gemiddelden over veel dagen: op een windstille, bewolkte winterdag ontbreekt de middagdip volledig. De prijzen voor morgen staan elke dag vanaf het begin van de middag vast en zijn te zien in de app van je leverancier en op onze pagina met actuele stroomprijzen.'
- q: Welke uren zijn gemiddeld het duurst?
  a: 'De ochtendpiek en vooral de avondpiek: grofweg 07:00-09:00 en 17:00-20:00. Dan is de vraag hoog terwijl er weinig of geen zonnestroom is. Het duurste uur van 2025 viel op 20 januari om 17:00 uur, met een kale prijs van 0,63 EUR per kWh.'
- q: Hoeveel levert verbruik verschuiven op?
  a: 'De rekenregel is simpel: het aantal verschoven kWh maal het prijsverschil per kWh, plus 21 procent btw. Energiebelasting en netbeheerkosten veranderen niet met het uur, dus die vallen tegen elkaar weg. Verschuif je 2.000 kWh per jaar met een gemiddeld verschil van 10 cent per kWh, dan is dat 200 EUR exclusief btw, ofwel circa 242 EUR inclusief btw. Zonder verschuifbaar verbruik is het voordeel klein.'
- q: Hoe stuurt een Sessy-thuisbatterij op de uurprijs?
  a: 'Charged, de fabrikant van Sessy, noemt vier bedrijfsmodi: zelfverbruik, een dynamische modus die op de uurprijzen stuurt, onbalanshandel en congestiepreventie. Er bestaat geen functie of algoritme met de naam "Sessy Radar"; die term komt niet voor in de documentatie van de fabrikant.'
- q: Zijn negatieve prijzen gunstig als je een thuisbatterij hebt?
  a: 'Bij een negatieve kale prijs is de leveringscomponent negatief, maar de energiebelasting van 0,09161 EUR per kWh (exclusief btw, tarief 2026) betaal je nog steeds. Je wordt dus in de praktijk zelden echt betaald om stroom af te nemen; het uur is wel uitzonderlijk goedkoop. In 2025 waren er 212 uren met een negatieve day-ahead-prijs in Nederland.'
- q: Waaruit bestaat het tarief dat je per uur betaalt?
  a: 'Uit de kale day-ahead-prijs voor dat uur, plus de inkoopvergoeding van je leverancier, plus energiebelasting, plus 21 procent btw over dat totaal. De netbeheerkosten staan daar los van: dat is voor kleinverbruikers een vast capaciteitstarief per jaar en geen bedrag per kWh, dus die post verandert niet met het uur waarop je verbruikt.'
schema_type: Article
---

*Disclosure: de links naar Sessy en Tibber in dit artikel zijn gewone verwijzingen — wij hebben met deze partijen geen affiliate- of commissierelatie.*

Op een dynamisch contract betaal je voor elk uur van de dag een andere prijs. Hoe groot dat verschil is, en wat het waard is om je verbruik te verschuiven, is met publieke data goed na te rekenen. Deze pagina zet de cijfers over 2025 op een rij, laat zien hoe je eindtarief per uur is opgebouwd en rekent met expliciete aannames door wat verschuiven en opslaan opleveren.

Alle prijzen hieronder zijn kale day-ahead-prijzen tenzij anders vermeld. De actuele uurprijzen van vandaag en morgen staan op onze pagina met [actuele stroomprijzen](/stroomprijzen/); de cijfers in dit artikel zijn jaarcijfers en gemiddelden, geen momentopname.

> **Kort antwoord:** de uurprijs schommelt structureel rond een nachtdal en twee pieken, met op zonnige dagen een extra dal midden op de dag. Het jaargemiddelde van de day-ahead-prijs lag in 2025 op 0,105 EUR per kWh; er waren 212 uren met een negatieve prijs en het duurste uur kostte 0,63 EUR per kWh. Het voordeel van een dynamisch contract is het aantal kWh dat je naar de goedkope uren verschuift maal het prijsverschil — verschuif je niets, dan verandert er weinig.

## Hoe de uurprijs tot stand komt

De day-ahead-markt is een dagelijkse veiling. Producenten en leveranciers bieden voor elk uur van de volgende dag vraag en aanbod in; de veiling sluit rond het middaguur en kort daarna liggen de prijzen voor alle uren van morgen vast. Die prijzen zijn openbaar en zijn de basis onder elk dynamisch contract in Nederland.

Dat vooruit vaststaan is precies wat sturen mogelijk maakt: je weet aan het begin van de middag al welke uren morgen goedkoop zijn. Een app, een laadpaal of een batterij kan daar dan een schema op bouwen. Naast day-ahead bestaat er ook een intradaymarkt voor bijsturing binnen de dag, maar het tarief dat een huishouden betaalt volgt de day-ahead-uitkomst.

## Wat 2025 liet zien

Drie cijfers over het kalenderjaar 2025 zijn bruikbaar als ijkpunt:

| Kengetal 2025 | Waarde |
|---|---|
| Jaargemiddelde day-ahead-prijs | 0,105 EUR/kWh |
| Uren met een negatieve prijs | 212 |
| Duurste uur | 0,63 EUR/kWh (20 januari 2025, 17:00) |

Die drie getallen zeggen samen meer dan een tabel met uurgemiddelden. Het jaargemiddelde is de prijs die je ongeveer betaalt als je nergens op stuurt. De 212 negatieve uren laten zien hoe vaak er een overschot is. En het duurste uur laat zien hoe ver de uitschieters naar boven kunnen gaan — een factor zes boven het jaargemiddelde, in één uur.

Wij publiceren hier bewust geen tabel met gemiddelde prijzen per klokuur. Zo'n tabel suggereert een precisie die er niet is: het gemiddelde over 365 dagen zegt weinig over de dag van morgen, waarop wind en zon het profiel volledig kunnen omgooien. Wat wel klopt is de vorm van het patroon, en die is hieronder beschreven.

## Het dagpatroon in woorden

**Nacht (ongeveer 01:00–06:00).** De vraag is laag en de basislast draait door. Dit is over het jaar heen het meest betrouwbare dal, ook in de winter, ook zonder zon.

**Ochtendpiek (ongeveer 07:00–09:00).** Huishoudens en bedrijven starten tegelijk op terwijl zonnestroom nog nauwelijks bijdraagt. In de winter is dit een van de twee duurste momenten van de dag.

**Midden van de dag.** Op een zonnige dag ontstaat hier een tweede dal, dat in het voorjaar en de zomer diep kan zijn en tot onder nul kan zakken. Op een bewolkte winterdag ontbreekt dit dal volledig — dan loopt de prijs van de ochtendpiek min of meer door naar de avond.

**Avondpiek (ongeveer 17:00–20:00).** Iedereen komt thuis, kookt en verwarmt, terwijl de zon weg is. Dit is structureel het duurste deel van de dag en het moment waarop uitschieters zoals dat uur van 0,63 EUR ontstaan.

De omvang van deze verschillen wisselt sterk per dag en per seizoen. In het voorjaar is de spreiding binnen één dag doorgaans het grootst, omdat een fors zonnedal en een fors verwarmingsafhankelijke avondpiek in dezelfde 24 uur vallen. Hoe groot de spreiding vandaag is, zie je op onze [pagina met actuele stroomprijzen](/stroomprijzen/); een verdieping over de negatieve uren staat op [negatieve stroomprijzen](/negatieve-stroomprijzen/).

## Waaruit je eindtarief bestaat

Dit onderdeel wordt vaak verkeerd weergegeven, en het bepaalt hoeveel verschuiven werkelijk oplevert.

| Component | Verandert per uur? | Bedrag |
|---|---|---|
| Kale day-ahead-prijs | ja | wisselt per uur |
| Inkoopvergoeding leverancier | nee | Tibber 0,0248 EUR/kWh; ANWB Energie 0,018 EUR/kWh |
| Energiebelasting stroom 2026 | nee | 0,09161 EUR/kWh excl. btw (0,11085 incl.) |
| Btw | — | 21% over het totaal |
| Netbeheerkosten | nee | vast capaciteitstarief per jaar, geen bedrag per kWh |
| Vaste kosten leverancier | nee | Tibber 5,99 EUR per maand per energiesoort |

Peildatum: augustus 2026. Bedragen van Tibber en ANWB Energie komen van hun eigen tarievenpagina's; Frank Energie publiceert de vaste kosten niet en rekent sinds 1 juni 2025 daarnaast een terugleverstaffel.

Twee gevolgen daarvan:

1. **Alleen de kale prijs verschilt per uur.** Energiebelasting en inkoopvergoeding zijn voor elk uur gelijk, en netbeheerkosten zijn een jaarbedrag. Verschuif je een kWh van een duur naar een goedkoop uur, dan bespaar je exact het verschil in kale prijs, vermeerderd met 21 procent btw. Niets meer.
2. **Negatieve prijzen leveren zelden geld op.** Bij een kale prijs van −0,02 EUR/kWh betaal je nog steeds 0,09161 EUR energiebelasting plus de inkoopvergoeding. Het uur is dan zeer goedkoop, maar je wordt niet betaald om stroom af te nemen. Dat gebeurt pas als de kale prijs dieper negatief gaat dan de vaste opslagen bij elkaar.

## Modelberekening: wat verschuiven oplevert

Dit is een modelberekening met expliciete aannames, geen meting en geen belofte. Vul je eigen cijfers in om hem te herhalen.

**Aannames**

- Kale prijs in een daluur: 0,04 EUR/kWh.
- Kale prijs in een piekuur: 0,20 EUR/kWh.
- Verschil: 0,16 EUR/kWh exclusief btw, ofwel 0,19 EUR/kWh inclusief btw.
- Energiebelasting, inkoopvergoeding en netbeheerkosten vallen tegen elkaar weg omdat ze niet uurafhankelijk zijn.

**Een wasbeurt.** Een was- of vaatwasprogramma verbruikt grofweg 0,5 tot 1,5 kWh. Bij 1 kWh verschoven is dat 19 cent per keer, of ruim 30 EUR per jaar bij tweehonderd draaibeurten. Dat is een reëel bedrag, maar het is geen reden om over te stappen.

**Een elektrische auto.** 2.400 kWh per jaar volledig in daluren laden in plaats van in de avondpiek: 2.400 × 0,16 = 384 EUR exclusief btw, ofwel circa 465 EUR inclusief btw. Dit is de grootste enkele post in de meeste huishoudens, en het is volledig te automatiseren met een laadschema.

**Let op de aanname.** Die 0,16 EUR spreiding is een gunstige dag, geen jaargemiddelde. Realistischer is dat een deel van je laadsessies op een dag valt met weinig spreiding. Reken daarom met de spreiding die je zelf op de [prijzenpagina](/stroomprijzen/) terugziet over een paar weken, en niet met een uitschieter.

## Thuisbatterij op een dynamisch contract

Een batterij automatiseert wat je met timers handmatig doet, en kan bovendien volume verschuiven dat je anders niet zou kunnen verplaatsen. Wat dat oplevert, hangt af van capaciteit, vermogen en rendement.

**Wat Charged over de Sessy publiceert** (fabrikantopgave, opgehaald augustus 2026): de 5 kWh-variant kost 3.550 EUR inclusief btw en exclusief installatie, laadt met 2,2 kW en ontlaadt met 1,7 kW, en is gespecificeerd op meer dan 6.000 cycli. Volledig laden duurt daarmee ruim twee uur, volledig ontladen bijna drie uur. Charged noemt vier bedrijfsmodi: zelfverbruik, een dynamische modus die op de uurprijzen stuurt, onbalanshandel en congestiepreventie.

Er bestaat geen functie met de naam "Sessy Radar". Die term duikt op in vergelijkingsartikelen, maar komt niet voor in de documentatie van de fabrikant. Wat er wel is, is de dynamische modus.

**Modelberekening één cyclus per dag.** Aannames: 5 kWh geladen bij een kale prijs van 0,04 EUR/kWh, ontladen ter vervanging van inkoop bij 0,20 EUR/kWh, round-trip-rendement 90 procent, energiebelasting 0,09161 EUR/kWh en 21 procent btw.

- Kosten laden: 5 kWh × (0,04 + 0,0248 + 0,09161) × 1,21 = 0,95 EUR
- Vermeden inkoop: 4,5 kWh × (0,20 + 0,0248 + 0,09161) × 1,21 = 1,72 EUR
- **Netto per cyclus: circa 0,77 EUR**
- Bij 250 bruikbare cyclusdagen per jaar: circa 190 EUR

Twee kanttekeningen die deze som eerlijk houden. Ten eerste betaal je energiebelasting over de volle 5 kWh die je laadt, ook over de halve kWh die door het rendementsverlies verdwijnt — dat is een kostenpost die in veel rekenvoorbeelden ontbreekt. Ten tweede geldt dit alleen als je de ontladen stroom zelf verbruikt. Lever je terug aan het net, dan krijg je de terugleververgoeding van je leverancier en niet je eigen inkooptarief; dat is per 1 januari 2027 een wezenlijk verschil, omdat de salderingsregeling dan volledig stopt.

Zet je die circa 190 EUR per jaar naast een aanschafprijs van 3.550 EUR, dan kom je op arbitrage alleen niet in de buurt van een korte terugverdientijd. De rest van het rendement moet komen uit eigen zonnestroom die je anders zou terugleveren, en eventueel uit onbalanshandel. Reken je eigen situatie door met onze [terugverdientijd-calculator](/terugverdientijd-thuisbatterij/) in plaats van met een vuistregel.

## Wat de aanbieders publiceren

| Aanbieder | Vaste kosten per maand | Inkoopvergoeding stroom | Bijzonderheden |
|---|---|---|---|
| Tibber | 5,99 EUR per energiesoort | 0,0248 EUR/kWh | maandelijks opzegbaar; open API |
| ANWB Energie | niet op de energiepagina vermeld | 0,018 EUR/kWh | biedt daarnaast vast en variabel aan |
| Frank Energie | niet gepubliceerd | aanwezig, bedrag niet gepubliceerd | terugleverstaffel sinds 1 juni 2025 |

Peildatum augustus 2026. Wij nemen hier alleen op wat de leveranciers zelf publiceren. Beoordelingen in sterren of cijfers geven wij niet: wij testen deze diensten niet zelf, en een cijfer zonder meting is een mening met een getal ervoor. Een bredere vergelijking staat op onze pagina [dynamisch energiecontract vergelijken](/dynamisch-energiecontract-vergelijken/) en in de [vergelijking Tibber en Frank Energie](/posts/tibber-vs-frank-energie-2026/).

## Wanneer een dynamisch contract níet loont

**Je kunt niets verschuiven.** Geen elektrische auto, geen batterij, geen apparaten met een timer: dan betaal je ongeveer het gemiddelde van de uurprijzen plus de vaste kosten van de leverancier. Dat verschilt weinig van een vast tarief, en de vaste kosten komen er bovenop.

**Je verbruikt vooral overdag op doordeweekse dagen.** Thuiswerken met verwarming, verlichting en apparatuur zit deels in de duurdere uren. Het profielgemiddelde ligt dan boven het rekenkundig jaargemiddelde.

**Je wilt prijszekerheid.** Een dynamisch contract geeft die niet. In periodes van marktstress kunnen de uurprijzen fors uitlopen, zoals het uur van 0,63 EUR in januari 2025 laat zien. Wie dat risico niet wil dragen, betaalt bij een vast contract een risico-opslag om het af te kopen. Dat is een legitieme afweging, geen fout.

## Waar je de prijzen zelf kunt volgen

- **Onze [pagina met actuele stroomprijzen](/stroomprijzen/)** — uurprijzen voor vandaag en morgen, met de goedkoopste momenten uitgelicht.
- **De app van je leverancier** — Tibber, Frank Energie en ANWB Energie tonen allemaal de uurprijzen zodra de veiling van die dag rond is.
- **ENTSO-E Transparency Platform** — de officiële Europese bron met day-ahead-prijzen per biedzone.
- **Home Assistant** — voor wie apparaten automatisch wil laten schakelen op de uurprijs, met integraties voor de meeste dynamische leveranciers.

## Conclusie

Een dynamisch contract verandert niet wat stroom kost, maar wél wanneer het goedkoop is. De rekensom is kort: verschoven kWh maal het verschil in kale prijs, plus btw. Alles daarbuiten — energiebelasting, netbeheerkosten, vaste kosten — beweegt niet mee met het uur.

Voor huishoudens met een elektrische auto is dat verschil groot genoeg om echt te merken. Voor huishoudens zonder verschuifbaar verbruik is het klein. En voor een thuisbatterij geldt dat de arbitragewinst alleen zelden de investering draagt; die som hangt vooral op je eigen zonnestroom en op wat er na het einde van de saldering per 1 januari 2027 met je teruglevering gebeurt.

<a href="https://go.duurzaamthuislab.nl/tibber" class="cta cta-affiliate" rel="noopener nofollow" target="_blank">Bekijk Tibber</a> (gewone verwijzing, wij ontvangen hiervoor geen vergoeding)

<a href="https://go.duurzaamthuislab.nl/sessy" class="cta cta-affiliate" rel="noopener nofollow" target="_blank">Bekijk Sessy</a> (gewone verwijzing, wij ontvangen hiervoor geen vergoeding)

## Gerelateerde artikelen

- [Energieleverancier overstappen 2026](/posts/energieleverancier-overstappen-2026-stappenplan/)
- [Dynamische energiecontracten vergelijking 2026](/posts/dynamische-energiecontracten-vergelijking-2026/)
- [Beste dynamisch contract met zonnepanelen 2026](/posts/beste-dynamisch-contract-met-zonnepanelen-2026/)
- [Saldering 2027 transitie-planner](/posts/saldering-2027-transitie-planner/)
- [Saldering stopt in 2027: de volledige gids](/posts/saldering-stopt-2027-volledige-gids/)
