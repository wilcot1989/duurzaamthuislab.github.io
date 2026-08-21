---
title: Dynamisch contract besparing — rekenmodel 2026
date: 2026-09-30 08:00:00+02:00
lastmod: 2026-08-21 08:00:00+02:00
draft: false
description: Narekenbaar rekenmodel voor een dynamisch energiecontract in 2026 — drie huishoudens doorgerekend op EPEX 2025, energiebelasting 2026 en de gepubliceerde Tibber-tarieven.
categories: [energie]
tags: [dynamisch-contract, Tibber, Frank-Energie, besparing, rekenmodel, EPEX]
keywords: [dynamisch contract besparing, tibber besparing berekenen, frank energie rekenmodel, vast vs dynamisch, dynamisch contract 2026]
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
  - q: 'Hoeveel kan ik besparen met een dynamisch contract in 2026?'
    a: 'In ons rekenmodel bespaart een huishouden van 3.500 kWh ongeveer 96 euro per jaar zonder iets te veranderen, en ongeveer 197 euro per jaar wanneer flexibel verbruik naar goedkope uren wordt geschoven. Het model rekent met het EPEX-jaargemiddelde 2025 (0,105 euro/kWh incl. btw), een opslag-aanname van 0,044 euro/kWh incl. btw en de energiebelasting van 2026, afgezet tegen een aangenomen vast tarief van 0,32 euro/kWh all-in. Andere aannames geven andere uitkomsten.'
  - q: 'Is Tibber goedkoper dan Frank Energie?'
    a: 'Dat is met publieke gegevens niet te berekenen. Tibber publiceert 5,99 euro per maand per energiesoort plus een inkoopvergoeding van 0,0248 euro per kWh. Frank Energie publiceert zijn vaste kosten niet op de openbare tarievenpagina en rekent naast een inkoopvergoeding ook een terugleverstaffel. Vraag bij beide een actueel tarievenoverzicht op voordat je vergelijkt.'
  - q: 'Wanneer is een vast contract beter dan dynamisch?'
    a: 'Vast loont vooral als je verbruik tussen 17:00 en 20:00 ligt en niet te verschuiven is, als je geen elektrische auto, warmtepomp of thuisbatterij hebt, en als je zekerheid over het maandbedrag zwaarder laat wegen dan een verwacht voordeel van enkele tientjes tot enkele honderden euro per jaar.'
  - q: 'Wat als de stroomprijs sterk stijgt?'
    a: 'In een week met een EPEX-gemiddelde van 0,21 euro/kWh komt het dynamische all-in tarief in ons model uit op ongeveer 0,365 euro/kWh, tegenover 0,32 euro op het aangenomen vaste tarief. Zo''n week weegt voor circa een tweeenvijftigste mee in het jaartotaal. Wie in die uren verbruik verschuift, beperkt het effect.'
  - q: 'Hoe werkt het EPEX day-ahead tarief precies?'
    a: 'Elke dag rond het middaguur worden de uurprijzen voor de volgende dag vastgesteld op de day-ahead markt. De uurprijs die je leverancier doorgeeft is al inclusief btw; daar telt hij een inkoopvergoeding en de energiebelasting (0,11085 euro/kWh incl. btw) bij op. Je betaalt daardoor 24 verschillende prijzen per dag in plaats van een.'
  - q: 'Heb ik een slimme meter nodig?'
    a: 'Ja. Voor een dynamisch contract zijn uur- of kwartierwaarden nodig, en die levert alleen een slimme meter. Check bij je netbeheerder of je meter op afstand uitleesbaar is en of de P1-poort openstaat.'
schema_type: Article
last_updated: '2026-08-21'
category: energie
---

Een vast contract van 0,33 euro per kWh met jaren lock-in tegenover een dynamisch contract dat de uurprijs volgt: welke is voordeliger? Het eerlijke antwoord is dat het afhangt van je verbruik, je flexibiliteit en van welke tarieven je invult. Daarom staat hieronder geen uitspraak maar een rekenmodel: alle aannames staan erbij, zodat je ze kunt vervangen door je eigen cijfers.

*Disclosure: wij hebben geen affiliate- of commissierelatie met Tibber, Frank Energie of ANWB Energie (stand augustus 2026) en ontvangen geen vergoeding als je via onze links overstapt. De links naar deze leveranciers zijn gewone verwijzingen.*

