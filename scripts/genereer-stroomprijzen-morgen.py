#!/usr/bin/env python3
"""Genereert dagelijks content/stroomprijzen-morgen.md uit de publieke DTL-data-API.
Draait via GitHub Actions ná publicatie van de day-ahead-prijzen (~15:00 NL).
Schrijft alleen als er daadwerkelijk morgen-data is; anders exit 0 zonder wijziging."""
import json, sys, urllib.request
from datetime import date, timedelta

API = "https://beheer.wtdigital.nl/api/public/stroomprijzen?dag=morgen"
BELASTING = 0.11085  # energiebelasting 2026 incl. btw
OPSLAG = 0.044       # inkoopopslag-aanname incl. btw (sitebrede rekenconstante)

def haal():
    req = urllib.request.Request(API, headers={"User-Agent": "DuurzaamThuisLab-daily/1.0 (+https://duurzaamthuislab.nl)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

d = haal()
morgen = (date.today() + timedelta(days=1)).isoformat()
if d.get("datum") != morgen or not d.get("uren") or len(d["uren"]) < 20:
    print(f"Geen (volledige) morgen-data: datum={d.get('datum')}, uren={len(d.get('uren') or [])}. Niets te doen.")
    sys.exit(0)

uren = d["uren"]
prijzen = [u["prijs"] for u in uren]
gem = round(sum(prijzen) / len(prijzen), 4)
mn = min(uren, key=lambda u: u["prijs"]); mx = max(uren, key=lambda u: u["prijs"])
neg = [u for u in uren if u["prijs"] < 0]

def blok(n):
    beste = min(range(len(uren) - n + 1), key=lambda i: sum(prijzen[i:i+n]))
    return uren[beste]["uur"], uren[beste+n-1]["uur"] + 1, round(sum(prijzen[beste:beste+n]) / n, 4)
b2 = blok(2); b4 = blok(4)

MAANDEN = ["januari","februari","maart","april","mei","juni","juli","augustus","september","oktober","november","december"]
dt = date.fromisoformat(morgen)
DAGEN = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
datum_nl = f"{DAGEN[dt.weekday()]} {dt.day} {MAANDEN[dt.month-1]} {dt.year}"

def eur(x): return f"€{x:.4f}".replace(".", ",")
def eurc(x): return f"€{x:.2f}".replace(".", ",")

allin_gem = gem + BELASTING + OPSLAG
if neg:
    negtekst = f"{len(neg)} uur met een negatieve beursprijs ({', '.join(f'{u['uur']}:00' for u in neg[:8])}{'…' if len(neg)>8 else ''})"
    negkort = f", met {len(neg)} negatieve uren"
else:
    negtekst = "geen negatieve uren"; negkort = ""

duiding = "een goedkope dag" if gem < 0.07 else ("een gemiddelde dag" if gem < 0.14 else "een dure dag")
spreiding = mx["prijs"] - mn["prijs"]

kwart = sorted(prijzen)[len(prijzen)//4]
goedkoop_uren = sorted(u["uur"] for u in uren if u["prijs"] <= kwart)[:8]

rijen = "\n".join(
    f"| {u['uur']:02d}:00–{(u['uur']+1)%24:02d}:00 | {eur(u['prijs'])} | {eur(u['prijs']+BELASTING+OPSLAG)} |"
    for u in uren)

md = f'''---
title: "Stroomprijzen morgen ({datum_nl}): uurprijzen en goedkoopste momenten"
description: "De dynamische stroomprijzen voor {datum_nl}: gemiddeld {eur(gem)}/kWh op de beurs{negkort}. Het goedkoopste blok en wat dat betekent voor wasmachine, EV en batterij."
date: 2026-08-21
lastmod: {date.today().isoformat()}
author: Team DuurzaamThuisLab
categories: [energiecontracten]
tags: [stroomprijzen, dynamisch contract]
affiliate: false
url: /stroomprijzen-morgen/
faq:
  - q: 'Hoe laat zijn de stroomprijzen van morgen bekend?'
    a: 'De day-ahead-veiling van de EPEX sluit om 12:00 en de uitkomst wordt in de loop van de middag gepubliceerd, meestal rond 15:00 Nederlandse tijd. Deze pagina wordt daarna automatisch bijgewerkt.'
  - q: 'Is de beursprijs wat ik echt betaal?'
    a: 'Nee. Bovenop de kale beursprijs (incl. btw) komen de energiebelasting van €0,11085 per kWh (2026, incl. btw) en de inkoopvergoeding en vaste kosten van je leverancier. De all-in-kolom hieronder rekent met onze sitebrede opslag-aanname van €0,044 incl. btw; jouw werkelijke opslag staat in je contract.'
  - q: 'Wat betekent een negatieve stroomprijs voor mij?'
    a: 'Bij een negatieve kale prijs krijg je op een dynamisch contract geld toe over de beurscomponent, maar de energiebelasting en de leveranciersopslag betaal je altijd. Pas als de kale prijs dieper daalt dan circa −€0,13 kan het totaal onder nul komen. Zie onze uitleg op de negatieve-stroomprijzen-pagina.'
---

> **Kort antwoord:** morgen ({datum_nl}) is de gemiddelde kale beursprijs **{eur(gem)}/kWh** (incl. btw) — {duiding} vergeleken met het 2025-gemiddelde van €0,105. Het goedkoopste uur is **{mn['uur']:02d}:00–{mn['uur']+1:02d}:00** ({eur(mn['prijs'])}), het duurste **{mx['uur']:02d}:00–{mx['uur']+1:02d}:00** ({eur(mx['prijs'])}). Er zijn morgen {negtekst}. Het goedkoopste 2-uursblok voor de wasmachine: **{b2[0]:02d}:00–{b2[1]:02d}:00**.

*Deze pagina wordt elke middag automatisch bijgewerkt zodra de day-ahead-prijzen zijn gepubliceerd. Kale EPEX-beursprijs incl. btw, excl. energiebelasting en leverancierskosten (bron: EnergyZero). Aan deze informatie kunnen geen rechten worden ontleend.*

## De prijzen van morgen in het kort

- **Gemiddelde beursprijs:** {eur(gem)}/kWh — all-in met belasting en opslag-aanname circa {eur(allin_gem)}/kWh
- **Goedkoopste uur:** {mn['uur']:02d}:00–{mn['uur']+1:02d}:00 ({eur(mn['prijs'])} kaal)
- **Duurste uur:** {mx['uur']:02d}:00–{mx['uur']+1:02d}:00 ({eur(mx['prijs'])} kaal)
- **Spreiding:** {eurc(spreiding)} tussen het goedkoopste en duurste uur — {'de moeite van het verschuiven waard' if spreiding > 0.08 else 'een vlakke dag; verschuiven levert weinig op'}
- **Negatieve uren:** {negtekst}

## De beste momenten om te verschuiven

| Wat | Beste moment morgen | Gemiddelde kale prijs |
|---|---|---|
| Wasmachine of vaatwasser (2 uur) | **{b2[0]:02d}:00–{b2[1]:02d}:00** | {eur(b2[2])} |
| EV of thuisbatterij laden (4 uur) | **{b4[0]:02d}:00–{b4[1]:02d}:00** | {eur(b4[2])} |

De goedkoopste uren van de dag zijn {', '.join(f"{u:02d}:00" for u in goedkoop_uren)}. Live meesturen met de actuele prijs kan op onze [stroomprijzen-pagina](/stroomprijzen/) en het beste wasmoment staat altijd actueel op [beste tijd wasmachine](/beste-tijd-wasmachine/).

## Alle uurprijzen voor {datum_nl}

| Uur | Kale beursprijs (incl. btw) | Indicatie all-in* |
|---|---|---|
{rijen}

*\\*All-in = kale prijs + energiebelasting €0,11085 + opslag-aanname €0,044 (beide incl. btw). Je werkelijke leveranciersopslag staat in je contract. Netbeheerkosten zijn een vast jaarbedrag en tellen niet per kWh mee.*

## Wat je hiermee kunt

Met een **dynamisch contract** betaal je deze uurprijzen (plus belasting en opslag) direct. Verschuifbaar verbruik — wasmachine, droger, EV, thuisbatterij — verplaats je naar de blokken hierboven. Wat dat op jaarbasis oplevert, hangt af van hoeveel je kunt verschuiven: reken het na met onze [energiekosten-calculator](/posts/energiebesparing-calculator-2027/) of lees de [vergelijking van dynamische contracten](/dynamisch-energiecontract-vergelijken/).

Met een **vast contract** verandert je kWh-prijs niet met deze uren; dan is deze pagina vooral interessant om te zien wat je zou kunnen besparen. Historische prijzen tot 2014 terug staan in ons [prijzenarchief](/stroomprijzen-historie/).
'''

open("content/stroomprijzen-morgen.md", "w").write(md)
print(f"Geschreven: {datum_nl}, gem {gem}, {len(neg)} negatieve uren")
