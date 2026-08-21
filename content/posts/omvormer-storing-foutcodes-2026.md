---
title: 'Omvormer storing: GoodWe- en Solis-foutcodes, en Huawei opzoeken'
date: '2026-08-18 08:00:00+02:00'
lastmod: '2026-08-21 08:00:00+02:00'
draft: false
description: 'De foutmeldingen die GoodWe en Solis zelf publiceren, met betekenis en eerste actie. Voor Huawei publiceert de fabrikant geen open codelijst — daarom staat hier de route om jouw alarm op te zoeken, plus de universele diagnosestappen die bij elk merk werken.'
categories:
- onderhoud
tags:
- onderhoud
- omvormer
- foutcodes
- storing
keywords:
- omvormer storing
- omvormer foutcode
- goodwe error
- solis foutcode
- huawei omvormer storing
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: Wat doe ik als eerste bij een omvormer-foutcode?
  a: 'Fotografeer de melding met tijdstip, zoek de code op in de handleiding van jouw exacte modelnummer of in de fabrikant-app, en herstart eenmaal volgens de handleiding — AC- en DC-scheider uit, twee minuten wachten, in omgekeerde volgorde weer aan. Blijft de melding terugkomen, bel dan je installateur. Werk nooit zelf aan de gelijkspanningszijde: daar staat bij daglicht spanning op die niet met een schakelaar verdwijnt.'
- q: Publiceren de fabrikanten hun foutcodes openbaar?
  a: 'Gedeeltelijk. GoodWe beschrijft in de eigen FAQ een reeks foutmeldingen bij naam met oorzaak en actie. Solis heeft in het servicekennisbank een categorie "Alarm Code Troubleshooting" met artikelen per code. Huawei publiceert geen open codelijst op de website: de alarmen staan in de productdocumentatie en in de FusionSolar-omgeving. De volledige lijst zit bij alle drie de merken in de handleiding van jouw specifieke model.'
- q: Wat betekent een netgerelateerde foutmelding?
  a: 'Dat de omvormer afschakelt omdat de netspanning of netfrequentie buiten de toegestane bandbreedte valt. Op een Nederlands laagspanningsnet moet de spanning binnen 207-253 V blijven; komt die structureel aan de bovengrens, dan schakelt een omvormer volgens NEN-EN 50549-1 verplicht af. Dat is geen defect aan je omvormer maar een netsituatie, en een nieuwe omvormer lost het niet op.'
- q: Hoeveel kan ik zelf oplossen?
  a: 'Aan de wisselspanningszijde en in de app: een eenmalige herstart, controleren of de AC-groep niet is uitgeschakeld, firmware bijwerken, koelribben afstoffen. Alles wat met isolatieweerstand, aardlekstroom, DC-spanning of stringmetingen te maken heeft, hoort bij de installateur. Dat is niet een kwestie van moeilijk maar van gevaarlijk.'
- q: Wanneer is vervangen echt nodig?
  a: 'Als de fout na herstel van de oorzaak blijft terugkomen en de fabrikant of installateur een defect vaststelt: bij herhaalde isolatiefouten zonder aanwijsbare oorzaak in de installatie, bij zichtbaar opgezwollen condensatoren, of bij een defecte MPPT-ingang waarvan de reparatie meer kost dan een vervangende omvormer. Vraag in alle gevallen eerst de foutlogs op: voor een garantieclaim heb je die historie nodig.'
- q: Wat zet ik in een supportticket?
  a: 'Serienummer, exact modelnummer, firmwareversie, de foutcode met datum en tijdstip, een foto van het display of een schermafdruk uit de app, en de gemeten netspanning op het moment van de fout. Met die zes gegevens erbij hoeft de servicedesk niet eerst een week te vragen wat je al weet.'
schema_type: Article
---

*Disclosure: GoodWe, Solis, Huawei en SMA worden in dit artikel redactioneel besproken. Wij hebben met geen van deze partijen een affiliate- of commissierelatie en ontvangen voor dit artikel geen vergoeding. Er staan geen commerciële links in; de links hieronder gaan naar de supportpagina's van de fabrikanten.*

