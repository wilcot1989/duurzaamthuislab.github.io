---
title: "Gasprijs vandaag per m³ (live) + verwachting morgen"
description: "De actuele gasprijs per m³ van vandaag en morgen, plus een grafiek van de afgelopen 30 dagen — rechtstreeks uit de day-ahead-beursdata (LEBA/TTF)."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
faq:
- q: 'Wat is de gasprijs vandaag per m³?'
  a: 'Die staat live bovenaan deze pagina, automatisch bijgewerkt uit de beursdata. Let op wat het getal is: de kale day-ahead-beursprijs inclusief btw. Wat jij per m³ aan je leverancier betaalt, is dat bedrag plus de energiebelasting en de inkoopvergoeding — dus altijd hoger.'
- q: 'Wat is de gasprijs verwachting?'
  a: 'De enige harde prijs vooruit is de day-ahead-prijs van morgen, en die staat bovenaan zodra hij gepubliceerd is. Verder vooruit doen wij geen voorspellingen: vulgraden van de opslagen, temperatuur, LNG-aanvoer en geopolitiek bepalen de prijs, en die zijn niet betrouwbaar te voorspellen.'
- q: 'Waarom staat de prijs voor morgen er nog niet?'
  a: 'De day-ahead-prijs voor de volgende gasdag komt in de loop van de dag beschikbaar. Staat er nog niets, kom dan later op de dag terug — de pagina haalt de data bij elk bezoek opnieuw op.'
- q: 'Waarom heeft gas één prijs per dag en stroom een prijs per uur?'
  a: 'De gasdag is de handelseenheid op de day-ahead-gasmarkt: één afrekenprijs van 06:00 tot 06:00. Stroom wordt per uur verhandeld, omdat vraag en aanbod van elektriciteit binnen de dag sterk wisselen. Verbruik verschuiven binnen de dag heeft bij gas dus geen prijseffect; bij stroom wel — zie [stroomprijzen](/stroomprijzen/).'
lastmod: 2026-08-20
---

*Disclosure: de aanbieders die op deze pagina genoemd of gelinkt worden, zijn gewone verwijzingen: wij hebben met hen geen affiliate- of commissierelatie en ontvangen niets als je daar een contract afsluit. Komt er wel een samenwerking, dan passen wij deze regel aan en markeren we de betreffende links als zodanig. De prijzen op deze pagina komen rechtstreeks uit de gasbeursdata en worden door geen enkele partij beïnvloed.*

> **Kort antwoord:** de gasprijs die je hierboven ziet, is de kale day-ahead-beursprijs per m³ inclusief btw — één prijs voor de hele gasdag (06:00 tot 06:00), en zodra de veiling die publiceert ook de prijs van morgen. Wat jij aan je leverancier betaalt, is dat bedrag plus de energiebelasting (2026: €0,60066/m³ excl. btw = €0,7268 incl. btw, schijf 1, bron: Belastingdienst-tarieventabel) plus diens inkoopvergoeding. Verder vooruit dan morgen geven wij geen verwachting: dat zou een aanname zijn, geen prijs.

Op deze pagina staat de **gasprijs van vandaag per m³** en, zodra die gepubliceerd is, de dagprijs van morgen. Het gaat om de kale day-ahead-beursprijs (LEBA/TTF) inclusief btw: precies het tarief waarop dynamische gascontracten van aanbieders als Frank Energie, Tibber, Zonneplan en ANWB Energie zijn gebaseerd.

