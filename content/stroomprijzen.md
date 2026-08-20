---
title: "Stroomprijzen, gasprijs en zonverwachting vandaag (live)"
description: "Actuele dynamische stroomprijzen per uur (vandaag en morgen), de gasprijs van vandaag en de verwachte zonnepanelen-opbrengst — automatisch ververst uit beursdata en weerdata."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
lastmod: 2026-08-20
---

*Disclosure: dit artikel bevat affiliate-links naar energieaanbieders. Sluit je via zo'n link een contract af, dan ontvangen wij mogelijk een commissie — dit kost jou niets extra en beïnvloedt de getoonde prijzen niet: die komen rechtstreeks van de stroombeurs.*

Op deze pagina zie je de **dynamische stroomprijzen per uur** voor vandaag en (na circa 15:00) morgen. Dit zijn de kale day-ahead-beursprijzen (EPEX) inclusief btw — precies de prijzen waarop dynamische contracten van aanbieders als Frank Energie, Tibber, ANWB Energie en Zonneplan zijn gebaseerd.

<div id="sp-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:flex;gap:.5rem;margin-bottom:1rem;flex-wrap:wrap;">
    <button id="sp-btn-vandaag" onclick="spLaad(0)" style="padding:.5rem 1.2rem;border-radius:8px;border:1px solid #0e7490;background:#0e7490;color:#fff;cursor:pointer;font:inherit;">Vandaag</button>
    <button id="sp-btn-morgen" onclick="spLaad(1)" style="padding:.5rem 1.2rem;border-radius:8px;border:1px solid #0e7490;background:#fff;color:#0e7490;cursor:pointer;font:inherit;">Morgen</button>
    <span id="sp-status" style="align-self:center;color:#666;font-size:.9rem;"></span>
  </div>
  <div id="sp-samenvatting" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.8rem;margin-bottom:1.2rem;"></div>
  <div id="sp-acties" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:.8rem;margin-bottom:1.2rem;"></div>
  <div id="sp-chart" style="display:flex;align-items:flex-end;gap:2px;height:180px;"></div>
  <div style="display:flex;justify-content:space-between;color:#888;font-size:.8rem;margin-top:.3rem;"><span>00:00</span><span>12:00</span><span>23:00</span></div>
  <p style="color:#666;font-size:.85rem;margin-top:.8rem;">Kale EPEX-prijs incl. btw, excl. energiebelasting en de inkoopvergoeding van je leverancier. Bron: day-ahead-veiling, elk kwartier ververst.</p>
</div>

