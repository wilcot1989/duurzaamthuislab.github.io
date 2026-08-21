---
title: "Warmtepomp kosten en besparing berekenen (rekentool)"
description: "Bereken met je eigen gasverbruik, SCOP en offertebedrag wat een hybride of all-electric warmtepomp per jaar kost of oplevert — met live gas- en stroomprijzen en alle aannames zelf aanpasbaar."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
faq:
- q: 'Waarom vullen jullie geen aanschafprijs in?'
  a: 'Omdat elk bedrag dat wij zouden noemen een verzinsel is. Prijzen hangen af van merk, vermogen, het benodigde leidingwerk, radiatoren, elektrawerk en de installateur. Een offertebedrag is het enige getal dat klopt voor jouw situatie — daarom is dat veld leeg.'
- q: 'Waar staat mijn SCOP?'
  a: 'Op het energielabel van het toestel en in het technische datasheet, altijd bij een opgegeven temperatuurregime (bijvoorbeeld 35 °C of 55 °C afgiftetemperatuur). Rekent je installateur met een ander cijfer, vraag dan bij welk regime dat hoort. Vul in de tool het cijfer in dat bij jóúw afgiftetemperatuur past, niet de mooiste waarde uit de brochure.'
- q: 'Waarom 9,77 kWh per m³ gas?'
  a: 'Dat is de gangbare Nederlandse rekenwaarde om een kubieke meter aardgas naar kWh om te rekenen: de bovenwaarde van Gronings aardgas is circa 35,17 MJ/m³, en 35,17 MJ is 9,77 kWh. Het blijft een vuistregel — de exacte energie-inhoud van het gas in je meter varieert licht per regio en per moment, en wie met de onderwaarde rekent (circa 31,65 MJ/m³, ongeveer 8,8 kWh) komt lager uit. Heb je een preciezer getal van je netbeheerder, dan verandert alleen stap 3 en 4 van de berekening.'
- q: 'Moet ik het rendement van mijn oude ketel niet meerekenen?'
  a: 'De tool rekent met je feitelijke gasverbruik, en daarin zit het ketelrendement al verwerkt: die m³ heb je nodig gehad om je huis warm te krijgen. De vermeden m³ vertegenwoordigen dus geleverde warmte inclusief ketelverlies — dat is de eerlijke vergelijking, omdat de warmtepomp precies diezelfde warmtebehoefte moet dekken.'
- q: 'De uitkomst is negatief. Doe ik iets verkeerd?'
  a: 'Niet noodzakelijk. Bij een lage SCOP, een hoge stroomprijs en een relatief lage gasprijs kan de rekening op jaarbasis inderdaad slechter uitpakken. Dat is precies de informatie waarvoor de tool bedoeld is. Kijk dan eerst naar isolatie en afgiftetemperatuur — die verhogen de SCOP — voordat je een toestel bestelt.'
lastmod: 2026-08-21
---

*Wij hebben geen affiliate- of samenwerkingsrelatie met warmtepompfabrikanten of -installateurs. Deze pagina bevat dus geen affiliate-links naar warmtepompen; de rekentool rekent uitsluitend met de waarden die jij invult.*

## Kort antwoord

Een warmtepomp ruilt gas in voor stroom. Of dat geld oplevert, hangt af van drie dingen: **hoeveel gas je vermijdt**, **hoeveel stroom je daarvoor terugkrijgt in de plaats** (dat is de SCOP) en **de verhouding tussen de gas- en de stroomprijs**. Vuistregel voor de omrekening: elke vermeden kubieke meter gas staat voor ongeveer **9,77 kWh warmte**; die haal je met een SCOP van 4,0 uit ruim 2,4 kWh stroom.

De terugverdientijd kun je pas berekenen met een **echt offertebedrag**. Wij vullen daarom géén aanschafprijs voor je in — dat veld laat je zelf vullen met het bedrag uit je eigen offerte, en de ISDE-subsidie zoek je op per apparaat. Alles hieronder is een **modelberekening, geen garantie**.