<div id="gp-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:.8rem;">
    <div style="background:#fff;border-radius:8px;padding:1rem;border:1px solid #e0e0e0;">
      <div style="font-size:.8rem;color:#666;">🔥 Gasprijs vandaag</div>
      <div id="gp-vandaag" style="font-size:2rem;font-weight:700;line-height:1.2;">—</div>
      <div id="gp-datum-vandaag" style="font-size:.75rem;color:#888;">per m³, kaal incl. btw</div>
    </div>
    <div style="background:#fff;border-radius:8px;padding:1rem;border:1px solid #e0e0e0;">
      <div style="font-size:.8rem;color:#666;">Morgen</div>
      <div id="gp-morgen" style="font-size:2rem;font-weight:700;line-height:1.2;">—</div>
      <div id="gp-verschil" style="font-size:.75rem;color:#888;">per m³, kaal incl. btw</div>
    </div>
  </div>
  <label style="display:flex;align-items:center;gap:.4rem;color:#444;font-size:.9rem;cursor:pointer;margin-top:.8rem;"><input type="checkbox" id="gp-belasting" onchange="gpRender()"> + energiebelasting (€0,727/m³ incl. btw, 2026)</label>
  <p style="color:#666;font-size:.85rem;margin-top:.8rem;margin-bottom:0;">Standaard tonen we de kale day-ahead-prijs (LEBA/TTF) incl. btw. Met het vinkje tellen we de energiebelasting 2026 erbij op (€0,60066/m³ excl. btw = €0,7268 incl. btw, schijf 1, bron: Belastingdienst-tarieventabel) — dat benadert wat je leverancier rekent; alleen diens inkoopvergoeding komt daar nog bovenop. Bron: EnergyZero. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

Anders dan bij stroom kent gas **één prijs per dag**. Die gaat om 06:00 in en geldt tot 06:00 de volgende ochtend. Er zijn dus geen goedkope en dure uren zoals bij [dynamische stroomprijzen](/stroomprijzen/) — verbruik verschuiven binnen de dag levert bij gas niets op.

## Gasprijs afgelopen 30 dagen

<div id="gp-hist" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:.5rem;">
    <div style="font-size:.9rem;color:#444;font-weight:600;">Dagprijs per m³</div>
    <div id="gp-range" style="font-size:.8rem;color:#888;"></div>
  </div>
  <div id="gp-chart" style="display:flex;align-items:flex-end;gap:2px;height:140px;margin-top:.8rem;"></div>
  <div id="gp-as" style="display:flex;justify-content:space-between;color:#888;font-size:.8rem;margin-top:.3rem;"></div>
  <p style="color:#666;font-size:.85rem;margin-top:.8rem;margin-bottom:0;">Kale day-ahead-prijs (LEBA/TTF) incl. btw, excl. energiebelasting en inkoopvergoeding. Bron: EnergyZero. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

## Wat komt er bovenop?

<div style="background:#fff;border:1px solid #e0e0e0;border-radius:12px;padding:1.25rem;margin:1.5rem 0;">
  <div style="font-weight:600;margin-bottom:.6rem;">Van kale beursprijs naar je rekening</div>
  <ul style="margin:0;padding-left:1.2rem;line-height:1.7;">
    <li><strong>Energiebelasting</strong> — een wettelijk vastgesteld bedrag per m³ dat de overheid jaarlijks opnieuw bepaalt. De actuele tarieven staan bij de Belastingdienst.</li>
    <li><strong>Inkoopvergoeding van je leverancier</strong> — de opslag per m³ die je aanbieder rekent; die verschilt per leverancier en staat in je contractvoorwaarden.</li>
    <li><strong>Vaste leveringskosten en netbeheerkosten</strong> — per maand, los van hoeveel gas je verbruikt.</li>
  </ul>
</div>

Het bedrag dat jij per m³ betaalt is dus altijd hoger dan de beursprijs hierboven. Wil je aanbieders vergelijken, doe dat op de totale opbouw — kale prijs plus opslag plus vaste kosten — en niet op één van die onderdelen los.

## Hoe komt de gasprijs tot stand?

Gas wordt verhandeld op de groothandelsmarkt, met TTF (Title Transfer Facility) als prijsreferentie voor Noordwest-Europa. Daar kopen leveranciers in, onder andere op de **day-ahead-markt**: de handel voor levering van morgen. Uit die handel rolt één afrekenprijs per gasdag, van 06:00 tot 06:00.

Dynamische leveranciers geven die dagprijs één-op-één door met hun vaste opslag en de energiebelasting erbij. Bij een vast contract koopt je leverancier vooraf in en zit het prijsrisico verwerkt in je tarief — de dagelijkse beursbeweging zie je dan niet terug op je rekening.

