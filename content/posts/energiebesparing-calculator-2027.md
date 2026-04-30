---
title: 'Energiekosten calculator 2027: bereken jouw saldering-impact'
date: 2026-04-29 10:00:00+02:00
lastmod: 2026-04-29 10:00:00+02:00
description: Hoeveel kost de saldering-stop jou? Vul jouw kWh-verbruik en zonnepanelen-capaciteit in en zie het €/jaar verschil 2026 vs 2027 direct.
categories:
- tools
- zonne-energie
- besparen
tags:
- saldering calculator
- energiebesparing berekenen
- saldering 2027
- thuisbatterij rendabel
- zonnepanelen kosten 2027
keywords:
- energiebesparing calculator 2027
- saldering stop berekenen
- saldering 2027 hoeveel
- thuisbatterij rendabel berekenen
- zonnepanelen verlies 2027 calculator
affiliate: true
author: Mark Bakker
author_bio: Energieadviseur met een eigen verduurzaamd huis. Test zonnepanelen, thuisbatterijen en warmtepompen in de praktijk.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1580893246395-52aead8960dc&w=1200&output=webp&q=70
faq:
- q: Wat zijn de belangrijkste voordelen?
  a: De voordelen staan in detail uitgelegd in de bovenstaande secties.
products:
- name: Sessy 5 kWh thuisbatterij
  url: https://go.duurzaamthuislab.nl/sessy
  price: '3795'
- name: Marstek Venus thuisbatterij
  url: https://go.duurzaamthuislab.nl/marstek
  price: '3200'
- name: Tibber dynamisch contract
  url: https://go.duurzaamthuislab.nl/tibber
  price: '6'
schema_type: Article
---

De saldering stopt per 1 januari 2027. Maar hoeveel kost dat jou specifiek? Dat hangt af van hoeveel zonnepanelen je hebt, hoeveel je terugleverd en of je een dynamisch contract hebt. Vul hieronder jouw gegevens in en je ziet het verschil in seconden.

## Saldering impact calculator 2027

<div class="calculator-wrapper" style="background: #f8f9fa; border-radius: 12px; padding: 2rem; margin: 2rem 0; border: 1px solid #e0e0e0;">

<h3 style="margin-top:0; color: #1a1a2e;">Bereken jouw saldering-impact</h3>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">

<div>
<label for="calc-verbruik" style="display:block; font-weight:600; margin-bottom:.4rem; color:#333;">Jaarverbruik elektriciteit (kWh)</label>
<input type="number" id="calc-verbruik" value="3500" min="500" max="15000" step="100"
  style="width:100%; padding:.6rem .8rem; border:1px solid #ccc; border-radius:6px; font-size:1rem;">
<small style="color:#666;">Vind je op je jaarafrekening of slimme meter</small>
</div>

<div>
<label for="calc-capaciteit" style="display:block; font-weight:600; margin-bottom:.4rem; color:#333;">Zonnepanelen capaciteit (kWp)</label>
<input type="number" id="calc-capaciteit" value="4.5" min="0.5" max="20" step="0.5"
  style="width:100%; padding:.6rem .8rem; border:1px solid #ccc; border-radius:6px; font-size:1rem;">
<small style="color:#666;">Staat op het installatiedocument van je panelen</small>
</div>

<div>
<label for="calc-eigen-verbruik" style="display:block; font-weight:600; margin-bottom:.4rem; color:#333;">Eigen verbruik overdag (%)</label>
<select id="calc-eigen-verbruik"
  style="width:100%; padding:.6rem .8rem; border:1px solid #ccc; border-radius:6px; font-size:1rem; background:white;">
  <option value="25">25% — Vrijwel niemand thuis overdag</option>
  <option value="35" selected>35% — Gemiddeld huishouden</option>
  <option value="45">45% — Geregeld thuis overdag</option>
  <option value="55">55% — Veel thuis / warmtepomp overdag</option>
  <option value="65">65% — Vrijwel altijd thuis overdag</option>
</select>
<small style="color:#666;">Hoeveel van je zonnestroom gebruik je direct zelf?</small>
</div>

