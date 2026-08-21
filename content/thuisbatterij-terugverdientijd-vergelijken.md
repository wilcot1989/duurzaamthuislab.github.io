---
title: "Terugverdientijd thuisbatterij per merk en model vergelijken"
description: "Terugverdientijd van Sessy, HomeWizard, EcoFlow STREAM en Zendure naast elkaar — doorgerekend op ons eigen archief van dynamische uurprijzen. Benuttingsfactor zelf instelbaar."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
faq:
- q: 'Waarom komt de terugverdientijd hier hoger uit dan bij de fabrikant?'
  a: 'Omdat wij alleen de handelsopbrengst rekenen, met de spread uit ons eigen archief en een benutting van 70%. Verkooprekenvoorbeelden tellen vaak ook de waarde van opgeslagen zonnestroom mee, rekenen met een hogere benutting en soms met een hogere spread. Beide kunnen kloppen — het verschil zit in de aannames, niet in de rekenkunde.'
- q: 'Kan ik de prijzen in de tabel zomaar naast elkaar leggen?'
  a: 'Nee, en daarom staat er per rij een voetnoot. De prijzen van Sessy, EcoFlow, HomeWizard en Zendure zijn exclusief installatie. Wil je echt appels met appels vergelijken, tel dan je eigen installatiekosten erbij op.'
- q: 'Waarom staat Zonneplan niet in de tabel?'
  a: 'Omdat de tabel een prijs nodig heeft en Zonneplan die niet publiceert. Op zonneplan.nl/thuisbatterij staat per 21-8-2026 geen prijslijst meer: je krijgt een persoonlijk voorstel. Zonder gepubliceerde prijs kunnen wij geen terugverdientijd berekenen die je kunt narekenen. Heb je zelf een voorstel binnen, gebruik dan de generieke rekentool en vul je eigen bedrag in.'
- q: 'Is een kleine plug-in-batterij dan altijd de beste keuze?'
  a: 'Op terugverdientijd per euro scoort een goedkope plug-in-batterij vaak gunstig, maar met 2 kWh dek je je avondpiek niet en kun je nauwelijks zonnestroom opslaan. De vraag is dus niet alleen wat het snelst is terugverdiend, maar ook hoeveel van je verbruik je wilt afdekken. Voor de keuze op basis van je eigen profiel is de [generieke rekentool](/terugverdientijd-thuisbatterij/) plus de [installateurskeuze](/installateur-kiezen/) het betere vertrekpunt.'
lastmod: 2026-08-20
---

*Disclosure: gemengd. Met EcoFlow hebben wij een affiliate-relatie via AWIN — koop je via onze EcoFlow-link, dan ontvangen wij mogelijk een commissie (kost jou niets extra). Met Zendure en HomeWizard hebben wij sinds augustus 2026 ook een affiliate-relatie (Daisycon). De verwijzingen naar Sessy en Zonneplan zijn gewone links zonder commissie. Op de berekening hieronder heeft dat geen invloed: die gebruikt alleen de vendorprijzen en onze eigen prijsdata.*

Elke fabrikant rekent zijn eigen terugverdientijd voor, met zijn eigen aannames. Wij doen het omgekeerd: **één model, één prijsbron, alle merken door dezelfde formule.** De prijsspread komt uit ons eigen archief van dynamische uurprijzen — dat is dezelfde spread voor elk merk, dus de verschillen in de tabel komen puur uit capaciteit, prijs en rendement.

## Het korte antwoord

- De motor van het rendement is de **dagelijkse prijsspread**: het verschil tussen het goedkoopste en het duurste uur van de dag. In ons archief van het afgelopen jaar is dat gemiddeld het bedrag dat je hieronder als kerncijfer ziet staan.
- Bij gelijke spread wint het model met de **laagste prijs per kWh capaciteit**. Kleine plug-in-batterijen (Zendure, EcoFlow STREAM) staan daarin gunstig; grote vaste systemen kosten meer per kWh maar dekken je avondpiek beter.
- De prijzen in de tabel zijn **inclusief btw, exclusief installatie**; per model staat de basis en de bron erbij. Aanbieders die geen prijs publiceren — zoals Zonneplan, dat per 21-8-2026 alleen nog een persoonlijk voorstel doet — staan niet in de tabel, omdat de terugverdientijd dan niet na te rekenen is.
- Zonder **dynamisch energiecontract** is de uitkomst nul: er is dan geen prijsverschil om op te handelen.

