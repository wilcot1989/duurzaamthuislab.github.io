---
title: 'Sessy software en modi 2026: wat de batterij écht doet'
date: 2026-06-06 08:00:00+01:00
lastmod: '2026-08-21 08:00:00+02:00'
description: 'Welke modi de Sessy thuisbatterij volgens Charged heeft (zelfverbruik, dynamisch, onbalans, congestiepreventie), hoe de firmware-updates lopen en waarom "Sessy Radar" niet bestaat.'
categories:
- thuisbatterijen
tags:
- Sessy
- thuisbatterij software
- dynamisch contract
- onbalansmarkt
- firmware
keywords:
- sessy radar
- sessy software update 2026
- sessy modi
- sessy dynamisch contract
- sessy open api
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1589276534126-adef63a95e05&w=1200&output=webp&q=70
faq:
- q: 'Bestaat ''Sessy Radar''?'
  a: 'Nee. Op sessy.nl komt geen functie, modus of algoritme met de naam Radar voor (gecontroleerd op 21 augustus 2026). De naam circuleert waarschijnlijk door verwarring met twee andere dingen: Radar is een consumentenprogramma van AVROTROS, en Zonneplan noemt zijn eigen sturing ''slimme aansturing''. Wat de Sessy wél doet, staat hieronder beschreven onder de namen die de fabrikant zelf gebruikt.'
- q: 'Welke modi heeft de Sessy?'
  a: 'Charged noemt op de productpagina vier toepassingen: zelfverbruik (zonnestroom opslaan in plaats van terugleveren), optimaliseren op een dynamisch tarief, handelen op de onbalansmarkt en het voorkomen van netcongestie. Welke daarvan je kunt gebruiken hangt af van je energiecontract: optimaliseren op uurprijzen vraagt een dynamisch contract, en onbalanshandel loopt via een partij die daar toegang toe heeft.'
- q: 'Heb ik een dynamisch contract nodig?'
  a: 'Voor de zelfverbruikmodus niet — die werkt op je eigen zonneproductie en verbruik. Voor optimalisatie op uurprijzen wel, want zonder doorgegeven uurprijzen is er geen prijsverschil om op te sturen. Met het einde van de saldering per 1 januari 2027 wordt de zelfverbruikmodus voor de meeste huishoudens overigens de belangrijkste van de twee.'
- q: 'Wat kost het gebruik van de software?'
  a: 'Charged adverteert de Sessy met ''geen abonnement'': de software en de firmware-updates zitten bij het product in. Dat is een relevant verschil met systemen waarbij handelsfuncties of app-functies achter een maandbedrag zitten. Wij hebben geen abonnementsprijs op sessy.nl kunnen vinden (stand 21 augustus 2026).'
- q: 'Kan ik de Sessy koppelen aan Home Assistant of Homey?'
  a: 'Ja. Sessy heeft een Open API waarmee koppelingen met Home Assistant en Homey mogelijk zijn. Dat is voor deze markt ongebruikelijk: veel fabrikanten houden de batterij in hun eigen app opgesloten. Praktisch betekent het dat je de batterij in een eigen domoticaomgeving kunt uitlezen en aansturen.'
- q: 'Welke firmwareversie is actueel?'
  a: 'Charged houdt een publieke firmware-updatepagina bij. De nieuwste versie die daar op 21 augustus 2026 stond, was 1.11.14 van 22 juni 2026, met een verbetering aan de ''unrecoverable''-statusdetectie. De pagina loopt chronologisch terug tot versie 1.0.0 uit december 2022. Controleer die pagina zelf voordat je op internetberichten over versienummers afgaat.'
- q: 'Hoeveel levert optimaliseren op uurprijzen op?'
  a: 'Dat is niet als vast bedrag te geven en hangt af van de prijsvolatiliteit in dat jaar. Een modelberekening met circa 4 kWh bruikbaar per cyclus, ongeveer 200 productieve cycli per jaar en een all-in prijsverschil van €0,10 tot €0,14 per kWh komt uit op grofweg €80 tot €115 per jaar uit pure prijsarbitrage. Dat is een modeluitkomst met aannames, geen meting en geen belofte.'
