---
title: "Historie dynamische stroomprijzen (dag- en maandgemiddelden + elke dag terug te kijken)"
description: "Historie van de dynamische stroomprijzen: maandgemiddelden van het afgelopen jaar, daggemiddelden van de laatste 30 dagen en de uurprijzen van elke dag vanaf 2014 — rechtstreeks uit de EPEX day-ahead-data."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
faq:
- q: 'Tot hoe ver terug kan ik prijzen opzoeken?'
  a: 'De datumkiezer gaat terug tot 1 januari 2014. Voor oudere jaren kan de dekking per dag verschillen; is er niets beschikbaar, dan meldt de tool dat.'
- q: 'Waarom wijkt het maandgemiddelde af van wat ik bij mijn leverancier zie?'
  a: 'Omdat hier de kale beursprijs staat: inclusief btw, maar zonder energiebelasting, inkoopvergoeding en vaste kosten. Je leverancier telt die er bovenop, en rekent bovendien met jouw eigen verbruiksprofiel in plaats van een ongewogen uurgemiddelde.'
- q: 'Kan ik uit deze historie afleiden wat stroom volgend jaar kost?'
  a: 'Nee. De historie toont patronen, geen voorspelling — prijzen uit het verleden bieden geen indicatie voor toekomstige prijzen. Wil je weten wat er nu speelt, kijk dan op [actuele stroomprijzen](/stroomprijzen/) met de uurprijzen voor vandaag en morgen.'
lastmod: 2026-08-20
---

*Disclosure: dit artikel bevat affiliate-links naar energieaanbieders. Sluit je via zo'n link een contract af, dan ontvangen wij mogelijk een commissie — dit kost jou niets extra en beïnvloedt de getoonde prijzen niet: die komen rechtstreeks van de stroombeurs.*

Op deze pagina zie je de **historie van de dynamische stroomprijzen**: de maandgemiddelden van het afgelopen jaar, de daggemiddelden van de laatste 30 dagen en de uurprijzen van élke dag vanaf 2014. Het gaat om de kale day-ahead-beursprijs (EPEX) inclusief btw — dezelfde basis waarop dynamische contracten van Frank Energie, Tibber, ANWB Energie en Zonneplan rekenen. De prijzen van vandaag en morgen staan op [actuele stroomprijzen](/stroomprijzen/).

## Maandgemiddelden afgelopen jaar

<div id="mh-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:.8rem;">
    <div style="font-size:.9rem;color:#666;">Gemiddelde kale prijs per maand (€/kWh)</div>
    <span id="mh-status" style="color:#666;font-size:.85rem;"></span>
  </div>
  <div id="mh-samenvatting" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.8rem;margin-bottom:1.2rem;"></div>
  <div id="mh-chart" style="display:flex;align-items:flex-end;gap:4px;height:170px;"></div>
  <div id="mh-labels" style="display:flex;gap:4px;margin-top:.3rem;color:#888;font-size:.7rem;"></div>
  <p style="color:#666;font-size:.85rem;margin-top:.8rem;">Kale EPEX-prijs incl. btw, excl. energiebelasting en inkoopvergoeding. Bron: day-ahead-veiling via EnergyZero. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

De staven laten zien hoe sterk het gemiddelde per maand schuift. Het patroon dat je meestal terugziet: in de zonnige maanden drukt zonnestroom de middagprijzen (en dus het maandgemiddelde), terwijl de donkere maanden met veel verwarmingsvraag en weinig zon structureel duurder uitvallen. Hoe hard dat verschil uitpakt, verschilt per jaar — gasprijzen, import en export en het weer wegen allemaal mee.

## Daggemiddelden laatste 30 dagen

<div id="dh-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:.8rem;">
    <div style="font-size:.9rem;color:#666;">Gemiddelde kale prijs per dag (€/kWh)</div>
    <span id="dh-status" style="color:#666;font-size:.85rem;"></span>
  </div>
  <div id="dh-samenvatting" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.8rem;margin-bottom:1.2rem;"></div>
  <div id="dh-chart" style="display:flex;align-items:flex-end;gap:2px;height:150px;"></div>
  <div id="dh-labels" style="display:flex;justify-content:space-between;color:#888;font-size:.75rem;margin-top:.3rem;"></div>
  <p style="color:#666;font-size:.85rem;margin-top:.8rem;">Kale EPEX-prijs incl. btw, excl. energiebelasting en inkoopvergoeding. Bron: day-ahead-veiling via EnergyZero. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

Op dagniveau valt vooral op hoe groot de spreiding is: een zonnige, winderige zondag met weinig vraag kan een fractie kosten van een windstille werkdag. Voor wie een dynamisch contract heeft, is dat geen ruis maar het verdienmodel — de dagen met een laag gemiddelde zijn precies de dagen waarop [verschuiven van verbruik](/beste-tijd-wasmachine/) het meeste oplevert.