Wil je met je eigen offertebedrag en eigen aannames rekenen (cycli, degradatie, eigen spread)? Gebruik dan de [generieke terugverdientijd-rekentool](/terugverdientijd-thuisbatterij/) — daar staat ook de volledige uitleg over degradatie, cycli en de opbrengst van eigen zonnestroom. Deze pagina is de per-model-variant: vaste vendorprijzen, één schuif.

<div id="mvt-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div id="mvt-kern" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;margin-bottom:1.2rem;">
    <span style="color:#666;font-size:.9rem;">archief laden…</span>
  </div>
  <div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.9rem;margin-bottom:1.2rem;">
    <label for="mvt-benut" style="display:block;font-weight:600;margin-bottom:.3rem;">Benuttingsfactor: <span id="mvt-benut-waarde">70%</span></label>
    <input id="mvt-benut" type="range" min="40" max="100" step="5" value="70" oninput="mvtReken()" style="width:100%;">
    <div style="display:flex;justify-content:space-between;font-size:.75rem;color:#888;"><span>40% (voorzichtig)</span><span>100% (volle spread elke dag)</span></div>
    <p style="font-size:.82rem;color:#666;margin:.6rem 0 0;">Welk deel van de volle dagspread je gemiddeld daadwerkelijk pakt. 100% zou betekenen: elke dag van het jaar volledig laden op het goedkoopste uur en volledig ontladen op het duurste. Dat haalt niemand — vandaar de modelaanname van 70%. Schuif zelf om te zien hoe gevoelig de uitkomst is.</p>
  </div>
  <div id="mvt-tabel" style="overflow-x:auto;"></div>
  <p style="color:#666;font-size:.85rem;margin-top:.9rem;"><strong>Modelberekening op ons eigen prijsarchief — geen voorspelling en geen garantie.</strong> De werkelijke opbrengst hangt af van sturing, contract en verbruiksprofiel. Deze berekening bevat alleen handelsopbrengst (laden goedkoop, ontladen duur); opslag van eigen zonnestroom, degradatie, rente en installatiekosten die niet in de prijsbasis zitten, zijn níet meegerekend. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

<script>
var mvtModellen = [
  { merk: 'Zendure',    naam: 'SolarFlow 800 Plus', cap: 1.92, prijs: 549,  rte: 0.85, basis: 'excl',  bron: 'zendure.nl',      noot: 'Plug-in-systeem, uit te breiden met extra accu’s.' },
  { merk: 'EcoFlow',    naam: 'STREAM AC Pro',      cap: 1.92, prijs: 749,  rte: 0.85, basis: 'excl',  bron: 'nl.ecoflow.com',  noot: 'Plug-in, modulair uit te breiden.', aff: true },
  { merk: 'EcoFlow',    naam: 'STREAM Ultra X',     cap: 3.84, prijs: 1199, rte: 0.85, basis: 'excl',  bron: 'nl.ecoflow.com',  noot: 'Dubbele capaciteit van de AC Pro.', aff: true },
  { merk: 'EcoFlow',    naam: 'STREAM AC',          cap: 5.02, prijs: 1599, rte: 0.85, basis: 'excl',  bron: 'nl.ecoflow.com',  noot: 'Grootste STREAM-variant.', aff: true },
  { merk: 'HomeWizard', naam: 'Plug-In Battery',    cap: 2.70, prijs: 1195, rte: 0.85, basis: 'excl',  bron: 'homewizard.com',  noot: 'Laad- en ontlaadvermogen 800 W — een volle cyclus duurt dus ruim 3 uur per richting.' },
  { merk: 'Sessy',      naam: '5 kWh',              cap: 5,    prijs: 3550, rte: 0.85, basis: 'excl',  bron: 'sessy.nl',        noot: 'Bruikbare capaciteit ≈ nominaal, rendement 85% (sessy.nl/specificaties).' },
  { merk: 'Sessy',      naam: '10 kWh',             cap: 10,   prijs: 5500, rte: 0.85, basis: 'excl',  bron: 'sessy.nl',        noot: 'Bruikbare capaciteit ≈ nominaal, rendement 85%.' },
  { merk: 'Sessy',      naam: 'Plus 15 kWh',        cap: 15,   prijs: 9400, rte: 0.85, basis: 'excl',  bron: 'sessy.nl',        noot: 'Bruikbare capaciteit ≈ nominaal, rendement 85%.' }
  // Zonneplan staat niet in deze lijst: zonneplan.nl/thuisbatterij publiceert per 21-8-2026 geen prijslijst
  // meer (route = persoonlijk voorstel). Zonder gepubliceerde prijs is er geen na te rekenen terugverdientijd.
];

