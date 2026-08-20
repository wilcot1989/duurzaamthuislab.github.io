---
title: "Dynamische stroomprijzen vandaag en morgen (per uur)"
description: "Actuele dynamische stroomprijzen per uur, vandaag en morgen — kale EPEX-beursprijs incl. btw, automatisch ververst. Zie direct de goedkoopste en duurste uren."
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

## Van kale beursprijs naar wat jij betaalt

De prijzen hierboven zijn de **kale inkoopprijzen** van de stroombeurs. Je leverancier telt daar per kWh bij op:

1. **Energiebelasting** — een vast wettelijk bedrag per kWh (jaarlijks opnieuw vastgesteld door de overheid; zie de actuele tarieven bij de Belastingdienst)
2. **Inkoopvergoeding** — de opslag van je leverancier, doorgaans één tot enkele centen per kWh, verschilt per aanbieder
3. **Vaste leveringskosten en netbeheerkosten** — per maand, los van je verbruik

De kale prijs bepaalt dus je *besparingskansen* (verschuiven naar goedkope uren), maar vergelijk aanbieders altijd op de totale opbouw. In onze [vergelijking van dynamische energiecontracten](/posts/dynamische-energiecontracten-vergelijking-2026/) zetten we de aanbieders naast elkaar; wie een thuisbatterij overweegt om op deze uurverschillen te handelen, vindt het rekenmodel in [dynamisch contract + thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

<a href="https://go.duurzaamthuislab.nl/frank-energie?ref=/stroomprijzen/" target="_blank" rel="noopener nofollow sponsored" class="cta-affiliate" style="display:inline-block;background:#0e7490;color:#fff;padding:.7rem 1.4rem;border-radius:8px;text-decoration:none;font-weight:600;margin:.5rem 0;">Bekijk Frank Energie (dynamisch contract) →</a>

## Veelgestelde vragen

**Waarom zijn de morgenprijzen er pas rond 15:00?**
De day-ahead-veiling van de EPEX-beurs sluit rond het middaguur; de uitslag voor de volgende dag wordt in de loop van de middag gepubliceerd.

**Zijn dit de prijzen van mijn leverancier?**
Bijna: alle dynamische leveranciers gebruiken dezelfde beursprijzen, maar tellen er hun eigen inkoopvergoeding en de energiebelasting bij op. De úúrpatronen (goedkoop/duur) zijn wel identiek.

**Wanneer is stroom meestal het goedkoopst?**
Structureel rond het middaguur op zonnige dagen (veel zonnestroom) en 's nachts; het duurst in de ochtend- en avondpiek. Uitzonderingen komen voor — daarom staat deze pagina er.
