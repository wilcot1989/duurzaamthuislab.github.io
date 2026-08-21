---
title: 'ANWB Energie review 2026: dynamisch contract met vlakke maandlasten'
date: 2026-05-09 08:00:00+02:00
lastmod: '2026-08-21 08:00:00+02:00'
description: ANWB Energie Dynamisch werkt met een vast maandtermijnbedrag en jaarverrekening. Wat de inkoopkosten zijn, voor wie het past en waar het niet de scherpste keuze is.
categories:
- energie
tags:
- ANWB Energie
- dynamisch contract
- review
- energieleverancier
keywords:
- anwb energie review
- anwb dynamisch
- anwb energie ervaringen
- anwb dynamisch contract
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: Wat is ANWB Energie Dynamisch?
  a: 'ANWB Energie levert een dynamisch contract waarbij je per uur de actuele EPEX day-ahead marktprijs betaalt. ANWB rekent daarbovenop inkoopkosten van €0,018/kWh incl. btw (anwb.nl, peildatum 21 augustus 2026) en vaste leveringskosten. Het onderscheidende kenmerk is de facturering: je betaalt een vast maandtermijnbedrag met jaarverrekening, waardoor je maandlasten vlak blijven.'
- q: Heeft ANWB een prijsplafond op de uurprijs?
  a: 'Nee, voor zover wij kunnen nagaan. Er circuleert het beeld dat ANWB extreme uurprijzen zou afvlakken of afkappen. Wij hebben zo''n plafond of dempingsmechanisme niet op anwb.nl kunnen verifiëren (peildatum 21 augustus 2026) en rekenen er in dit artikel dan ook niet mee. Wat ANWB wél doet, is je maandlasten vlakken via een vast termijnbedrag — het verbruik zelf wordt gewoon tegen de uurprijs afgerekend, alleen later.'
- q: Wat is het verschil met Tibber of Frank?
  a: 'Op de kWh: Tibber rekent €0,0248/kWh inkoopvergoeding, ANWB €0,018/kWh, Frank rekent geen marge op EPEX. Op de vaste kosten: Tibber vraagt €5,99 per maand per energiesoort (stroom en gas apart), ANWB en Frank publiceren hun vaste kosten niet op één vaste plek — opvragen dus. Op de facturering: alleen ANWB werkt met een vast termijnbedrag met jaarverrekening.'
- q: Voor wie is ANWB Energie geschikt?
  a: Voor wie de gemiddelde besparing van een dynamisch contract wil, maar geen zin heeft in een maandrekening die na een koudegolf verdubbelt. Het vaste termijnbedrag vlakt je cashflow. Ook voor wie telefonische klantenservice belangrijk vindt.
- q: Werkt ANWB met zonnepanelen?
  a: Ja. ANWB rekent volgens de eigen site geen aparte terugleverkosten (peildatum 21 augustus 2026). Bij teruglevering krijg je het uurtarief van dat moment — op zonnige middagen kan dat laag of zelfs negatief zijn. Zolang de saldering geldt (tot 1 januari 2027) wordt teruglevering verrekend met je afname.
- q: Hoe goed is de app?
  a: 'Functioneel. De app toont uurprijzen, verbruik en de prijzen voor de volgende dag. Er is geen open API en geen native slim-laden voor elektrische auto''s, zoals Tibber die wel heeft. Voor wie alleen wil weten wat hij betaalt: voldoende. Voor Home Assistant-gebruikers: te beperkt.'
- q: Wat als je wilt overstappen?
  a: 'ANWB regelt de opzegging bij je vorige leverancier. Volgens de eigen site geldt een opzegtermijn van 30 dagen zonder boete (peildatum 21 augustus 2026). Zit je nog in een lopend vast contract, check dan eerst de opzegvergoeding daar: de ACM begrenst die tot €50 tot €125 per energievorm.'
- q: Wat is de jaarbesparing vs een vast contract?
  a: 'Dat hangt volledig af van je verbruik en van het vaste maandbedrag dat ANWB jou rekent. In onze modelberekening hieronder (3.500 kWh, EPEX-jaargemiddelde 2025 van €0,105/kWh incl. btw) komt het variabele deel bij ANWB op circa €818 per jaar tegen €1.120 bij een vast contract van €0,32/kWh all-in. Die €0,32 is een gelabelde aanname: ligt het vaste tarief dat jij kunt krijgen op €0,28, dan verdwijnt het voordeel van passief dynamisch afnemen vrijwel volledig. Tel daar de vaste kosten van beide contracten bij op voordat je de besparing hard maakt.'
