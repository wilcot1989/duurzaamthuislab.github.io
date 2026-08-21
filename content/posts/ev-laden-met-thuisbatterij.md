---
title: 'EV laden met thuisbatterij: levert het geld op?'
date: 2026-07-08 08:00:00+02:00
lastmod: 2026-08-21 08:00:00+02:00
description: 'Wanneer loont het om je elektrische auto en een thuisbatterij te combineren? Modelberekeningen met een dynamisch contract, vóór en ná het einde van de saldering.'
categories:
- elektrische-auto
tags:
- EV laden thuisbatterij
- slim laden elektrische auto
- V2H bidirectioneel laden
- dynamisch energiecontract
- thuisbatterij saldering
keywords:
- EV laden met thuisbatterij
- elektrische auto thuisbatterij combinatie
- V2H laden
- bidirectioneel laden Nederland
- slim laden dynamisch contract
- Sessy EV laden
- thuisbatterij EV combinatie rendabel
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1671785253964-bdb43087ed99&w=1200&output=webp&q=70
faq:
- q: Kan ik mijn elektrische auto laden via mijn thuisbatterij?
  a: 'Technisch kan dat, maar het is zelden de verstandigste route. Een thuisbatterij van 10 kWh is klein ten opzichte van een laadsessie van een EV, en elke extra opslagstap kost rendement. In de meeste huishoudens levert het meer op om de auto direct in de goedkoopste netuuren te laden en de thuisbatterij het huis te laten voeden.'
- q: Wat is het verschil tussen V2L, V2H en V2G?
  a: 'V2L (Vehicle to Load) is een stopcontact in de auto voor losse apparaten. V2H (Vehicle to Home) voedt het huis via een bidirectionele omvormer. V2G (Vehicle to Grid) levert terug aan het net. In Nederland is V2G nog geen breed beschikbaar consumentenproduct.'
- q: Welke elektrische auto''s ondersteunen bidirectioneel laden?
  a: 'De ondersteuning verschilt sterk per merk, per model en per bouwjaar, en fabrikanten voegen modellen toe of schrappen functies via software-updates. Controleer daarom altijd de actuele specificatie van het exacte model en bouwjaar bij de importeur, in plaats van af te gaan op een lijst in een artikel. In de praktijk zijn het vooral modellen op 800V- en Hyundai/Kia-platforms die V2L en V2H bieden.'
- q: Heb ik een speciale laadpaal nodig voor V2H?
  a: 'Ja. Een gewone laadpaal laadt alleen van net naar auto. Voor V2H heb je een bidirectionele omvormer of laadpaal nodig. Die zijn in Nederland beperkt leverbaar en de fabrikanten publiceren er geen consumentenprijs voor; reken op een veelvoud van een gewone laadpaal en vraag een offerte inclusief installatie.'
- q: Is een thuisbatterij of een EV-accu voordeliger als opslagoptie?
  a: 'Per kWh is de auto-accu goedkoper, simpelweg omdat je die al hebt. Maar de auto staat niet altijd thuis, en dat is precies wanneer je de opslag nodig hebt. Een thuisbatterij is als continue buffer betrouwbaarder; een EV-accu is alleen interessant als de auto overdag en ''s avonds daadwerkelijk aan de lader hangt.'
- q: Wat levert een dynamisch contract op bij slim laden?
  a: 'Dat is de grootste en goedkoopste winst in dit hele verhaal, omdat er geen hardware voor nodig is. De rekenregel: je jaarlijkse laadvolume in kWh × het verschil tussen het tarief dat je nu betaalt en het tarief van de nachturen waarnaar je verschuift. Wij rekenen op deze site met €0,32 per kWh all-in als vaste-contractreferentie en met €0,220 per kWh all-in voor EV-laden in de nachturen (beide gelabelde aannames). Dat is €0,10 verschil: bij 2.700 kWh laadverbruik circa €270 per jaar. Vul je eigen tariefblad in.'
