---
title: 'openHAB voor zonnepanelen en thuisbatterij: things, rules en sitemap'
date: '2026-08-04 08:00:00+02:00'
lastmod: '2026-08-21 08:00:00+02:00'
draft: false
description: openHAB als open-source alternatief voor Home Assistant. Werkende voorbeelden van things, items, rules en een sitemap voor zonnepanelen, een thuisbatterij en een dynamisch tarief.
categories:
- smart-home
tags:
- smart-home
- verduurzamen
- duurzaam wonen
- openhab
keywords:
- openhab zonnepanelen
- openhab batterij sturing
- openhab modbus
- openhab energie dashboard
- slim laden openhab
affiliate: true
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: 'Waarom openHAB kiezen en niet Home Assistant?'
  a: 'Twee redenen komen in de forums structureel terug: je hebt al een openHAB-installatie en migreren is te bewerkelijk, of je wil de Modbus- en Rules-DSL-implementatie van openHAB gebruiken bij industriële apparatuur. Begin je nieuw en wil je alleen energiesturing, dan is Home Assistant of EVCC doorgaans de kortere route — meer kant-en-klare integraties voor consumentenhardware.'
- q: 'Welke bindings heb ik nodig voor een energieopstelling?'
  a: 'Meestal drie: de Modbus-binding voor omvormer en batterij, de HTTP-binding voor API''s die geen eigen binding hebben (day-ahead-prijzen, de lokale API van een P1-meter) en een persistence-service zoals InfluxDB of rrd4j om te kunnen graphen. Sommige merken hebben een eigen binding; check altijd de bindings-lijst van jouw openHAB-versie, want de Modbus-binding is tussen major releases gewijzigd.'
- q: 'Kan ik met openHAB mijn thuisbatterij op prijs laten laden?'
  a: 'Ja, mits je batterij een lokale schrijfbare interface heeft: Modbus TCP of een gedocumenteerde lokale HTTP-API. Je zet dan de bedrijfsmodus of het laadvermogen vanuit een rule. Batterijen die alleen via de fabrikantcloud te sturen zijn, kun je uitlezen maar niet betrouwbaar aansturen.'
- q: 'Hoe voorkom ik dat een fout in een rule mijn batterij leegtrekt?'
  a: 'Bouw drie dingen in: een minimum-SoC waaronder de rule niet meer ontlaadt, een timeout die de modus na maximaal een paar uur terugzet naar automatisch, en caching van de prijsdata zodat een mislukte API-aanroep niet als prijs nul wordt gelezen. Een prijs die als 0 binnenkomt is de klassieke oorzaak van ongewenst laden.'
- q: 'Op welke hardware draait openHAB stabiel?'
  a: 'Een x86-mini-pc of NAS met SSD is de veilige keuze; een Raspberry Pi met SSD (dus niet op een SD-kaart) werkt voor kleine opstellingen. Reken vooral op geheugen: openHAB draait op de JVM en een setup met persistence en veel items gebruikt beduidend meer RAM dan een lichte installatie.'
products:
- name: HomeWizard P1-meter
  url: https://go.duurzaamthuislab.nl/homewizard
  price: '24.95'
schema_type: Article
last_updated: '2026-08-21'
---
*Disclosure: de link naar HomeWizard in dit artikel is een affiliate-link (via Daisycon). Koop je daarvia, dan ontvangen wij mogelijk een commissie, zonder extra kosten voor jou. Met de overige genoemde merken (Sessy, SMA, BYD) hebben wij géén commissie- of affiliaterelatie; de link naar Sessy levert ons niets op. HomeWizard-prijs: homewizard.com, prijspeil augustus 2026.*

> **Kort antwoord:** in openHAB bouw je een energieopstelling op in vier lagen: **things** (verbinding met omvormer, batterij en prijsbron), **items** (de meetwaarden en stuurgrepen), **rules** (wanneer laden en ontladen) en een **sitemap** (het dashboard). Hieronder van elke laag een werkend voorbeeld dat je kunt aanpassen aan je eigen hardware.