- q: Wat zijn de nadelen?
  a: 'Drie zaken: (1) de inkoopkosten van €0,018/kWh maken ANWB per kWh duurder dan Frank, (2) er is geen open API en geen native slim laden voor EV''s, (3) het vaste termijnbedrag vlakt je cashflow maar verlaagt je jaarkosten niet — een dure winter kom je bij de jaarafrekening alsnog tegen.'
schema_type: Review
---
De meest gehoorde reden om bij een vast contract te blijven is niet de prijs, maar de piek: de angst voor een maandrekening die na een koude, windstille week ineens verdubbelt. ANWB Energie Dynamisch speelt daar op in — alleen anders dan vaak wordt gedacht.

Onze conclusie vooraf: ANWB is een verdedigbare tussenoplossing, maar niet de scherpste keuze. Je betaalt inkoopkosten per kWh die hoger liggen dan bij Frank, en de "bescherming" die ANWB biedt zit in de facturering, niet in de prijs.

*Werkwijze: deze analyse is gebaseerd op de publieke tarieven- en voorwaardenpagina's van ANWB Energie (peildatum 21 augustus 2026) en op EPEX day-ahead-marktdata. Wij meten niet zelf en hebben geen contract bij ANWB.*

*Disclosure: wij hebben geen affiliate- of commissierelatie met ANWB Energie, Tibber of Frank Energie (stand augustus 2026). Wij ontvangen geen vergoeding als je via een link op deze pagina een contract afsluit.*

---

> **Kort antwoord:** ANWB Energie Dynamisch rekent de EPEX-uurprijs door plus €0,018/kWh inkoopkosten incl. btw (anwb.nl, peildatum 21 augustus 2026) en vaste leveringskosten. Het onderscheidende kenmerk is niet een prijsplafond — dat hebben wij niet kunnen verifiëren — maar een vast maandtermijnbedrag met jaarverrekening. Dat vlakt je maandlasten; het verlaagt je jaarkosten niet.

## Eerst het misverstand uit de weg: is er een prijsplafond?

Op fora en in vergelijkers duikt met enige regelmaat het beeld op dat ANWB een plafond of dempingsmechanisme op de uurprijs zou hanteren, bijvoorbeeld boven €0,40/kWh. Wij hebben dat op anwb.nl niet kunnen terugvinden (peildatum 21 augustus 2026), en ANWB beschrijft het eigen product juist als een één-op-één doorgifte van marktprijs en inkoopkosten.

Wij rekenen in dit artikel daarom **niet** met een plafond. Kom je een vergelijking tegen die dat wel doet, vraag dan door naar de bron. Zolang die er niet is, moet je ervan uitgaan dat je bij ANWB net als bij Tibber en Frank de volle uurprijs betaalt.

Wat er wél staat: ANWB werkt met een **vast maandtermijnbedrag met jaarverrekening**. Je uurprijzen volgen de markt, maar je maandlasten blijven gelijk tot de jaarafrekening. Dat is een reëel verschil met leveranciers die maandelijks je werkelijke verbruik factureren — maar het is een cashflow-verschil, geen kortingsmechanisme.

## ANWB Energie in context

ANWB is met enkele miljoenen leden een van de grootste consumentenorganisaties van Nederland. De energiedivisie is relatief jong en bedient volgens de eigen site bijna 200.000 huishoudens (peildatum 21 augustus 2026). In tegenstelling tot Tibber (Noors) of Frank Energie (Nederlands, kleiner) leunt ANWB op een lang opgebouwde naamsbekendheid.

Dat bepaalt ook de positionering: ANWB richt zich op de consument die dynamisch wil maar niet dagelijks naar EPEX-grafieken wil kijken. Dat is een legitieme niche — en het betekent dat je als Home Assistant-gebruiker of maximale-bespaarder waarschijnlijk beter af bent bij een andere partij.

## Wat ANWB rekent

De tariefopbouw bij een dynamisch contract bestaat uit vier lagen. Drie daarvan zijn voor elke leverancier gelijk:

- **EPEX day-ahead uurprijs** — de kale marktprijs, verschilt per uur
- **Energiebelasting** — in 2026 €0,09161/kWh excl. btw, oftewel €0,11085/kWh incl. btw. De ODE bestaat sinds 2023 niet meer als aparte heffing
- **Netbeheerkosten** — een vast jaarbedrag voor je aansluiting, per netbeheerder verschillend en niet afhankelijk van je leverancier
- **De opslag van je leverancier** — hier zit het verschil

Bij ANWB bestaat die laatste laag uit twee posten:

- **Inkoopkosten €0,018/kWh incl. btw** (anwb.nl, peildatum 21 augustus 2026)
- **Vaste leveringskosten per maand** — het bedrag staat op de tarievenpagina van ANWB en wijzigt per periode; wij nemen het niet als vast getal over

ANWB stelt zelf geen winst te maken op je verbruik en alleen te verdienen aan de vaste leveringskosten. Die claim is niet te controleren zonder inzage in hun inkoop, maar hij is wel consistent met de gepubliceerde tariefopbouw.

## Modelberekening: drie profielen

Onderstaand een **modelberekening**, geen meting. De aannames staan er expliciet bij zodat je ze met je eigen cijfers kunt vervangen.

**Aannames:**

| Variabele | Waarde | Bron |
|---|---|---|
| EPEX-jaargemiddelde 2025 | €0,105/kWh incl. btw | EPEX day-ahead via EnergyZero, geteld door onze redactie, peildatum 21 augustus 2026 |
| Energiebelasting stroom 2026 | €0,11085/kWh incl. btw (€0,09161 excl. btw) | Belastingtarieven 2026; de ODE bestaat sinds 2023 niet meer |
| Btw | 21%, al verwerkt in de bedragen in deze tabel | — |
| Inkoopkosten ANWB | €0,018/kWh incl. btw | anwb.nl, peildatum 21 augustus 2026 |
| Inkoopvergoeding Tibber | €0,0248/kWh incl. btw | tibber.com, peildatum 21 augustus 2026 |
| Vaste kosten Tibber | €5,99/mnd per energiesoort (hier: alleen stroom, €72/jaar) | tibber.com |
| Marge Frank op EPEX | €0,00/kWh; vaste kosten niet publiek | frankenergie.nl |
| Benchmark vast contract | €0,32/kWh all-in | modelaanname — een vast contract bevat een risicopremie en ligt daarom boven het dynamische tarief. Gevoelig: bij €0,28/kWh verdwijnt het voordeel van passief dynamisch afnemen volledig |

Netbeheerkosten laten wij buiten de vergelijking: dat is een vast jaarbedrag dat bij elke leverancier hetzelfde is.

De basis onder alle drie de dynamische contracten is dezelfde: €0,105 EPEX incl. btw + €0,11085 energiebelasting incl. btw = **€0,216/kWh all-in**. De beursprijzen die wij gebruiken zijn al inclusief btw, dus er komt geen extra btw-opslag meer over de basis. Daarbovenop komt de opslag van de leverancier, die ook al inclusief btw is:

- **Frank:** €0,216 + geen marge = **€0,216/kWh** (plus onbekende vaste kosten)
- **ANWB:** €0,216 + €0,018 = **€0,234/kWh** (plus onbekend vast maandbedrag)
- **Tibber:** €0,216 + €0,0248 = **€0,241/kWh** (plus €72/jaar vaste kosten)

Ter oriëntatie hanteren wij op deze site een all-in modelconstante van **€0,26/kWh** voor dynamische stroom, opgebouwd uit €0,105 EPEX incl. btw + €0,11085 energiebelasting incl. btw + €0,044 aan inkoopopslag en omgeslagen vaste kosten (aanname, incl. btw). Die constante ligt dus bewust boven de kale leveranciersbasis; Tibber en ANWB komen er met hun vaste kosten meegerekend in de buurt, Frank blijft eronder.

**Profiel 1 — appartement, geen zonnepanelen, 2.800 kWh afname**