<script>
async function spLaad(dag){
  var st = document.getElementById('sp-status');
  document.getElementById('sp-btn-vandaag').style.background = dag===0 ? '#0e7490' : '#fff';
  document.getElementById('sp-btn-vandaag').style.color = dag===0 ? '#fff' : '#0e7490';
  document.getElementById('sp-btn-morgen').style.background = dag===1 ? '#0e7490' : '#fff';
  document.getElementById('sp-btn-morgen').style.color = dag===1 ? '#fff' : '#0e7490';
  st.textContent = 'laden…';
  try {
    var r = await fetch('https://beheer.wtdigital.nl/api/public/stroomprijzen' + (dag ? '?dag=morgen' : ''));
    var d = await r.json();
    if (!d.uren || !d.uren.length) { st.textContent = dag ? 'Morgenprijzen komen rond 15:00 beschikbaar.' : 'Geen data beschikbaar.'; document.getElementById('sp-chart').innerHTML=''; document.getElementById('sp-samenvatting').innerHTML=''; return; }
    st.textContent = '';
    var prijzen = d.uren.map(function(u){ return u.prijs; });
    var min = Math.min.apply(null, prijzen), max = Math.max.apply(null, prijzen);
    var gem = prijzen.reduce(function(a,b){return a+b;},0) / prijzen.length;
    function uurNL(uurUTC){
      var dt = new Date(Date.UTC(2026,0,1,uurUTC));
      dt = new Date(d.datum + 'T' + String(uurUTC).padStart(2,'0') + ':00:00Z');
      return dt.toLocaleTimeString('nl-NL',{timeZone:'Europe/Amsterdam',hour:'2-digit',minute:'2-digit'});
    }
    var goedkoop = d.uren.filter(function(u){return u.prijs===min;}).map(function(u){return uurNL(u.uur);}).join(', ');
    var duur = d.uren.filter(function(u){return u.prijs===max;}).map(function(u){return uurNL(u.uur);}).join(', ');
    document.getElementById('sp-samenvatting').innerHTML =
      '<div style="background:#fff;border-radius:8px;padding:.8rem;border:1px solid #e0e0e0;"><div style="font-size:.8rem;color:#666;">Gemiddeld</div><div style="font-size:1.3rem;font-weight:700;">€ ' + gem.toFixed(3) + '</div><div style="font-size:.75rem;color:#888;">per kWh</div></div>' +
      '<div style="background:#e8f5ee;border-radius:8px;padding:.8rem;border:1px solid #b7dfc9;"><div style="font-size:.8rem;color:#1a7a4a;">Goedkoopste uur</div><div style="font-size:1.3rem;font-weight:700;">€ ' + min.toFixed(3) + '</div><div style="font-size:.75rem;color:#1a7a4a;">' + goedkoop + '</div></div>' +
      '<div style="background:#fdeeee;border-radius:8px;padding:.8rem;border:1px solid #f0c4c4;"><div style="font-size:.8rem;color:#b03a3a;">Duurste uur</div><div style="font-size:1.3rem;font-weight:700;">€ ' + max.toFixed(3) + '</div><div style="font-size:.75rem;color:#b03a3a;">' + duur + '</div></div>';
    // Beste actiemomenten: goedkoopste blokken van 2 (was/droger) en 4 (EV) aaneengesloten uren
    function goedkoopsteBlok(n){
      var best = null, bestSom = Infinity;
      for (var i = 0; i + n <= d.uren.length; i++){
        var som = 0;
        for (var j = i; j < i + n; j++) som += d.uren[j].prijs;
        if (som < bestSom){ bestSom = som; best = i; }
      }
      return best === null ? null : { van: uurNL(d.uren[best].uur), tot: uurNL(d.uren[Math.min(best+n, d.uren.length-1)].uur), gem: bestSom / n };
    }
    var was = goedkoopsteBlok(2), ev = goedkoopsteBlok(4);
    var actiesHtml = '';
    if (was) actiesHtml += '<div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;"><div style="font-size:.8rem;color:#666;">🧺 Wasmachine / vaatwasser</div><div style="font-weight:700;">' + was.van + ' – ' + was.tot + '</div><div style="font-size:.75rem;color:#888;">goedkoopste 2 uur (gem. € ' + was.gem.toFixed(3) + ')</div></div>';
    if (ev) actiesHtml += '<div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;"><div style="font-size:.8rem;color:#666;">🚗 EV / thuisbatterij laden</div><div style="font-weight:700;">' + ev.van + ' – ' + ev.tot + '</div><div style="font-size:.75rem;color:#888;">goedkoopste 4 uur (gem. € ' + ev.gem.toFixed(3) + ')</div></div>';
    if (min < 0) actiesHtml += '<div style="background:#0e7490;color:#fff;border-radius:8px;padding:.8rem;"><div style="font-size:.8rem;opacity:.85;">⚡ Negatieve prijzen</div><div style="font-weight:700;">Je krijgt geld toe op ' + goedkoop + '</div><div style="font-size:.75rem;opacity:.85;">verschuif zoveel mogelijk verbruik</div></div>';
    document.getElementById('sp-acties').innerHTML = actiesHtml;
    var span = (max - min) || 1;
    document.getElementById('sp-chart').innerHTML = d.uren.map(function(u){
      var h = 15 + ((u.prijs - min) / span) * 85;
      var kleur = u.prijs === min ? '#1a7a4a' : (u.prijs === max ? '#b03a3a' : '#0e7490');
      return '<div title="' + uurNL(u.uur) + ' — € ' + u.prijs.toFixed(3) + '/kWh" style="flex:1;height:' + h.toFixed(0) + '%;background:' + kleur + ';border-radius:3px 3px 0 0;min-width:4px;"></div>';
    }).join('');
  } catch(e) { st.textContent = 'Kon prijzen niet laden — probeer het later opnieuw.'; }
}
spLaad(0);
</script>

## Gasprijs vandaag

Ook de gasprijs beweegt dagelijks mee met de beurs (LEBA/TTF). Anders dan stroom heeft gas **één prijs per dag**, die om 06:00 ingaat. Dit is de kale beursprijs inclusief btw — je leverancier telt er energiebelasting en zijn inkoopvergoeding bij op.