- q: Wordt de combinatie EV plus thuisbatterij rendabeler na 2027?
  a: 'Ja. De saldering stopt volledig per 1 januari 2027 — er is geen afbouwpad. Zolang je saldeert, is een teruggeleverde kWh evenveel waard als een afgenomen kWh en levert extra eigen verbruik vrijwel niets op. Vanaf 2027 is het verschil tussen je afnameprijs en de terugleververgoeding wél de waarde van elke kWh die je zelf opslaat en gebruikt.'
- q: 'Wat kost een complete setup: zonnepanelen, thuisbatterij en bidirectionele laadpaal?'
  a: 'Dat hangt te veel van je dak en je meterkast af om er één bedrag op te plakken. Wat je wel kunt vastzetten: zonnepanelen vallen onder het 0%-btw-tarief, een thuisbatterij niet — daar geldt 21% btw. Vraag drie all-in offertes en reken de terugverdientijd door met de rekenregels in dit artikel, niet met een bedrag uit een folder.'
schema_type: Article
---
De combinatie van een elektrische auto en een thuisbatterij klinkt logisch: overdag zonnestroom opslaan, 's avonds de auto laden uit de batterij. In de praktijk gaat het geregeld anders dan verwacht, en de reden is bijna altijd dezelfde: de volgorde. Wordt de thuisbatterij 's avonds leeggetrokken door een laadsessie, dan laadt diezelfde batterij 's nachts weer bij uit het net — met omzetverliezen erbij. Zonder goede sturing werkt de combinatie tegen je.

Hieronder rekenen wij door wanneer EV laden via een thuisbatterij wél loont, welke techniek daarvoor nodig is en hoe de rekensom verandert zodra de saldering per 1 januari 2027 stopt.

*Disclosure: de links naar Sessy en Zonneplan in dit artikel zijn gewone verwijzingen — wij hebben met deze partijen geen affiliate- of commissierelatie en ontvangen hiervoor geen vergoeding. De berekeningen hieronder zijn modelberekeningen met zichtbare aannames, geen metingen.*

---

💡 *Niet zeker wat er per 1 januari 2027 verandert? Lees de [Saldering 2027 transitie-planner](/posts/saldering-2027-transitie-planner/).*

> **Kort antwoord:** het goedkoopste rendement zit niet in hardware maar in sturing — een dynamisch contract met slim laden vraagt geen investering en levert direct op.
>
> Een thuisbatterij verdient zich in deze combinatie pas terug ná het einde van de saldering, en zelfs dan komt de terugverdientijd in ons model uit rond de twintig jaar (rond de vijftien jaar als je op een dynamisch contract ook op de uurprijzen handelt). V2H (de auto-accu als thuisbatterij) is rekenkundig het interessantst, maar alleen als de auto overdag daadwerkelijk thuis aan de lader hangt.

## Hoe werkt de combinatie eigenlijk?

Een thuisbatterij slaat energie op en geeft die af. Een elektrische auto heeft ook een accu — meestal een veelvoud van de thuisbatterij. De vraag is hoe je die twee op elkaar afstemt.

Er zijn drie basisscenario's:

**Scenario 1: gescheiden systemen (meest voorkomend).** De thuisbatterij regelt het huis, de laadpaal laadt de auto rechtstreeks uit het net of van de panelen. Voordeel: simpel. Nadeel: zonder sturing trekt de auto de thuisbatterij leeg op het verkeerde moment.

**Scenario 2: gecombineerd via slimme sturing.** Een energiemanagementsysteem bepaalt wanneer de batterij het huis voedt en wanneer de laadpaal actief is. Dat is de configuratie waarin de combinatie doet wat je ervan verwacht.

**Scenario 3: bidirectioneel laden (V2H/V2G).** De auto-accu functioneert als thuisbatterij. Vereist zowel een geschikte auto als een bidirectionele omvormer.

### Wat zijn V2L, V2H en V2G?

| Techniek | Wat het doet | Status in Nederland, augustus 2026 |
|---|---|---|
| V2L (Vehicle to Load) | Stopcontact in de auto voor losse apparaten | Beschikbaar op een deel van de modellen |
| V2H (Vehicle to Home) | Auto voedt het huis via een bidirectionele omvormer | Technisch mogelijk, beperkt aantal installateurs |
| V2G (Vehicle to Grid) | Terugleveren aan het net vanuit de auto-accu | Pilots, geen breed consumentenproduct |