| Contract | Variabele kosten | Vaste kosten | Totaal |
|---|---|---|---|
| Vast contract €0,32/kWh | €896 | n.v.t. | €896 |
| ANWB Dynamisch | €655 | zie anwb.nl | €655 + vast bedrag |
| Tibber | €674 | €72 | €746 |
| Frank Energie | €604 | zie frankenergie.nl | €604 + vast bedrag |

**Profiel 2 — tussenwoning met 10 zonnepanelen, 3.500 kWh netto afname na saldering**

| Contract | Variabele kosten | Vaste kosten | Totaal |
|---|---|---|---|
| Vast contract €0,32/kWh | €1.120 | n.v.t. | €1.120 |
| ANWB Dynamisch | €818 | zie anwb.nl | €818 + vast bedrag |
| Tibber | €842 | €72 | €914 |
| Frank Energie | €755 | zie frankenergie.nl | €755 + vast bedrag |

**Profiel 3 — vrijstaand huis met 20 zonnepanelen, 5.200 kWh netto afname na saldering**

| Contract | Variabele kosten | Vaste kosten | Totaal |
|---|---|---|---|
| Vast contract €0,32/kWh | €1.664 | n.v.t. | €1.664 |
| ANWB Dynamisch | €1.216 | zie anwb.nl | €1.216 + vast bedrag |
| Tibber | €1.251 | €72 | €1.323 |
| Frank Energie | €1.122 | zie frankenergie.nl | €1.122 + vast bedrag |

**Wat hieruit volgt:**

Het verschil tussen ANWB en Tibber op de kWh is €0,0068 — bij 3.500 kWh gaat het om €24 per jaar in het voordeel van ANWB, dat bij Tibber weer wordt ingehaald door de vaste kosten van €72 en omgekeerd door het vaste maandbedrag van ANWB. Met andere woorden: **op de variabele kosten liggen ANWB en Tibber vrijwel gelijk, en de keuze wordt beslist door de vaste kosten en de features.**

Frank is per kWh structureel goedkoper omdat er geen inkoopopslag is: €0,018/kWh × 3.500 kWh = €63 per jaar verschil met ANWB. Of Frank onder de streep goedkoper uitpakt, kunnen wij niet hard maken — Frank publiceert de vaste kosten niet, en rekent sinds 1 juni 2025 bovendien een terugleverstaffel die bij zonnepanelen meetelt. Vraag beide op voordat je de keuze maakt.

Belangrijk: alle bovenstaande bedragen zijn gebaseerd op het jaargemiddelde van 2025. Wie zijn verbruik actief naar goedkope uren verschuift, betaalt structureel minder dan dat gemiddelde; wie alles op vaste tijden draait, meer.

## Vergelijking op kenmerken

| Aspect | ANWB Energie | Tibber | Frank Energie |
|---|---|---|---|
| Vaste kosten/mnd | Zie anwb.nl | €5,99 per energiesoort | Zie frankenergie.nl |
| Opslag per kWh | €0,018 inkoopkosten (incl. btw) | €0,0248 inkoopvergoeding | Geen marge op EPEX |
| Prijsplafond op uurprijs | Niet geverifieerd | Nee | Nee |
| Vlakke maandlasten | Ja (vast termijnbedrag, jaarverrekening) | Nee | Nee |
| Terugleverkosten | Geen (anwb.nl) | Geen | Staffel sinds 1-6-2025 |
| Telefonische support | Ja | Nee (chat) | Ja (werkdagen) |
| Open API | Nee | Ja | Via derden |
| Native slim laden EV | Nee | Ja (auto-API) | Via EVCC/derden |
| Opzegtermijn | 30 dagen, geen boete | Maandelijks opzegbaar | Zie voorwaarden |

## Voor wie ANWB goed is

**1. Wie een dure winterweek niet in één maand kan opvangen.** Het vaste termijnbedrag is hier het echte argument. Tijdens de koudegolf van januari 2025 lag de duurste uurprijs op €0,63/kWh (20 januari, 17:00; EPEX day-ahead incl. btw via EnergyZero, geteld door onze redactie, peildatum 21 augustus 2026). Bij een leverancier die maandelijks je werkelijke verbruik factureert, zie je zo'n week direct terug. Bij ANWB blijft de maandlast gelijk en komt het verschil bij de jaarafrekening. Snap wel wat dat is: uitstel, geen korting.