products:
- name: Sessy thuisbatterij
  url: https://go.duurzaamthuislab.nl/sessy
  price: '3550'
schema_type: Article
---
Rond de Sessy circuleert hardnekkig de term "Sessy Radar", meestal als naam voor een slim algoritme dat de batterij automatisch op de uurprijzen laat handelen. Wij hebben dat op 21 augustus 2026 nagelopen op de eigen kanalen van de fabrikant: op sessy.nl komt geen functie, modus of algoritme met die naam voor. Wat de batterij wél kan, heet anders — en is concreter dan de mythe.

Dit artikel beschrijft de software van de Sessy op basis van wat Charged, de Nederlandse fabrikant uit Andelst, zelf publiceert: de productpagina, de handleidingensectie en de publieke firmware-updatepagina, opgehaald op 21 augustus 2026. Waar iets niet publiek is, staat dat er als zodanig bij.

*Disclosure: wij hebben geen affiliate- of commissierelatie met Sessy of Charged en verdienen niets aan de links in dit artikel.*

> **Kort antwoord:** "Sessy Radar" bestaat niet. De Sessy kent vier toepassingen die de fabrikant zelf benoemt: zelfverbruik, sturen op een dynamisch tarief, handelen op de onbalansmarkt en het voorkomen van netcongestie. De software zit zonder abonnement bij het product, firmware-updates worden publiek gedocumenteerd (nieuwste versie 1.11.14 van 22 juni 2026) en er is een Open API voor Home Assistant en Homey.

## Waar de naam "Radar" waarschijnlijk vandaan komt

Twee dingen lopen hier door elkaar. Radar is in Nederland vooral bekend als het consumentenprogramma van AVROTROS, dat regelmatig over energiecontracten en thuisbatterijen bericht. En Zonneplan, een andere partij in dit segment, stuurt zijn batterijen aan met wat het zelf "slimme aansturing" noemt. In samenvattingen en forumdiscussies raken die twee makkelijk verstrengeld tot een productnaam die nooit heeft bestaan.

Het praktische gevolg is niet onschuldig. Wie op zoek gaat naar de instellingen van "Radar" in de Sessy-app vindt niets, en wie een batterij koopt omdat een artikel een handelsalgoritme met die naam beschrijft, koopt op een verkeerde verwachting. Daarom eerst de namen die de fabrikant zelf gebruikt.

## De vier toepassingen die Charged noemt

Op de productpagina van Sessy staan vier manieren waarop de batterij waarde levert. Ze sluiten elkaar niet uit, maar ze vragen wel verschillende dingen van je contract en je installatie.

**Zelfverbruik.** De batterij slaat zonnestroom op die je anders zou terugleveren, en levert die later op de dag aan je huis. De waarde per kWh is het verschil tussen wat je voor afname betaalt en wat je voor teruglevering krijgt. Zolang de saldering bestaat, is dat verschil klein en is deze modus financieel weinig waard. Per 1 januari 2027 stopt de saldering volledig, en dan wordt dit voor de meeste huishoudens juist de belangrijkste functie van de batterij.

**Sturen op een dynamisch tarief.** Bij een contract waarbij de uurprijzen worden doorgegeven, kan de batterij laden op goedkope uren en het huis voeden op dure uren. Dit vraagt een dynamisch contract; zonder doorgegeven uurprijzen is er geen prijssignaal om op te sturen.

**Onbalanshandel.** De batterij kan meedoen aan het opvangen van onbalans op het elektriciteitsnet — het verschil tussen wat er op enig moment wordt geproduceerd en verbruikt. Dit loopt via een partij met toegang tot die markt, niet via jouw eigen contract met een leverancier. Charged noemt de functie, maar publiceert geen opbrengstcijfers per huishouden. Wij nemen daarom geen bedrag op.

**Netcongestiepreventie.** De batterij kan afname en teruglevering afvlakken zodat je aansluiting minder piekt. Dat is vooral relevant op plekken waar het net vol zit, en bij aansluitingen waar de piek meetelt in de kosten.

## Wat de software niet is

Twee misverstanden zijn het waard om expliciet weg te nemen.