<div id="wp-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.1rem;">
    <div>
      <label for="wp-gas" style="display:block;font-weight:600;margin-bottom:.3rem;">Huidig gasverbruik (m³/jaar)</label>
      <input id="wp-gas" type="number" min="0" max="10000" step="10" value="1200" oninput="wpReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Modelaanname: 1.200 m³. Vul het jaarverbruik van je eigen jaarafrekening in. Kook je op gas of heb je een gasgeiser, trek dat deel er dan af — een warmtepomp vervangt alleen je verwarming (en bij all-electric ook warm tapwater).</span>
    </div>
    <div>
      <label for="wp-type" style="display:block;font-weight:600;margin-bottom:.3rem;">Type warmtepomp</label>
      <select id="wp-type" onchange="wpTypeWissel()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;background:#fff;">
        <option value="hybride" selected>Hybride (warmtepomp + bestaande ketel)</option>
        <option value="all">All-electric (ketel eruit)</option>
      </select>
      <span style="font-size:.8rem;color:#666;">Bij hybride neemt de warmtepomp een deel van de warmtevraag over en springt de ketel bij op koude dagen. Bij all-electric verdwijnt de gasrekening volledig.</span>
    </div>
    <div>
      <label for="wp-dekking" style="display:block;font-weight:600;margin-bottom:.3rem;">Dekking warmtevraag (%)</label>
      <input id="wp-dekking" type="number" min="1" max="100" step="1" value="60" oninput="wpReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Modelaanname: 60% bij hybride, 100% bij all-electric. Het aandeel van je warmtevraag dat de warmtepomp levert. Hoe lager je afgiftetemperatuur en hoe beter je isolatie, hoe hoger dit percentage kan liggen. Vraag je installateur wat híj aanhoudt.</span>
    </div>
    <div>
      <label for="wp-scop" style="display:block;font-weight:600;margin-bottom:.3rem;">SCOP (seizoensrendement)</label>
      <input id="wp-scop" type="number" min="1" max="8" step="0.1" value="4" oninput="wpReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span id="wp-scop-hint" style="font-size:.8rem;color:#666;">Modelaanname: 4,0 voor het warmtepompdeel van een hybride opstelling. Uit 1 kWh stroom komt dan 4 kWh warmte. Het cijfer voor jóúw toestel staat op het productlabel en in het datasheet, bij een opgegeven temperatuurregime.</span>
    </div>
    <div>
      <label for="wp-inv" style="display:block;font-weight:600;margin-bottom:.3rem;">Investeringsbedrag (€)</label>
      <input id="wp-inv" type="number" min="0" max="100000" step="100" placeholder="vul je offertebedrag in" oninput="wpReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Leeg gelaten met opzet: wij vullen hier geen bedrag in. Neem het totaalbedrag inclusief installatie, eventuele radiatoren en elektrawerk uit je offerte over. Zonder dit veld rekent de tool alleen je jaarbesparing uit.</span>
    </div>
    <div>
      <label for="wp-isde" style="display:block;font-weight:600;margin-bottom:.3rem;">ISDE-subsidie (€)</label>
      <input id="wp-isde" type="number" min="0" max="50000" step="50" value="0" oninput="wpReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Het subsidiebedrag verschilt per apparaat en per jaar. Zoek het bedrag voor jouw type en merk op in de apparatenlijst van <a href="https://www.rvo.nl/subsidies-financiering/isde" target="_blank" rel="noopener nofollow">RVO (ISDE)</a> en vul het hier in. Wij noemen geen bedragen omdat ze wijzigen.</span>
    </div>
    <div>
      <label for="wp-gasprijs" style="display:block;font-weight:600;margin-bottom:.3rem;">Gasprijs all-in (€/m³)</label>
      <input id="wp-gasprijs" type="number" min="0" max="5" step="0.01" value="1.10" oninput="wpReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span id="wp-gas-hint" style="font-size:.8rem;color:#666;">Startwaarde € 1,10/m³ (rekenconstante van deze site). Wordt geladen: kale dagprijs van de gasbeurs + € 0,7268 energiebelasting incl. btw (2026) + de opslag hieronder.</span>
    </div>
    <div>
      <label for="wp-gasopslag" style="display:block;font-weight:600;margin-bottom:.3rem;">Leveranciersopslag gas (€/m³)</label>
      <input id="wp-gasopslag" type="number" min="0" max="1" step="0.005" value="0.05" oninput="wpHerbereken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Modelaanname: € 0,05/m³. De inkoopvergoeding van je leverancier; het exacte bedrag staat in je contract of leveringsovereenkomst.</span>
    </div>
    <div>
      <label for="wp-stroomprijs" style="display:block;font-weight:600;margin-bottom:.3rem;">Stroomprijs all-in (€/kWh)</label>
      <input id="wp-stroomprijs" type="number" min="0" max="2" step="0.005" value="0.26" oninput="wpReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span id="wp-stroom-hint" style="font-size:.8rem;color:#666;">Startwaarde € 0,26/kWh (rekenconstante van deze site). Wordt geladen: daggemiddelde van de uurprijzen + € 0,11085 energiebelasting incl. btw (2026) + de opslag hieronder.</span>
    </div>
    <div>
      <label for="wp-stroomopslag" style="display:block;font-weight:600;margin-bottom:.3rem;">Leveranciersopslag stroom (€/kWh)</label>
      <input id="wp-stroomopslag" type="number" min="0" max="1" step="0.005" value="0.025" oninput="wpHerbereken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Modelaanname: € 0,025/kWh. Ook dit is contractafhankelijk — vul het tarief van je eigen leverancier in.</span>
    </div>
  </div>
  <div id="wp-uitkomst" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:.8rem;margin-top:1.4rem;"></div>
  <div id="wp-tabel" style="margin-top:1.2rem;overflow-x:auto;"></div>
  <p style="color:#666;font-size:.85rem;margin-top:.9rem;"><strong>Modelberekening — geen garantie.</strong> De tool rekent met vaste jaarprijzen en één SCOP over het hele seizoen; in de praktijk bewegen energieprijzen en verandert het rendement met de buitentemperatuur en je afgiftetemperatuur. Onderhoud, financieringskosten en de restwaarde van je ketel zitten er niet in. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