> **Kort antwoord:** in ons model met het EPEX-jaargemiddelde 2025 van 0,105 euro/kWh en de energiebelasting van 2026 bespaart een huishouden van 3.500 kWh circa 96 euro per jaar op een dynamisch contract zonder iets te veranderen, en circa 197 euro per jaar met actief verschuiven van verbruik. Voor 2.000 kWh is dat circa 24 respectievelijk 82 euro, voor 6.000 kWh circa 216 respectievelijk 390 euro. De uitkomst is sterk afhankelijk van het vaste tarief waarmee je vergelijkt.

## De aannames van dit model

Elke uitkomst hieronder is een modelberekening. Dit zijn de invoerwaarden, met bron en peildatum:

| Invoerwaarde | Waarde | Bron / peildatum |
|---|---|---|
| EPEX day-ahead NL, jaargemiddelde 2025 | 0,105 euro/kWh incl. btw | day-ahead marktdata 2025 |
| Negatieve uren 2025 | 212 uur | day-ahead marktdata 2025 |
| Duurste uur 2025 | 0,63 euro/kWh incl. btw (20 januari 2025, 17:00) | day-ahead marktdata 2025 |
| Energiebelasting stroom 2026 | 0,09161 euro/kWh excl. btw (0,11085 incl.) | Belastingdienst-tarieven 2026, aug 2026 |
| Btw | 21% | — |
| Tibber vaste kosten | 5,99 euro/mnd **per energiesoort** | tibber.com, aug 2026 |
| Tibber inkoopvergoeding | 0,0248 euro/kWh | tibber.com, aug 2026 |
| ANWB Energie inkoopkosten | 0,018 euro/kWh | anwb.nl, aug 2026 |
| Frank Energie vaste kosten | publiceert geen consumentenprijs | frankenergie.nl, aug 2026 |
| Opslag-aanname in het model | 0,044 euro/kWh incl. btw (inkoopopslag + omslag vaste kosten) | eigen aanname, gebruikt in alle modellen op deze site |
| Dynamisch all-in bij het jaargemiddelde | 0,26 euro/kWh = 0,105 + 0,11085 + 0,044, alle bedragen incl. btw | eigen model |
| Vast referentietarief (aanname) | 0,32 euro/kWh all-in | eigen aanname, vervang door je eigen aanbod |

Twee posten laten we bewust buiten de vergelijking omdat ze in beide contractvormen identiek zijn en het verschil dus niet beinvloeden: de **netbeheerkosten** (een vast jaarbedrag van je regionale netbeheerder, geen bedrag per kWh) en de **vermindering energiebelasting** (een vaste jaarlijkse korting op je rekening). De **ODE bestaat sinds 2023 niet meer** als aparte post; die is in de energiebelasting opgegaan.

## Van EPEX-prijs naar wat je werkelijk betaalt

Het tarief dat je op een dynamisch contract per kWh betaalt, is opgebouwd als: uurprijs incl. btw + energiebelasting incl. btw (0,11085) + inkoopopslag incl. btw. De day-ahead uurprijs die je leverancier doorgeeft is namelijk al inclusief btw; je moet er dus niet nog eens 21% over rekenen.

Met het jaargemiddelde van 2025 en de opslag-aanname van 0,044 euro/kWh: 0,105 + 0,11085 + 0,044 = **0,26 euro/kWh**. Dat is de rekenconstante die wij op deze site voor alle modellen gebruiken. Tibber rekent volgens de eigen tarievenpagina 0,0248 euro/kWh inkoopvergoeding, oftewel circa 0,019 euro/kWh minder dan onze opslag-aanname — op 3.500 kWh circa 67 euro per jaar. Dat is geen netto voordeel: onze aanname van 0,044 euro/kWh bevat naast de inkoopopslag ook een omslag van de vaste kosten, terwijl Tibber die apart factureert (5,99 euro per maand per energiesoort, oftewel 71,88 euro per jaar voor stroom). Die twee bedragen liggen zo dicht bij elkaar dat de vergelijking op jaarbasis ongeveer gelijk uitvalt.

De 0,26 euro/kWh is het *ongewogen* gemiddelde. Je verbruik valt echter niet gelijkmatig over de uren: een huishouden dat 's avonds kookt, wast en de auto laadt, verbruikt relatief veel in dure uren. Dat werkelijk betaalde tarief heet de load-weighted prijs en ligt hoger dan het simpele gemiddelde. Wij rekenen daarom met twee profielen, beide expliciet als aanname en beide een gemotiveerde afwijking van de 0,26:

- **Passief profiel:** load-weighted uurprijs = jaargemiddelde + 8% = 0,1134 euro/kWh → all-in **0,272 euro/kWh**.
- **Actief profiel (verbruik verschuiven):** load-weighted uurprijs = jaargemiddelde − 15% = 0,08925 euro/kWh → all-in **0,243 euro/kWh**.