Het is geen zwarte doos die per definitie geld verdient. Op vlakke prijsdagen levert een cyclus niets op, en elke cyclus kost een fractie van de levensduur. De Sessy heeft volgens de fabrikant een garantie van 6.000+ cycli of maximaal tien jaar — dat is ruim, maar niet oneindig.

Het is ook geen handelsplatform waar jij zelf posities inneemt. De optimalisatie draait op je eigen verbruik en de gepubliceerde marktprijzen; jij kiest de modus, niet de individuele transactie.

## Firmware: wat er publiek wordt gedocumenteerd

Dit is een van de sterkere punten van dit merk, en het is makkelijk over het hoofd te zien. Charged houdt een publieke firmware-updatepagina bij waarop elke versie met datum en wijziging staat. Dat maakt het mogelijk om te controleren wat er in jouw batterij is veranderd, in plaats van te vertrouwen op wat een verkoper zegt.

Stand op 21 augustus 2026:

| Versie | Datum | Wijziging volgens Charged |
|---|---|---|
| 1.11.14 | 22-06-2026 | Verbeterde "unrecoverable"-statusdetectie via een eigen coulombteller; robuustere beveiliging, minder valse meldingen |
| 1.11.13 | 08-06-2026 | Betere portaalverbinding, voorkomt onterechte offline-meldingen |
| 1.11.12 | 03-06-2026 | Kleine stabiliteitsverbeteringen |
| 1.11.11 | 03-04-2026 | Voorkomt dat het systeem onterecht in "unrecoverable"-status gaat |

De lijst loopt chronologisch terug tot versie 1.0.0 uit december 2022. Wat opvalt aan de releases van 2026 is dat het onderhoudswerk betreft — statusdetectie, verbindingsstabiliteit — en geen nieuwe handelsfuncties. Wie ergens leest over versienummers in de 3.x-reeks met nieuwe optimalisatiemodi: die staan niet op de officiële updatepagina.

Updates zijn volgens Charged inbegrepen; er is geen abonnement voor de software.

## Open API: koppelen aan Home Assistant en Homey

De Sessy heeft een Open API. Dat betekent dat je de batterij kunt uitlezen en aansturen vanuit een eigen domotica-omgeving zoals Home Assistant of Homey, in plaats van uitsluitend via de app van de fabrikant.

Voor een deel van de kopers is dit het doorslaggevende argument, en niet zonder reden. Een gesloten systeem is afhankelijk van de levensduur van één app en één cloudkoppeling; een open API laat je zelf bepalen hoe de batterij in de rest van je installatie past — bijvoorbeeld samen met een warmtepomp, een laadpaal of een P1-uitlezing van een andere fabrikant.

Wat wij niet kunnen vaststellen op basis van de publieke documentatie, is hoe volledig de API is: welke aansturing precies mogelijk is en welke uitsluitend in de app zit. Vraag dat na bij de leverancier als je een specifieke koppeling voor ogen hebt.

## De hardware waarop de software draait

Voor de context, met de opgave van de fabrikant (stand 21 augustus 2026):

| Spec | Opgave Charged |
|---|---|
| Capaciteit | 5 kWh, 10 kWh; 15 kWh (Sessy Plus) |
| Laadvermogen | 2,2 kW |
| Ontlaadvermogen | 1,7 kW |
| Chemie | LFP (lithium-ijzerfosfaat) |
| Cycli/garantie | 6.000+ cycli of maximaal 10 jaar |
| Afmetingen 5 kWh | 41 × 20 × 67 cm |
| Afmetingen 10 kWh | 41 × 27 × 78 cm |
| Adviesprijs | €3.550 (5 kWh) / €5.500 (10 kWh) / €9.400 (Plus 15 kWh), incl. btw, excl. installatie |
| Koppeling | Werkt met 1- en 3-fase omvormers van elk merk |

Let op het ontlaadvermogen van 1,7 kW. Dat is bescheiden: een waterkoker en een oven tegelijk trekken meer dan de batterij kan leveren, dus de rest komt van het net. Bij het inschatten van wat de software voor je kan doen, is dat een hardere grens dan het algoritme.

<a href="https://go.duurzaamthuislab.nl/sessy" class="cta cta-affiliate" rel="nofollow noopener" target="_blank">Bekijk Sessy</a>