## Bekijk een dag uit het verleden

<div id="dd-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:flex;gap:.5rem;margin-bottom:1rem;flex-wrap:wrap;align-items:center;">
    <input type="date" id="dd-datum" min="2014-01-01" style="padding:.45rem .6rem;border-radius:8px;border:1px solid #cfd8dc;font:inherit;">
    <button onclick="ddLaad()" style="padding:.5rem 1.2rem;border-radius:8px;border:1px solid #0e7490;background:#0e7490;color:#fff;cursor:pointer;font:inherit;">Bekijk uurprijzen</button>
    <span id="dd-status" style="color:#666;font-size:.9rem;"></span>
  </div>
  <div id="dd-samenvatting" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.8rem;margin-bottom:1.2rem;"></div>
  <div id="dd-chart" style="display:flex;align-items:flex-end;gap:2px;height:180px;"></div>
  <div style="display:flex;justify-content:space-between;color:#888;font-size:.8rem;margin-top:.3rem;"><span>00:00</span><span>12:00</span><span>23:00</span></div>
  <p style="color:#666;font-size:.85rem;margin-top:.8rem;">Kale EPEX-prijs incl. btw, excl. energiebelasting en inkoopvergoeding. Bron: day-ahead-veiling via EnergyZero. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

<script>
var MH_API = 'https://beheer.wtdigital.nl/api/public/stroomprijzen';
function mhKleur(v, min, max){ return v === min ? '#1a7a4a' : (v === max ? '#b03a3a' : '#0e7490'); }
function mhKaart(label, waarde, sub, stijl){
  var b = stijl === 'laag' ? 'background:#e8f5ee;border:1px solid #b7dfc9;' : (stijl === 'hoog' ? 'background:#fdeeee;border:1px solid #f0c4c4;' : 'background:#fff;border:1px solid #e0e0e0;');
  var c = stijl === 'laag' ? '#1a7a4a' : (stijl === 'hoog' ? '#b03a3a' : '#666');
  return '<div style="' + b + 'border-radius:8px;padding:.8rem;"><div style="font-size:.8rem;color:' + c + ';">' + label + '</div><div style="font-size:1.3rem;font-weight:700;">' + waarde + '</div><div style="font-size:.75rem;color:' + c + ';">' + sub + '</div></div>';
}

// A. Maandgemiddelden
fetch(MH_API + '?maanden=13').then(function(r){ return r.json(); }).then(function(d){
  var alle = d.maanden || [];
  if (!alle.length) { document.getElementById('mh-status').textContent = 'Geen data beschikbaar.'; return; }
  var m = alle.filter(function(x, i){ return x.metingen >= 600 || i === alle.length - 1; });
  if (!m.length) { document.getElementById('mh-status').textContent = 'Geen data beschikbaar.'; return; }
  var laatsteIdx = m.length - 1;
  var lopend = m[laatsteIdx].metingen < 600;
  var volledig = lopend ? m.slice(0, laatsteIdx) : m;
  var ws = volledig.map(function(x){ return x.gemiddelde; });
  var min = Math.min.apply(null, ws), max = Math.max.apply(null, ws);
  var laagste = volledig.filter(function(x){ return x.gemiddelde === min; })[0];
  var hoogste = volledig.filter(function(x){ return x.gemiddelde === max; })[0];
  function maandNL(s){ var p = s.split('-'); return new Date(Date.UTC(+p[0], +p[1] - 1, 1)).toLocaleDateString('nl-NL', { timeZone: 'UTC', month: 'short', year: '2-digit' }); }
  var gemAlle = ws.reduce(function(a, b){ return a + b; }, 0) / ws.length;
  document.getElementById('mh-samenvatting').innerHTML =
    mhKaart('Gemiddelde van deze maanden', '€ ' + gemAlle.toFixed(3), 'per kWh, kaal', '') +
    mhKaart('Laagste maand', '€ ' + min.toFixed(3), maandNL(laagste.maand), 'laag') +
    mhKaart('Hoogste maand', '€ ' + max.toFixed(3), maandNL(hoogste.maand), 'hoog');
  var alleW = m.map(function(x){ return x.gemiddelde; });
  var bMin = Math.min.apply(null, alleW), bMax = Math.max.apply(null, alleW), span = (bMax - bMin) || 1;
  document.getElementById('mh-chart').innerHTML = m.map(function(x, i){
    var h = 15 + ((x.gemiddelde - bMin) / span) * 85;
    var isLopend = lopend && i === laatsteIdx;
    var kleur = isLopend ? '#9aa5a8' : mhKleur(x.gemiddelde, min, max);
    var t = x.maand + ' — € ' + x.gemiddelde.toFixed(3) + '/kWh' + (isLopend ? ' (lopende maand)' : '');
    return '<div title="' + t + '" style="flex:1;height:' + h.toFixed(0) + '%;background:' + kleur + ';border-radius:3px 3px 0 0;min-width:8px;"></div>';
  }).join('');
  document.getElementById('mh-labels').innerHTML = m.map(function(x, i){
    return '<div style="flex:1;min-width:8px;text-align:center;">' + maandNL(x.maand).replace(' ', '&nbsp;') + (lopend && i === laatsteIdx ? '<br>lopend' : '') + '</div>';
  }).join('');
}).catch(function(){ document.getElementById('mh-status').textContent = 'Kon maandgemiddelden niet laden.'; });

