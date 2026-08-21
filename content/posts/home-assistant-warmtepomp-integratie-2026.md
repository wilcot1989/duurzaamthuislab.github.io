---
title: 'Home Assistant + warmtepomp: koppelen via Modbus, met YAML-voorbeelden'
date: '2026-08-02 08:00:00+02:00'
lastmod: '2026-08-21 08:00:00+02:00'
draft: false
description: Een warmtepomp koppelen aan Home Assistant via Modbus of een merkintegratie. Stappenplan, werkende YAML-voorbeelden, automatiseringen op day-ahead-prijzen en de valkuilen.
categories:
- smart-home
tags:
- smart-home
- verduurzamen
- duurzaam wonen
- home
keywords:
- home assistant warmtepomp
- ha modbus warmtepomp
- quatt home assistant
- slimme warmtepomp sturing
- ha energie automatisering
affiliate: true
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1466611653911-95081537e5b7&w=1200&output=webp&q=70
faq:
- q: 'Welke warmtepompmerken hebben een officiële Home Assistant-integratie?'
  a: 'In Home Assistant core staan onder meer Nibe (nibe_heatpump, sinds HA 2022.10, Modbus TCP of nibegw), Mitsubishi Electric via MELCloud (cloud polling, lucht-lucht én lucht-water), Daikin (lokaal, via de wifi-controller BRP069A4x), Viessmann ViCare (cloud polling) en Atag One (lokaal). Gecontroleerd op home-assistant.io, 21 augustus 2026. Voor Quatt staat er op dat moment géén integratiepagina in Home Assistant core; koppeling loopt via een niet door HA-core onderhouden custom-integratie. Dat is dus onbevestigd.'
- q: 'Heb ik Modbus nodig of kan het via de app-cloud?'
  a: 'Beide kan. Een cloudintegratie (MELCloud, ViCare, Onecta-hardware) is sneller opgezet, maar valt uit als het internet of de fabrikantcloud uit ligt en kent API-limieten — ViCare staat op de gratis laag bijvoorbeeld 120 aanroepen per 10 minuten toe. Modbus TCP werkt lokaal en blijft werken zonder internet, maar je hebt het serviceboek met de registeradressen van jouw toestel nodig.'
- q: 'Wat heb ik minimaal nodig om op prijs te sturen?'
  a: 'Drie dingen: een entiteit met de day-ahead-prijs per uur, een entiteit waarmee je het setpoint of de bedrijfsmodus van de warmtepomp kunt zetten, en een buffer om de warmte in te parkeren (buffervat, boiler of de traagheid van de vloerverwarming). Zonder buffer schuif je niets op; je zet de pomp dan alleen uit op dure momenten en dat kost comfort.'
- q: 'Heb ik een P1-meter nodig?'
  a: 'Niet voor prijssturing, wel om te zien of het werkt. Een P1-meter geeft je verbruik per seconde in plaats van de kwartierwaarden van je leverancier. De HomeWizard P1 (HWE-P1) heeft een officiële, lokale HA-integratie sinds HA 2022.2; een ESP32 met DSMR-leesbril of Smartgateways werkt ook.'
- q: 'Verliest mijn warmtepomp rendement door prijssturing?'
  a: 'Ja, en dat moet je meerekenen. Warmte wegzetten op een hogere aanvoertemperatuur verlaagt de COP: bij 55 °C is die merkbaar lager dan bij 40 °C. De prijswinst per kWh moet dus groter zijn dan het rendementsverlies. Bij smalle prijsspreads valt dat negatief uit.'
products:
- name: HomeWizard P1-meter
  url: https://go.duurzaamthuislab.nl/homewizard
  price: '24.95'
schema_type: Article
last_updated: '2026-08-21'
---
*Disclosure: de link naar HomeWizard in dit artikel is een affiliate-link (via Daisycon). Koop je daarvia, dan ontvangen wij mogelijk een commissie, zonder extra kosten voor jou. Met warmtepompfabrikanten en energieleveranciers in dit artikel hebben wij géén commissie- of affiliaterelatie; die namen worden alleen genoemd omdat hun integratie of documentatie relevant is. Bron voor de integratie-informatie: home-assistant.io, opgehaald op 21 augustus 2026. HomeWizard-prijs: homewizard.com, prijspeil augustus 2026.*