De opslag van +8% en de korting van −15% zijn geen gemeten waarden maar bandbreedtes die we aannemen; wie zijn eigen kwartierdata heeft, kan de werkelijke load-weighted prijs exact uitrekenen en hier invullen.

## De drie scenario's doorgerekend

Vaste kosten in het dynamische scenario: Tibber 5,99 euro per maand voor stroom = 71,88 euro per jaar. Heb je ook gas bij dezelfde leverancier, dan geldt dat bedrag nog een keer — dat is de betekenis van "per energiesoort".

| Scenario | Jaarverbruik | Vast (0,32) | Dynamisch passief (0,272 + 72) | Dynamisch actief (0,243 + 72) | Voordeel passief | Voordeel actief |
|---|---|---|---|---|---|---|
| Klein huishouden (1-2p, geen EV) | 2.000 kWh | 640 euro | 616 euro | 558 euro | 24 euro | 82 euro |
| Gemiddeld (gezin, gasketel) | 3.500 kWh | 1.120 euro | 1.024 euro | 923 euro | 96 euro | 197 euro |
| Groot (EV + warmtepomp) | 6.000 kWh | 1.920 euro | 1.704 euro | 1.530 euro | 216 euro | 390 euro |

Wat het model laat zien: bij een klein verbruik weegt de vaste maandprijs zwaar en blijft er van het voordeel weinig over. Het voordeel schaalt mee met het verbruik en vooral met de mate waarin je verbruik kunt verschuiven. Bij 6.000 kWh levert het verschuiven zelf 174 euro op — bijna even veel als het hele verschil tussen vast en passief dynamisch (216 euro). De winst zit dus minstens zoveel in gedrag als in het contract.

Let op de gevoeligheid: het aangenomen vaste tarief van 0,32 euro/kWh bepaalt de uitkomst sterk. Ligt jouw vaste aanbod op 0,28 euro/kWh, dan verdwijnt het passieve voordeel in alle drie de scenario's en blijft alleen het actieve profiel over.

## Hoe het uurpatroon eruitziet

Het patroon over de dag is grofweg: laag 's nachts, een tweede dal midden op de dag door zonproductie, en pieken in de ochtend en vooral tussen 17:00 en 20:00. In 2025 waren er 212 uren met een negatieve prijs, en het duurste uur van het jaar was 0,63 euro/kWh incl. btw op 20 januari 2025 om 17:00.

Exacte gemiddelde tarieven per tijdvak publiceren we hier bewust niet: die verschillen sterk per maand en per jaar, en een cijfer zonder peildatum is onbruikbaar. De actuele uurprijzen van vandaag en morgen staan op onze [stroomprijzenpagina](/stroomprijzen/); daar zie je ook meteen welke uren vandaag de goedkoopste zijn.

Voor een diepere vergelijking van de leveranciers onderling: de [Tibber review](/posts/tibber-review-ervaringen-2026/) en de [Frank Energie review](/posts/frank-energie-review-ervaringen-2026/).

<div class="cta cta-affiliate">
<strong>Tibber bekijken</strong><br>
Tibber rekent 5,99 euro per maand per energiesoort plus 0,0248 euro per kWh inkoopvergoeding (peildatum augustus 2026) en is maandelijks opzegbaar. Wij ontvangen geen vergoeding als je overstapt.<br>
<a href="https://go.duurzaamthuislab.nl/tibber" rel="noopener nofollow">Naar Tibber</a>
</div>

## Verbruik verschuiven — per apparaat doorgerekend

Verschuiven betekent dat de EV-lader, vaatwasser, droger of warmtepompboiler draait in de goedkoopste uren. Tibber stuurt ondersteunde laders automatisch aan; Frank Energie biedt een vergelijkbare functie in de eigen app.

De tabel hieronder is een modelberekening met drie tarieven: vast 0,32 euro/kWh, dynamisch passief 0,272 euro/kWh en dynamisch met verschuiven. Voor apparaten die volledig naar de nachtelijke daluren kunnen (EV-laden) rekenen we met een aangenomen uurprijs van 0,07 euro/kWh → all-in 0,220 euro/kWh; voor deels verschuifbaar verbruik met 0,252 euro/kWh all-in (uurprijs −8%).

| Apparaat | Verbruik/jaar | Op vast | Dynamisch passief | Dynamisch met verschuiven |
|---|---|---|---|---|
| EV (15.000 km, 18 kWh/100 km) | 2.700 kWh | 864 euro | 734 euro | 594 euro |
| Hybride warmtepomp | 1.800 kWh | 576 euro | 490 euro | 454 euro |
| Vaatwasser dagelijks | 220 kWh | 70 euro | 60 euro | 53 euro |
| Wasdroger 3x per week | 240 kWh | 77 euro | 65 euro | 58 euro |