Een omvormer die op storing staat, kost per dag opbrengst. Het probleem is dat de meeste overzichten van foutcodes op internet lijsten met codes bevatten die aan geen enkel merk toe te wijzen zijn. Dit artikel doet het omgekeerd: **alleen wat de fabrikanten zelf publiceren, met vermelding van waar het staat.** Opgehaald op 21 augustus 2026.

Voor twee van de drie merken levert dat een echte tabel op. Voor Huawei niet — die fabrikant publiceert geen open codelijst, en dan zeggen we dat in plaats van er een te verzinnen.

> **Kort antwoord:** de meeste omvormerstoringen zijn netgerelateerd of installatiegerelateerd, niet een defecte omvormer. Fotografeer de melding, zoek hem op in de handleiding van jouw exacte modelnummer, herstart eenmaal en meet je netspanning voordat je iets vervangt. GoodWe en Solis publiceren hun foutmeldingen; bij Huawei lees je het alarm uit in FusionSolar en zoek je het op in de productdocumentatie.

## Eerst dit: de universele route

Deze vijf stappen gelden bij elk merk en in deze volgorde.

1. **Leg de melding vast.** Foto van het display of schermafdruk uit de app, met datum en tijdstip. Zonder dat heb je later geen garantiedossier.
2. **Zoek de code op bij jouw exacte modelnummer.** Codes zijn merkspecifiek en soms zelfs seriespecifiek. Een F-code van het ene merk betekent bij het andere iets anders. Het typeplaatje op de omvormer geeft het modelnummer.
3. **Herstart eenmaal, volgens de handleiding.** Doorgaans: AC-scheider uit, DC-scheider uit, twee minuten wachten, DC aan, AC aan. Eén keer. Blijft de fout terugkomen, dan maskeert herstarten het probleem in plaats van het op te lossen.
4. **Meet je netspanning.** Via de P1-poort van de slimme meter of via de app van de omvormer. Dit is de meest onderschatte stap; zie de sectie over netspanning verderop.
5. **Bel de installateur voor alles aan de DC-kant.** Isolatieweerstand, aardlekstroom, stringspanning: daar staat bij daglicht spanning op die niet met een schakelaar verdwijnt.

## GoodWe: de meldingen die de fabrikant zelf beschrijft

GoodWe beschrijft in de eigen FAQ zes foutmeldingen bij naam, met oorzaak en aanbevolen actie. Dit is de tabel zoals de fabrikant hem geeft; de volledige lijst per model staat in de handleiding in het download center.

| Melding | Wat GoodWe als oorzaak noemt | Eerste actie volgens GoodWe |
|---|---|---|
| Utility Loss | Geen spanning gedetecteerd aan de AC-zijde | Controleer of het net eraf is, of de AC-groep is ingeschakeld en of de aansluitingen goed vastzitten |
| Vac Failure | AC-spanning buiten het bereik van de ingestelde veiligheidsnorm (safety country) | Meet de AC-spanning met een multimeter en controleer of de juiste landinstelling is gekozen |
| Fac Failure | AC-frequentie buiten het bereik van de ingestelde veiligheidsnorm | Controleer de actuele netfrequentie en de landinstelling |
| ISO Failure | Isolatieweerstand van de panelen naar aarde te laag | Panelen één voor één opnieuw aansluiten, controleren op een onderbroken aardverbinding of beschadigde bekabeling |
| Ground I Failure | Lekstroom te hoog | Panelen één voor één opnieuw aansluiten om het foute paneel te vinden, aarding en bekabeling inspecteren |
| PV overvoltage | Paneelspanning boven het DC-bereik van de omvormer | Paneelspanning meten en zo nodig het aantal panelen in de string verlagen |