> **Kort antwoord:** een warmtepomp koppel je aan Home Assistant via een merkintegratie (Nibe, MELCloud, Daikin, ViCare, Atag One) of — als die er niet is — via Modbus TCP met de registeradressen uit het serviceboek. Daarna heb je een prijsentiteit en een buffer nodig om warmte naar goedkope uren te verschuiven. Hieronder de YAML die daarvoor nodig is.

## Wat werkt er echt: de integraties die in Home Assistant core zitten

Dit is het eerste dat je wil weten voordat je iets koopt of aansluit. De volgende integraties staan in Home Assistant core (gecontroleerd op home-assistant.io, 21 augustus 2026):

| Integratie | Merk/toestel | Verbinding | Sinds |
|---|---|---|---|
| `nibe_heatpump` | Nibe F- en S-serie, VVM | Modbus TCP (S-serie), nibegw (RS485), Modbus RTU | HA 2022.10 |
| `melcloud` | Mitsubishi Electric, lucht-lucht en lucht-water | cloud polling | ouder dan 2022 |
| `daikin` | Daikin met wifi-controller BRP069A41/42/43/45 | lokaal (UDP) | HA 0.59 |
| `vicare` | Viessmann ViCare | cloud polling (API-limiet op gratis laag) | HA 0.99 |
| `atag` | Atag One thermostaat | lokaal | HA 0.109 |
| `homewizard` | P1-meter, Energy Socket, kWh-meter, Plug-In Battery | lokaal, 5 s polling | HA 2022.2 |
| `modbus` | elk toestel met Modbus TCP/RTU | lokaal | core |

Twee dingen die hier níet in staan, en die je elders wel als feit ziet opduiken:

- **Quatt.** Er is op 21 augustus 2026 geen integratiepagina voor Quatt in Home Assistant core (`home-assistant.io/integrations/quatt/` geeft een 404). Koppelen kan via een custom-integratie uit de community, maar dat is geen door HA-core onderhouden en gedocumenteerde integratie. Wij noemen die koppeling daarom **onbevestigd** en niet als officiële integratie.
- **Vaillant en Bosch.** Ook hiervoor staat niets in core. Er bestaan community-integraties op basis van de fabrikant-app-API's; die kunnen breken zodra de fabrikant zijn app-API wijzigt.

De les: check vóór aanschaf of jouw exacte model in core staat of een Modbus-poort heeft. Een merk dat alleen via een app-API te bereiken is, is de kwetsbaarste route.

## Stappenplan

**Stap 1 — meet eerst, stuur later.** Zet een P1-meter in Home Assistant en laat het een tot twee weken meelopen. Je wil weten hoeveel kWh de warmtepomp per etmaal trekt en op welke uren. Zonder dat getal kun je later niet zien of je automatisering iets oplevert.

Wij gebruiken zelf een P1-meter als databron voor de energiepagina's op deze site. <a href="https://go.duurzaamthuislab.nl/homewizard?ref=/posts/home-assistant-warmtepomp-integratie-2026/" class="cta cta-affiliate" rel="noopener nofollow sponsored" target="_blank">Bekijk de HomeWizard P1-meter (€24,95)</a>

**Stap 2 — haal de prijsdata binnen.** Je hebt een entiteit nodig met de prijs per uur voor vandaag en (na ongeveer 13:00) morgen. Dat kan via de integratie van je leverancier, of via een REST-sensor op een publieke bron. Zie het YAML-voorbeeld hieronder met onze eigen open endpoint.

**Stap 3 — koppel de warmtepomp.** Eerst kijken of je merk in de tabel hierboven staat. Zo niet: serviceboek erbij, Modbus TCP aanzetten op de regelaar en de registeradressen opzoeken. Begin met alleen *lezen* (temperaturen, vermogen) voordat je iets gaat schrijven.

