---
title: 'Energiekosten calculator 2027: bereken jouw saldering-impact'
date: 2026-04-29 10:00:00+02:00
lastmod: 2026-08-21 08:00:00+02:00
description: Hoeveel kost de saldering-stop jou? Vul je kWh-verbruik en zonnepanelen-capaciteit in en zie het verschil tussen 2026 en 2027 — met alle aannames zichtbaar.
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
affiliate: false
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1580893246395-52aead8960dc&w=1200&output=webp&q=70
faq:
- q: Wat rekent deze calculator precies uit?
  a: 'Het verschil tussen twee situaties bij hetzelfde verbruik en dezelfde opwek: 2026, waarin je teruglevering nog volledig wordt weggestreept tegen je afname, en 2027, waarin dat niet meer gebeurt. Het verlies is in de kern één som: je teruglevering maal het verschil tussen je inkooptarief en je terugleververgoeding.'
- q: Met welke tarieven rekent de calculator?
  a: 'Met een all-in stroomtarief van €0,26/kWh, opgebouwd uit €0,105 EPEX-jaargemiddelde 2025 (incl. btw) + €0,11085 energiebelasting (incl. btw) + €0,044 inkoopopslag en vaste-kostenomslag (aanname, incl. btw). Voor de terugleververgoeding in 2027 rekenen wij met een gelabelde aanname van €0,07/kWh: de tarieven voor 2027 zijn op het moment van schrijven niet gepubliceerd. Beide getallen kun je hieronder terugvinden en zelf narekenen.'
- q: Waarom stopt de saldering precies?
  a: 'De salderingsregeling stopt volledig per 1 januari 2027. Er is geen afbouwpad: het wetsvoorstel met een stapsgewijze afbouw is verworpen. Tot en met 31 december 2026 saldeer je dus voor 100%, daarna niet meer.'
- q: Wat als ik niet 100% flexibel verbruik heb?
  a: 'De calculator gaat er bij de keuze voor een dynamisch contract van uit dat je je eigen verbruik met 5 procentpunt kunt verhogen door apparaten naar zonuren te verschuiven. Kun je dat niet — vaste werktijden, niemand thuis, geen warmtepomp of EV — zet die optie dan op ''vast contract''. Dan verandert er in de uitkomst niets, en dat is dan ook de eerlijke uitkomst.'
- q: Wat als mijn teruglevering geweigerd wordt door netcongestie?
  a: 'Bij hoge zomerse instraling kan een omvormer terugregelen als de netspanning te hoog wordt; dat heet curtailment. Hoeveel dat kost, verschilt sterk per wijk en per omvormerinstelling en is niet met één percentage te dekken — wij nemen er daarom geen getal voor op. Wil je weten of het bij jou speelt, vergelijk dan de opbrengst uit je omvormer-app met de PVGIS-verwachting voor je dakvlak.'
- q: Hoe zit het met btw op de batterij?
  a: 'Op een thuisbatterij betaal je 21% btw. Het 0%-tarief voor zonnepanelen dekt volgens de Belastingdienst uitdrukkelijk niet de levering en installatie van een accupakket of thuisbatterij — ook niet als je de batterij samen met panelen koopt. De calculator rekent daarom met de prijs inclusief btw en zonder btw-correctie. Er is ook geen ISDE-subsidie voor thuisbatterijen.'
schema_type: Article
---
De saldering stopt volledig per 1 januari 2027. Er is geen afbouwpad — het wetsvoorstel met een stapsgewijze afbouw is verworpen. Wat het je kost, hangt af van hoeveel je teruglevert en hoeveel je daarvoor terugkrijgt. Vul hieronder je gegevens in.

*Disclosure: wij hebben geen affiliate- of commissierelatie met Tibber, Frank Energie, Sessy of Marstek (stand augustus 2026). De links in dit artikel zijn gewone verwijzingen en leveren ons geen vergoeding op.*

---

> **Kort antwoord:** het verlies door de saldering-stop is in de kern één som: je jaarlijkse teruglevering maal het verschil tussen je inkooptarief en je terugleververgoeding. Met de modelconstantes van deze site — €0,26/kWh inkoop en een gelabelde aanname van €0,07/kWh teruglevering — is dat €0,19 per teruggeleverde kWh. Bij 2.000 kWh teruglevering praat je dus over circa €380 per jaar.

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
  <option value="yes">Ja — dynamisch (bijv. Tibber, Frank of ANWB)</option>