var mvtBasisLabel = {
  excl: { code: '1', tekst: 'incl. btw, <strong>exclusief</strong> installatie' },
  btw:  { code: '2', tekst: '<strong>na btw-teruggave, inclusief</strong> installatie' }
};

var mvtSpread = null, mvtDagen = 0, mvtNegUren = 0;

function mvtEuro(v, dec){
  return '€ ' + v.toLocaleString('nl-NL', { minimumFractionDigits: dec, maximumFractionDigits: dec });
}

function mvtReken(){
  var benut = parseInt(document.getElementById('mvt-benut').value, 10) / 100;
  document.getElementById('mvt-benut-waarde').textContent = Math.round(benut * 100) + '%';
  var tab = document.getElementById('mvt-tabel');
  if (mvtSpread === null){ tab.innerHTML = '<p style="color:#666;font-size:.9rem;">Wachten op het prijsarchief…</p>'; return; }

  var rijen = mvtModellen.map(function(m){
    // Jaaropbrengst = capaciteit x round-trip-rendement x gemiddelde dagspread x 365 x benuttingsfactor
    var jaar = m.cap * m.rte * mvtSpread * 365 * benut;
    var tvt  = jaar > 0 ? m.prijs / jaar : null;
    return { m: m, jaar: jaar, tvt: tvt, perKwh: m.prijs / m.cap };
  }).sort(function(a, b){ return a.tvt - b.tvt; });

  var beste = rijen[0].tvt;
  var html = '<table style="width:100%;border-collapse:collapse;font-size:.9rem;background:#fff;border:1px solid #e0e0e0;border-radius:8px;min-width:640px;">' +
    '<thead><tr style="background:#f1f3f5;text-align:left;">' +
    '<th style="padding:.5rem .6rem;">Model</th>' +
    '<th style="padding:.5rem .6rem;">Capaciteit</th>' +
    '<th style="padding:.5rem .6rem;">Prijs</th>' +
    '<th style="padding:.5rem .6rem;">€/kWh</th>' +
    '<th style="padding:.5rem .6rem;">Opbrengst/jaar</th>' +
    '<th style="padding:.5rem .6rem;">Terugverdientijd</th></tr></thead><tbody>';

  rijen.forEach(function(r){
    var kleur = r.tvt === beste ? '#1a7a4a' : (r.tvt > 15 ? '#b03a3a' : '#0e7490');
    var basis = mvtBasisLabel[r.m.basis];
    html += '<tr>' +
      '<td style="padding:.45rem .6rem;border-bottom:1px solid #eee;"><strong>' + r.m.merk + '</strong> ' + r.m.naam + '</td>' +
      '<td style="padding:.45rem .6rem;border-bottom:1px solid #eee;">' + r.m.cap.toLocaleString('nl-NL') + ' kWh</td>' +
      '<td style="padding:.45rem .6rem;border-bottom:1px solid #eee;">' + mvtEuro(r.m.prijs, 0) + ' <sup style="color:#0e7490;">' + basis.code + '</sup></td>' +
      '<td style="padding:.45rem .6rem;border-bottom:1px solid #eee;">' + mvtEuro(r.perKwh, 0) + '</td>' +
      '<td style="padding:.45rem .6rem;border-bottom:1px solid #eee;">' + mvtEuro(r.jaar, 0) + '</td>' +
      '<td style="padding:.45rem .6rem;border-bottom:1px solid #eee;font-weight:700;color:' + kleur + ';">' + r.tvt.toFixed(1).replace('.', ',') + ' jaar</td>' +
      '</tr>' +
      '<tr><td colspan="6" style="padding:0 .6rem .5rem;border-bottom:1px solid #eee;font-size:.78rem;color:#888;">Rendement ' + Math.round(r.m.rte * 100) + '% · prijs ' + basis.tekst.replace(/<\/?strong>/g, '') + ' · bron ' + r.m.bron + ' · ' + r.m.noot + '</td></tr>';
  });

  html += '</tbody></table>' +
    '<p style="font-size:.8rem;color:#666;margin:.7rem 0 0;"><sup style="color:#0e7490;">1</sup> ' + mvtBasisLabel.excl.tekst + ' — installatie of een slimme meter-koppeling komt er nog bij. Prijspeil augustus 2026, vendorprijzen; controleer altijd de actuele prijs bij de leverancier. Aanbieders zonder gepubliceerde prijs (Zonneplan, gecontroleerd 21-8-2026) staan niet in de tabel.</p>';
  tab.innerHTML = html;
}