V2G is voor de meeste huishoudens nog niet relevant. V2H is beschikbaar maar duur. V2L is de instapoptie die nu al werkt.

---

## De rekensommen

### Basiscase: laadpaal plus dynamisch contract, zonder thuisbatterij

Aannames in dit model: 15.000 km per jaar, verbruik 18 kWh per 100 km, dus 2.700 kWh laadverbruik per jaar.

- Vaste-contractreferentie à €0,32/kWh all-in: 2.700 × €0,32 = **€864 per jaar**
- Dynamisch contract, laden in de nachturen à €0,220/kWh all-in: 2.700 × €0,220 = **€594 per jaar**
- Verschil in dit model: **circa €270 per jaar**

Waarom het nachttarief niet lager kan: een all-in kWh bevat altijd €0,11085 energiebelasting incl. btw plus onze opslag-aanname van €0,044 incl. btw, samen €0,155. Ook bij een marktprijs van nul kom je daar niet onder. Onze €0,220 is opgebouwd uit €0,07 marktprijs incl. btw in de nachturen plus die €0,155. Bedragen die je elders ziet van 9 of 10 cent all-in kunnen dus niet kloppen.

Let op wat hier gebeurt: die besparing komt volledig uit het verschuiven van het tijdstip. Er is geen thuisbatterij voor nodig. Beide tarieven zijn gelabelde aannames — vul je eigen tariefblad in en de uitkomst schuift mee. Twee gevoeligheden: is je vaste tarief €0,28 in plaats van €0,32, dan blijft er circa €162 over; laad je al op een dynamisch contract maar zonder sturing (wij rekenen dan met €0,272 all-in), dan levert het verschuiven naar de nacht circa €140 per jaar op.

### Case 2: thuisbatterij van 10 kWh naast zonnepanelen

Aannames: 16 panelen (6,4 kWp) met een opbrengst van 5.500 kWh per jaar, een huishoudverbruik van 3.500 kWh, eigen verbruik zonder batterij 35 procent (1.925 kWh), afnameprijs €0,26/kWh all-in, terugleververgoeding ná 2027 €0,07/kWh (gelabelde aanname, niemand publiceert dit tarief nog), round-trip rendement van de batterij 90 procent.

Hoeveel een batterij daadwerkelijk kan verschuiven, is niet zijn capaciteit maal 365. Wij rekenen met de laagste van drie grenzen: capaciteit × 150 zoncycli (10 × 150 = 1.500 kWh), het zonoverschot × 90 procent (3.575 × 0,9 = 3.218 kWh) en de netto netafname die je nog kunt vervangen (3.500 − 1.925 = 1.575 kWh). De bindende grens is hier de eerste: **1.500 kWh per jaar**. Om die 1.500 kWh af te kunnen geven, moet er 1.667 kWh in (10 procent omzetverlies).

**Zolang je saldeert (tot en met 2026)** is een teruggeleverde kWh evenveel waard als een afgenomen kWh. Extra eigen verbruik levert dan dus vrijwel niets op: je verplaatst alleen waar de kWh vandaan komt. Het enige echte voordeel in 2026 zit in de terugleverkosten die veel leveranciers apart in rekening brengen — minder terugleveren betekent minder van die kosten. Dat is een bedrag van tientallen euro's, geen honderden, en het verschilt per leverancier.

**Vanaf 1 januari 2027 stopt de saldering volledig.** Er is geen afbouwpad: de regeling houdt in één keer op. Vanaf dat moment is elke kWh die je zelf opslaat en gebruikt het verschil waard tussen je afnameprijs en de terugleververgoeding.

| Post (modelberekening, ná 2027) | Zonder batterij | Met batterij 10 kWh |
|---|---|---|
| Eigen verbruik van zonnestroom | 1.925 kWh | 3.425 kWh (1.925 + 1.500 uit de batterij) |
| Teruggeleverd | 3.575 kWh | 1.908 kWh (3.575 − 1.667 ingeladen) |
| Bespaarde inkoop à €0,26/kWh | €501 | €891 |
| Terugleververgoeding à €0,07/kWh | €250 | €134 |
| **Totaal voordeel per jaar** | **€751** | **€1.025** |
| Extra voordeel van de batterij | — | **€274** |