</select>
<small style="color:#666;">Bij dynamisch rekent het model met 5 procentpunt meer eigen verbruik, doordat je apparaten naar zonuren kunt verschuiven</small>
</div>

</div>

<button onclick="berekenSaldering()"
  style="background: #2d7d46; color: white; border: none; padding: .8rem 2rem; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; width: 100%;">
  Bereken mijn saldering-impact →
</button>

<div id="calc-resultaat" style="margin-top:1.5rem; display:none;">

<hr style="border:1px solid #ddd; margin-bottom:1.5rem;">

<h4 style="margin-top:0; color:#1a1a2e;">Jouw modelberekening</h4>

<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1rem; margin-bottom:1.5rem;">

<div style="background:white; border-radius:8px; padding:1rem; border:1px solid #e0e0e0; text-align:center;">
<div style="font-size:.85rem; color:#666; margin-bottom:.3rem;">Waarde zonnestroom 2026 (met saldering)</div>
<div id="res-2026" style="font-size:1.6rem; font-weight:700; color:#2d7d46;">—</div>
<div style="font-size:.8rem; color:#888;">per jaar</div>
</div>

<div style="background:white; border-radius:8px; padding:1rem; border:1px solid #e0e0e0; text-align:center;">
<div style="font-size:.85rem; color:#666; margin-bottom:.3rem;">Waarde zonnestroom 2027 (na de stop)</div>
<div id="res-2027" style="font-size:1.6rem; font-weight:700; color:#e67e22;">—</div>
<div style="font-size:.8rem; color:#888;">per jaar</div>
</div>

<div style="background:#fef3f2; border-radius:8px; padding:1rem; border:1px solid #f5c6cb; text-align:center;">
<div style="font-size:.85rem; color:#666; margin-bottom:.3rem;">Verschil per jaar</div>
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

<p style="font-size:.85rem; color:#666; margin-top:1rem; margin-bottom:0;">Dit is een modelberekening met de aannames die onder deze calculator staan. Het is geen aanbod, geen advies en geen voorspelling; aan de uitkomst kunnen geen rechten worden ontleend. Controleer je eigen tarieven en teruglevering voordat je een beslissing neemt.</p>

</div>

</div>