**2. Wie telefonisch contact wil.** Frank en Tibber zijn overwegend chat-gedreven. ANWB heeft een telefonische klantenservice. Voor wie daar waarde aan hecht — en dat is een reële groep — telt dat.

**3. Wie zonnepanelen heeft en geen terugleverkosten wil.** ANWB rekent volgens de eigen site geen aparte terugleverkosten. Dat is een concreet verschil met Frank, dat sinds 1 juni 2025 een terugleverstaffel hanteert, en met de meeste vaste contracten.

**4. Wie een gevestigde naam prefereert.** Geen "wat als deze startup omvalt"-zorg.

## Voor wie ANWB niet de beste keus is

**1. EV-rijders en smart-home gebruikers.** Geen native auto-API, geen open API. Wie zijn auto automatisch op de goedkoopste uren wil laden of zijn warmtepomp op de prijs wil sturen, komt bij Tibber verder.

**2. Wie op de laatste euro stuurt.** De inkoopkosten van €0,018/kWh kosten bij 3.500 kWh €63 per jaar meer dan bij Frank. Over vijf jaar is dat ruim €300.

**3. Wie maximaal wil profiteren van lage en negatieve uren.** Zonder open API en zonder automatisering moet je alles handmatig plannen. Dat kán — de app toont de prijzen voor de volgende dag — maar het vergt discipline.

## Veelgemaakte fouten bij het overstappen

**Fout 1: overstappen zonder je verbruiksgewoonten aan te passen.** Een dynamisch contract rendeert pas echt als je verbruik verschuift. Wie doorgaat met wassen om 18:00, betaalt voor flexibiliteit zonder er iets voor terug te krijgen.

**Fout 2: niet checken of je in een boeteperiode zit.** Overstappen uit een lopend vast contract kan een opzegvergoeding kosten. De ACM begrenst die tot €50 tot €125 per energievorm. Reken die mee in je eerste jaar.

**Fout 3: rekenen op een prijsplafond dat er niet aantoonbaar is.** Zie de eerste paragraaf van dit artikel. Wie een dynamisch contract afsluit omdat "ANWB de pieken afvlakt", baseert die keuze op iets wat wij niet hebben kunnen verifiëren.

**Fout 4: het vaste termijnbedrag voor besparing aanzien.** Een vlakke maandlast is geen lage jaarrekening. Controleer je jaarafrekening en pas je termijnbedrag aan als het structureel te laag of te hoog staat.

## Saldering stopt op 1 januari 2027: wat betekent dat?

Per 1 januari 2027 stopt de salderingsregeling volledig. Er is geen afbouwpad: het wetsvoorstel met een stapsgewijze afbouw is verworpen. Tot en met 31 december 2026 saldeer je dus nog voor 100%, daarna niet meer.

Voor dynamische contracten betekent dat: je teruggeleverde stroom wordt vanaf 2027 apart afgerekend tegen de uurprijs van het moment van teruglevering. Op zonnige middagen is dat vaak laag en soms negatief, terwijl je 's avonds tegen een hoger tarief inkoopt. Dat verschil is precies waar een thuisbatterij of slim laden van een EV waarde toevoegt.

Wat ANWB na 1 januari 2027 precies gaat hanteren voor teruglevering, is op het moment van schrijven niet gepubliceerd. Wij nemen daarover geen verwachting op — check de tarievenpagina van ANWB als de voorwaarden voor 2027 bekend zijn.

Lees verder: [saldering stopt in 2027 — volledige gids](/posts/saldering-stopt-2027-volledige-gids/).

## Actief sturen op de dagprijzen: wat levert dat op?

ANWB toont de uurprijzen voor de volgende dag in de app. Hieronder de rekenregel waarmee je zelf kunt uitrekenen wat verschuiven oplevert, met een modelvoorbeeld erbij.

**De rekenregel:** het verschil tussen een duur en een goedkoop uur is simpelweg het verschil in marktprijs zelf — EPEX duur − EPEX goedkoop. Die marktprijzen zijn al inclusief btw, dus er komt geen btw-factor meer bij. De energiebelasting en de inkoopkosten zijn in beide gevallen gelijk en vallen tegen elkaar weg.

Modelaanname: een verschil van **€0,30/kWh incl. btw** tussen een duur avonduur en een goedkoop nachtuur — dat is dus ook precies het verschil op de marktprijs. Een normale spreiding, geen extreme dag.