Bij een Sessy van 10 kWh à €5.500 inclusief btw en exclusief installatie (opgave Charged, prijspeil augustus 2026) komt dat model uit op een terugverdientijd van **circa 20 jaar**, en langer zodra je de installatie meerekent. Dat is langer dan de gebruikelijke garantietermijn.

Eén post kan daar nog bij: op een dynamisch contract kun je met de batterij ook op het prijsverschil tussen uren handelen. Wij rekenen daarvoor met €8 per kWh capaciteit per jaar (gelabelde eigen afleiding: circa 100 wintercycli tegen €0,10 netto spreiding), dus €80 bij 10 kWh. Dat brengt het totaal op circa €354 per jaar en de terugverdientijd op ruim vijftien jaar — nog altijd langer dan de garantietermijn, en alleen haalbaar met een dynamisch contract en automatische sturing.

Twee variabelen bepalen die uitkomst volledig: de terugleververgoeding die jouw leverancier na 2027 hanteert, en je afnameprijs. Loopt de vergoeding richting nul en je afnameprijs op, dan korten die jaren snel in. Vul daarom je eigen cijfers in — dit is een rekenmodel, geen voorspelling.

<a href="https://go.duurzaamthuislab.nl/sessy" class="cta cta-affiliate" rel="noopener nofollow" target="_blank">Bekijk Sessy</a> (gewone verwijzing, wij ontvangen hiervoor geen vergoeding)

### Case 3: de EV-accu als thuisbatterij (V2H)

Hier wordt het rekenkundig interessant. Een EV-accu van 60 tot 80 kWh is een veelvoud van een thuisbatterij, en je hebt hem al. Zet je 30 kWh daarvan in als buffer, dan heb je drie keer zoveel opslag als een thuisbatterij van 10 kWh, zonder een tweede accu te kopen.

**De harde beperking is aanwezigheid.** Wie dagelijks forenst, heeft de auto weg tussen acht en zes — precies wanneer de zon schijnt. V2H doet dan niets voor zonneopslag.

Het werkt wél voor wie thuiswerkt, een tweede auto heeft, of de auto vooral in het weekend gebruikt.

Modelberekening voor een thuiswerkscenario waarin de auto het grootste deel van de dag aan de lader hangt, met 30 kWh beschikbare buffer:

- Extra eigen verbruik ten opzichte van geen opslag: circa 2.800 kWh per jaar (aanname; dat blijft ruim onder de 150-cycli-grens van 30 kWh × 150 = 4.500 kWh, dus de aanwezigheid van de auto is hier de beperking, niet de accu)
- Om 2.800 kWh af te geven moet er bij 90 procent rendement 3.111 kWh in
- Bespaarde inkoop: 2.800 × €0,26 = €728; gemiste terugleververgoeding: 3.111 × €0,07 = €218
- Jaarlijks voordeel in dit model: circa **€510**
- Investering: een bidirectionele lader inclusief installatie. Fabrikanten publiceren daar geen consumentenprijs voor; reken in dit model met €4.500 als aanname en vervang dat door je eigen offerte
- Terugverdientijd in dit model: **bijna negen jaar**

Dat is de gunstigste uitkomst van de drie cases — maar hij staat of valt met de aanname dat de auto er overdag daadwerkelijk staat. Haal die aanname weg en de business case verdwijnt mee.

---

## Dynamisch contract: Frank Energie en Tibber

Bij slim laden is een dynamisch contract de basis. De twee bekendste spelers in Nederland:

| | Frank Energie | Tibber |
|---|---|---|
| Vaste kosten | niet publiek; opvragen via frankenergie.nl | €5,99 per maand per energiesoort |
| Inkoopvergoeding | ja, plus een terugleverstaffel sinds 1 juni 2025 | €0,0248/kWh |
| Sturing | via OCPP op de laadpaal | via auto-API of via OCPP |
| Opzegbaarheid | zie voorwaarden leverancier | maandelijks |

Beide rekenen dus een opslag bovenop de beursprijs; die opslag is precies het bedrag dat je van je bruto besparing moet aftrekken. Reken bij Tibber met €5,99 per maand per energiesoort plus €0,0248/kWh over je hele afname, niet alleen over je laadvolume.