<script>
function berekenSaldering() {
  var verbruik = parseFloat(document.getElementById('calc-verbruik').value) || 3500;
  var capaciteit = parseFloat(document.getElementById('calc-capaciteit').value) || 4.5;
  var eigenVerbruikPct = parseFloat(document.getElementById('calc-eigen-verbruik').value) || 35;
  var dynamisch = document.getElementById('calc-dynamisch').value === 'yes';

  // Modelconstanten (zie de aannames-sectie onder de calculator)
  var productiePerKwp = 875;        // kWh per kWp per jaar, NL-gemiddelde
  var prijsAfname = 0.26;           // €/kWh all-in: 0,105 EPEX (incl. btw) + 0,11085 belasting (incl. btw) + 0,044 opslag-aanname
  var terugleverAanname2027 = 0.07; // €/kWh, gelabelde aanname; 2027-tarieven niet gepubliceerd
  var spreadDynamisch = 0.30;       // €/kWh verschil dal-piek incl. btw, modelaanname

  // Een dynamisch contract verhoogt niet je terugleververgoeding, maar wel je
  // eigen verbruik: je kunt apparaten naar de zonuren verschuiven.
  var effEigenPct = dynamisch ? Math.min(eigenVerbruikPct + 5, 90) : eigenVerbruikPct;

  var jaarproductie = capaciteit * productiePerKwp;
  var eigenVerbruikKwh = jaarproductie * (effEigenPct / 100);
  var teruggeleverd = Math.max(jaarproductie - eigenVerbruikKwh, 0);

  // 2026: teruglevering wordt weggestreept tegen afname, dus elke kWh is het
  // volle inkooptarief waard.
  var waarde2026 = jaarproductie * prijsAfname;

  // 2027: eigen verbruik blijft het inkooptarief waard, teruglevering levert
  // alleen de terugleververgoeding op.
  var waarde2027 = (eigenVerbruikKwh * prijsAfname) + (teruggeleverd * terugleverAanname2027);

  var verschil = waarde2026 - waarde2027;

  // Thuisbatterij: 5 kWh, prijs Sessy 5 kWh EUR 3.550 (sessy.nl, incl. btw,
  // excl. installatie) + EUR 800 installatie-aanname = EUR 4.350.
  var batterijKwh = 5;
  var nuttigeDagen = 300;
  var batterijPrijs = 4350;
  var maxDoorzet = batterijKwh * nuttigeDagen;                       // 1.500 kWh/jaar
  var opvangbaar = Math.min(teruggeleverd * 0.65, maxDoorzet);
  var besparingZon = opvangbaar * (prijsAfname - terugleverAanname2027);
  var besparingArbitrage = dynamisch ? (maxDoorzet * spreadDynamisch * 0.9) : 0;
  // Dezelfde cyclus kan niet twee keer gebruikt worden: neem de hoogste van de twee.
  var batterijBesparing = Math.max(besparingZon, besparingArbitrage);
  var terugverdienJaar = batterijBesparing > 0 ? (batterijPrijs / batterijBesparing) : 999;
  var batterijRendabel = terugverdienJaar <= 12;

  function fmt(n) { return '€' + Math.round(n).toLocaleString('nl-NL'); }
  function fmtJr(n) { return n >= 40 ? '>40 jaar' : n.toFixed(1) + ' jaar'; }

  document.getElementById('res-2026').textContent = fmt(waarde2026);
  document.getElementById('res-2027').textContent = fmt(waarde2027);
  document.getElementById('res-verschil').textContent = fmt(verschil);

  var details = '<strong>Jouw zonnepanelen:</strong> ' + capaciteit + ' kWp x 875 kWh/kWp = ~' + Math.round(jaarproductie) + ' kWh/jaar productie<br>' +
    '<strong>Direct eigen verbruik:</strong> ~' + Math.round(eigenVerbruikKwh) + ' kWh (' + effEigenPct + '%) - waard ' + fmt(eigenVerbruikKwh * prijsAfname) + '/jaar tegen €0,26/kWh<br>' +
    '<strong>Teruglevering:</strong> ~' + Math.round(teruggeleverd) + ' kWh - in 2026 gesaldeerd en dus ' + fmt(teruggeleverd * prijsAfname) + ' waard, in 2027 tegen de aanname van €0,07/kWh nog ' + fmt(teruggeleverd * terugleverAanname2027) + '<br>' +
    '<strong>Het verlies is dus:</strong> ' + Math.round(teruggeleverd) + ' kWh x (€0,26 - €0,07) = ' + fmt(verschil) + '/jaar' +
    (dynamisch ? '<br><strong>Dynamisch contract:</strong> gerekend met 5 procentpunt meer eigen verbruik dan je hebt opgegeven' : '');

  document.getElementById('res-details').innerHTML = details;

  var adviesText = '';
  var adviesKleur = '';

  if (verschil < 200) {
    adviesKleur = '#a8d5b9';
    adviesText = '<strong>Beperkt verschil</strong> - onder €200 per jaar in dit model. De goedkoopste maatregel is je eigen verbruik verhogen: apparaten naar de zonuren, en eventueel een warmwaterboiler of EV die overdag laadt. Een thuisbatterij verdient zich bij dit volume vrijwel zeker niet terug.';
  } else if (verschil < 500) {
    adviesKleur = '#fce8a6';
    adviesText = '<strong>Merkbaar verschil</strong> - €200 tot €500 per jaar. Begin met verbruik verschuiven en een contractvorm die daarbij past. Reken een thuisbatterij pas door als je weet hoeveel van je overschot je er werkelijk in kwijt kunt.';
  } else if (verschil < 900) {
    adviesKleur = '#f5c6a0';
    adviesText = '<strong>Substantieel verschil</strong> - €500 tot €900 per jaar. Je hebt veel teruglevering. Kijk eerst naar grote verbruikers die je naar de middag kunt verplaatsen (warmwaterboiler, EV, warmtepomp), want die kosten niets en werken direct. Daarna is een batterij een rekensom, geen automatisme.';
  } else {
    adviesKleur = '#f5b0a0';
    adviesText = '<strong>Groot verschil</strong> - meer dan €900 per jaar. Bij dit volume is de eerste vraag niet ''welke batterij'' maar ''hoeveel van mijn overschot kan ik zelf gebruiken''. Een batterij van 5 kWh dekt maximaal circa 1.500 kWh per jaar; heb je veel meer overschot dan dat, dan blijft er ook met batterij een groot deel onbenut.';
  }

  document.getElementById('res-advies').style.borderColor = adviesKleur;
  document.getElementById('res-advies').style.background = adviesKleur + '33';
  document.getElementById('res-advies').innerHTML = adviesText;

  var batterijDiv = document.getElementById('res-batterij');
  batterijDiv.style.display = 'block';
  var basis = 'Model: 5 kWh batterij, €4.350 (Sessy 5 kWh €3.550 incl. btw excl. installatie, plus €800 installatie-aanname), 21% btw, geen ISDE-subsidie op thuisbatterijen. Doorzet maximaal ' + maxDoorzet + ' kWh per jaar.';
  if (batterijRendabel) {
    batterijDiv.innerHTML = '<div style="background:#f0f7f4; border-radius:8px; padding:1rem; border:1px solid #2d7d46;">' +
      '<strong>Terugverdientijd in dit model: ~' + fmtJr(terugverdienJaar) + '</strong><br>' +
      'Jaarlijkse besparing in het model: ' + fmt(batterijBesparing) + '.<br>' + basis +
      '</div>';
  } else {
    batterijDiv.innerHTML = '<div style="background:#f9f9f9; border-radius:8px; padding:1rem; border:1px solid #ddd;">' +
      '<strong>Terugverdientijd in dit model: ~' + fmtJr(terugverdienJaar) + '</strong> - dat is lang, en bij een verwachte levensduur van 10 tot 15 jaar betekent het dat de batterij zich op deze aannames niet terugverdient.<br>' +
      'Jaarlijkse besparing in het model: ' + fmt(batterijBesparing) + '.<br>' + basis + '<br>' +
      'Wat de uitkomst wel kan kantelen: een lagere aanschafprijs, een hogere prijsspread op een dynamisch contract, of veel avondverbruik dat je met de batterij afdekt.' +
      '</div>';
  }

  document.getElementById('calc-resultaat').style.display = 'block';
  document.getElementById('calc-resultaat').scrollIntoView({behavior: 'smooth', block: 'start'});
}
</script>