| Apparaat | Verbruik per beurt | Verschil per beurt | Beurten/jaar | Modelbesparing |
|---|---|---|---|---|
| Wasmachine 30°C | 0,5 kWh | €0,15 | 150 | €23 |
| Vaatwasser eco | 0,8 kWh | €0,24 | 208 | €50 |
| Droger (condens) | 2,0 kWh | €0,60 | 100 | €60 |

Bij elkaar praat je in dit model over ruim €130 per jaar, bovenop het basisverschil tussen dynamisch en vast. Het klopt alleen als je het daadwerkelijk elke keer doet — reken met je eigen aantal beurten en met de spreiding die jij in de app ziet, niet met deze getallen.

Voor grote posten wordt het interessanter. Een EV die 3.200 kWh per jaar laadt, scheelt bij €0,30 verschil per kWh ruim €950 tussen "altijd om 18:00" en "altijd 's nachts". Dat is precies waar de ontbrekende automatisering van ANWB voelbaar wordt: je moet het handmatig plannen.

## Overstapproces

**Stap 1 — offerte.** Via anwb.nl/energie vul je je huidige contract, jaarverbruik en adres in.

**Stap 2 — ondertekenen.** ANWB regelt de opzegging bij je vorige leverancier. Controleer of je daar nog in een boeteperiode zit; die vergoeding betaalt ANWB niet.

**Stap 3 — verwerking.** Reken op enkele weken tussen ondertekening en de daadwerkelijke overstapdatum.

**Stap 4 — eerste factuur.** Vanaf dat moment zie je de uurprijzen in de app en wordt je afname per uur verrekend, met een vast maandbedrag als termijn.

**Let op:** controleer na de overstap of de uurmeting daadwerkelijk in de app staat. Komt de P1-data na twee weken nog niet correct door, meld dat dan bij de klantenservice — zonder die data zie je je verbruik niet per uur.

## Onze aanbeveling

**ANWB is een logische keuze voor:**

- huishoudens die dynamisch willen maar geen schommelende maandlast kunnen dragen
- mensen die telefonische klantenservice belangrijk vinden
- zonnepaneelbezitters die geen terugleverkosten willen betalen

**ANWB is niet de beste keuze voor:**

- EV-rijders en Home Assistant-gebruikers (dan Tibber)
- wie op de laagste kosten per kWh stuurt (dan Frank, mits de vaste kosten meevallen)

[Lees onze Tibber review →](/posts/tibber-review-ervaringen-2026/) · [Frank Energie review →](/posts/frank-energie-review-ervaringen-2026/)

---

## Conclusie

ANWB Energie Dynamisch is een degelijke, niet-scherpe optie. De inkoopkosten van €0,018/kWh liggen tussen Frank (geen opslag) en Tibber (€0,0248) in, de vaste kosten zijn niet publiek en de app is functioneel maar zonder automatisering.

De belangrijkste correctie op het beeld dat over dit contract bestaat: **ANWB dempt je maandlast, niet je uurprijs.** Een prijsplafond hebben wij niet kunnen verifiëren. Wie voor de zekerheid van een vlakke maandrekening kiest, krijgt precies dat — en betaalt aan het eind van het jaar alsnog de werkelijke uurprijzen.

<a href="https://go.duurzaamthuislab.nl/anwb-energie" class="cta cta-affiliate" target="_blank" rel="nofollow noopener">Bekijk ANWB Energie</a>

*Wij ontvangen geen vergoeding als je via deze link een contract afsluit.*

*Vragen? Mail [info@duurzaamthuislab.nl](mailto:info@duurzaamthuislab.nl).*

---

## Gerelateerde artikelen

- [Beste dynamisch energiecontract 2026](/posts/beste-dynamisch-energiecontract-2026/)
- [Saldering vs dynamisch contract: rekenmodel](/posts/saldering-vs-dynamisch-contract-rekenmodel/)
- [Tibber review en ervaringen](/posts/tibber-review-ervaringen-2026/)
- [Frank Energie review](/posts/frank-energie-review-ervaringen-2026/)
- [Saldering stopt 2027: volledige gids](/posts/saldering-stopt-2027-volledige-gids/)