**Rekenvoorbeeld met zichtbare aannames.** Laad je 225 kWh per maand en verschuif je die naar uren die gemiddeld €0,17/kWh goedkoper zijn dan je oude tarief, dan is de bruto winst 225 × €0,17 = €38,25 per maand. Daar gaat bij Tibber €5,99 vaste kosten voor stroom af, plus de inkoopvergoeding van €0,0248/kWh: over 225 kWh is dat €5,58. Netto blijft er **circa €26,70 per maand** over. Let op: die inkoopvergoeding geldt over je hele stroomafname, niet alleen over je laadvolume — verbruik je thuis nog 3.000 kWh voor de rest van het huishouden, dan gaat daar per jaar nog eens circa €74 aan inkoopvergoeding af.

Die €0,17 is een zelfgekozen spread. Reken je met onze eigen constanten — €0,32 all-in vast tegenover €0,220 all-in EV-nacht, dus €0,10 verschil — dan is de bruto winst €22,50 per maand en houd je na vaste kosten en inkoopvergoeding circa €11 per maand over. Het verschil tussen die twee uitkomsten is precies waarom je met je eigen tariefblad moet rekenen.

---

## Welke auto's ondersteunen bidirectioneel laden?

De ondersteuning verschilt per merk, per model, per bouwjaar en soms per softwareversie. Fabrikanten voegen functies toe en halen ze weg, en importeurs bieden in Nederland niet altijd hetzelfde aan als in andere markten. Een lijst in een artikel is daarom binnen een half jaar achterhaald.

Wat wél stabiel is als vuistregel:

- **V2L** — een stopcontact in de auto — zit op een groeiend deel van de modellen en vraagt geen extra hardware thuis.
- **V2H** — de auto als huisbatterij — vereist naast een geschikte auto een bidirectionele omvormer, en is in Nederland beperkt beschikbaar.
- **V2G** — terugleveren aan het net — loopt in pilots en is voor consumenten nog geen product.

Controleer vóór aanschaf bij de importeur of het exacte model en bouwjaar dat je op het oog hebt, V2H ondersteunt in de Nederlandse uitvoering — en met welke laders dat is vrijgegeven.

---

## Thuisbatterij of EV-accu: wat is goedkoper per kWh?

| | Sessy 10 kWh | EV-accu (bruikbaar deel) |
|---|---|---|
| Bruikbare capaciteit | 10 kWh | 30-40 kWh, afhankelijk van de ingestelde ondergrens |
| Prijs | €5.500 incl. btw, excl. installatie (opgave Charged, aug. 2026) | geen aparte investering — de auto had je al |
| Altijd beschikbaar | ja | nee, alleen als de auto thuis is |
| Cycli | 6.000+ (opgave Charged) | telt mee in de slijtage van je autoaccu |
| Extra hardware | nee | bidirectionele omvormer |

Per kWh wint de auto altijd, want die accu heb je al betaald. Maar beschikbaarheid is hier geen bijzaak: een buffer die er de helft van de tijd niet is, dekt niet dezelfde uren af.

Andere merken laten wij hier bewust weg met een prijs erbij: Marstek voert inmiddels een andere productlijn dan de veelgenoemde Venus-serie en publiceert voor Nederland maar één consumentenprijs, en Huawei publiceert voor de LUNA-serie geen consumentenprijs. Prijzen die daarvoor circuleren, zijn straatprijzen van resellers en geen fabrikantsopgave.

---

## Voor wie is de combinatie zinvol?

**Wel interessant voor:**

- thuiswerkers met een auto die V2H ondersteunt
- huishoudens met een fors dakvermogen die zich op het einde van de saldering voorbereiden
- wie toch al een thuisbatterij overweegt én elektrisch rijdt, zodat de sturing in één systeem komt
- huishoudens die een dynamisch contract willen combineren met automatische sturing

**Niet interessant voor:**

- forenzen die de auto overdag weg hebben — V2H doet dan niets
- huurders zonder eigen laadpunt of panelen
- huishoudens met een klein dakvermogen: te weinig overschot om op te slaan
- wie snel wil terugverdienen; in onze modellen liggen de terugverdientijden van een thuisbatterij tussen de vijftien en twintig jaar