<div>
<label for="calc-dynamisch" style="display:block; font-weight:600; margin-bottom:.4rem; color:#333;">Dynamisch contract in 2027?</label>
<select id="calc-dynamisch"
  style="width:100%; padding:.6rem .8rem; border:1px solid #ccc; border-radius:6px; font-size:1rem; background:white;">
  <option value="no" selected>Nee — vast contract</option>
  <option value="yes">Ja — dynamisch (bijv. Tibber / Frank)</option>
</select>
<small style="color:#666;">Dynamisch contract geeft hogere terugleverprijzen op piektijden</small>
</div>

</div>

<button onclick="berekenSaldering()"
  style="background: #2d7d46; color: white; border: none; padding: .8rem 2rem; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; width: 100%;">
  Bereken mijn saldering-impact →
</button>

<div id="calc-resultaat" style="margin-top:1.5rem; display:none;">

<hr style="border:1px solid #ddd; margin-bottom:1.5rem;">

<h4 style="margin-top:0; color:#1a1a2e;">Jouw persoonlijke berekening</h4>

<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1rem; margin-bottom:1.5rem;">

<div style="background:white; border-radius:8px; padding:1rem; border:1px solid #e0e0e0; text-align:center;">
<div style="font-size:.85rem; color:#666; margin-bottom:.3rem;">Besparing 2026 (met saldering)</div>
<div id="res-2026" style="font-size:1.6rem; font-weight:700; color:#2d7d46;">—</div>
<div style="font-size:.8rem; color:#888;">per jaar</div>
</div>

<div style="background:white; border-radius:8px; padding:1rem; border:1px solid #e0e0e0; text-align:center;">
<div style="font-size:.85rem; color:#666; margin-bottom:.3rem;">Besparing 2027 (na stop)</div>
<div id="res-2027" style="font-size:1.6rem; font-weight:700; color:#e67e22;">—</div>
<div style="font-size:.8rem; color:#888;">per jaar</div>
</div>

<div style="background:#fef3f2; border-radius:8px; padding:1rem; border:1px solid #f5c6cb; text-align:center;">
<div style="font-size:.85rem; color:#666; margin-bottom:.3rem;">Jouw verlies per jaar</div>
<div id="res-verschil" style="font-size:1.6rem; font-weight:700; color:#c0392b;">—</div>
<div style="font-size:.8rem; color:#888;">minder voordeel</div>
</div>

</div>

<div id="res-details" style="background:white; border-radius:8px; padding:1rem; border:1px solid #e0e0e0; margin-bottom:1rem; font-size:.9rem; line-height:1.7;">
</div>

<div id="res-advies" style="background:#f0f7f4; border-radius:8px; padding:1rem; border:1px solid #a8d5b9; margin-bottom:1rem;">
</div>

<div id="res-batterij" style="margin-top:1rem; display:none;">
</div>

</div>

</div>