## Wat optimaliseren op uurprijzen modelmatig oplevert

Onderstaande berekening is een model met expliciete aannames, geen meting aan een bestaande installatie.

**Aannames:** Sessy 5 kWh, waarvan na een reserve-instelling en rondgangsverlies circa 4 kWh per cyclus bruikbaar is voor arbitrage. All-in prijsverschil (dus inclusief energiebelasting en btw) tussen het laadmoment en het vermeden afnamemoment: €0,10 tot €0,14 per kWh. Aantal cycli waarop arbitrage daadwerkelijk iets oplevert: circa 200 per jaar; op vlakke prijsdagen levert een cyclus niets op.

**Uitkomst:** 4 kWh × €0,10 tot €0,14 = €0,40 tot €0,56 per productieve cyclus, oftewel circa €80 tot €115 per jaar uit pure prijsarbitrage.

Dat is bewust een smalle uitkomst, en het is de eerlijke: op €80 tot €115 per jaar is een batterij van €3.550 niet terug te verdienen. De business case draait op de optelsom met eigenverbruik, en die component wordt pas echt zwaar zodra de saldering per 1 januari 2027 wegvalt. Hoe die rekensom er in jouw situatie uitziet, kun je narekenen met onze [terugverdientijd-berekening voor thuisbatterijen](/terugverdientijd-thuisbatterij/).

Ter referentie voor de volatiliteit waarop dit soort optimalisatie leunt: in 2025 lag het jaargemiddelde van de day-ahead prijs op €0,105 per kWh, waren er 212 uren met een negatieve prijs, en piekte het duurste uur op €0,63 (20 januari 2025, 17:00 uur).

## Wat wij zouden nagaan vóór aanschaf

1. **Welke modus je realistisch gaat gebruiken.** Zonder dynamisch contract valt de arbitragecomponent weg en blijft alleen zelfverbruik over.
2. **Of je leverancier teruglevering vergoedt op het uurtarief**, als je op teruglevering wilt sturen. Dat verschilt per contract en staat niet in de batterij.
3. **Of het ontlaadvermogen van 1,7 kW bij je verbruikspatroon past.** Bij een huishouden met een warmtepomp of laadpaal is dat een reële beperking.
4. **Of je de Open API nodig hebt**, en zo ja: welke aansturing er precies in zit. Vraag dit schriftelijk na.
5. **Wat installatie kost.** De genoemde prijzen zijn exclusief installatie; noodstroom als functie vraagt een basisinstallatie die volgens de fabrikant €1.200 kost.

## Conclusie

De Sessy is softwarematig sterker dan gemiddeld in dit segment, maar om andere redenen dan de mythe suggereert. Er is geen "Radar"-algoritme. Er zijn vier benoemde toepassingen, een publiek bijgehouden firmwarelijst, geen abonnement en een Open API — en dat is bij elkaar een transparanter softwareverhaal dan de meeste concurrenten publiceren.

De begrenzing zit in de hardware, niet in de code: 1,7 kW ontlaadvermogen en 5 tot 15 kWh capaciteit bepalen wat er te optimaliseren valt. Wie op basis van de software een verdienmodel verwacht, komt bedrogen uit; wie een batterij zoekt die controleerbaar en koppelbaar is, zit hier goed.

## Gerelateerde artikelen

- [Sessy review 2026](/posts/sessy-review-thuisbatterij-nederland/)
- [Sessy versus Marstek](/posts/sessy-vs-marstek-vergelijking-2026/)
- [Thuisbatterij zonder zonnepanelen: heeft het zin in 2027?](/posts/batterij-na-2027-zonder-zonnepanelen-zin-2026/)
- [Beste 10 kWh thuisbatterij 2026](/posts/thuisbatterij-10-kwh-vergelijking-2026/)
- [Thuisbatterij binnen of buiten plaatsen](/posts/thuisbatterij-buiten-vs-binnen-installeren-2026/)

**Externe bron:** [RVO — ISDE voor woningeigenaren](https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren) — het officiële overzicht van welke maatregelen de ISDE wel en niet dekt. Thuisbatterijen vallen er niet onder.