<script>
function wpGetal(id, min, max){
  var el = document.getElementById(id);
  if (el.value === '') return null;
  var v = parseFloat(el.value.replace(',', '.'));
  if (isNaN(v) || v < min || v > max) return null;
  return v;
}
function wpEuro(x){ return '€ ' + x.toFixed(2).replace('.', ','); }
function wpEuro0(x){ return '€ ' + Math.round(x).toLocaleString('nl-NL'); }

function wpTypeWissel(){
  var t = document.getElementById('wp-type').value;
  document.getElementById('wp-dekking').value = (t === 'all') ? 100 : 60;
  document.getElementById('wp-scop').value = (t === 'all') ? 3.5 : 4;
  document.getElementById('wp-scop-hint').innerHTML = (t === 'all')
    ? 'Modelaanname: 3,5 voor een all-electric systeem, dat ook op koude dagen en voor warm tapwater moet leveren. Het cijfer voor jóúw toestel staat op het productlabel en in het datasheet, bij een opgegeven temperatuurregime.'
    : 'Modelaanname: 4,0 voor het warmtepompdeel van een hybride opstelling. Uit 1 kWh stroom komt dan 4 kWh warmte. Het cijfer voor jóúw toestel staat op het productlabel en in het datasheet, bij een opgegeven temperatuurregime.';
  wpReken();
}

// Energie-inhoud Nederlands (Gronings) aardgas: bovenwaarde circa 35,17 MJ/m3 = 9,77 kWh/m3.
// Dat is de gangbare rekenwaarde waarmee energieleveranciers m3 gas naar kWh omrekenen.
// De onderwaarde ligt lager (circa 31,65 MJ/m3 = circa 8,8 kWh/m3); wie daarmee wil rekenen,
// vult zelf een andere waarde in het model in.
var WP_KWH_PER_M3 = 9.77;
// Energiebelasting 2026 incl. btw: gas EUR 0,7268/m3, elektriciteit EUR 0,11085/kWh (bron: Belastingdienst-tarieventabel).
var WP_BEL_GAS = 0.7268;
var WP_BEL_STROOM = 0.11085;
window.wpKaalGas = null;
window.wpKaalStroom = null;