---

## Hoe werkt de berekening?

De calculator gebruikt vier modelconstanten. Ze staan hier expliciet, zodat je kunt zien wat je uitkomst bepaalt en zelf kunt narekenen wat er verandert als je andere getallen aanhoudt.

| Constante | Waarde | Onderbouwing |
|---|---|---|
| Zonne-opbrengst | 875 kWh per kWp per jaar | NL-gemiddelde; loopt uiteen van circa 825 kWh/kWp in het noorden tot circa 920 kWh/kWp in het zuiden. Reken je eigen dakvlak na met PVGIS |
| Stroom all-in | €0,26/kWh | €0,105 EPEX-jaargemiddelde 2025 (incl. btw) + €0,11085 energiebelasting (incl. btw) + €0,044 inkoopopslag en vaste-kostenomslag (aanname, incl. btw) |
| Terugleververgoeding 2027 | €0,07/kWh | **Gelabelde aanname.** De tarieven voor 2027 zijn op het moment van schrijven niet gepubliceerd. Wij nemen geen verwachting van leveranciers over als feit |
| Prijsspread dal-piek | €0,30/kWh incl. btw | Modelaanname voor batterij-arbitrage op een dynamisch contract; op grijze winterdagen is de spread veel kleiner |

**De kernsom is eenvoudig.** Zolang de saldering geldt, is elke teruggeleverde kWh het volle inkooptarief waard, want hij wordt weggestreept tegen een kWh die je anders had moeten kopen. Vanaf 2027 is diezelfde kWh alleen nog de terugleververgoeding waard. Je verlies is dus:

**teruglevering (kWh) × (inkooptarief − terugleververgoeding)** = teruglevering × €0,19

Bij 1.000 kWh teruglevering is dat €190 per jaar; bij 3.000 kWh €570.