fetch('https://beheer.wtdigital.nl/api/public/energie-archief?dagen=365')
  .then(function(r){ return r.json(); })
  .then(function(d){
    var dagen = (d.dagen || []).filter(function(x){ return typeof x.stroom_max === 'number' && typeof x.stroom_min === 'number'; });
    if (!dagen.length) throw new Error('geen data');
    // Gemiddelde dagspread = gemiddelde van (hoogste uurprijs - laagste uurprijs) over alle dagen met data
    var som = dagen.reduce(function(a, x){ return a + (x.stroom_max - x.stroom_min); }, 0);
    mvtSpread  = som / dagen.length;
    mvtDagen   = dagen.length;
    mvtNegUren = (d.dagen || []).reduce(function(a, x){ return a + (x.stroom_negatieve_uren || 0); }, 0);
    document.getElementById('mvt-kern').innerHTML =
      '<div style="background:#fff;border-radius:8px;padding:.8rem;border:1px solid #e0e0e0;"><div style="font-size:.8rem;color:#666;">Gem. dagspread</div><div style="font-size:1.4rem;font-weight:700;color:#0e7490;">€ ' + mvtSpread.toFixed(3).replace('.', ',') + '</div><div style="font-size:.75rem;color:#888;">per kWh, hoogste min laagste uur</div></div>' +
      '<div style="background:#fff;border-radius:8px;padding:.8rem;border:1px solid #e0e0e0;"><div style="font-size:.8rem;color:#666;">Dagen data</div><div style="font-size:1.4rem;font-weight:700;">' + mvtDagen + '</div><div style="font-size:.75rem;color:#888;">eigen archief</div></div>' +
      '<div style="background:#e8f5ee;border-radius:8px;padding:.8rem;border:1px solid #b7dfc9;"><div style="font-size:.8rem;color:#1a7a4a;">Negatieve uren</div><div style="font-size:1.4rem;font-weight:700;color:#1a7a4a;">' + mvtNegUren + '</div><div style="font-size:.75rem;color:#1a7a4a;">afgelopen jaar</div></div>';
    mvtReken();
  })
  .catch(function(){
    document.getElementById('mvt-kern').innerHTML = '<span style="color:#b03a3a;font-size:.9rem;">Kon het prijsarchief niet laden — probeer het later opnieuw.</span>';
    document.getElementById('mvt-tabel').innerHTML = '';
  });
mvtReken();
</script>

## Hoe deze berekening is opgebouwd

De formule staat expres in één regel, zodat je hem kunt narekenen:

**Jaaropbrengst = capaciteit (kWh) × round-trip-rendement × gemiddelde dagspread (€/kWh) × 365 × benuttingsfactor**
**Terugverdientijd = aanschafprijs ÷ jaaropbrengst**

De vier onderdelen:

1. **Capaciteit** — de bruikbare capaciteit uit de vendorspecificatie. Voor Sessy geldt dat bruikbaar ongeveer gelijk is aan nominaal (sessy.nl/specificaties).
2. **Round-trip-rendement** — 85% voor alle modellen in de tabel, de waarde die onder andere Sessy in zijn specificaties noemt. Dat is een vendoropgave, geen meting van ons.
3. **Gemiddelde dagspread** — het gemiddelde van (duurste uur − goedkoopste uur) over alle dagen in ons archief van day-ahead-uurprijzen. Dit is de kale beursprijs inclusief btw, dezelfde data als op onze [stroomprijzen-pagina](/stroomprijzen/) en in de [historie](/stroomprijzen-historie/).
4. **Benuttingsfactor** — de modelaanname (standaard 0,7) die uitdrukt dat je niet elke dag de volle spread pakt.

Wat er *niet* in zit: degradatie, rente, HEMS- of installatiekosten die buiten de prijsbasis vallen, en de opbrengst van het opslaan van eigen zonnestroom. Die laatste is voor veel huishoudens een aparte, forse post — hoe je die meerekent staat in [dynamisch energiecontract + thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/) en in de [generieke rekentool](/terugverdientijd-thuisbatterij/).

## Waarom de spread de motor is