function wpHerbereken(){
  // Prijsvelden opnieuw vullen zodra de opslag wijzigt (alleen als de live kale prijs bekend is)
  var og = wpGetal('wp-gasopslag', 0, 1);
  var os = wpGetal('wp-stroomopslag', 0, 1);
  if (window.wpKaalGas !== null && og !== null) document.getElementById('wp-gasprijs').value = (window.wpKaalGas + WP_BEL_GAS + og).toFixed(3);
  if (window.wpKaalStroom !== null && os !== null) document.getElementById('wp-stroomprijs').value = (window.wpKaalStroom + WP_BEL_STROOM + os).toFixed(3);
  wpReken();
}

function wpReken(){
  var gas     = wpGetal('wp-gas', 0, 10000);
  var dekking = wpGetal('wp-dekking', 1, 100);
  var scop    = wpGetal('wp-scop', 1, 8);
  var inv     = wpGetal('wp-inv', 0, 100000);      // mag leeg blijven
  var isde    = wpGetal('wp-isde', 0, 50000);
  var pGas    = wpGetal('wp-gasprijs', 0, 5);
  var pStroom = wpGetal('wp-stroomprijs', 0, 2);
  var uit = document.getElementById('wp-uitkomst');
  var tab = document.getElementById('wp-tabel');

  if (gas === null || dekking === null || scop === null || pGas === null || pStroom === null){
    uit.innerHTML = '<div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.9rem;grid-column:1/-1;color:#b03a3a;">Vul gasverbruik, dekking, SCOP en beide energieprijzen in met een geldige waarde.</div>';
    tab.innerHTML = '';
    return;
  }
  if (isde === null) isde = 0;

  var vermedenGas  = gas * (dekking / 100);
  var besparingGas = vermedenGas * pGas;
  var warmteKwh    = vermedenGas * WP_KWH_PER_M3;
  var extraKwh     = warmteKwh / scop;
  var kostenStroom = extraKwh * pStroom;
  var netto        = besparingGas - kostenStroom;

  var tvt = (inv !== null && netto > 0) ? Math.max(0, inv - isde) / netto : null;
  var tvtTekst, tvtSub;
  if (inv === null){ tvtTekst = '—'; tvtSub = 'vul je offertebedrag in'; }
  else if (netto <= 0){ tvtTekst = 'geen'; tvtSub = 'deze opzet levert per jaar geen besparing op'; }
  else { tvtTekst = tvt.toFixed(1).replace('.', ',') + ' jaar'; tvtSub = 'na aftrek van ' + wpEuro0(isde) + ' subsidie'; }

  var pos = netto > 0;
  uit.innerHTML =
    '<div style="background:#fff;border-radius:8px;padding:.9rem;border:1px solid #e0e0e0;"><div style="font-size:.8rem;color:#666;">Minder gas</div><div style="font-size:1.3rem;font-weight:700;">' + Math.round(vermedenGas).toLocaleString('nl-NL') + ' m³</div><div style="font-size:.75rem;color:#888;">per jaar</div></div>' +
    '<div style="background:#fff;border-radius:8px;padding:.9rem;border:1px solid #e0e0e0;"><div style="font-size:.8rem;color:#666;">Meer stroom</div><div style="font-size:1.3rem;font-weight:700;">' + Math.round(extraKwh).toLocaleString('nl-NL') + ' kWh</div><div style="font-size:.75rem;color:#888;">per jaar</div></div>' +
    '<div style="background:' + (pos ? '#e8f5ee' : '#fdeeee') + ';border-radius:8px;padding:.9rem;border:1px solid ' + (pos ? '#b7dfc9' : '#f0c4c4') + ';"><div style="font-size:.8rem;color:#444;">Netto jaarbesparing</div><div style="font-size:1.3rem;font-weight:700;">' + wpEuro0(netto) + '</div><div style="font-size:.75rem;color:#666;">' + (pos ? 'voordeel per jaar' : 'nadeel per jaar') + '</div></div>' +
    '<div style="background:#fff;border-radius:8px;padding:.9rem;border:1px solid #e0e0e0;"><div style="font-size:.8rem;color:#666;">Terugverdientijd</div><div style="font-size:1.3rem;font-weight:700;">' + tvtTekst + '</div><div style="font-size:.75rem;color:#888;">' + tvtSub + '</div></div>';

  var rij = function(stap, som, uitkomst, sterk){
    return '<tr' + (sterk ? ' style="background:#f1f3f5;font-weight:600;"' : '') + '>' +
      '<td style="padding:.4rem .6rem;border-bottom:1px solid #eee;">' + stap + '</td>' +
      '<td style="padding:.4rem .6rem;border-bottom:1px solid #eee;color:#555;">' + som + '</td>' +
      '<td style="padding:.4rem .6rem;border-bottom:1px solid #eee;white-space:nowrap;">' + uitkomst + '</td></tr>';
  };
  var rijen =
    rij('1. Vermeden gas', Math.round(gas).toLocaleString('nl-NL') + ' m³ × ' + dekking + '%', Math.round(vermedenGas).toLocaleString('nl-NL') + ' m³') +
    rij('2. Besparing op gas', Math.round(vermedenGas).toLocaleString('nl-NL') + ' m³ × ' + wpEuro(pGas), wpEuro0(besparingGas)) +
    rij('3. Warmte die je moet vervangen', Math.round(vermedenGas).toLocaleString('nl-NL') + ' m³ × 9,77 kWh/m³', Math.round(warmteKwh).toLocaleString('nl-NL') + ' kWh') +
    rij('4. Extra stroom', Math.round(warmteKwh).toLocaleString('nl-NL') + ' kWh ÷ SCOP ' + String(scop).replace('.', ','), Math.round(extraKwh).toLocaleString('nl-NL') + ' kWh') +
    rij('5. Kosten stroom', Math.round(extraKwh).toLocaleString('nl-NL') + ' kWh × ' + wpEuro(pStroom), wpEuro0(kostenStroom)) +
    rij('6. Netto jaarbesparing', 'besparing gas − kosten stroom', wpEuro0(netto), true) +
    rij('7. Terugverdientijd', inv === null ? 'investering nog niet ingevuld' : '(' + wpEuro0(inv) + ' − ' + wpEuro0(isde) + ') ÷ ' + wpEuro0(netto) + '/jaar', tvtTekst, true);
  tab.innerHTML = '<table style="width:100%;border-collapse:collapse;font-size:.9rem;background:#fff;border:1px solid #e0e0e0;border-radius:8px;">' +
    '<thead><tr style="background:#f1f3f5;text-align:left;"><th style="padding:.45rem .6rem;">Stap</th><th style="padding:.45rem .6rem;">Berekening</th><th style="padding:.45rem .6rem;">Uitkomst</th></tr></thead><tbody>' +
    rijen + '</tbody></table>' +
    '<p style="color:#666;font-size:.8rem;margin:.6rem 0 0;">Modelberekening op basis van de waarden die jij invulde — geen garantie. Aan deze informatie kunnen geen rechten worden ontleend.</p>';
}