## Wat je nodig hebt

- **openHAB 4.x** op een machine die 24/7 aan staat.
- De **Modbus-binding** voor omvormer en batterij. Let op: de configuratiesyntax van deze binding is tussen major versies gewijzigd — kopieer geen voorbeelden uit oude forumposts zonder te checken voor welke versie ze zijn.
- De **HTTP-binding** voor alles zonder eigen binding: day-ahead-prijzen en de lokale API van een P1-meter.
- Een **persistence-service** (rrd4j is standaard, InfluxDB als je langere reeksen en Grafana wil).
- Een **P1-meter** om te kunnen controleren of je sturing werkelijk iets doet. De HomeWizard P1 heeft een gedocumenteerde lokale API die je zonder cloud kunt uitlezen. <a href="https://go.duurzaamthuislab.nl/homewizard?ref=/posts/openhab-zonnepanelen-batterij-sturing-2026/" class="cta cta-affiliate" rel="noopener nofollow sponsored" target="_blank">Bekijk de HomeWizard P1-meter (€24,95)</a>

Voor de batterij geldt dezelfde regel als bij Home Assistant: je kunt alleen sturen wat lokaal schrijfbaar is. Sessy documenteert een open API voor koppeling met domotica; Modbus TCP is bij omvormers (SMA, SolarEdge, Huawei, Goodwe) de gebruikelijke route. <a href="https://go.duurzaamthuislab.nl/sessy" class="cta cta-affiliate" rel="noopener nofollow" target="_blank">Bekijk Sessy</a> — wij verdienen niets aan deze link.

## Laag 1: things

Twee dingen tegelijk: de Modbus-verbinding met omvormer en batterij, en de HTTP-verbinding voor de prijsdata.

```java
// things/energie.things

// Omvormer via Modbus TCP
Bridge modbus:tcp:omvormer [ host="192.168.1.50", port=502, id=3 ] {
    Bridge poller pvData [ start=30775, length=6, refresh=5000, type="input" ] {
        Thing data pvVermogen  [ readStart="30775", readValueType="int32" ]
        Thing data pvDagTotaal [ readStart="30777", readValueType="uint32", readTransform="JS:divide1000.js" ]
    }
}

// Batterij via Modbus TCP (registeradressen zijn voorbeelden — zie het
// Modbus-document van jouw fabrikant; verkeerde adressen schrijven is riskant)
Bridge modbus:tcp:batterij [ host="192.168.1.60", port=502, id=1 ] {
    Bridge poller battStatus [ start=0, length=8, refresh=5000, type="holding" ] {
        Thing data soc      [ readStart="0", readValueType="uint16" ]
        Thing data vermogen [ readStart="2", readValueType="int16" ]
    }
    Bridge poller battControl [ start=100, length=2, refresh=10000, type="holding" ] {
        Thing data setpoint [ readStart="100", readValueType="int16",
                              writeStart="100", writeValueType="int16", writeType="holding" ]
    }
}

// Day-ahead-prijzen via de HTTP-binding: hele JSON als string binnenhalen
Thing http:url:prijzen "Day-ahead prijzen" [
    baseURL="https://beheer.wtdigital.nl/api/public/stroomprijzen",
    refresh=900,
    timeout=5000
] {
    Channels:
        Type string : json [ stateTransformation="JSONPATH:$" ]
        Type number : gemiddelde [ stateTransformation="JSONPATH:$.gemiddelde" ]
}

// Lokale API van de P1-meter
Thing http:url:p1 "P1-meter" [
    baseURL="http://192.168.1.70/api/v1/data",
    refresh=10000
] {
    Channels:
        Type number : verbruikNu [ stateTransformation="JSONPATH:$.active_power_w" ]
}
```

De prijsbron in dit voorbeeld is onze eigen open endpoint. Die geeft per uur de kale day-ahead-prijs terug (EPEX inclusief btw, **exclusief** energiebelasting en inkoopvergoeding). Voor sturing maakt dat niet uit — de belasting is elk uur gelijk, dus de spread tussen uren blijft hetzelfde — maar reken je je besparing uit, tel dan €0,11085 energiebelasting per kWh (inclusief btw, tarief 2026) plus de opslag van je leverancier erbij.