**Wat een dynamisch contract wel en niet doet.** Een dynamisch contract verhoogt je terugleververgoeding niet — die volgt de uurprijs, en die is op zonnige middagen juist laag omdat alle panelen tegelijk produceren. Wat het wél doet, is je in staat stellen verbruik naar de zonuren te schuiven, waardoor je meer zelf gebruikt en minder teruglevert. Daarom rekent de calculator bij een dynamisch contract met 5 procentpunt meer eigen verbruik en niet met een hogere terugleverprijs.

---

## Wanneer is een thuisbatterij rendabel?

Hier zit de belangrijkste nuance van dit artikel, en die valt anders uit dan veel andere overzichten suggereren.

Een **5 kWh batterij** kan per dag maximaal 5 kWh opslaan. Over 300 bruikbare dagen per jaar — meer haal je in Nederland niet, want in de winter is er weinig overschot — is de maximale doorzet 1.500 kWh per jaar. Elke opgeslagen kWh is €0,19 waard: het verschil tussen zelf gebruiken (€0,26) en terugleveren (€0,07, aanname).

Rekenen we met een prijs van **€4.350** — Sessy 5 kWh voor €3.550 inclusief btw exclusief installatie (sessy.nl, peildatum 21 augustus 2026) plus €800 installatie-aanname, en zonder subsidie, want voor thuisbatterijen bestaat geen ISDE — dan ziet het er zo uit:

| Jaarlijkse teruglevering | Opvangbaar (65%, max 1.500) | Besparing/jaar | Terugverdientijd |
|---|---|---|---|
| 1.000 kWh | 650 kWh | €124 | circa 35 jaar |
| 1.500 kWh | 975 kWh | €185 | circa 24 jaar |
| 2.000 kWh | 1.300 kWh | €247 | circa 18 jaar |
| 2.500 kWh | 1.500 kWh (maximum) | €285 | circa 15 jaar |
| 3.000 kWh | 1.500 kWh (maximum) | €285 | circa 15 jaar |
| 4.000 kWh | 1.500 kWh (maximum) | €285 | circa 15 jaar |

*Modelberekening. Aannames: inkoop €0,26/kWh, terugleververgoeding €0,07/kWh (gelabelde aanname), batterij vangt 65% van de teruglevering op tot een maximum van 1.500 kWh per jaar, prijs €4.350 inclusief 21% btw, geen subsidie.*

**Wat hieruit volgt:** boven circa 2.300 kWh teruglevering raakt een 5 kWh batterij verzadigd. Meer teruglevering levert dan geen extra besparing meer op, en de terugverdientijd blijft op circa vijftien jaar staan. Bij een verwachte levensduur van tien tot vijftien jaar betekent dat: **een 5 kWh batterij die je uitsluitend koopt om de saldering-stop te compenseren, verdient zich op deze aannames niet terug.**

Drie dingen kunnen die uitkomst kantelen, en het is verstandig om ze alle drie na te rekenen voordat je koopt:

1. **Arbitrage op een dynamisch contract.** Laden op een goedkoop nachtuur en ontladen op de avondpiek levert bij een spread van €0,30/kWh, 5 kWh per dag, 300 dagen en 90% retourrendement circa €405 per jaar op — meer dan het opslaan van zonneoverschot. Terugverdientijd wordt dan circa 11 jaar. Let op: dezelfde cyclus kun je niet twee keer gebruiken, dus arbitrage en zonneopslag tel je niet bij elkaar op. En de spread is niet elke dag €0,30.
2. **Een lagere aanschafprijs.** De terugverdientijd is recht proportioneel met de prijs. Bij €3.000 in plaats van €4.350 zakt hij met bijna een derde.
3. **Veel avondverbruik.** Een warmtepomp of een EV die 's avonds laadt, vergroot het deel van de batterij dat je daadwerkelijk elke dag rondzet.

### En een grotere batterij?

Een grotere batterij verhoogt de maximale doorzet, maar ook de prijs. Op sessy.nl staat de 10 kWh-variant op €5.500 en de Plus met 15 kWh op €9.400, in alle gevallen inclusief btw en exclusief installatie (peildatum 21 augustus 2026). Voor andere merken geldt: neem alleen prijzen mee die de fabrikant of leverancier zelf publiceert, met de datum waarop je ze hebt gezien.