---

## Drie setups, en waar het geld zit

### Setup 1: alleen slim laden

Een laadpaal met sturing plus een dynamisch contract. Geen batterij. Dit is de setup met veruit de kortste terugverdientijd, omdat de besparing volledig uit tijdverschuiving komt en niet uit hardware.

### Setup 2: zonnepanelen, thuisbatterij en slim laden

Panelen, een thuisbatterij en een laadpaal met sturing. Reken deze setup door met de tabel uit case 2 en met je eigen offertes. Houd er rekening mee dat de batterij 21 procent btw draagt: het 0%-tarief geldt alleen voor zonnepanelen en wat direct nodig is om die te laten werken.

<a href="https://go.duurzaamthuislab.nl/zonneplan" class="cta cta-affiliate" rel="noopener nofollow" target="_blank">Bekijk Zonneplan</a> (gewone verwijzing, wij ontvangen hiervoor geen vergoeding)

### Setup 3: V2H

Panelen plus een bidirectionele lader, en de auto als buffer. Rekenkundig de gunstigste van de drie in ons model, maar met de zwaarste aanname: de auto moet er overdag staan. Vraag hier altijd een offerte inclusief installatie op; consumentenprijzen worden voor deze laders niet gepubliceerd.

---

## Praktische stappen

**Stap 1: controleer je laadsituatie.** Laad je via een vaste laadpaal of via een adapter op een gewoon stopcontact? Een vaste laadpaal met sturing is de basis voor alle verdere optimalisatie.

**Stap 2: bekijk je rijgedrag.** Hoe ver rijd je per dag, en wanneer staat de auto thuis? Dit bepaalt of V2H realistisch is. Je laadapp of auto-app laat dat zien.

**Stap 3: kies eerst een dynamisch contract.** Doe dat vóórdat je hardware koopt. De besparing is direct en vraagt geen installatie.

**Stap 4: bereken je zonne-overschot.** Kijk in je omvormer-app hoeveel je de afgelopen twaalf maanden hebt teruggeleverd. Hoe hoger dat getal, hoe meer een batterij kan opvangen.

**Stap 5: kies tussen een thuisbatterij en V2H.** Staat de auto overdag thuis en ondersteunt hij V2H, dan is dat de goedkoopste opslag die je hebt. Zo niet, dan is een thuisbatterij de enige route.

**Stap 6: check lokale regelingen.** Landelijk is er geen ISDE voor thuisbatterijen, zonnepanelen of laadpalen. Gemeentelijke en provinciale regelingen bestaan wel; check de subsidiechecker van je eigen gemeente en vraag aan vóór de installatie.

---

## Wat verandert er na 1 januari 2027?

Per 1 januari 2027 stopt de saldering volledig. Er is geen stapsgewijze afbouw: het wetsvoorstel met een afbouwpad is verworpen, de regeling houdt in één keer op.

Wat dat betekent: teruggeleverde stroom levert vanaf dat moment de terugleververgoeding van je leverancier op — een fractie van wat je voor afname betaalt. Elke kWh die je zelf opslaat en gebruikt, wordt daarmee het verschil tussen die twee waard.

| Situatie | Waarde van een extra zelf verbruikte kWh |
|---|---|
| Tot en met 2026 (saldering) | vrijwel nul, behalve besparing op terugleverkosten |
| Vanaf 2027 | afnameprijs min terugleververgoeding |

Wie nu een thuisbatterij koopt, koopt die dus vooral voor de jaren daarna. Dat is een legitieme afweging — maar reken de terugverdientijd door vanaf 2027, niet vanaf vandaag.

---

## Wettelijk kader 2026

**Geen ISDE voor een thuisbatterij.** De ISDE voor woningeigenaren dekt volgens RVO uitsluitend isolatie, ventilatie in combinatie met isolatie, (hybride) warmtepompen, zonneboilers, een warmtenetaansluiting en elektrisch koken. Thuisbatterijen, zonnepanelen en laadpalen staan er niet in.