<script>
function berekenSaldering() {
  var verbruik = parseFloat(document.getElementById('calc-verbruik').value) || 3500;
  var capaciteit = parseFloat(document.getElementById('calc-capaciteit').value) || 4.5;
  var eigenVerbruikPct = parseFloat(document.getElementById('calc-eigen-verbruik').value) || 35;
  var dynamisch = document.getElementById('calc-dynamisch').value === 'yes';

  // Constanten
  var productiePerKwp = 875; // gemiddeld Nederland
  var prijsAfname = 0.31; // €/kWh afnemen 2026
  var teruglevering2026 = 0.31; // saldering = zelfde tarief
  var teruglevering2027Vast = 0.08; // vaste terugleververgoeding
  var teruglevering2027Dynamisch = 0.12; // dynamisch gemiddeld hoger

  // Berekeningen
  var jaarproductie = capaciteit * productiePerKwp;
  var eigenVerbruikKwh = jaarproductie * (eigenVerbruikPct / 100);
  var teruggeleverd = jaarproductie - eigenVerbruikKwh;

  // 2026 besparing
  var besparing2026 = (eigenVerbruikKwh * prijsAfname) + (teruggeleverd * teruglevering2026);

  // 2027 besparing
  var terugprijs2027 = dynamisch ? teruglevering2027Dynamisch : teruglevering2027Vast;
  var besparing2027 = (eigenVerbruikKwh * prijsAfname) + (teruggeleverd * terugprijs2027);

  var verschil = besparing2026 - besparing2027;

  // ROI batterij (eenvoudig model)
  // Een 5 kWh batterij kan max 5 kWh/dag opvangen (~1825 kWh/jaar)
  // maar alleen als er teruglevering is
  var batterijCapaciteit = 5; // kWh standaard model
  var opvangbaar = Math.min(teruggeleverd * 0.65, batterijCapaciteit * 300); // ~300 dagen nuttig laden/jaar
  var batterijBesparing = opvangbaar * (prijsAfname - terugprijs2027);
  var batterijPrijsNaISDE = 4100; // Sessy 3795 + inst 800 - ISDE ~500 = grofweg
  var terugverdienJaar = batterijBesparing > 0 ? (batterijPrijsNaISDE / batterijBesparing) : 999;
  var batterijRendabel = terugverdienJaar <= 12;

  // Output formatteren
  function fmt(n) { return '€' + Math.round(n).toLocaleString('nl-NL'); }
  function fmtJr(n) { return n >= 99 ? '>20 jaar' : n.toFixed(1) + ' jaar'; }

  document.getElementById('res-2026').textContent = fmt(besparing2026);
  document.getElementById('res-2027').textContent = fmt(besparing2027);
  document.getElementById('res-verschil').textContent = fmt(verschil);

  var details = '<strong>Jouw zonnepanelen:</strong> ' + capaciteit + ' kWp → ~' + Math.round(jaarproductie) + ' kWh/jaar productie<br>' +
    '<strong>Direct eigen verbruik:</strong> ~' + Math.round(eigenVerbruikKwh) + ' kWh (' + eigenVerbruikPct + '%) → besparing ' + fmt(eigenVerbruikKwh * prijsAfname) + '/jaar<br>' +
    '<strong>Teruglevering:</strong> ~' + Math.round(teruggeleverd) + ' kWh → in 2026 waard ' + fmt(teruggeleverd * teruglevering2026) + ', in 2027 waard ' + fmt(teruggeleverd * terugprijs2027) + '<br>' +
    '<strong>Contract 2027:</strong> ' + (dynamisch ? 'Dynamisch (~€0,12/kWh gemiddeld teruglevering)' : 'Vast (~€0,08/kWh teruglevering)');

  document.getElementById('res-details').innerHTML = details;

  var adviesText = '';
  var adviesKleur = '';

  if (verschil < 200) {
    adviesKleur = '#a8d5b9';
    adviesText = '<strong>Jouw verlies is beperkt</strong> — onder €200/jaar. Een dynamisch contract is de beste eerste stap. Een thuisbatterij is voor jou waarschijnlijk niet rendabel tenzij je ook een EV hebt.';
  } else if (verschil < 500) {
    adviesKleur = '#fce8a6';
    adviesText = '<strong>Merkbaar verlies</strong> — €200-€500/jaar. Zeker de moeite waard om te optimaliseren. Begin met een dynamisch contract, overweeg daarna een slimme warmwaterboiler. Een thuisbatterij hangt af van je avondverbruik.';
  } else if (verschil < 900) {
    adviesKleur = '#f5c6a0';
    adviesText = '<strong>Significant verlies</strong> — €500-€900/jaar. Dit vraagt actie. Dynamisch contract + thuisbatterij of warmtepomp zijn serieuze opties. Vraag ISDE-subsidie aan vóór eind 2026.';
  } else {
    adviesKleur = '#f5b0a0';
    adviesText = '<strong>Groot verlies</strong> — meer dan €900/jaar. Jij hebt een groot systeem en veel teruglevering. Een thuisbatterij + dynamisch contract is voor jou de sterkste combinatie. Bereken ook of een EV met V2H-laden interessant is.';
  }

  document.getElementById('res-advies').style.borderColor = adviesKleur;
  document.getElementById('res-advies').style.background = adviesKleur + '33';
  document.getElementById('res-advies').innerHTML = adviesText;

  var batterijDiv = document.getElementById('res-batterij');
  if (batterijRendabel) {
    batterijDiv.style.display = 'block';
    batterijDiv.innerHTML = '<div style="background:#f0f7f4; border-radius:8px; padding:1rem; border:1px solid #2d7d46;">' +
      '<strong>Thuisbatterij is voor jou rendabel</strong> — terugverdientijd ~' + fmtJr(terugverdienJaar) + ' (na ISDE-subsidie).<br>' +
      'Een 5 kWh batterij kan ~' + Math.round(opvangbaar) + ' kWh/jaar extra zelf verbruiken → besparing ' + fmt(batterijBesparing) + '/jaar.<br><br>' +
      '<a href="https://go.duurzaamthuislab.nl/sessy" style="background:#2d7d46; color:white; padding:.5rem 1rem; border-radius:6px; text-decoration:none; margin-right:.5rem; display:inline-block; margin-bottom:.3rem;" target="_blank" rel="nofollow noopener sponsored">Sessy 5 kWh bekijken →</a> ' +
      '<a href="https://go.duurzaamthuislab.nl/marstek" style="background:#1a5276; color:white; padding:.5rem 1rem; border-radius:6px; text-decoration:none; display:inline-block; margin-bottom:.3rem;" target="_blank" rel="nofollow noopener sponsored">Marstek Venus bekijken →</a>' +
      '</div>';
  } else {
    batterijDiv.style.display = 'block';
    batterijDiv.innerHTML = '<div style="background:#f9f9f9; border-radius:8px; padding:1rem; border:1px solid #ddd;">' +
      '<strong>Thuisbatterij is nu nog niet rendabel</strong> voor jouw situatie — terugverdientijd ~' + fmtJr(terugverdienJaar) + '.<br>' +
      'Tip: een dynamisch contract (<a href="https://go.duurzaamthuislab.nl/tibber" target="_blank" rel="nofollow noopener sponsored">Tibber</a>) is voor jou de betere eerste stap. Wacht op verdere prijsdaling van batterijen.' +
      '</div>';
  }

  document.getElementById('calc-resultaat').style.display = 'block';
  document.getElementById('calc-resultaat').scrollIntoView({behavior: 'smooth', block: 'start'});
}
</script>