// B. Daggemiddelden
fetch(MH_API + '?historie=30').then(function(r){ return r.json(); }).then(function(d){
  var dg = (d.dagen || []).filter(function(x){ return x.metingen >= 20; });
  if (!dg.length) { document.getElementById('dh-status').textContent = 'Geen data beschikbaar.'; return; }
  var ws = dg.map(function(x){ return x.gemiddelde; });
  var min = Math.min.apply(null, ws), max = Math.max.apply(null, ws), span = (max - min) || 1;
  var gem = ws.reduce(function(a, b){ return a + b; }, 0) / ws.length;
  function datumNL(s){ return new Date(s + 'T12:00:00Z').toLocaleDateString('nl-NL', { timeZone: 'UTC', day: 'numeric', month: 'short' }); }
  var laagste = dg.filter(function(x){ return x.gemiddelde === min; })[0];
  var hoogste = dg.filter(function(x){ return x.gemiddelde === max; })[0];
  document.getElementById('dh-samenvatting').innerHTML =
    mhKaart('Gemiddelde over deze periode', '€ ' + gem.toFixed(3), 'per kWh, kaal', '') +
    mhKaart('Goedkoopste dag', '€ ' + min.toFixed(3), datumNL(laagste.datum), 'laag') +
    mhKaart('Duurste dag', '€ ' + max.toFixed(3), datumNL(hoogste.datum), 'hoog');
  document.getElementById('dh-chart').innerHTML = dg.map(function(x){
    var h = 15 + ((x.gemiddelde - min) / span) * 85;
    return '<div title="' + x.datum + ' — € ' + x.gemiddelde.toFixed(3) + '/kWh" style="flex:1;height:' + h.toFixed(0) + '%;background:' + mhKleur(x.gemiddelde, min, max) + ';border-radius:2px 2px 0 0;min-width:4px;"></div>';
  }).join('');
  document.getElementById('dh-labels').innerHTML = '<span>' + datumNL(dg[0].datum) + '</span><span>' + datumNL(dg[dg.length - 1].datum) + '</span>';
}).catch(function(){ document.getElementById('dh-status').textContent = 'Kon daggemiddelden niet laden.'; });

// C. Losse dag uit het verleden
(function(){
  var inp = document.getElementById('dd-datum');
  var vandaag = new Date();
  var iso = vandaag.getFullYear() + '-' + String(vandaag.getMonth() + 1).padStart(2, '0') + '-' + String(vandaag.getDate()).padStart(2, '0');
  inp.max = iso;
  var jaarTerug = new Date(vandaag.getTime() - 365 * 86400000);
  inp.value = jaarTerug.getFullYear() + '-' + String(jaarTerug.getMonth() + 1).padStart(2, '0') + '-' + String(jaarTerug.getDate()).padStart(2, '0');
})();
async function ddLaad(){
  var st = document.getElementById('dd-status');
  var datum = document.getElementById('dd-datum').value;
  var chart = document.getElementById('dd-chart'), sam = document.getElementById('dd-samenvatting');
  if (!datum) { st.textContent = 'Kies eerst een datum.'; return; }
  st.textContent = 'laden…';
  try {
    var r = await fetch(MH_API + '?datum=' + datum);
    var d = await r.json();
    if (!d.uren || !d.uren.length) { st.textContent = 'Voor deze datum is geen data beschikbaar.'; chart.innerHTML = ''; sam.innerHTML = ''; return; }
    st.textContent = '';
    var ps = d.uren.map(function(u){ return u.prijs; });
    var min = Math.min.apply(null, ps), max = Math.max.apply(null, ps), span = (max - min) || 1;
    var gem = ps.reduce(function(a, b){ return a + b; }, 0) / ps.length;
    function uurNL(uurUTC){
      var dt = new Date(datum + 'T' + String(uurUTC).padStart(2, '0') + ':00:00Z');
      return dt.toLocaleTimeString('nl-NL', { timeZone: 'Europe/Amsterdam', hour: '2-digit', minute: '2-digit' });
    }
    var goedkoop = d.uren.filter(function(u){ return u.prijs === min; }).map(function(u){ return uurNL(u.uur); }).join(', ');
    var duur = d.uren.filter(function(u){ return u.prijs === max; }).map(function(u){ return uurNL(u.uur); }).join(', ');
    sam.innerHTML =
      mhKaart('Gemiddeld', '€ ' + gem.toFixed(3), 'per kWh op ' + datum, '') +
      mhKaart('Goedkoopste uur', '€ ' + min.toFixed(3), goedkoop, 'laag') +
      mhKaart('Duurste uur', '€ ' + max.toFixed(3), duur, 'hoog');
    chart.innerHTML = d.uren.map(function(u){
      var h = 15 + ((u.prijs - min) / span) * 85;
      return '<div title="' + uurNL(u.uur) + ' — € ' + u.prijs.toFixed(3) + '/kWh" style="flex:1;height:' + h.toFixed(0) + '%;background:' + mhKleur(u.prijs, min, max) + ';border-radius:3px 3px 0 0;min-width:4px;"></div>';
    }).join('');
  } catch(e) { st.textContent = 'Voor deze datum is geen data beschikbaar.'; }
}
ddLaad();
</script>