**Stap 4 — bepaal wat je stuurt.** Er zijn drie realistische stuurgrepen, in volgorde van veiligheid: (a) het setpoint van het buffervat of de warmtapwaterboiler, (b) een verschuiving op de stooklijn (een paar graden op of af), (c) aan/uit via een blokkeeringang. Optie (c) is het grofst en kost het meeste rendement.

**Stap 5 — bouw een fallback.** De warmtepomp moet zonder Home Assistant zijn eigen regeling blijven volgen. Schrijf nooit een permanente blokkade weg die blijft staan als HA crasht, en zet een `for`-duur of een watchdog-automatisering op elke blokkade.

**Stap 6 — evalueer over een heel stookseizoen.** Vergelijk niet twee weken met twee weken: correct voor graaddagen. Een milde week ziet er altijd uit als een succesvolle automatisering.

## YAML-voorbeeld 1: Modbus TCP (generiek)

Onderstaande configuratie is een **template**: de registeradressen hieronder zijn voorbeelden en verschillen per fabrikant en zelfs per firmwareversie. Haal jouw adressen uit het Modbus-document of serviceboek van je toestel — verkeerde adressen schrijven kan instellingen overschrijven.

```yaml
# configuration.yaml
modbus:
  - name: warmtepomp
    type: tcp
    host: 192.168.1.50
    port: 502
    delay: 5
    message_wait_milliseconds: 30
    sensors:
      - name: wp_aanvoertemperatuur
        slave: 1
        address: 40001          # voorbeeldadres — vervang door dat van jouw toestel
        input_type: holding
        data_type: int16
        scale: 0.1
        precision: 1
        unit_of_measurement: "°C"
        device_class: temperature
      - name: wp_retourtemperatuur
        slave: 1
        address: 40002
        input_type: holding
        data_type: int16
        scale: 0.1
        precision: 1
        unit_of_measurement: "°C"
        device_class: temperature
      - name: wp_elektrisch_vermogen
        slave: 1
        address: 40010
        input_type: holding
        data_type: uint16
        unit_of_measurement: W
        device_class: power
        state_class: measurement
    climates:
      - name: warmtepomp_buffer
        slave: 1
        address: 40100
        input_type: holding
        target_temp_register: 40100
        data_type: int16
        scale: 0.1
        precision: 1
        min_temp: 20
        max_temp: 55
        temp_step: 0.5
```

Dit levert je een `climate.warmtepomp_buffer` plus drie sensoren op. Begin met de sensoren en laat het `climates`-blok eruit tot je zeker weet dat het adres klopt.

## YAML-voorbeeld 2: day-ahead-prijzen als REST-sensor

Heeft je leverancier geen integratie, dan kun je de uurprijzen ophalen uit een publieke bron. Onderstaand voorbeeld gebruikt onze eigen open endpoint, die de day-ahead-prijzen (kale EPEX-prijs inclusief btw, exclusief energiebelasting en inkoopvergoeding) per uur teruggeeft:

```yaml
# configuration.yaml
rest:
  - resource: https://beheer.wtdigital.nl/api/public/stroomprijzen
    scan_interval: 900
    sensor:
      - name: stroomprijs_gemiddeld_vandaag
        value_template: "{{ value_json.gemiddelde }}"
        unit_of_measurement: "EUR/kWh"
      - name: stroomprijs_nu
        value_template: >
          {% set u = now().hour %}
          {{ (value_json.uren | selectattr('uur','eq',u) | map(attribute='prijs') | first) | default(0) }}
        unit_of_measurement: "EUR/kWh"
        json_attributes:
          - uren
          - datum
          - bron
```

Let op: dit is de **kale** marktprijs. Wat jij per kWh betaalt is die prijs plus energiebelasting (€0,11085 per kWh inclusief btw in 2026) plus de inkoopvergoeding en vaste kosten van je leverancier. Voor sturing maakt dat niet uit — de belasting is elk uur gelijk, dus de spread tussen uren is hetzelfde — maar voor het uitrekenen van je besparing wel.

## YAML-voorbeeld 3: is dit een goedkoop uur?

Een drempel van "onder 10 cent" werkt in de winter anders dan in de zomer. Beter is een relatieve drempel: goedkoop ten opzichte van het daggemiddelde.