// Live kale dagprijzen ophalen en de all-in prijzen vullen
fetch('https://beheer.wtdigital.nl/api/public/gasprijs').then(function(r){ return r.json(); }).then(function(d){
  if (typeof d.prijs_m3 !== 'number') return;
  window.wpKaalGas = d.prijs_m3;
  var og = wpGetal('wp-gasopslag', 0, 1); if (og === null) og = 0;
  document.getElementById('wp-gasprijs').value = (d.prijs_m3 + WP_BEL_GAS + og).toFixed(3);
  document.getElementById('wp-gas-hint').innerHTML = 'Live: kale beursprijs € ' + d.prijs_m3.toFixed(3) + '/m³ (' + (d.datum || 'vandaag') + ') + € 0,7268 energiebelasting incl. btw + € ' + og.toFixed(3).replace('.', ',') + ' opslag. Pas het veld aan naar het tarief op je eigen jaarnota.';
  wpReken();
}).catch(function(){ document.getElementById('wp-gas-hint').textContent = 'Live prijs niet beschikbaar — vul het all-in gastarief van je eigen contract in.'; });

fetch('https://beheer.wtdigital.nl/api/public/stroomprijzen').then(function(r){ return r.json(); }).then(function(d){
  var gem = null;
  if (d.uren && d.uren.length) gem = d.uren.reduce(function(a, u){ return a + u.prijs; }, 0) / d.uren.length;
  else if (typeof d.gemiddelde === 'number') gem = d.gemiddelde;
  if (gem === null) return;
  window.wpKaalStroom = gem;
  var os = wpGetal('wp-stroomopslag', 0, 1); if (os === null) os = 0;
  document.getElementById('wp-stroomprijs').value = (gem + WP_BEL_STROOM + os).toFixed(3);
  document.getElementById('wp-stroom-hint').innerHTML = 'Live: daggemiddelde kale beursprijs € ' + gem.toFixed(3) + '/kWh (' + (d.datum || 'vandaag') + ') + € 0,11085 energiebelasting incl. btw + € ' + os.toFixed(3).replace('.', ',') + ' opslag. Zie ook de <a href="/stroomprijzen/">uurprijzen van vandaag</a>.';
  wpReken();
}).catch(function(){ document.getElementById('wp-stroom-hint').textContent = 'Live prijs niet beschikbaar — vul het all-in stroomtarief van je eigen contract in.'; });