De datumkiezer werkt terug tot 1 januari 2014 — handig om na te kijken wat er op een specifieke dag gebeurde: een storm met veel windaanbod, een zonnige feestdag met weinig industriële vraag, of een koude windstille avond. De uurprijzen staan in Nederlandse tijd, dus je kunt ze naast je eigen verbruik leggen.

## Wat je uit historie wél kunt halen

Historische prijzen zijn nuttig voor **patroonherkenning**, en daar houdt het op. Drie dingen die je er redelijk uit kunt lezen:

1. **Het dagpatroon.** Wanneer valt de dip en wanneer de piek? Dat vertelt je of automatisch laden 's nachts of juist rond het middaguur logisch is voor jouw situatie.
2. **De seizoensinvloed.** Vergelijk zomer- en wintermaanden in de eerste grafiek: het aanbod aan zon en de warmtevraag verschuiven het hele niveau.
3. **De spreiding.** Het verschil tussen het goedkoopste en duurste uur van een dag bepaalt of een [thuisbatterij of slimme sturing](/terugverdientijd-thuisbatterij/) rekenkundig iets oplevert. Zit alles dicht bij elkaar, dan valt er weinig te verdienen met verschuiven.

## Wat je er niet uit kunt halen

**Prijzen uit het verleden zijn geen indicatie voor de toekomst.** De day-ahead-prijs komt elke dag opnieuw tot stand uit gasprijzen, weersverwachting, importcapaciteit, onderhoud aan centrales en beleid. Een reeks goedkope maanden zegt niets over de maanden die volgen, en een reeks dure maanden ook niet. Wij doen daarom geen prijsvoorspellingen en raden af om een contractkeuze te baseren op een doorgetrokken lijn — ook niet op de lijnen op deze pagina.

Let er ook op dat deze cijfers de **kale beursprijs** zijn. Je eindprijs is die kale prijs plus energiebelasting, de inkoopvergoeding van je leverancier en vaste kosten. Twee mensen met exact dezelfde uurprijzen kunnen dus een merkbaar verschillende rekening hebben.

## Vast of dynamisch: hoe je deze data gebruikt

Historie helpt bij die keuze op één manier: het laat zien hoe *beweeglijk* de markt is en hoeveel ruimte er zit tussen goedkope en dure uren. Kun je verbruik echt verschuiven — een wasmachine met uitgestelde start, een EV die 's nachts laadt, een warmtepomp of batterij met slimme sturing — dan is die beweeglijkheid je voordeel. Kun je dat niet, dan betaal je bij een dynamisch contract simpelweg het gemiddelde, met het risico van uitschieters erbij.

Een vast contract ruilt dat risico in voor zekerheid, tegen een opslag die de leverancier daarvoor rekent. Welke van de twee gunstiger uitpakt, weet je pas achteraf; wat je vóóraf wél kunt doen is de tariefopbouw vergelijken — per aanbieder naast elkaar in onze [vergelijking van dynamische energiecontracten](/dynamisch-energiecontract-vergelijken/). Zie je veel dagen met een heel laag gemiddelde, kijk dan ook naar [negatieve stroomprijzen](/negatieve-stroomprijzen/).

<a href="https://go.duurzaamthuislab.nl/frank-energie?ref=/stroomprijzen-historie/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk Frank Energie (dynamisch contract) →</a>