```yaml
# configuration.yaml
template:
  - binary_sensor:
      - name: Goedkoop uur
        unique_id: goedkoop_uur
        state: >
          {% set nu = states('sensor.stroomprijs_nu') | float(0) %}
          {% set gem = states('sensor.stroomprijs_gemiddeld_vandaag') | float(0) %}
          {{ gem > 0 and nu < (gem - 0.05) }}
        availability: >
          {{ states('sensor.stroomprijs_nu') not in ['unknown', 'unavailable'] }}
```

## YAML-voorbeeld 4: buffer opladen in de goedkope uren

```yaml
# automations.yaml
- alias: Buffer opladen bij lage dagprijs
  id: wp_buffer_laden_goedkoop
  trigger:
    - platform: state
      entity_id: binary_sensor.goedkoop_uur
      to: "on"
  condition:
    - condition: numeric_state
      entity_id: sensor.buitentemperatuur
      above: -2
    - condition: numeric_state
      entity_id: sensor.wp_aanvoertemperatuur
      below: 42
  action:
    - service: climate.set_temperature
      target:
        entity_id: climate.warmtepomp_buffer
      data:
        temperature: 47
    - delay: "02:00:00"
    - service: climate.set_temperature
      target:
        entity_id: climate.warmtepomp_buffer
      data:
        temperature: 38
  mode: single
```

Twee dingen over deze automatisering. Ten eerste: de `delay` met een terugzet-actie is de eenvoudigste vorm van een fallback — na twee uur staat het setpoint weer normaal, ook als de prijsdata daarna uitvalt. Ten tweede: `service:` mag in recente Home Assistant-versies ook `action:` heten; beide werken, `service:` is de vorm die in alle versies sinds jaren geldig is.

Wil je hetzelfde voor warmtapwater, dan is dat vaak de veiligere eerste stap: een boiler van 180 liter die je van 45 naar 55 °C opwarmt parkeert ongeveer 2 kWh warmte, en anders dan bij vloerverwarming merkt niemand het in het comfort.

## YAML-voorbeeld 5: blokkeren op de piek, met watchdog

```yaml
# automations.yaml
- alias: Warmtepomp terugschroeven op het duurste uur
  id: wp_piek_terug
  trigger:
    - platform: template
      value_template: >
        {% set uren = state_attr('sensor.stroomprijs_nu','uren') | default([], true) %}
        {% set nu = states('sensor.stroomprijs_nu') | float(0) %}
        {% set top = uren | map(attribute='prijs') | list | sort | last | default(0) %}
        {{ uren | count > 0 and nu >= top }}
  action:
    - service: climate.set_temperature
      target:
        entity_id: climate.warmtepomp_buffer
      data:
        temperature: 32
  mode: single

- alias: Watchdog — setpoint nooit langer dan 3 uur verlaagd
  id: wp_watchdog
  trigger:
    - platform: numeric_state
      entity_id: climate.warmtepomp_buffer
      attribute: temperature
      below: 34
      for: "03:00:00"
  action:
    - service: climate.set_temperature
      target:
        entity_id: climate.warmtepomp_buffer
      data:
        temperature: 38
  mode: single
```

## Wat levert het op? Een modelberekening

Onderstaande cijfers zijn een **modelberekening met expliciete aannames**, geen meting van een eigen installatie.

Aannames: een warmtepomp die per etmaal 20 kWh elektrisch verbruikt in een koude periode, waarvan je 6 kWh kunt verschuiven van een duur naar een goedkoop uur. Op basis van de EPEX-data over 2025 (jaargemiddelde €0,105/kWh inclusief btw) is een spread van €0,08/kWh tussen het goedkoopste en het duurste kwart van de dag een realistische orde van grootte in het stookseizoen; sommige dagen zijn veel beter, sommige vlak.

- Bruto prijswinst: 6 kWh × €0,08 = €0,48 per etmaal.
- Rendementsverlies: warmte wegzetten op een hogere temperatuur verlaagt de COP. Ga uit van 8 procent slechter rendement op die 6 kWh, dan kost dat ongeveer 0,5 kWh extra tegen een gemiddelde all-in prijs van €0,26/kWh (aanname all-in: EPEX €0,105 + energiebelasting €0,11085 + €0,044 opslag en vaste-kostenomslag, alle bedragen inclusief btw) — circa €0,13.
- Netto: ongeveer €0,35 per etmaal, over 150 stookdagen circa **€50 per jaar**.