wpReken();
</script>

## Waar de aannames vandaan komen

| Veld | Startwaarde | Onderbouwing |
|---|---|---|
| Gasverbruik | 1.200 m³/jaar | Modelaanname als startpunt voor een rijtjeswoning. Je eigen cijfer staat op je jaarafrekening en is altijd beter. |
| Dekking hybride | 60% | Modelaanname. Een hybride warmtepomp is gedimensioneerd op het grootste deel van het seizoen, niet op de koudste dagen; de ketel springt bij als het vermogen of de afgiftetemperatuur niet meer volstaat. Het werkelijke aandeel volgt uit de dimensionering in je offerte. |
| Dekking all-electric | 100% | De ketel gaat eruit, dus alle warmte (en meestal ook warm tapwater) komt van de warmtepomp. |
| SCOP hybride-deel | 4,0 | Modelaanname. Fabrikanten geven het seizoensrendement op bij een vastgelegd temperatuurregime; lucht-water-toestellen halen kwalitatief gezien hun hoogste waarden bij lage afgiftetemperaturen (vloerverwarming, lage-temperatuurradiatoren) en in de mildere delen van het seizoen — precies het bereik waarin een hybride opstelling werkt. Neem het cijfer van het productlabel van jóúw toestel over. |
| SCOP all-electric | 3,5 | Modelaanname, lager dan bij hybride omdat het toestel ook op de koudste dagen en voor warm tapwater moet leveren; juist dan zakt het rendement. |
| Energie-inhoud gas | 9,77 kWh/m³ | Vuistregel voor Nederlands (Gronings) aardgas: bovenwaarde circa 35,17 MJ/m³, oftewel 9,77 kWh per m³. Dit is de rekenwaarde die energieleveranciers en rekenmodellen in Nederland gebruiken om m³ gas naar kWh om te zetten. Rekenen met de onderwaarde (circa 31,65 MJ/m³ ≈ 8,8 kWh) valt lager uit; je kunt dat getal in stap 3 zelf aanhouden. |
| Energiebelasting gas | € 0,7268/m³ | Wettelijk tarief 2026 inclusief btw, schijf 1 (bron: tarieventabel Belastingdienst). |
| Energiebelasting stroom | € 0,11085/kWh | Wettelijk tarief 2026 inclusief btw, schijf 1 (bron: tarieventabel Belastingdienst). |
| Leveranciersopslag | € 0,05/m³ en € 0,025/kWh | Modelaannames. De inkoopvergoeding verschilt per leverancier en per contract; het exacte bedrag staat in je leveringsovereenkomst. |
| Kale beursprijzen | live | Dagprijs gas (LEBA/TTF) en het daggemiddelde van de uurprijzen stroom (EPEX), via onze eigen [stroomprijzenpagina](/stroomprijzen/). Heb je een vast contract, vul dan gewoon je eigen tarieven in. |
| Investeringsbedrag | leeg | Bewust leeg. Wij noemen geen aanschafprijzen: die lopen per merk, vermogen, woning en installateur ver uiteen, en een verzonnen gemiddelde maakt de uitkomst onbruikbaar. |
| ISDE-subsidie | € 0 | Zoek het bedrag voor jouw specifieke apparaat op in de ISDE-apparatenlijst van RVO en vul het zelf in. Bedragen en voorwaarden wijzigen per jaar. |