Een thuisbatterij kan bovenop dit voordeel handelen op het verschil tussen dal- en piekuren, maar dat resultaat hangt volledig af van de spreiding in de uurprijzen, van het aantal cycli per jaar en van de laad- en ontlaadverliezen. Wij zetten er hier geen bedrag bij; de doorrekening staat in [terugverdientijd thuisbatterij](/terugverdientijd-thuisbatterij/) en in [ROI thuisbatterij na saldering](/posts/roi-thuisbatterij-na-saldering-2027-berekening/).

## Seizoenseffect

Een jaargemiddelde verbergt dat de uitkomst per maand verschilt. In de donkere maanden is er weinig zonproductie, ligt de gemiddelde uurprijs hoger en zijn de avondpieken langer; dan kan een vast contract in die maanden gunstiger uitpakken. In het voor- en najaar met veel zon en lage middagprijzen is dynamisch duidelijk voordeliger. Je wint dus niet elke maand — wie slecht tegen een schommelend maandbedrag kan, moet dat meewegen.

Maandbedragen per maand geven we hier niet: daarvoor zouden we maandgemiddelden per jaar moeten publiceren die we niet met een controleerbare bron kunnen onderbouwen.

## Gevoeligheidsanalyse: wat bij hoge prijzen

Dit is een what-if, geen voorspelling. We variëren alleen de EPEX-prijs (incl. btw) en houden de opslag-aanname en de energiebelasting gelijk.

| Aangenomen EPEX-gemiddelde | Dynamisch all-in (model) | Vast (aanname 0,32) | Verschil |
|---|---|---|---|
| 0,21 euro/kWh (dure week) | 0,365 euro/kWh | 0,32 euro | dynamisch circa 14% duurder |
| 0,14 euro/kWh (normale winterweek) | 0,295 euro/kWh | 0,32 euro | dynamisch circa 8% goedkoper |
| 0,11 euro/kWh (winterkwartaal) | 0,265 euro/kWh | 0,32 euro | dynamisch circa 17% goedkoper |

Een enkele dure week weegt voor circa een tweeenvijftigste mee in het jaartotaal. Wie in zulke weken verbruik uit de avondpiek haalt, verkleint het effect verder.

## Wanneer een vast contract logischer is

| Situatie | Vast contract overwegen? |
|---|---|
| Geen flexibiliteit tussen 17:00 en 20:00, vast eetritueel, gasketel | Ja |
| Geen apparaten met timer of aansturing | Ja |
| Zekerheid over het maandbedrag weegt zwaarder dan het verwachte voordeel | Ja |
| Verhuizing binnen enkele maanden | Ja, weinig tijd om het voordeel te pakken |
| Verbruik onder 1.500 kWh per jaar | Vaak wel — de vaste maandprijs weegt dan zwaar |

De uitgebreide vergelijking staat in [dynamisch vs vast contract 2026](/posts/dynamisch-vs-vast-contract-2026/) en het volledige aanbodoverzicht in onze [vergelijker dynamische energiecontracten](/dynamisch-energiecontract-vergelijken/).

## Tibber en Frank naast elkaar — voor zover publiek

Beide leveranciers rekenen de day-ahead uurprijs door met een opslag. De veelgehoorde bewering dat zij "de kale beursprijs zonder marge" doorgeven, klopt niet: beide rekenen een inkoopvergoeding, en Frank Energie hanteert daarnaast sinds 1 juni 2025 een terugleverstaffel voor huishoudens met zonnepanelen.

| Aspect | Tibber | Frank Energie |
|---|---|---|
| Vaste kosten per maand | 5,99 euro per energiesoort (aug 2026) | publiceert geen consumentenprijs |
| Inkoopvergoeding per kWh | 0,0248 euro (aug 2026) | rekent een inkoopvergoeding; bedrag niet publiek |
| Terugleveren met zonnepanelen | terugleverkosten volgens actuele voorwaarden | terugleverstaffel sinds 1 juni 2025 |
| Opzegtermijn | maandelijks opzegbaar | zie voorwaarden |
| Aansturing apparaten | eigen app, ondersteunde laders | eigen app |

Omdat Frank zijn vaste kosten niet publiceert, kunnen wij de twee niet op jaartotaal vergelijken. Wie dat wil doen, vraagt bij beide een actueel tarievenoverzicht op en vult dat in het model hierboven in. ANWB Energie rekent volgens de eigen tarievenpagina 0,018 euro/kWh aan inkoopkosten; over een eventueel prijsdempingsmechanisme doen wij geen uitspraak omdat wij dat niet in de voorwaarden hebben kunnen verifieren.