Een thuisbatterij verdient met handelen niets aan de hoogte van de stroomprijs, maar aan het **verschil** binnen een dag. Is stroom de hele dag €0,25, dan levert laden en ontladen door het rendementsverlies zelfs geld op kosten. Is het 's nachts €0,10 en in de avondpiek €0,35, dan is die 25 cent per kWh je brutomarge.

Daarom zie je in de tabel dat alle merken bij dezelfde spread in dezelfde orde van grootte eindigen: de spread is voor iedereen gelijk, dus wat overblijft is de prijs per kWh capaciteit. En daarom is de spread ook de onzekerste variabele van het model — hij verschilt per seizoen en per jaar. Ons archief laat het afgelopen jaar zien, geen voorspelling van het volgende.

De negatieve uren in het kerncijfer zijn hierbij het interessante detail: op die uren krijg je geld toe om te laden. Wat dat precies betekent staat op [negatieve stroomprijzen](/negatieve-stroomprijzen/).

## Waarom de benutting nooit 100% is

De schuif staat standaard op 70%, en dat is optimistisch bedoeld noch pessimistisch — het is een aanname met vier redenen erachter:

- **Vlakke dagen.** Op dagen met te weinig spread is een cyclus verlieslatend; een goede sturing slaat die over. Dat kost cycli, maar voorkomt verlies.
- **Vermogenslimiet.** Een batterij die met 800 W laadt (zoals de HomeWizard Plug-In Battery) heeft ruim drie uur nodig voor een volle lading. Het goedkoopste *uur* is dan niet genoeg; je laadt over meerdere, gemiddeld duurdere uren.
- **Voorspelfouten.** De sturing kiest de uren vooraf op basis van de day-ahead-prijzen. Dat gaat vaak goed, maar niet altijd optimaal.
- **Andere prioriteiten.** Staat de batterij al vol met eigen zonnestroom, of houdt hij reserve voor noodstroom, dan is er die dag geen ruimte om te handelen.

Zet de schuif op 100% en je ziet het theoretische plafond; op 40% een voorzichtige ondergrens. Het verschil tussen beide is je risicomarge — geen van beide is een belofte.

## Een dynamisch contract is de voorwaarde

Zonder dynamisch energiecontract is de uitkomst van deze hele tabel nul. Bij een vast tarief betaal je elk uur hetzelfde, dus er valt niets te verdienen aan verschuiven. Alleen bij een uurtarief-contract komt de spread bij jou terecht.

Welke aanbieders een dynamisch contract leveren en wat ze aan vaste kosten en inkoopvergoeding rekenen, staat in onze [vergelijker van dynamische energiecontracten](/dynamisch-energiecontract-vergelijken/). Wil je eerst zien hoe de prijzen zich over langere periodes gedragen, dan is de [prijshistorie](/stroomprijzen-historie/) het startpunt — daar zie je per maand hoe groot de spread was.

## Naar de leveranciers

De verdienende links hieronder zijn die van EcoFlow, Zendure en HomeWizard; de rest zijn gewone verwijzingen zonder commissie.

<a href="https://go.duurzaamthuislab.nl/ecoflow?ref=/thuisbatterij-terugverdientijd-vergelijken/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk EcoFlow STREAM (affiliate) →</a>

<a href="https://go.duurzaamthuislab.nl/sessy?ref=/thuisbatterij-terugverdientijd-vergelijken/" target="_blank" rel="noopener nofollow" class="cta">Bekijk Sessy →</a>

<a href="https://go.duurzaamthuislab.nl/zonneplan?ref=/thuisbatterij-terugverdientijd-vergelijken/" target="_blank" rel="noopener nofollow" class="cta">Bekijk Zonneplan thuisbatterij →</a>

<a href="https://go.duurzaamthuislab.nl/homewizard?ref=/thuisbatterij-terugverdientijd-vergelijken/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk HomeWizard Plug-In Battery →</a>

<a href="https://go.duurzaamthuislab.nl/zendure?ref=/thuisbatterij-terugverdientijd-vergelijken/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk Zendure SolarFlow →</a>

Losse reviews per model: [Sessy](/posts/sessy-review-thuisbatterij-nederland/), [Zonneplan](/posts/zonneplan-thuisbatterij-review-2026/), [Zendure SolarFlow](/posts/zendure-solarflow-review-2026/) en de [vergelijking van 10 kWh-batterijen](/posts/thuisbatterij-10-kwh-vergelijking-2026/).