Geen van deze getallen is een meting van ons. De rekentool is een rekenmachine met transparante formules — de uitkomst wordt pas bruikbaar als je de aannames vervangt door je eigen jaarafrekening, je eigen productlabel en je eigen offerte.

## Wat bepaalt of het uit kan

De tool laat één ding meteen zien: de netto besparing staat of valt bij de verhouding tussen de gasprijs en de stroomprijs gedeeld door de SCOP. Vier factoren bepalen aan welke kant je uitkomt.

**1. Isolatie eerst.** Een warmtepomp levert warmte bij een lagere temperatuur dan een ketel. Hoe slechter de schil, hoe hoger de afgiftetemperatuur moet zijn om het huis warm te krijgen — en hoe lager de SCOP. Isoleren verlaagt bovendien je gasverbruik, en daarmee de investering die je nodig hebt (kleiner vermogen). Reken de isolatiestap dus eerst door: [dakisolatie van binnenuit of buitenaf](/posts/dakisolatie-binnenuit-vs-buitenuit-2026/) zet de opties naast elkaar.

**2. Hybride of all-electric.** Hybride vraagt een lagere investering en verdraagt een hogere afgiftetemperatuur, maar je houdt een gasaansluiting met vastrecht en je bespaart alleen op het deel dat de warmtepomp overneemt. All-electric bespaart het volledige gasverbruik, maar stelt zwaardere eisen aan isolatie, afgifte en soms de netaansluiting. Vul in de tool beide scenario's in met de bijbehorende offertebedragen en vergelijk. Achtergrond: [warmtepomp versus hybride warmtepomp](/posts/warmtepomp-vs-hybride-warmtepomp-2026/) en onze [vergelijking van hybride warmtepompen](/posts/beste-hybride-warmtepomp-2026/).

**3. Onderhoud en vaste lasten.** De tool rekent alleen brandstofkosten. Daarbovenop komen jaarlijks onderhoud en periodieke controles, en bij hybride houd je ook het ketelonderhoud plus het vastrecht van je gasaansluiting. Reken dat bedrag van je jaarbesparing af voordat je conclusies trekt: zie [warmtepomp onderhoud en kosten](/posts/warmtepomp-onderhoud-kosten-2026/).

**4. De offerte zelf.** Het investeringsbedrag is de variabele met de grootste spreiding en tegelijk de enige die je hard kunt maken. Vraag meerdere offertes op met dezelfde uitgangspunten (gewenste dekking, afgiftetemperatuur, geluidseisen) zodat je ze kunt vergelijken. Waar je op moet letten staat in [installateur kiezen](/installateur-kiezen/).

Verandert de energieprijsverhouding, dan kantelt de uitkomst. Wie een dynamisch contract heeft, kan de stroomkosten van een warmtepomp verlagen door in goedkope uren te verwarmen of te bufferen — de actuele uurprijzen staan op [stroomprijzen vandaag](/stroomprijzen/).