Bron: [GoodWe FAQ](https://en.goodwe.com/faqs), opgehaald 21 augustus 2026.

Twee kanttekeningen bij die tabel. De acties bij **ISO Failure** en **Ground I Failure** — panelen één voor één opnieuw aansluiten — zijn werk aan de gelijkspanningszijde. GoodWe schrijft ze op voor installateurs; doe dat niet zelf. En bij **Vac Failure** en **Fac Failure** is de veiligheidsnorminstelling ("safety country") de eerste verdachte: staat die op een ander land dan Nederland, dan schakelt de omvormer op verkeerde grenswaarden af. Dat is een instelling die de installateur bij oplevering had moeten zetten.

Voor de complete codelijst verwijst GoodWe naar de handleiding van het specifieke type in het [download center](https://en.goodwe.com/support) en naar het eigen supportportaal.

## Solis: de alarmcodes uit het servicekennisbank

Solis heeft in het servicekennisbank een aparte categorie **"Alarm Code Troubleshooting"**, met artikelen per code. De codes die daar op 21 augustus 2026 als eigen artikel stonden:

| Alarmcode | Waar het over gaat |
|---|---|
| GRID-INTF | Netinterferentie: de omvormer stelt een netsituatie vast waarop hij niet kan of mag blijven leveren |
| PV ISO PRO | Isolatiebeveiliging aan de PV-zijde — de tegenhanger van GoodWe's ISO Failure |
| I-Leak-Pro / Leakage current | Lekstroombeveiliging |
| AFCI Protection | De vlambogendetectie heeft aangeslagen |

Bron: [Solis service- en supportportaal, kennisbank](https://solis-service.solisinverters.com/nl/support/home), opgehaald 21 augustus 2026.

Het kennisbank bevat naast deze codes ook artikelen over een omvormer die niet opstart, een leeg of beschadigd HMI-scherm, de keuze van een externe aardlekschakelaar, AC-groepen die afslaan en batterijdiagnose voor Pylontech, BYD en WeCo. Handleidingen en datasheets staan in het Solis **downloadcenter**; voor Nederland publiceert Solis een eigen servicenummer, **+31 85 048 1300**. Dat lokale kanaal is een reëel voordeel bij een garantietraject.

Eén ding om te weten over **AFCI Protection**: vlambogendetectie is een veiligheidsfunctie, geen storingsmelding die je wegklikt. Slaat die herhaald aan, dan is dat een reden om de installateur met urgentie te laten komen kijken, niet om te resetten tot het stil blijft.

## Huawei: geen open codelijst, wel een vaste route

Huawei publiceert op de website geen vrij toegankelijke tabel met alarm-ID's voor residentiële SUN2000-omvormers. Wat er wél is:

- **De FusionSolar-app of het portaal.** Daar staat het actieve alarm met naam en tijdstip. Dat is je uitgangspunt, en het is de reden dat je de Smart Dongle bij oplevering wilt hebben; zonder verbinding zie je alleen ledlampjes.
- **Het productdocumentatieportaal van Huawei.** Daar staan de gebruikershandleidingen en de O&M-documentatie per productserie, met de alarmbeschrijvingen erin.
- **Het Smart PV Forum en het online support-kanaal.** Huawei verwijst daar zelf naar voor vragen die technisch personeel beantwoordt.

Bron: [Huawei FusionSolar support](https://solar.huawei.com/en/support), opgehaald 21 augustus 2026.

De praktische route is dus: alarm uitlezen in FusionSolar, exacte alarmnaam en modelnummer noteren, en die opzoeken in de handleiding van jouw serie of doorgeven aan je installateur. Wat wij níet doen is een lijst met Huawei-alarmcodes publiceren die we niet bij de fabrikant hebben kunnen terugvinden. Kom je zulke lijsten elders tegen zonder bronvermelding, behandel ze dan met wantrouwen: een verkeerd geïnterpreteerd alarm leidt tot een onnodige vervanging.

## Netspanning: waarom "F47" bij SMA vaak geen defect is

Het duidelijkste voorbeeld van een netgerelateerde melding is **F47 bij SMA-omvormers**: netonderspanning. De omvormer schakelt af omdat de netspanning buiten de toegestane bandbreedte valt.

Volgens de Nederlandse netcode moet de spanning op een laagspanningsnet binnen **207-253 V** blijven; komt die structureel aan de bovengrens (rond 250 V) of onder de ondergrens, dan schakelt een omvormer volgens **NEN-EN 50549-1** verplicht af. Dat betekent dat zo'n melding vaak géén defecte omvormer aanwijst maar een netprobleem in de straat — iets wat in wijken met veel zonnestroom op zonnige middagen structureel voorkomt.

De route is dan:

1. Netspanning uitlezen via de P1-poort van je slimme meter (de sensor "voltage") of via de app van de omvormer.
2. De meetwaarden over enkele dagen vastleggen, met tijdstippen.
3. Melding doen bij je netbeheerder, met die meetreeks erbij.

Netbeheerders kunnen de tap-stand van de wijktransformator aanpassen wanneer de spanning aantoonbaar te hoog of te laag is. **Les: controleer eerst je netspanning voordat je een nieuwe omvormer koopt.** Vervanging lost een netprobleem niet op — de nieuwe omvormer schakelt op dezelfde grenswaarde af.

Dezelfde logica geldt voor de netgerelateerde meldingen van de andere merken in dit artikel: GoodWe's Vac Failure en Fac Failure en Solis' GRID-INTF wijzen in eerste instantie naar het net of naar de landinstelling, niet naar de hardware.

## Vijf fouten bij het diagnosticeren

1. **Direct de installateur bellen zonder de handleiding open te doen.** Een deel van de meldingen is met de bijlage in de handleiding en een eenmalige herstart af te handelen.
2. **Blijven resetten.** Bij een netmelding of een isolatiefout bestaat het probleem na de reset nog steeds; je verliest alleen de logregels die het bewijzen.
3. **Geen logbestand bewaren.** Voor een garantieclaim heb je vaak een aantal weken historie nodig. Exporteer de logs zodra de fout optreedt.
4. **Firmware niet controleren.** Een deel van de meldingen verdwijnt met een firmware-update die de fabrikant al heeft uitgebracht.
5. **Zelf aan de DC-kant gaan meten.** Zonder de juiste referentie en meetapparatuur levert dat foutieve waarden op, en het is de gevaarlijkste kant van de installatie.

## Wanneer een omvormer écht vervangen wordt

Er zijn drie situaties waarin vervanging de uitkomst is, en in alle drie stelt de installateur of de fabrikant dat vast — niet een codelijst op internet:

- **Herhaalde isolatiefouten** waarbij de installateur geen oorzaak in de bekabeling, de panelen of de aarding kan aanwijzen.
- **Zichtbaar opgezwollen condensatoren.** Dat is een veiligheidskwestie; laat het toestel dan spanningsloos maken.
- **Een defecte MPPT-ingang** waarbij één string niet meer werkt en de reparatiekosten in de buurt van of boven een vervangende omvormer liggen.

Reken bij die afweging met een verwachte levensduur van 12 tot 15 jaar voor een omvormer op een paneelinstallatie die 25 jaar meegaat: één omvormervervanging in de looptijd is een normale kostenpost, geen incident. Hoe je dat in je opbrengstberekening meeneemt, staat op [zonnepanelen opbrengst berekenen](/zonnepanelen-opbrengst-berekenen/).

## Een supportticket dat in één keer wordt opgepakt

Zet deze zes gegevens in de eerste mail:

1. Serienummer en exact modelnummer (typeplaatje).
2. Firmwareversie.
3. De foutcode of alarmnaam, met datum en tijdstip.
4. Foto van het display of schermafdruk uit de app.
5. Gemeten netspanning op het moment van de fout.
6. Wat je al hebt gedaan (bijvoorbeeld: eenmaal herstart volgens handleiding, fout kwam na X minuten terug).

Dat scheelt de heen-en-weer-mail waarin de servicedesk precies deze zes dingen opvraagt.

## Bronnen

- [GoodWe FAQ](https://en.goodwe.com/faqs) en [GoodWe support](https://en.goodwe.com/support), opgehaald 21 augustus 2026: de zes beschreven foutmeldingen met oorzaak en actie, en de verwijzing naar handleiding en download center voor de volledige lijst.
- [Solis service- en supportportaal](https://solis-service.solisinverters.com/nl/support/home), opgehaald 21 augustus 2026: de categorie Alarm Code Troubleshooting met GRID-INTF, PV ISO PRO, I-Leak-Pro en AFCI Protection, en het Nederlandse servicenummer.
- [Huawei FusionSolar support](https://solar.huawei.com/en/support), opgehaald 21 augustus 2026: geen open alarmcodelijst; verwijzing naar productdocumentatie, O&M-guides en het Smart PV Forum.