<div class="cta cta-affiliate">
<strong>Frank Energie bekijken</strong><br>
Frank Energie publiceert zijn vaste kosten niet op de openbare tarievenpagina; vraag het actuele tarievenoverzicht op voordat je overstapt. Wij ontvangen geen vergoeding als je overstapt.<br>
<a href="https://go.duurzaamthuislab.nl/frank-energie" rel="noopener nofollow">Naar Frank Energie</a>
</div>

## Het model voor je eigen situatie — vijf stappen

1. **Pak je laatste jaarafrekening** en zoek je jaarverbruik in kWh.
2. **Vermenigvuldig met je eigen vaste tarief** (all-in, inclusief energiebelasting en btw). Heb je dat niet bij de hand, gebruik dan de aanname 0,32.
3. **Vermenigvuldig hetzelfde verbruik met 0,272** — het load-weighted dynamische tarief uit dit model voor een passief huishouden.
4. **Tel 71,88 euro op** voor de Tibber-maandkosten voor stroom (en nog eens 71,88 euro als je ook gas afneemt).
5. **Vergelijk.** Kun je verbruik echt verschuiven, reken stap 3 dan opnieuw met 0,243.

Voorbeeld bij 3.500 kWh: 3.500 x 0,32 = 1.120 euro vast, tegenover 3.500 x 0,272 + 71,88 = 1.024 euro dynamisch passief. Verschil: circa 96 euro. Met verschuiven: 3.500 x 0,243 + 71,88 = 923 euro, oftewel circa 197 euro voordeel.

## Zonnepanelen: wat verandert er per 1 januari 2027

De salderingsregeling **stopt volledig per 1 januari 2027**. Er is geen afbouwpad en geen percentage dat daarna nog geldt: vanaf die datum verrekent je leverancier de teruggeleverde stroom niet meer tegen je afnametarief, maar geldt de terugleververgoeding uit je contract, verminderd met eventuele terugleverkosten.

Op een dynamisch contract wordt teruglevering afgerekend tegen de uurprijs van dat moment. Dat pakt op zonnige middagen laag uit — dat is precies wanneer de meeste panelen produceren — maar levert in de avonduren juist meer op dan een vaste terugleververgoeding. Welke vorm gunstiger is, hangt dus af van hoeveel je zelf verbruikt en of je met een batterij of slimme aansturing kunt schuiven. De volledige uitleg staat in [saldering stopt 2027](/posts/saldering-stopt-2027-volledige-gids/). Concrete bedragen noemen we niet: die hangen af van contractvoorwaarden die per leverancier verschillen en die per 2027 nog kunnen wijzigen.

## Risico's en beperkingen van dit model

- **De uitkomst staat of valt met het vaste tarief waarmee je vergelijkt.** Dat is de gevoeligste aanname in het hele model.
- **De load-weighted opslag is een aanname**, geen meting. Wie eigen kwartierdata heeft, kan het exact berekenen.
- **Prijzen kunnen sterk stijgen.** In koude, windstille periodes lopen de uurprijzen op; het jaareffect blijft beperkt, het maandeffect niet.
- **Verschuiven vereist inspanning.** Zonder aanstuurbare apparaten en instelwerk blijft alleen het passieve voordeel over.
- **Tarieven wijzigen.** Alle bedragen hierboven hebben peildatum augustus 2026; controleer ze op de tarievenpagina van de leverancier.

Voor onafhankelijke informatie over je rechten als energieconsument: [ConsuWijzer van de ACM](https://www.consuwijzer.nl/energie).

## Samenvatting

Op basis van dit model levert een dynamisch contract een huishouden van 3.500 kWh circa 96 euro per jaar op zonder gedragsverandering en circa 197 euro met actief verschuiven, afgezet tegen een aangenomen vast tarief van 0,32 euro/kWh. Bij 2.000 kWh is het verschil klein genoeg om te verdwijnen bij een iets scherper vast aanbod; bij 6.000 kWh met een elektrische auto loopt het op tot bijna 400 euro.

Wat je vandaag kunt doen: vul je eigen jaarverbruik en je eigen vaste tarief in de vijfstappenmethode in, en kijk daarna op de [stroomprijzenpagina](/stroomprijzen/) hoe de uurprijzen zich in jouw week gedragen.

Lees ook de [Tibber review](/posts/tibber-review-ervaringen-2026/), onze [vergelijker dynamische energiecontracten](/dynamisch-energiecontract-vergelijken/) en de [Sessy thuisbatterij review](/posts/sessy-review-thuisbatterij-nederland/).