Dat is het eerlijke beeld: prijssturing van een warmtepomp is geen verdienmodel maar een optimalisatie. Het loont vooral als je toch al een dynamisch contract hebt, als je een echt buffervat hebt (niet alleen vloerverwarming) en als je het opzetten als hobby ziet. Heb je een vast contract, dan is er geen spread om op te sturen en blijft alleen hysterese-optimalisatie over — dat is voor de meeste huishoudens de tijdsinvestering niet waard.

Reken het door met je eigen cijfers: kijk in [de stroomprijzen per uur](/stroomprijzen/) hoe groot de spread op jouw dagen werkelijk is.

## Voorbeeldopzet: Daikin Altherma 3H op een dynamisch contract

Een opzet die volledig uit publiek gedocumenteerde onderdelen bestaat: een Daikin Altherma 3H, gekoppeld via de wifi-controller (BRP069A4x) en de `daikin`-integratie in HA core, met de uurprijzen uit een leveranciersintegratie of de REST-sensor hierboven.

De automatisering: zakt de dag-vooruitprijs onder de drempel én ligt de buitentemperatuur boven nul, dan gaat het setpoint van het buffervat omhoog zodat er warmte wordt weggezet in de goedkope uren. In de dure uren draait de pomp op een lager setpoint of staat hij stil.

Wat dit oplevert hangt af van drie dingen: de bufferomvang (hoeveel kWh je kunt wegzetten), het temperatuurverschil dat je bereid bent te accepteren, en de spread tussen goedkope en dure uren. Het verschuiven van warmte naar een hogere aanvoertemperatuur kost rendement — een warmtepomp die naar 55 °C opwarmt heeft een merkbaar lagere COP dan bij 40 °C — dus de prijswinst moet groter zijn dan het COP-verlies. Bij smalle spreads valt dat nadelig uit, bij brede spreads gunstig.

## Veelgemaakte integratiefouten

1. **Te agressief sturen.** Modulerende warmtepompen werken het efficiëntst op een constante curve. Vaker schakelen verlaagt de COP juist.
2. **Buitensensor negeren.** Sturen op alleen prijs, zonder buitentemperatuur, leidt in het voorjaar tot oververhitting en in strenge vorst tot een pomp die op het verkeerde moment uit staat.
3. **Verkeerde Modbus-mapping.** Niet elk toestel van hetzelfde merk heeft dezelfde registeradressen; ze wijzigen ook tussen firmwareversies. Serviceboek erbij, en eerst alleen lezen.
4. **Geen veiligheidsfallback.** Als HA crasht moet de warmtepomp zijn eigen logica blijven volgen. Bouw een watchdog zoals in voorbeeld 5.
5. **Vloerverwarmingstraagheid onderschatten.** Een vloer reageert in uren op een setpointwijziging, niet in minuten. Plan vooruit, of stuur op het buffervat en de boiler in plaats van op de vloer.
6. **Cloud-API-limieten negeren.** Bij ViCare loop je op de gratis laag tegen de limiet aan als je elke 10 seconden pollt; de integratie valt dan uit precies wanneer je hem nodig hebt.

## Wanneer integratie de moeite niet waard is

Heb je een vast energiecontract, dan is er geen prijsverschil per uur om op te sturen; wat overblijft is comfort en inzicht, niet besparing. Heb je een hybride opstelling zonder dataport voor modulatie, dan kun je via HA hooguit aan/uit sturen — en dat doet de regeling van de installatie zelf doorgaans beter. En heb je geen enkele buffer (geen buffervat, geen boiler, alleen radiatoren), dan is er niets om warmte in te parkeren.

Verder lezen: [energiemonitor en P1-meters vergeleken](/posts/beste-energiemonitor-p1-meter-2026/), [de day-ahead-prijzen per uur](/stroomprijzen/) en [wat het einde van de saldering betekent](/posts/saldering-stopt-2027-volledige-gids/).