## Laag 2: items

```java
// items/energie.items

Group gEnergie
Group:Number:AVG gPrijs

Number:Power     PV_Vermogen      "Zonneproductie [%.0f W]"      <solarplant> (gEnergie)
    { channel="modbus:data:omvormer:pvData:pvVermogen:number" }
Number:Energy    PV_DagTotaal     "Opbrengst vandaag [%.1f kWh]" <energy>     (gEnergie)
    { channel="modbus:data:omvormer:pvData:pvDagTotaal:number" }

Number           Batterij_SOC     "Batterij [%.0f %%]"           <battery>    (gEnergie)
    { channel="modbus:data:batterij:battStatus:soc:number" }
Number:Power     Batterij_Vermogen "Batterijvermogen [%.0f W]"   <energy>     (gEnergie)
    { channel="modbus:data:batterij:battStatus:vermogen:number" }
Number           Batterij_Setpoint "Setpoint [%.0f W]"           <energy>
    { channel="modbus:data:batterij:battControl:setpoint:number" }
String           Batterij_Modus   "Modus [%s]"                   <settings>

Number:Power     P1_VerbruikNu    "Netafname [%.0f W]"           <energy>     (gEnergie)
    { channel="http:url:p1:verbruikNu:number" }

String           Prijs_Json       "Prijzen JSON [%s]"
    { channel="http:url:prijzen:json" }
Number           Prijs_Gemiddeld  "Gemiddelde dagprijs [%.3f EUR/kWh]" <price> (gPrijs)
    { channel="http:url:prijzen:gemiddelde:number" }
Number           Prijs_Nu         "Prijs dit uur [%.3f EUR/kWh]"       <price> (gPrijs)
Switch           Goedkoop_Uur     "Goedkoop uur [%s]"                  <price>
```

`Prijs_Nu` en `Goedkoop_Uur` hebben geen channel: die vult de rule hieronder, uit de JSON die de HTTP-binding ophaalt.

## Laag 3: rules

Voorbeeld in de klassieke Rules DSL (bestand `rules/energie.rules`). Werk je met de nieuwe JS-scripting-add-on, dan is de logica dezelfde maar de syntax anders.

```java
// rules/energie.rules

rule "Prijs van dit uur uit de JSON halen"
when
    Item Prijs_Json changed or
    Time cron "0 1 * * * ?"
then
    val json = Prijs_Json.state.toString
    if (json === null || json.length < 10) {
        logWarn("energie", "Geen prijsdata — sturing blijft op automatisch")
        return;
    }
    val uur = now.getHour
    val prijs = transform("JSONPATH", "$.uren[" + uur + "].prijs", json)
    if (prijs === null || prijs == "") {
        logWarn("energie", "Uur " + uur + " niet gevonden in prijsdata")
        return;
    }
    Prijs_Nu.postUpdate(Float::parseFloat(prijs))

    val gem = (Prijs_Gemiddeld.state as Number).floatValue
    if (Float::parseFloat(prijs) < (gem - 0.05)) {
        Goedkoop_Uur.postUpdate(ON)
    } else {
        Goedkoop_Uur.postUpdate(OFF)
    }
end

rule "Batterij laden in de goedkoopste uren"
when
    Item Goedkoop_Uur changed to ON
then
    val soc = (Batterij_SOC.state as Number).intValue
    if (soc >= 95) {
        logInfo("energie", "Batterij vol — niet laden")
        return;
    }
    // Positief setpoint = laden. Blijf onder het maximale laadvermogen
    // dat je fabrikant opgeeft; buiten die grenzen kan garantie vervallen.
    Batterij_Setpoint.sendCommand(2000)
    Batterij_Modus.postUpdate("LADEN")
end

rule "Ontladen op de dagpiek, met ondergrens"
when
    Item Prijs_Nu changed
then
    val prijs = (Prijs_Nu.state as Number).floatValue
    val gem   = (Prijs_Gemiddeld.state as Number).floatValue
    val soc   = (Batterij_SOC.state as Number).intValue

    if (prijs > (gem + 0.05) && soc > 20) {
        Batterij_Setpoint.sendCommand(-1700)   // negatief = ontladen
        Batterij_Modus.postUpdate("ONTLADEN")
    } else if (soc <= 20) {
        Batterij_Setpoint.sendCommand(0)
        Batterij_Modus.postUpdate("AUTO")
    }
end

rule "Failsafe: nooit langer dan drie uur handmatig gestuurd"
when
    Time cron "0 */15 * * * ?"
then
    if (Batterij_Modus.state.toString != "AUTO") {
        val minuten = (now.toEpochSecond() -
            (Batterij_Modus.lastUpdate("rrd4j").toEpochSecond())) / 60
        if (minuten > 180) {
            Batterij_Setpoint.sendCommand(0)
            Batterij_Modus.postUpdate("AUTO")
            logWarn("energie", "Failsafe: modus teruggezet naar automatisch")
        }
    }
end

rule "Waarschuwing bij verouderde prijsdata"
when
    Time cron "0 30 * * * ?"
then
    if (Prijs_Gemiddeld.state == NULL || Prijs_Gemiddeld.state == UNDEF) {
        Batterij_Setpoint.sendCommand(0)
        Batterij_Modus.postUpdate("AUTO")
        logWarn("energie", "Prijsbron onbereikbaar — sturing uitgeschakeld")
    }
end
```