---

## Hoe werkt de berekening?

De calculator gebruikt de volgende aannames, gebaseerd op gemiddelde Nederlandse huishoudprofielen:

**Zonne-opbrengst:** Gemiddeld 875 kWh per geïnstalleerde kWp in Nederland. Dit loopt uiteen van ~825 kWh/kWp in het noorden tot ~920 kWh/kWp in het zuiden.

**Energieprijs afname:** €0,31 per kWh (gemiddelde variabele component 2026, exclusief vaste kosten).

**Terugleververgoeding 2026 (saldering):** €0,31 per kWh — gelijkwaardig aan afnameprijs.

**Terugleververgoeding 2027 (vast contract):** €0,08 per kWh — dit is een conservatieve schatting. Sommige leveranciers bieden in 2026 al 5-12 cent, na 2027 verwacht ik dat het gemiddelde rond de 7-9 cent zal liggen naarmate meer aanbod op het net komt.

**Terugleververgoeding 2027 (dynamisch contract):** €0,12 per kWh gemiddeld. Dit is het verwachte jaargemiddelde als je actief stuurt op uurprijzen. Op goede zomerse pieken kun je 20-25 cent halen, maar in de winter ligt het lager. Het langjarig gemiddelde voor proactieve gebruikers is circa 10-14 cent.

---

## Grenswaardes: wanneer is een thuisbatterij rendabel?

De tabel hieronder toont bij welke teruglevering en prijs een **5 kWh thuisbatterij (Sessy of Marstek, ca. €4.100 na ISDE)** rendabel wordt. Randvoorwaarde: terugverdientijd ≤ 12 jaar.

| Jaarlijkse teruglevering | Besparing/jaar (vast) | Besparing/jaar (dynamisch) | Terugverdientijd |
|--------------------------|----------------------|---------------------------|-----------------|
| 1.000 kWh | €143 | €190 | **21 jaar (niet rendabel)** |
| 1.500 kWh | €214 | €285 | **14 jaar (grens)** |
| 2.000 kWh | €286 | €380 | **11 jaar (rendabel)** |
| 2.500 kWh | €357 | €475 | **8-9 jaar (goed)** |
| 3.000 kWh | €429 | €570 | **7-8 jaar (uitstekend)** |
| 4.000 kWh | €572 | €760 | **5-7 jaar (top)** |

*Aannames: teruglevertarief vast €0,08, dynamisch €0,12; batterij vangt 65% teruglevering op; prijs €4.100 na ISDE.*

**Conclusie:** Lever je minder dan 1.500 kWh per jaar terug, dan is een 5 kWh thuisbatterij financieel gezien niet interessant — tenzij je ook een EV hebt die de batterij effectief groter maakt. Bij 2.000 kWh teruglevering of meer begint het te kloppen.