**Geen landelijke laadpaalsubsidie.** Voor een thuislaadpaal bij een koopwoning is er geen rijksregeling. Gemeentelijke en provinciale regelingen verschillen sterk; check de subsidiechecker van je eigen gemeente vóór je opdracht geeft.

**Btw op een thuisbatterij: 21 procent.** Het 0%-tarief geldt volgens de Belastingdienst voor zonnepanelen plus wat direct nodig is om die te laten werken — kabels, montagemateriaal, optimizers, omvormers en aanpassingen aan meterkast en dak. Een accupakket valt daar uitdrukkelijk buiten en houdt 21 procent btw, ook bij gelijktijdige aanschaf met panelen.

**V2G.** Terugleveren aan het net vanuit een auto-accu loopt in Nederland via pilots en is nog geen breed beschikbaar consumentenproduct. Netbeheerders werken aan generieke voorzieningen; een datum daarvoor is niet vastgesteld.

---

## Veelgemaakte fouten

**Fout 1: thuisbatterij en auto allebei 's avonds laden.** Trekt de auto 's avonds de batterij leeg, dan laadt die batterij 's nachts opnieuw uit het net — met omzetverliezen erbij. Scheid de taken: de auto laadt direct uit het net in het goedkope venster, de batterij voedt het huis.

**Fout 2: een bidirectionele lader kopen zonder V2H-geschikte auto.** Controleer eerst bij de importeur of jouw exacte model en bouwjaar het in de Nederlandse uitvoering ondersteunt, en met welke laders dat is vrijgegeven.

**Fout 3: de laadtoestand van de auto niet bewaken.** V2H onttrekt vermogen aan je autoaccu. Stel altijd een ondergrens in, zodat je 's ochtends nog kunt rijden.

**Fout 4: rekenen zonder omzetverliezen.** Laden en ontladen kost rendement. Bij LFP-thuisbatterijen ligt het round-trip rendement volgens de specificaties doorgaans rond de 90 procent; via een bidirectionele lader komt er een extra omzetstap bij en ligt het lager. Reken daarmee, anders komt je model structureel te gunstig uit.

**Fout 5: geen dynamisch contract nemen.** Dit is de duurste fout, omdat het de goedkoopste winst is. Wie investeert in batterij en laadpaal maar op een vast contract blijft, laat het grootste deel van het effect liggen.

---

## Conclusie

De combinatie EV plus thuisbatterij is in 2026 geen vanzelfsprekende investering. In ons model komt de terugverdientijd van een losse thuisbatterij van 10 kWh uit rond de twintig jaar, ook ná het einde van de saldering — en rond de vijftien jaar als je er op een dynamisch contract ook uurprijshandel bij optelt.

Wat wél opgaat:

1. **Slim laden op een dynamisch contract** — geen hardware nodig, effect direct, en het is de basis onder alle andere stappen.
2. **V2H** als je auto het ondersteunt én overdag thuisstaat — dan gebruik je opslag waarvoor je al betaald hebt.
3. **Een thuisbatterij** als bewuste voorbereiding op de jaren ná 2027, met de terugverdientijd doorgerekend vanaf dat moment.

Begin bij stap 1. Die kost niets en maakt de rest van de rekensom pas zinvol.

---

## Gerelateerde artikelen

- [Beste thuisbatterij Nederland 2026](/posts/beste-thuisbatterij-nederland-2026/)
- [Sessy review thuisbatterij Nederland](/posts/sessy-review-thuisbatterij-nederland/)
- [Marstek Venus review](/posts/marstek-venus-review-thuisbatterij/)
- [Saldering stopt 2027: wat moet je nu doen?](/posts/saldering-stopt-2027-volledige-gids/)
- [Thuisbatterij terugverdientijd berekenen](/posts/thuisbatterij-terugverdientijd-berekenen-2026/)
- [Thuisbatterij subsidie 2026: volledig overzicht](/posts/thuisbatterij-subsidie-2026-overzicht/)

---

**Externe bron:** [RVO — ISDE voor woningeigenaren](https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren) — het officiële overzicht van welke maatregelen de ISDE wel en niet dekt (thuisbatterijen, zonnepanelen en laadpalen vallen er niet onder).