De laatste twee rules zijn geen luxe. Een prijs die als `0` of `NULL` binnenkomt bij een mislukte API-aanroep is de meest voorkomende oorzaak van een batterij die op het duurste moment gaat laden.

Voor de `lastUpdate`-aanroep heb je persistence nodig:

```java
// persistence/rrd4j.persist
Strategies {
    everyMinute : "0 * * * * ?"
    default = everyChange
}
Items {
    gEnergie*, gPrijs*, Batterij_Modus : strategy = everyChange, everyMinute, restoreOnStartup
}
```

## Laag 4: sitemap

```java
// sitemaps/energie.sitemap

sitemap energie label="Energie" {
    Frame label="Nu" {
        Text   item=PV_Vermogen      icon="solarplant"
        Text   item=P1_VerbruikNu    icon="energy"
        Text   item=Batterij_SOC     icon="battery"
        Text   item=Batterij_Vermogen
    }
    Frame label="Prijs" {
        Text   item=Prijs_Nu         icon="price"
        Text   item=Prijs_Gemiddeld
        Text   item=Goedkoop_Uur     icon="price"
    }
    Frame label="Sturing" {
        Selection item=Batterij_Modus icon="settings"
            mappings=["AUTO"="Automatisch", "LADEN"="Laden", "ONTLADEN"="Ontladen"]
        Setpoint  item=Batterij_Setpoint minValue=-1700 maxValue=2200 step=100
    }
    Frame label="Vandaag" {
        Chart  item=PV_Vermogen      period=D refresh=60000
        Chart  item=Batterij_SOC     period=D refresh=60000
        Chart  item=Prijs_Nu         period=D refresh=300000
    }
    Frame label="Week" {
        Chart  item=PV_DagTotaal     period=W
    }
}
```

De `Setpoint`-grenzen in dit voorbeeld (2.200 W laden, 1.700 W ontladen) zijn de opgaven van één specifieke batterij. Vul hier de waarden van je eigen toestel in; sturen buiten de fabrieksgrenzen is de snelste manier om een garantiediscussie te krijgen.

## Wat levert het op? Een modelberekening

Onderstaande cijfers zijn een modelberekening met expliciete aannames, geen meting.