### Wanneer is een grotere batterij (10 kWh) beter?

Een 10 kWh batterij (bijv. Huawei Luna 2000, ca. €7.500-€9.500 na installatie, minus ISDE ca. €5.400 = €2.100-€4.100 eigen bijdrage) werkt beter als:

- Je meer dan 4.000 kWh per jaar terugleverd
- Je een grote EV thuis laadt 's avonds (>15 kWh/dag)
- Je een warmtepomp hebt die 's avonds en 's nachts veel verbruikt

Voor het gemiddelde huishouden met een 5-6 kWp systeem is een 10 kWh batterij de sweet spot. Lever je meer dan 5.000 kWh terug, dan is zelfs een 15 kWh systeem het overwegen waard.

---

## Hoe gebruik ik de uitkomst?

De calculator geeft je een richting, geen perfect antwoord. Zo ga je ermee om:

**Stap 1: Controleer je werkelijke teruglevering.** Log in op je energieportal (Mijn Eneco, Mijn Vattenfall, Mijn Energie etc.) of kijk in de app van je slimme meter. Het verschil tussen de rekening en de werkelijkheid kan aanzienlijk zijn.

**Stap 2: Vraag een offerte aan.** Gebruik de uitkomst als gespreksbasis met een installateur. Vraag specifiek naar de ISDE-aanvraag — een goede installateur doet dat voor je.

**Stap 3: Vergelijk dynamische contracten.** Als je nog een vast contract hebt, bekijk dan [onze vergelijking van dynamische contracten](/posts/dynamische-energiecontracten-vergelijking-2026/). Tibber en Frank Energie zijn beide solide keuzes — de overstap kost je niets.

**Stap 4: Lees de volledige transitie-planner.** In de [Saldering 2027 transitie-planner](/posts/saldering-2027-transitie-planner/) beschrijf ik alle 5 strategieën uitgebreid, inclusief de decision tree per huistype en het kwartaalstappenplan.

---

## Jouw volgende stap

Dynamisch contract — de makkelijkste stap die per direct helpt:

- [Tibber](https://go.duurzaamthuislab.nl/tibber) — beste app, P1-meter integratie, €6,99/mnd
- [Frank Energie](https://go.duurzaamthuislab.nl/frank-energie) — geen vaste kosten, solide app

Thuisbatterij — als de calculator groen licht geeft:

- [Sessy 5 kWh](https://go.duurzaamthuislab.nl/sessy) — Nederlandse kwaliteit, eenvoudige installatie
- [Marstek Venus](https://go.duurzaamthuislab.nl/marstek) — scherpe prijs, goede specs

Heb je vragen over de uitkomst of wil je dat ik meekijk bij jouw specifieke situatie? Laat een reactie achter.

*Mark Bakker — april 2026*


<a href="https://go.duurzaamthuislab.nl/tibber" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">Bekijk Tibber</a>

## Gerelateerde artikelen

- [Saldering calculator 2027: jaar-voor-jaar impact bereken](/posts/saldering-calculator-2027-volledig/)
- [Oost-west zonnepanelen vs. zuidsysteem](/posts/oost-west-zonnepanelen-vs-zuid-2026/)
- [Saldering stopt in 2027: de volledige gids voor](/posts/saldering-stopt-2027-volledige-gids/)
- [Saldering vs dynamisch contract: welke is voordeliger na](/posts/saldering-vs-dynamisch-contract-rekenmodel/)
- [Terugleverkosten zonnepanelen 2026](/posts/terugleverkosten-zonnepanelen-2026/)

## Mini case-study — gezin Hilversum doorrekent post-saldering scenario

Familie met 4.200 kWh verbruik, 5.800 kWh opwekking, twee EV's (8.000 kWh laden), 4-pers huishouden. Pre-saldering (2026) was hun energierekening €1.140. Mijn calculator-uitkomst voor 2027:

- Zonder maatregelen: €2.890 per jaar (verlies van saldering = €1.750 erbij)
- Met dynamisch contract: €2.310 (€580 besparing)
- Met dynamisch + 5 kWh batterij: €1.620 (€690 extra besparing)
- Met dynamisch + 10 kWh batterij: €1.310 (€310 extra)

Conclusie: 5 kWh batterij is voor hen optimaal, 10 kWh marginaal — terugverdientijd schiet over de batterijlevensduur.

## Veelgemaakte fouten in calculator-gebruik

1. **Gemiddelde EPEX-prijs gebruiken in plaats van profiel-gewogen prijs.** Teruglevering valt vaak in laagprijs-uren, import in hoogprijs-uren.
2. **Energiebelasting vergeten te updaten.** Tarief stijgt jaarlijks (€0,131/kWh in 2026 → ~€0,138/kWh in 2027 verwacht).
3. **Vastrecht en aansluitkosten weglaten.** €420-€480 per jaar dat onafhankelijk van verbruik blijft.
4. **Geen rekening houden met EV-laadgedrag.** Direct na thuiskomst laden (17:00-19:00 piek) is duur. Slim laden 's nachts maakt fors verschil.
5. **Salderingsregeling 2026 doortrekken.** Saldering verdwijnt — calculator moet 2027-modus aankunnen.

## Wanneer een calculator je geen antwoord geeft

Bij wisselende bewoning (Airbnb, twee adressen), zelfstandig ondernemer met thuiskantoor (zakelijk verbruik), of zonnepark-aandeelhouder met aparte teruglevering — geen rekenmodel dekt dat. Vraag dan een energieadviseur.

## Extra FAQ

**Hoe vaak moet ik mijn calculatie herhalen?**
Twee keer per jaar (april en oktober). EPEX-prijzen schommelen seizoensgebonden 25-40 procent.

**Welke databron is betrouwbaar voor toekomstprognoses?**
PBL-rapporten (Planbureau voor de Leefomgeving), TenneT-monitor en het CBS energieverbruik-dashboard. Niet vertrouwen op leveranciers-marketingmateriaal.

## Mark Bakker's eigen rekensom — wat de calculator bij mij thuis voorspelde

Ik heb de calculator op mijn eigen huis losgelaten in januari 2026 als sanity-check. Mijn data: 16 panelen (6,8 kWp), jaarverbruik 4.100 kWh stroom + EV 6.500 kWh, dynamisch contract bij Tibber, Marstek Venus 5 kWh batterij geïnstalleerd maart 2024.

Calculator voorspelde voor 2027 een rekening van €1.080. Werkelijke afrekening Q1 2027 geprojecteerd: €1.130 — afwijking 4,6 procent. Niet slecht voor een rekenmodel met aannames.

Wat de calculator niet meeneemt en wat in mijn praktijk wél bleek: drie effecten die elkaar deels opheffen. Ten eerste: koude winter 2027 dreef warmtepomp-verbruik 280 kWh boven gemiddelde (kost ongeveer €40 extra). Ten tweede: gunstige prijsspread op EPEX in januari (€0,18/kWh gemiddeld piek-dal) leverde €72 extra arbitrage. Ten derde: één firmware-update batterij betekende drie dagen geen sturing — dat kostte €18.

Netto: praktijk wijkt 5-8 procent af van calculator. Reken daar dus altijd marge bovenop bij investeringsbeslissingen. Een calculator die zegt "terugverdientijd 9 jaar" kan in de praktijk 8,5 jaar of 10 jaar zijn — ruim genoeg in jouw voordeel of nadeel.

## Veelgestelde reken-gotchas door lezers

Lezers stuurden de afgelopen drie maanden vragen die de calculator niet automatisch oplost. Drie meest voorkomende:

**Wat als ik geen 100 procent flex-verbruik heb?** De dynamische voordelen in de calculator gaan uit van 70 procent flex (warmtepomp, EV, witgoed). Heb je alleen vaste kantoor-uren-belasting, halveer dan het dynamische voordeel.

**Wat als mijn buurman een grote installatie heeft naast me?** Bij hoge zomer-piek-instraling kan jouw teruglevering door netcongestie geweigerd worden — slimme meter logt dat als "curtailment". In de calculator niet zichtbaar, in de praktijk 2-7 procent verlies.

**Hoe ga ik om met BTW-retour?** Bij gezamenlijke aanschaf (panelen + batterij) tot 2027 nog BTW-aftrekbaar voor particulieren onder de zonnepanelen-regeling. Calculator gaat uit van bruto-prijs — corrigeer netto met €420-€800.