<div id="gas-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.8rem;">
  <div style="background:#fff;border-radius:8px;padding:.8rem;border:1px solid #e0e0e0;"><div style="font-size:.8rem;color:#666;">🔥 Gasprijs vandaag</div><div id="gas-prijs" style="font-size:1.6rem;font-weight:700;">—</div><div style="font-size:.75rem;color:#888;">per m³, kaal incl. btw</div></div>
  <div style="background:#fff;border-radius:8px;padding:.8rem;border:1px solid #e0e0e0;align-self:stretch;"><div style="font-size:.8rem;color:#666;">Wat komt erbij?</div><div style="font-size:.85rem;color:#555;line-height:1.5;margin-top:.3rem;">Energiebelasting (wettelijk tarief per m³, zie Belastingdienst) + inkoopvergoeding van je leverancier.</div></div>
  <div style="grid-column:1/-1;background:#fff;border-radius:8px;padding:.8rem;border:1px solid #e0e0e0;">
    <div style="display:flex;justify-content:space-between;align-items:baseline;"><div style="font-size:.8rem;color:#666;">Gasprijs afgelopen 30 dagen</div><div id="gas-range" style="font-size:.75rem;color:#888;"></div></div>
    <div id="gas-chart" style="display:flex;align-items:flex-end;gap:2px;height:70px;margin-top:.5rem;"></div>
  </div>
</div>

Wie veel gas verbruikt, bespaart structureel meer met [isoleren](/posts/dakisolatie-binnenuit-vs-buitenuit-2026/) of een [(hybride) warmtepomp](/posts/beste-hybride-warmtepomp-2026/) dan met overstappen alleen.

## Zonverwachting: verwachte opbrengst zonnepanelen

Hoeveel leveren je zonnepanelen vandaag en de komende dagen op? Onderstaande verwachting is gebaseerd op de instralings-forecast van Open-Meteo (De Bilt). De opbrengst-indicatie is een **modelberekening**: instraling × performance ratio 0,85 — de werkelijke opbrengst hangt af van oriëntatie, hellingshoek en schaduw.

<div id="zon-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div id="zon-dagen" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.8rem;"><span style="color:#666;font-size:.9rem;">laden…</span></div>
  <p style="color:#666;font-size:.85rem;margin-top:.8rem;">Voorbeeld: bij een installatie van 4 kWp is de verwachte dagopbrengst 4 × het getal per kWp. Bron: Open-Meteo instraling-forecast; opbrengst = modelberekening (PR 0,85).</p>
</div>

Wil je weten wat dit voor jóúw installatie betekent? Gebruik de [opbrengst-calculator](/zonnepanelen-opbrengst-berekenen/) — aantal panelen en oriëntatie invullen, en je ziet de verwachting per dag.

Op zonnige middagen drukt al die zonnestroom de beursprijs — vaak tot onder nul. Wat dat betekent (en wanneer je echt geld toe krijgt) staat op [negatieve stroomprijzen](/negatieve-stroomprijzen/). Precies dan loont een [thuisbatterij bij een dynamisch contract](/posts/dynamische-energiecontracten-thuisbatterij-2026/): overdag goedkoop (of met toeslag) laden, in de avondpiek gebruiken.

<script>
fetch('https://beheer.wtdigital.nl/api/public/gasprijs?historie=30').then(function(r){return r.json();}).then(function(d){
  if (typeof d.prijs_m3 === 'number') document.getElementById('gas-prijs').textContent = '€ ' + d.prijs_m3.toFixed(3);
  var h = d.historie || [];
  if (h.length > 1) {
    var ps = h.map(function(x){return x.prijs_m3;});
    var min = Math.min.apply(null, ps), max = Math.max.apply(null, ps), span = (max - min) || 1;
    document.getElementById('gas-range').textContent = 'laagste € ' + min.toFixed(2) + ' — hoogste € ' + max.toFixed(2);
    document.getElementById('gas-chart').innerHTML = h.map(function(x){
      var hh = 15 + ((x.prijs_m3 - min) / span) * 85;
      var k = x.prijs_m3 === min ? '#1a7a4a' : (x.prijs_m3 === max ? '#b03a3a' : '#c9803f');
      return '<div title="' + x.datum + ' — € ' + x.prijs_m3.toFixed(3) + '/m³" style="flex:1;height:' + hh.toFixed(0) + '%;background:' + k + ';border-radius:2px 2px 0 0;min-width:3px;"></div>';
    }).join('');
  }
}).catch(function(){ document.getElementById('gas-prijs').textContent = 'n.b.'; });
fetch('https://beheer.wtdigital.nl/api/public/zonverwachting').then(function(r){return r.json();}).then(function(d){
  if (!d.dagen || !d.dagen.length) return;
  var namen = ['Vandaag', 'Morgen', 'Overmorgen'];
  document.getElementById('zon-dagen').innerHTML = d.dagen.map(function(dag, i){
    var zonScore = dag.opbrengst_kwh_per_kwp >= 4 ? '☀️☀️☀️' : (dag.opbrengst_kwh_per_kwp >= 2.5 ? '☀️☀️' : '☀️');
    return '<div style="background:#fff;border-radius:8px;padding:.8rem;border:1px solid #e0e0e0;">' +
      '<div style="font-size:.8rem;color:#666;">' + (namen[i] || dag.datum) + ' ' + zonScore + '</div>' +
      '<div style="font-size:1.4rem;font-weight:700;">' + dag.opbrengst_kwh_per_kwp.toFixed(1) + ' kWh</div>' +
      '<div style="font-size:.75rem;color:#888;">per kWp · ' + dag.zonuren.toFixed(1) + ' zonuren</div></div>';
  }).join('');
}).catch(function(){ document.getElementById('zon-dagen').innerHTML = '<span style="color:#666;font-size:.9rem;">Kon verwachting niet laden.</span>'; });
</script>