Aannames: een batterij van 10 kWh, een dynamisch contract en een verschuifbaar volume van ongeveer 1.350 kWh per jaar (10 kWh × 150 zoncycli, begrensd door overschot en afname), retourrendement 90 procent. Bij een all-in inkoopprijs van €0,26/kWh (EPEX €0,105 + energiebelasting €0,11085 + €0,044 opslag en vaste-kostenomslag, alles inclusief btw, de opslag is een gelabelde aanname) en een aangenomen terugleververgoeding van €0,07/kWh vanaf 2027, komt de waarde van zelfverbruik uit op circa €230 per jaar. Daar bovenop rekenen wij €8 per kWh capaciteit per jaar aan netarbitrage — een eigen afleiding uit ongeveer 100 wintercycli met €0,10 netto spreiding, alleen haalbaar op een dynamisch contract — dus €80. Samen circa **€310 per jaar** voor een systeem van 10 kWh.

Wat openHAB daar precies aan toevoegt, is niet los te meten: de batterij zou met de eigen fabrieksregeling ook een deel van dat bedrag halen. De winst van eigen sturing zit in de uren die de fabrieksregeling laat liggen, en die winst is voor iedereen anders. Wie een percentage noemt zonder je eigen kwartiergegevens te kennen, verzint het.

Reken het door met je eigen cijfers: zie [de terugverdientijd-vergelijker voor thuisbatterijen](/thuisbatterij-terugverdientijd-vergelijken/) en [de day-ahead-prijzen per uur](/stroomprijzen/).

## Voorbeeldopzet: openHAB met SMA-omvormer en BYD-batterij

Een opzet die met publiek beschikbare bindings te bouwen is: openHAB 4.x op een NAS of mini-pc, een SMA Sunny Boy via Modbus (SMA documenteert zijn Modbus-profiel), een BYD Battery-Box via Modbus TCP, en de day-ahead-prijzen via de HTTP-binding zoals hierboven. Van daaruit stuur je zowel batterij-laden als EV-laden met rules.

Wat je met zo'n opzet bereikt is een hogere zelfconsumptie dan zonder sturing — hoe hoog precies, hangt af van je verbruikprofiel, de batterijcapaciteit en hoeveel van je verbruik verschuifbaar is. Reken het door met je eigen kwartiergegevens.

## Veelgemaakte fouten in een openHAB-energiestack

1. **Voorbeelden van de verkeerde versie kopiëren.** De Modbus-binding heeft tussen major releases een andere configuratiesyntax gehad; oude forumvoorbeelden geven cryptische fouten. Check altijd voor welke openHAB-versie een voorbeeld is geschreven.
2. **Geen persistence ingesteld.** Zonder rrd4j of InfluxDB heb je geen grafieken, geen `lastUpdate` en dus ook geen bruikbare failsafe.
3. **Rules zonder typecheck en zonder null-check.** `state as Number` op een item dat `NULL` is, laat de hele rule stilvallen — vaak precies op het moment dat je hem nodig hebt.
4. **Prijsdata niet cachen of niet valideren.** Een mislukte aanroep die als prijs 0 wordt gelezen, laat je batterij op de duurste momenten laden.
5. **Geen minimum-SoC.** Bouw een ondergrens (bijvoorbeeld 20 procent) in de ontlaadrule, niet alleen in de app van de fabrikant.
6. **Buiten de fabrieksgrenzen sturen.** Laad- en ontlaadvermogens hebben een maximum. Sturen daarboven kan garantie kosten; check de voorwaarden van je fabrikant.

## Wanneer openHAB minder geschikt is

Zonder ervaring met Linux, JVM-onderhoud en een teksteditor kom je in openHAB vaker vast te zitten dan in Home Assistant, dat meer via de interface werkt. Wil je uitsluitend slim laden en batterijsturing, dan is EVCC eenvoudiger en doelgerichter. Heb je al een openHAB-installatie met tientallen things voor licht, verwarming en beveiliging, dan is de energiestack erbij bouwen juist de logische keuze.

Verder lezen: [Home Assistant en een warmtepomp koppelen](/posts/home-assistant-warmtepomp-integratie-2026/), [P1-meters en energiemonitors vergeleken](/posts/beste-energiemonitor-p1-meter-2026/) en [de day-ahead-prijzen per uur](/stroomprijzen/).