Een grotere batterij loont pas als je hem ook vol krijgt én leeg maakt. Dat vraagt in de praktijk om een combinatie van veel teruglevering (meer dan 4.000 kWh per jaar) en veel avond- of nachtverbruik. Reken het door met dezelfde som: doorzet per jaar × €0,19, en vergelijk dat met de prijs.

---

## Rekenvoorbeeld: huishouden met twee elektrische auto's

Een uitgewerkt voorbeeld met alle stappen zichtbaar. **Aannames:** 4.200 kWh huishoudelijk verbruik, 8.000 kWh laden voor twee EV's, samen 12.200 kWh afname. Opwek 5.800 kWh, waarvan 35% direct zelf gebruikt (2.030 kWh) en 3.770 kWh teruggeleverd.

**2026, met saldering.** Bruto afname van het net: 12.200 − 2.030 = 10.170 kWh. Daarvan wordt 3.770 kWh weggestreept tegen de teruglevering, dus je betaalt over 6.400 kWh. Bij €0,26/kWh: **€1.664**.

**2027, zonder saldering.** Je betaalt over de volle 10.170 kWh afname: €2.644. Daarvan gaat de terugleveropbrengst af: 3.770 × €0,07 = €264. Netto: **€2.380**.

**Het verschil is €716 per jaar** — precies 3.770 kWh × €0,19, zoals de kernsom voorspelt.

Wat daaraan te doen valt, in volgorde van effect:

- **Slim laden van de EV's.** 8.000 kWh verschuiven van het jaargemiddelde (€0,26) naar nachtelijke uren (€0,196 all-in bij een EPEX-prijs van €0,05) scheelt 8.000 × €0,064 = **circa €510 per jaar**. Dit is de grootste post, en hij kost niets behalve een laadschema.
- **Een 5 kWh batterij erbij.** Levert maximaal 1.500 × €0,19 = **€285 per jaar** op, tegen €4.350 aanschaf. Terugverdientijd circa 15 jaar.

Conclusie voor dit huishouden: het laadgedrag is de hefboom, de batterij is marginaal. Dat is bij veel EV-huishoudens de uitkomst, omdat een auto veel meer kWh kan verschuiven dan een batterij kan opslaan.

---

## Hoe gebruik je de uitkomst?

**Stap 1: controleer je werkelijke teruglevering.** Kijk op je jaarafrekening of in de app van je slimme meter, niet in de brochure van je installateur. Het verschil tussen verwachting en werkelijkheid is vaak aanzienlijk.

**Stap 2: kijk eerst naar verbruik verschuiven.** Dat kost niets en werkt direct. Warmwaterboiler, vaatwasser, wasmachine, EV en warmtepomp naar de zonuren: elke kWh die je daarmee zelf gebruikt in plaats van teruglevert, is €0,19 waard.

**Stap 3: vraag pas daarna een offerte voor een batterij.** Vraag om een prijs inclusief 21% btw en inclusief installatie, en check of je gemeente of provincie een eigen regeling heeft — een landelijke subsidie voor thuisbatterijen is er niet. Gebruik de tabel hierboven als toets: welke doorzet per jaar belooft de installateur, en klopt dat met jouw teruglevering?

**Stap 4: vergelijk contractvormen.** Zie [beste dynamisch energiecontract 2026](/posts/beste-dynamisch-energiecontract-2026/) en de [vergelijking van dynamische contracten](/posts/dynamische-energiecontracten-vergelijking-2026/).

## Veelgemaakte fouten bij het gebruik van zo'n calculator

1. **Het jaargemiddelde gebruiken voor teruglevering.** Teruglevering valt in laagprijsuren, afname in hoogprijsuren. Wie voor beide hetzelfde tarief invult, overschat de opbrengst van teruglevering structureel.
2. **De energiebelasting verkeerd invullen.** In 2026 is die €0,09161/kWh exclusief btw, oftewel €0,11085/kWh inclusief btw. De ODE bestaat sinds 2023 niet meer als aparte heffing. Voor 2027 zijn de tarieven nog niet vastgesteld; vul geen verwachting in als feit.
3. **Netbeheer- en vaste kosten in de vergelijking meenemen.** Die zijn er ook zonder zonnepanelen en veranderen niet door de saldering-stop, dus ze horen niet in het verschil tussen 2026 en 2027 thuis.
4. **Geen rekening houden met laadgedrag.** Direct na thuiskomst laden, in de avondpiek, is de duurste manier om een EV te laden.
5. **Uitgaan van een afbouwpad.** De saldering stopt volledig per 1 januari 2027. Rekenmodellen die met 73%, 64% of 28% saldering per jaar werken, gebruiken een verworpen wetsvoorstel.