## Van kale beursprijs naar wat jij betaalt

De prijzen hierboven zijn de **kale inkoopprijzen** van de stroombeurs. Je leverancier telt daar per kWh bij op:

1. **Energiebelasting** — een vast wettelijk bedrag per kWh (jaarlijks opnieuw vastgesteld door de overheid; zie de actuele tarieven bij de Belastingdienst)
2. **Inkoopvergoeding** — de opslag van je leverancier, doorgaans één tot enkele centen per kWh, verschilt per aanbieder
3. **Vaste leveringskosten en netbeheerkosten** — per maand, los van je verbruik

De kale prijs bepaalt dus je *besparingskansen* (verschuiven naar goedkope uren), maar vergelijk aanbieders altijd op de totale opbouw. In onze [vergelijking van dynamische energiecontracten](/posts/dynamische-energiecontracten-vergelijking-2026/) zetten we de aanbieders naast elkaar; wie een thuisbatterij overweegt om op deze uurverschillen te handelen, vindt het rekenmodel in [dynamisch contract + thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

<a href="https://go.duurzaamthuislab.nl/frank-energie?ref=/stroomprijzen/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk Frank Energie (dynamisch contract) →</a>

## Deze prijzen op jouw website?

Wij bieden een gratis embed-widget met de actuele uurprijzen — handig voor blogs, VvE-sites of installateurs. De embed-code staat op de [embed-pagina](/embed-codes/); de enige voorwaarde is dat de bronvermelding blijft staan.

## Veelgestelde vragen

**Waarom zijn de morgenprijzen er pas rond 15:00?**
De day-ahead-veiling van de EPEX-beurs sluit rond het middaguur; de uitslag voor de volgende dag wordt in de loop van de middag gepubliceerd.

**Zijn dit de prijzen van mijn leverancier?**
Bijna: alle dynamische leveranciers gebruiken dezelfde beursprijzen, maar tellen er hun eigen inkoopvergoeding en de energiebelasting bij op. De úúrpatronen (goedkoop/duur) zijn wel identiek.

**Hoe komt de gasprijs tot stand?**
De dagprijs volgt de gasbeurs (LEBA/TTF-day-ahead). Dynamische leveranciers geven die één-op-één door met een vaste opslag; bij vaste contracten zit het beursrisico in het tarief verwerkt.

**Wat betekent "opbrengst per kWp"?**
kWp is het piekvermogen van je installatie. Heb je bijvoorbeeld 10 panelen van 400 Wp (= 4 kWp) en staat er 3,0 kWh per kWp, dan is de verwachte dagopbrengst circa 12 kWh — bij gemiddelde oriëntatie en zonder schaduw (modelberekening).

**Wat is de beste tijd om de wasmachine aan te zetten?**
Met een dynamisch contract: het goedkoopste 2-uursblok van de dag — dat staat live (met het blok van morgen) op [beste tijd wasmachine](/beste-tijd-wasmachine/). Met een vast contract maakt het tijdstip voor je kWh-prijs niet uit.

**Wanneer is stroom meestal het goedkoopst?**
Structureel rond het middaguur op zonnige dagen (veel zonnestroom) en 's nachts; het duurst in de ochtend- en avondpiek. Uitzonderingen komen voor — daarom staat deze pagina er.