## Gasprijs verwachting

Dit is de vraag die het vaakst gesteld wordt, en het eerlijke antwoord valt in twee delen.

**Wat wél een verwachting is:** de day-ahead-prijs van morgen. Die staat bovenaan deze pagina zodra hij gepubliceerd is, en dat is de enige harde prijs vooruit die er bestaat — vastgesteld door de markt, niet geschat.

**Wat geen verwachting is:** alles daarna. Wij doen geen prijsvoorspellingen, om de simpele reden dat niemand de gasprijs betrouwbaar kan voorspellen. De factoren die de prijs bepalen zijn deels onvoorspelbaar van aard:

- **Vulgraad van de gasopslagen** in Noordwest-Europa. Volle bergingen aan het begin van het stookseizoen dempen prijspieken, lege versterken ze. De actuele vulgraden zijn publiek (GIE/AGSI).
- **Weer en temperatuur.** Gasverbruik voor verwarming is sterk temperatuurafhankelijk; een koude periode trekt vraag en prijs omhoog, een milde winter drukt beide.
- **LNG-aanvoer.** Europa concurreert op de wereldmarkt met Azië om vloeibaar gas. Verschuift de vraag daar, dan merkt de Europese prijs dat.
- **Geopolitiek en aanbodstoringen.** Onderhoud aan velden en terminals, sancties en conflicten kunnen het aanbod plotseling veranderen.

Sites die een gasprijs voor volgend kwartaal beloven, geven je in werkelijkheid een aanname. Wat je wél kunt doen: kiezen op basis van wat je wilt. Zoek je zekerheid en een voorspelbare maandlast, dan past een **vast contract** — je betaalt daarvoor doorgaans een risico-opslag. Wil je de marktprijs volgen, met schommelingen omhoog en omlaag, dan past een **dynamisch contract**. Welke goedkoper uitpakt, weet je pas achteraf.

## Besparen op gas: waar het echt zit

Overstappen verandert je opslag en je vaste kosten. Dat kan de moeite waard zijn, maar het verandert niets aan het aantal kubieke meters dat je huis verstookt — en daar zit de grootste knop.

**Isolatie** werkt het jaar rond, gaat decennia mee en verlaagt je verbruik ongeacht wat de beurs doet. Dak, vloer en glas hebben in de meeste woningen het grootste effect; welke aanpak bij jouw dak past, staat in [dakisolatie van binnenuit of van buitenaf](/posts/dakisolatie-binnenuit-vs-buitenuit-2026/).

Daarna komt de warmtevraag zelf. Een **(hybride) warmtepomp** neemt een deel van je stookbehoefte over met elektriciteit; de modellen en randvoorwaarden staan in [beste hybride warmtepomp](/posts/beste-hybride-warmtepomp-2026/). Let op de wisselwerking: minder gas betekent meer stroom, dus reken beide kanten mee.

Pas als je verbruik op orde is, loont het om het contract onder de loep te nemen. In onze [vergelijker van dynamische energiecontracten](/dynamisch-energiecontract-vergelijken/) staan de aanbieders naast elkaar op opslag en vaste kosten.

<a href="https://go.duurzaamthuislab.nl/frank-energie?ref=/gasprijs/" target="_blank" rel="noopener nofollow" class="cta">Bekijk Frank Energie (dynamisch contract) →</a>