## Wanneer een calculator je geen antwoord geeft

Bij wisselende bewoning (verhuur, twee adressen), een zakelijk deel in je verbruik, of deelname aan een collectief zonproject met aparte verrekening dekt geen enkel algemeen rekenmodel je situatie. Vraag dan een onafhankelijk energieadviseur.

## Wat deze calculator níét meeneemt

Elk model is een vereenvoudiging. Drie factoren verklaren het grootste deel van het verschil tussen de uitkomst en je jaarafrekening.

**Weer.** Een koud jaar verhoogt je verbruik en verlaagt je opbrengst; een zonnig jaar doet het omgekeerde. Beide kunnen tientallen tot ruim honderd euro schelen.

**Prijsspread.** De arbitragewinst van een batterij staat of valt met het verschil tussen dal- en piekuren. In maanden met een brede spread valt het voordeel hoger uit dan het model aanneemt, in vlakke maanden lager. Historische EPEX-uurdata zijn publiek op te vragen bij de beurs en bij ENTSO-E, en de actuele prijzen staan op onze [stroomprijzen-pagina](/stroomprijzen/).

**Stilstand.** Een firmware-update, netonderhoud of een storing betekent een of meer dagen zonder sturing. Dat kost direct het volledige dagvoordeel.

Lees een uitkomst daarom als een bandbreedte, niet als een getal. "Terugverdientijd 15 jaar" betekent in de praktijk grofweg 13 tot 18 jaar.

## Jouw volgende stap

Verbruik verschuiven kost niets en werkt direct — begin daar. Wil je daarna een contractvorm die daarbij past:

- **Tibber** — €5,99/maand per energiesoort plus €0,0248/kWh inkoopvergoeding; sterkste app en native slim laden voor EV's
- **Frank Energie** — geen marge op de marktprijs; vaste kosten publiceert Frank niet, dus opvragen, en let op de terugleverstaffel sinds 1 juni 2025
- **ANWB Energie** — €0,018/kWh inkoopkosten, vast maandtermijnbedrag met jaarverrekening

<a href="https://go.duurzaamthuislab.nl/tibber" class="cta cta-affiliate" target="_blank" rel="nofollow noopener">Bekijk Tibber</a> · <a href="https://go.duurzaamthuislab.nl/frank-energie" class="cta cta-affiliate" target="_blank" rel="nofollow noopener">Bekijk Frank Energie</a> · <a href="https://go.duurzaamthuislab.nl/anwb-energie" class="cta cta-affiliate" target="_blank" rel="nofollow noopener">Bekijk ANWB Energie</a>

Overweeg je een thuisbatterij, gebruik dan eerst de tabel hierboven en daarna de [thuisbatterij terugverdientijd-vergelijking](/thuisbatterij-terugverdientijd-vergelijken/).

*Wij ontvangen geen vergoeding als je via een van deze links een contract afsluit of een product koopt.*

*Vragen over de uitkomst of mis je een variabele in het model? Mail de redactie via [info@duurzaamthuislab.nl](mailto:info@duurzaamthuislab.nl).*

## Gerelateerde artikelen

- [Saldering calculator 2027: jaar-voor-jaar impact](/posts/saldering-calculator-2027-volledig/)
- [Oost-west zonnepanelen vs. zuidsysteem](/posts/oost-west-zonnepanelen-vs-zuid-2026/)
- [Saldering stopt in 2027: de volledige gids](/posts/saldering-stopt-2027-volledige-gids/)
- [Saldering vs dynamisch contract: rekenmodel](/posts/saldering-vs-dynamisch-contract-rekenmodel/)
- [Terugleverkosten zonnepanelen 2026](/posts/terugleverkosten-zonnepanelen-2026/)