<script>
var gpData = null, gpMorgen = null;
function gpFmt(v){ return '€ ' + v.toFixed(3); }
function gpNlDatum(s){
  var p = String(s).split('-');
  if (p.length !== 3) return s;
  return new Date(Date.UTC(+p[0], +p[1]-1, +p[2])).toLocaleDateString('nl-NL',{timeZone:'UTC',day:'numeric',month:'long'});
}
function gpRender(){
  // Energiebelasting gas 2026 schijf 1: EUR 0,60066/m3 excl. btw = EUR 0,7268 incl. btw (Belastingdienst-tarieventabel)
  var opslag = document.getElementById('gp-belasting').checked ? 0.7268 : 0;
  var d = gpData;
  if (d && typeof d.prijs_m3 === 'number') {
    document.getElementById('gp-vandaag').textContent = gpFmt(d.prijs_m3 + opslag);
    document.getElementById('gp-datum-vandaag').textContent = 'per m³ · ' + gpNlDatum(d.datum) + (opslag ? ' · incl. belasting' : ' · kaal incl. btw');
  }
  var elM = document.getElementById('gp-morgen'), sub = document.getElementById('gp-verschil');
  if (gpMorgen && typeof gpMorgen.prijs_m3 === 'number') {
    elM.style.fontSize = ''; elM.style.fontWeight = '';
    elM.textContent = gpFmt(gpMorgen.prijs_m3 + opslag);
    var basis = 'per m³ · ' + gpNlDatum(gpMorgen.datum);
    if (d && typeof d.prijs_m3 === 'number' && gpMorgen.prijs_m3 !== d.prijs_m3) {
      var diff = gpMorgen.prijs_m3 - d.prijs_m3;
      var op = diff > 0;
      sub.innerHTML = basis + ' · <span style="color:' + (op ? '#b03a3a' : '#1a7a4a') + ';font-weight:600;">' + (op ? '↑' : '↓') + ' ' + gpFmt(Math.abs(diff)) + ' t.o.v. vandaag</span>';
    } else {
      sub.textContent = basis + (d && typeof d.prijs_m3 === 'number' ? ' · gelijk aan vandaag' : '');
    }
  } else if (gpMorgen !== null) {
    elM.style.fontSize = '1rem'; elM.style.fontWeight = '600';
    elM.textContent = 'De prijs voor morgen is nog niet gepubliceerd.';
    sub.textContent = 'kom later op de dag terug';
  }
  var h = (d && d.historie) || [];
  if (h.length > 1) {
    var ps = h.map(function(x){ return x.prijs_m3 + opslag; });
    var min = Math.min.apply(null, ps), max = Math.max.apply(null, ps), span = (max - min) || 1;
    document.getElementById('gp-range').textContent = 'laagste ' + gpFmt(min) + ' — hoogste ' + gpFmt(max);
    document.getElementById('gp-chart').innerHTML = h.map(function(x){
      var v = x.prijs_m3 + opslag;
      var hh = 15 + ((v - min) / span) * 85;
      var k = v === min ? '#1a7a4a' : (v === max ? '#b03a3a' : '#c9803f');
      var lbl = v === min ? 'laagste' : (v === max ? 'hoogste' : '');
      return '<div title="' + gpNlDatum(x.datum) + ' — ' + gpFmt(v) + '/m³' + (lbl ? ' (' + lbl + ')' : '') + '" style="position:relative;flex:1;height:' + hh.toFixed(0) + '%;background:' + k + ';border-radius:2px 2px 0 0;min-width:4px;">' +
        (lbl ? '<span style="position:absolute;bottom:100%;left:50%;transform:translateX(-50%);white-space:nowrap;font-size:.7rem;color:' + k + ';">' + lbl + ' ' + gpFmt(v) + '</span>' : '') + '</div>';
    }).join('');
    document.getElementById('gp-as').innerHTML = '<span>' + gpNlDatum(h[0].datum) + '</span><span>' + gpNlDatum(h[h.length-1].datum) + '</span>';
  }
}
fetch('https://beheer.wtdigital.nl/api/public/gasprijs?historie=30').then(function(r){return r.json();}).then(function(d){
  gpData = d; gpRender();
}).catch(function(){
  document.getElementById('gp-vandaag').textContent = 'n.b.';
  document.getElementById('gp-range').textContent = 'Kon de gasprijzen niet laden — probeer het later opnieuw.';
});
fetch('https://beheer.wtdigital.nl/api/public/gasprijs?dag=morgen').then(function(r){return r.json();}).then(function(d){
  gpMorgen = d; gpRender();
}).catch(function(){
  gpMorgen = {}; gpRender();
});
</script>
