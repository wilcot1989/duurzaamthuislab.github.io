---
title: "Powerstation-calculator: runtime en piekvermogen berekenen (tool)"
description: "Bereken hoe lang een powerstation je apparaten voedt en of het piekvermogen genoeg is. Runtime-calculator plus aanloopstroom-checker met vendor-geverifieerde capaciteiten en continu vermogens."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
faq:
- q: 'Waarom haal ik in de praktijk een kortere runtime dan de tool aangeeft?'
  a: 'De uitkomst is een modelberekening met een vast omvormer-rendement van 0,85. In werkelijkheid speelt meer mee: bij lage belasting verbruikt de omvormer zelf relatief veel (een station dat aan staat met alleen een telefoon eraan, verliest een merkbaar deel aan zichzelf), koude verlaagt de bruikbare capaciteit, en de meeste fabrikanten laten de accu niet volledig leeglopen. Reken op een marge en niet op de exacte uitkomst.'
- q: 'Kan ik een waterkoker of airfryer op een powerstation gebruiken?'
  a: 'Dat hangt volledig af van het continu vermogen, niet van de capaciteit. Een waterkoker van 2.000 W vraagt een model dat minstens 2.000 W continu levert; een R600 (600 W) of een EB70S (800 W) redt dat niet, ongeacht hoe vol de accu is. Vul het echte wattage van het apparaat in blok 1 in en lees in blok 2 af welke modellen het halen.'
- q: 'Wat betekent de aanloopfactor precies, en waar komt hij vandaan?'
  a: 'Het is onze vuistregel-modelaanname voor de inschakelstroom: het wattage van het apparaat maal 3 bij een compressor, maal 2,5 bij elektrisch gereedschap, maal 1 bij elektronica en laders. Het is geen fabrieksopgave en geen meting. De exacte startstroom van jouw apparaat staat op het typeplaatje of in de handleiding; gebruik de factor om te zien of je marge nodig hebt, niet als getal om op te bouwen.'
- q: 'Zijn de vermelde capaciteiten, vermogens en prijzen actueel?'
  a: 'De capaciteiten en continu vermogens komen uit de fabrieksspecificaties, en de prijzen zijn adviesprijzen met peildatum augustus 2026. Waar "zie site" staat, wisselt de prijs te vaak om hier zinvol te noemen. Fabrikanten brengen regelmatig nieuwe generaties uit onder een vrijwel identieke naam — met andere Wh en W. Controleer bij aanschaf altijd de specificatie van de variant die je in je mandje hebt.'
lastmod: 2026-08-20
---

*Disclosure: dit artikel bevat affiliate-links. Voor EcoFlow, ALLPOWERS, Anker SOLIX, Jackery en Bluetti lopen bij ons goedgekeurde partnerprogramma's via het affiliate-netwerk AWIN. Koop je via zo'n link, dan ontvangen wij mogelijk een commissie — dat kost jou niets extra en verandert niets aan de specificaties en berekeningen op deze pagina.*

Twee vragen bepalen of een powerstation bij je past, en ze gaan over verschillende dingen. **Hoeveel wattuur (Wh)** het apparaat heeft, bepaalt hoe *lang* je stroom hebt. **Hoeveel watt (W)** het kan leveren, bepaalt *wat* je erop kunt aansluiten. Een powerstation met 2.000 Wh dat maar 600 W levert, draait je koelbox een weekend lang — maar slaat af zodra je de koffiezetter aanzet.

Hieronder staan twee tools. De eerste rekent de runtime uit, de tweede toetst of het gevraagde vermogen (inclusief aanloopstroom) binnen het continu vermogen van het model past. Beide gebruiken dezelfde apparatenlijst: wat je in blok 1 aanvinkt, rekent blok 2 direct mee.

## Kort antwoord

- **Runtime** ≈ (capaciteit in Wh × 0,85) ÷ het gezamenlijke wattage van je apparaten. Die 0,85 is een gelabelde modelaanname voor omvormerverlies.
- **Wat je aan kunt sluiten** hangt niet af van de Wh maar van het **continu vermogen** in W. Een R600 (600 W) kan geen waterkoker van 1.800 W voeden, ongeacht de accu.
- **Aanloopstroom** is de meestvoorkomende faalmodus: motoren en compressoren (koelkast, koelbox, pomp, boormachine) trekken bij het opstarten kort een veelvoud van hun opgegeven wattage.
- Voor laptops, telefoons, CPAP en een koelbox is capaciteit de bepalende factor. Voor keukenapparaten, gereedschap en alles met een verwarmingselement is dat vermogen.

<div id="pwc-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="font-size:.95rem;font-weight:700;margin-bottom:.9rem;">1. Runtime-calculator</div>

  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.8rem;margin-bottom:.6rem;">
    <label style="font-size:.85rem;color:#555;">Model
      <select id="pwc-model" style="width:100%;margin-top:.3rem;padding:.5rem;border:1px solid #ccc;border-radius:8px;font:inherit;"></select>
    </label>
    <label id="pwc-vrij-wrap" style="font-size:.85rem;color:#555;display:none;">Capaciteit (Wh)
      <input id="pwc-vrij" type="number" min="50" max="30000" step="10" value="1000" style="width:100%;margin-top:.3rem;padding:.5rem;border:1px solid #ccc;border-radius:8px;font:inherit;">
    </label>
    <label id="pwc-vrij-w-wrap" style="font-size:.85rem;color:#555;display:none;">Continu vermogen (W)
      <input id="pwc-vrij-w" type="number" min="50" max="10000" step="50" value="1000" style="width:100%;margin-top:.3rem;padding:.5rem;border:1px solid #ccc;border-radius:8px;font:inherit;">
    </label>
  </div>
  <div id="pwc-modelinfo" style="font-size:.8rem;color:#666;margin-bottom:1.1rem;"></div>

  <div style="font-size:.85rem;color:#555;font-weight:600;margin-bottom:.5rem;">Wat wil je aansluiten? (wattages zijn bewerkbaar)</div>
  <div id="pwc-apparaten" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:.5rem;margin-bottom:.6rem;"></div>
  <p style="color:#666;font-size:.8rem;margin:0 0 1.1rem;">De vooringevulde wattages zijn <strong>voorbeeldwaarden</strong> om mee te beginnen, geen meetwaarden van jouw apparaat. Het echte wattage staat op het typeplaatje of de adapter — vul dat in voor een bruikbare uitkomst.</p>

  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.8rem;">
    <div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;">
      <div style="font-size:.8rem;color:#666;">Gevraagd vermogen</div>
      <div id="pwc-som" style="font-size:1.5rem;font-weight:700;">—</div>
      <div style="font-size:.75rem;color:#888;">som van de aangevinkte apparaten</div>
    </div>
    <div style="background:#e8f5ee;border:1px solid #b7dfc9;border-radius:8px;padding:.8rem;">
      <div style="font-size:.8rem;color:#1a7a4a;">Geschatte runtime</div>
      <div id="pwc-runtime" style="font-size:1.5rem;font-weight:700;">—</div>
      <div id="pwc-runtime-sub" style="font-size:.75rem;color:#1a7a4a;">bij gelijkmatig verbruik</div>
    </div>
    <div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;">
      <div style="font-size:.8rem;color:#666;">Bruikbare energie</div>
      <div id="pwc-bruikbaar" style="font-size:1.5rem;font-weight:700;">—</div>
      <div style="font-size:.75rem;color:#888;">capaciteit × rendement 0,85</div>
    </div>
  </div>

  <p style="color:#666;font-size:.85rem;margin:1rem 0 0;">Rekenregel: runtime = (capaciteit in Wh × <strong>omvormer-rendement 0,85 — modelaanname</strong>) ÷ som van de wattages. Modelberekening met gelabelde aannames — geen garantie. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

<div id="pwc-piek" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="font-size:.95rem;font-weight:700;margin-bottom:.4rem;">2. Piekvermogen- en aanloopstroom-checker</div>
  <p style="color:#666;font-size:.85rem;margin:0 0 1.1rem;">Deze checker gebruikt dezelfde selectie als blok 1. Per apparaattype rekenen we met een <strong>aanloopfactor als vuistregel-modelaanname</strong>: apparaten met een compressor ×3, elektrisch gereedschap ×2,5, al het overige ×1. Werkelijke inschakelstromen verschillen per fabrikant, bouwjaar en of het apparaat een softstart heeft.</p>

  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.8rem;margin-bottom:1rem;">
    <div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;">
      <div style="font-size:.8rem;color:#666;">Benodigd continu</div>
      <div id="pwc-continu" style="font-size:1.5rem;font-weight:700;">—</div>
      <div style="font-size:.75rem;color:#888;">wat het model blijvend moet leveren</div>
    </div>
    <div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;">
      <div style="font-size:.8rem;color:#666;">Benodigde piek</div>
      <div id="pwc-piekw" style="font-size:1.5rem;font-weight:700;">—</div>
      <div id="pwc-piek-sub" style="font-size:.75rem;color:#888;">met aanloopfactor</div>
    </div>
    <div id="pwc-verdict" style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;">
      <div style="font-size:.8rem;color:#666;">Gekozen model</div>
      <div id="pwc-verdict-kop" style="font-size:1.1rem;font-weight:700;">—</div>
      <div id="pwc-verdict-sub" style="font-size:.75rem;color:#888;"></div>
    </div>
  </div>

  <div style="font-size:.85rem;color:#555;font-weight:600;margin-bottom:.5rem;">Alle modellen naast je selectie</div>
  <div id="pwc-tabel" style="display:grid;gap:.35rem;"></div>

  <p style="color:#666;font-size:.85rem;margin:1rem 0 0;">We toetsen op het <strong>continu vermogen</strong> uit de fabrieksspecificatie. Veel powerstations kunnen een piek daarboven kort opvangen, maar hoeveel en hoe lang staat per model in de handleiding — dat nemen we niet aan. Modelberekening met gelabelde aannames — geen garantie. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

<script>
(function(){
  // Capaciteit en continu vermogen: fabrieksspecificaties (peildatum augustus 2026).
  // Prijzen: adviesprijzen augustus 2026; waar leeg staat verwijzen we naar de site van de leverancier.
  var MODELLEN = [
    { id:'ecoflow-delta-2',   naam:'EcoFlow Delta 2',            wh:1024, w:1800, prijs:'€ 599',   merk:'ecoflow' },
    { id:'ecoflow-delta-3',   naam:'EcoFlow Delta 3 Classic',    wh:1024, w:1800, prijs:'€ 549',   merk:'ecoflow' },
    { id:'allpowers-r600',    naam:'ALLPOWERS R600',             wh:299,  w:600,  prijs:'€ 229',   merk:'allpowers' },
    { id:'allpowers-r1500',   naam:'ALLPOWERS R1500',            wh:1152, w:1800, prijs:'€ 569',   merk:'allpowers' },
    { id:'allpowers-r2500',   naam:'ALLPOWERS R2500-V2',         wh:1920, w:2500, prijs:'€ 849',   merk:'allpowers' },
    { id:'jackery-2000plus',  naam:'Jackery Explorer 2000 Plus',  wh:2042, w:3000, prijs:'zie site', merk:'jackery' },
    { id:'anker-c1000',       naam:'Anker SOLIX C1000',          wh:1056, w:1800, prijs:'zie site', merk:'anker-solix' },
    { id:'bluetti-eb70s',     naam:'Bluetti EB70S',              wh:716,  w:800,  prijs:'zie site', merk:'bluetti' }
  ];
  // Aanloopfactoren = vuistregel-modelaannames, geen fabrieksopgave.
  var APPARATEN = [
    { id:'telefoon',  naam:'Telefoon laden',    w:10,   factor:1,   type:'elektronica' },
    { id:'laptop',    naam:'Laptop',            w:60,   factor:1,   type:'elektronica' },
    { id:'koelbox',   naam:'Koelbox (compressor)', w:45, factor:3,  type:'compressor' },
    { id:'tv',        naam:'Televisie',         w:80,   factor:1,   type:'elektronica' },
    { id:'cpap',      naam:'CPAP-apparaat',     w:40,   factor:1,   type:'elektronica' },
    { id:'ebike',     naam:'E-bike-accu laden', w:150,  factor:1,   type:'lader' },
    { id:'koffie',    naam:'Koffiezetapparaat', w:1000, factor:1,   type:'verwarming' },
    { id:'boor',      naam:'Boormachine',       w:600,  factor:2.5, type:'gereedschap' }
  ];

  function nl(x,d){ return x.toLocaleString('nl-NL',{minimumFractionDigits:d,maximumFractionDigits:d}); }
  function uren(h){
    if (!isFinite(h) || h <= 0) return '—';
    if (h >= 100) return nl(Math.round(h),0) + ' uur';
    var u = Math.floor(h), m = Math.round((h - u) * 60);
    if (m === 60) { u += 1; m = 0; }
    return u > 0 ? (u + ' u ' + String(m).padStart(2,'0') + ' min') : (m + ' min');
  }

  var sel = document.getElementById('pwc-model');
  sel.innerHTML = MODELLEN.map(function(m,i){
    return '<option value="' + i + '">' + m.naam + ' — ' + nl(m.wh,0) + ' Wh · ' + nl(m.w,0) + ' W · ' + m.prijs + '</option>';
  }).join('') + '<option value="vrij">Ander model — zelf Wh en W invullen</option>';

  document.getElementById('pwc-apparaten').innerHTML = APPARATEN.map(function(a){
    return '<label style="display:flex;align-items:center;gap:.5rem;background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.5rem .6rem;font-size:.85rem;">' +
      '<input type="checkbox" id="pwc-c-' + a.id + '" data-id="' + a.id + '">' +
      '<span style="flex:1;">' + a.naam + '</span>' +
      '<input type="number" id="pwc-w-' + a.id + '" value="' + a.w + '" min="1" max="5000" step="5" style="width:74px;padding:.3rem;border:1px solid #ccc;border-radius:6px;font:inherit;text-align:right;">' +
      '<span style="color:#888;">W</span></label>';
  }).join('');
  ['laptop','koelbox'].forEach(function(id){ document.getElementById('pwc-c-' + id).checked = true; });

  function huidigModel(){
    if (sel.value === 'vrij') {
      var wh = parseFloat(document.getElementById('pwc-vrij').value);
      var w  = parseFloat(document.getElementById('pwc-vrij-w').value);
      return { naam:'Eigen invoer', wh: wh > 0 ? wh : 0, w: w > 0 ? w : 0, prijs:'', eigen:true };
    }
    return MODELLEN[parseInt(sel.value,10)];
  }

  function reken(){
    var vrij = sel.value === 'vrij';
    document.getElementById('pwc-vrij-wrap').style.display = vrij ? '' : 'none';
    document.getElementById('pwc-vrij-w-wrap').style.display = vrij ? '' : 'none';
    var m = huidigModel();
    document.getElementById('pwc-modelinfo').textContent = vrij
      ? 'Vul de capaciteit en het continu vermogen van je eigen model in — die staan op het typeplaatje of in de handleiding.'
      : m.naam + ': ' + nl(m.wh,0) + ' Wh capaciteit, ' + nl(m.w,0) + ' W continu vermogen (fabrieksspecificatie) · prijsindicatie ' + m.prijs + ' (augustus 2026).';

    var som = 0, piek = 0, aantal = 0, zwaarste = null;
    APPARATEN.forEach(function(a){
      if (!document.getElementById('pwc-c-' + a.id).checked) return;
      var w = parseFloat(document.getElementById('pwc-w-' + a.id).value);
      if (!(w > 0)) return;
      aantal++;
      som += w;
      var p = w * a.factor;
      piek += p;
      if (!zwaarste || p > zwaarste.p) zwaarste = { naam:a.naam, p:p, factor:a.factor };
    });

    var bruikbaar = m.wh * 0.85;
    document.getElementById('pwc-bruikbaar').textContent = m.wh > 0 ? nl(Math.round(bruikbaar),0) + ' Wh' : '—';
    document.getElementById('pwc-som').textContent = aantal ? nl(Math.round(som),0) + ' W' : '—';

    var rt = document.getElementById('pwc-runtime'), rtSub = document.getElementById('pwc-runtime-sub');
    if (!aantal) {
      rt.textContent = '—'; rtSub.textContent = 'vink minstens één apparaat aan';
    } else if (!(m.wh > 0)) {
      rt.textContent = '—'; rtSub.textContent = 'vul een capaciteit in Wh in';
    } else {
      rt.textContent = uren(bruikbaar / som);
      rtSub.textContent = aantal + (aantal === 1 ? ' apparaat' : ' apparaten') + ' · ' + nl(Math.round(som),0) + ' W continu';
    }

    document.getElementById('pwc-continu').textContent = aantal ? nl(Math.round(som),0) + ' W' : '—';
    document.getElementById('pwc-piekw').textContent = aantal ? nl(Math.round(piek),0) + ' W' : '—';
    document.getElementById('pwc-piek-sub').textContent = zwaarste && zwaarste.factor > 1
      ? 'zwaarste aanloop: ' + zwaarste.naam + ' (×' + nl(zwaarste.factor,1).replace(',0','') + ')'
      : 'geen apparaat met aanloopstroom aangevinkt';

    var kop = document.getElementById('pwc-verdict-kop'), sub = document.getElementById('pwc-verdict-sub'), box = document.getElementById('pwc-verdict');
    function stel(kleur,rand,tekst,detail){ box.style.background = kleur; box.style.borderColor = rand; kop.textContent = tekst; sub.textContent = detail; }
    if (!aantal || !(m.w > 0)) {
      stel('#fff','#e0e0e0','—', aantal ? 'vul een continu vermogen in W in' : 'maak eerst een selectie');
    } else if (som > m.w) {
      stel('#fdeeee','#f0c4c4','Past niet', m.naam + ' levert ' + nl(m.w,0) + ' W continu; je vraagt ' + nl(Math.round(som),0) + ' W. Zet apparaten niet gelijktijdig aan of kies een zwaarder model.');
    } else if (piek > m.w) {
      stel('#fff8e6','#e8d08a','Let op de aanloop', 'Het continu verbruik past (' + nl(Math.round(som),0) + ' van ' + nl(m.w,0) + ' W), maar de geschatte piek van ' + nl(Math.round(piek),0) + ' W ligt boven het continu vermogen. Of dat lukt hangt af van de piekcapaciteit in de handleiding.');
    } else {
      stel('#e8f5ee','#b7dfc9','Past', 'Continu ' + nl(Math.round(som),0) + ' W en piek ' + nl(Math.round(piek),0) + ' W blijven onder de ' + nl(m.w,0) + ' W van ' + m.naam + '.');
    }

    document.getElementById('pwc-tabel').innerHTML = MODELLEN.map(function(x){
      var ok = aantal && som <= x.w && piek <= x.w;
      var deels = aantal && som <= x.w && piek > x.w;
      var kleur = !aantal ? '#888' : (ok ? '#1a7a4a' : (deels ? '#a07818' : '#b03a3a'));
      var label = !aantal ? '—' : (ok ? '✓ past' : (deels ? '± aanloop onzeker' : '✗ te zwaar'));
      var rt2 = (aantal && som > 0) ? uren(x.wh * 0.85 / som) : '—';
      return '<div style="display:flex;justify-content:space-between;gap:.6rem;background:#fff;border:1px solid #e0e0e0;border-radius:6px;padding:.45rem .6rem;font-size:.82rem;flex-wrap:wrap;">' +
        '<span style="flex:1;min-width:150px;">' + x.naam + ' <span style="color:#888;">' + nl(x.wh,0) + ' Wh · ' + nl(x.w,0) + ' W</span></span>' +
        '<span style="color:#555;">runtime ' + rt2 + '</span>' +
        '<span style="color:' + kleur + ';font-weight:600;min-width:120px;text-align:right;">' + label + '</span></div>';
    }).join('');
  }

  sel.addEventListener('change', reken);
  ['pwc-vrij','pwc-vrij-w'].forEach(function(id){ document.getElementById(id).addEventListener('input', reken); });
  APPARATEN.forEach(function(a){
    document.getElementById('pwc-c-' + a.id).addEventListener('change', reken);
    document.getElementById('pwc-w-' + a.id).addEventListener('input', reken);
  });
  reken();
})();
</script>

Wil je de modellen naast elkaar zien op looptijd, gewicht en laadsnelheid in plaats van alleen op vermogen? Die vergelijking staat in [beste draagbare powerstation 2026](/posts/beste-draagbare-powerstation-2026/), en voor kampeergebruik in [beste powerstation voor camping 2026](/posts/beste-powerstation-camping-2026/).

<a href="https://go.duurzaamthuislab.nl/ecoflow?ref=/powerstation-calculator/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk de EcoFlow Delta-serie →</a>

<a href="https://go.duurzaamthuislab.nl/allpowers?ref=/powerstation-calculator/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk ALLPOWERS (R600 · R1500 · R2500-V2) →</a>

<a href="https://go.duurzaamthuislab.nl/anker-solix?ref=/powerstation-calculator/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk Anker SOLIX C1000 →</a>

<a href="https://go.duurzaamthuislab.nl/jackery?ref=/powerstation-calculator/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk Jackery Explorer 2000 Plus →</a>

<a href="https://go.duurzaamthuislab.nl/bluetti?ref=/powerstation-calculator/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk Bluetti EB70S →</a>

## Wattuur en watt: twee getallen die niet uitwisselbaar zijn

In vrijwel elke productnaam zitten beide getallen verstopt. "1024 Wh · 1800 W" zegt: er zit ongeveer één kilowattuur energie in, en de omvormer kan daar maximaal 1.800 watt tegelijk uit trekken. Dat zijn twee volstrekt verschillende grenzen, en ze knellen bij verschillende soorten gebruik.

**De Wh knelt bij lange, lichte belasting.** Een CPAP-apparaat van 40 W, een koelbox die met tussenpozen 45 W trekt, een laptop en een telefoon: samen misschien 150 W. Geen enkel powerstation heeft daar moeite mee qua vermogen. Wat je dan wilt weten is uitsluitend: hoeveel nachten haal ik? Bij 1.024 Wh is dat, na aftrek van omvormerverlies, ruim 870 Wh bruikbaar — bij 150 W komt dat neer op een kleine zes uur continu. Draait de koelbox maar een derde van de tijd (wat bij een compressorkoelbox gebruikelijk is), dan schuift die uitkomst flink op. Dat is precies de reden dat de tool op continu-verbruik rekent en niet op een geschatte inschakelduur: die duur weet alleen jij, en die verschilt per buitentemperatuur.

**De W knelt bij korte, zware belasting.** Alles met een verwarmingselement — waterkoker, koffiezetapparaat, tosti-ijzer, haardroger, elektrische kookplaat, dompelaar — trekt tussen de 800 en 2.200 W. Dat vraagt geen energie op de schaal die je accu tekortdoet (een koffiezetter van 1.000 W die vier minuten aan staat, kost slechts zo'n 67 Wh) maar het vraagt wél al dat vermogen op hetzelfde moment. Een ALLPOWERS R600 met 600 W continu heeft ruimschoots genoeg energie voor die kop koffie en levert hem toch niet: de omvormer valt terug of slaat af. Zwaarder inkopen op capaciteit helpt daar niet. Je hebt een model nodig met een hoger continu vermogen, en dat is een andere zoekvraag.

## Waarom aanloopstroom de echte faalmodus is

De meeste teleurstellingen met powerstations komen niet uit de rekensom die mensen wél maken, maar uit de piek die ze niet zien. Apparaten met een elektromotor of een compressor — een koelkast, een koelbox, een dompelpomp, een compressor, een boormachine, een cirkelzaag — trekken bij het inschakelen kort een veelvoud van hun nominale wattage. De motor staat stil en moet in een fractie van een seconde op toeren komen; die inschakelstroom kan gemakkelijk twee tot drie keer het opgegeven verbruik zijn, en bij oudere compressoren nog meer.

Het gevolg is een verwarrend storingsbeeld. Een koelkast die op het typeplaatje 120 W zegt, hoort volgens elke rekensom prima te werken op een station van 600 W. Maar bij elke keer dat de compressor aanslaat, vraagt hij kortstondig ergens rond de 350 W — en als er dan óók een waterkoker of een laptoplader aan hangt, tikt het totaal tegen de grens aan. Het powerstation beschermt zichzelf en schakelt uit. Voor de gebruiker lijkt dat willekeurig: "hij doet het soms wel en soms niet." Het patroon zit in de compressorcyclus, niet in het apparaat.

Daarom rekent blok 2 met een aanloopfactor. De factoren (×3 voor compressoren, ×2,5 voor elektrisch gereedschap, ×1 voor elektronica en laders) zijn vuistregels, geen fabrieksopgaven. Ze zijn er om je te laten zien *waar* de piek zit en hoe groot de marge boven je continu verbruik ongeveer moet zijn — niet om de inschakelstroom van jouw specifieke koelkast te voorspellen. Wie het exact wil weten, vindt de startstroom (soms als "LRA", locked rotor amps) op het typeplaatje van het apparaat of in de technische bijlage van de handleiding.

Fabrikanten geven bovendien vaak een piekvermogen op dat boven het continu vermogen ligt, en sommige merken bieden een softwarematige truc — EcoFlow noemt dat X-Boost — die het vermogen van weerstandsapparaten kunstmatig afknijpt zodat ze net wel werken. Dat helpt bij een waterkoker (die dan simpelweg langzamer opwarmt), maar niet bij een motor, die zijn koppel niet in porties kan afnemen. Hoeveel piek een model precies opvangt en hoe lang, staat per apparaat in de handleiding. Wij toetsen daarom bewust op het geverifieerde continu vermogen en geven een expliciete waarschuwing zodra de geschatte piek daarboven uitkomt: dan is het antwoord "misschien, kijk in de specificaties", en niet "ja".

## Hoe je van de uitkomst naar een keuze komt

Werk in deze volgorde, dan valt de keuze meestal snel.

1. **Zoek het zwaarste apparaat dat je gelijktijdig wilt gebruiken.** Dat bepaalt het minimale continu vermogen, en daarmee de ondergrens van je zoekgebied. Wil je koken of koffiezetten, dan begin je pas bij circa 1.800 W.
2. **Tel op wat er tegelijk aan hangt.** Niet wat je bezit, maar wat er daadwerkelijk op hetzelfde moment draait. Dit is waar mensen structureel te ruim inkopen.
3. **Bepaal daarna de gewenste looptijd.** Nu pas komt de capaciteit in beeld — en die kun je bij veel modellen later nog uitbreiden met een extra accu, terwijl het vermogen van de omvormer vastligt.
4. **Reken het toe naar je gebruiksscenario.** Voor stroomuitval is de vraag "hoeveel uur haal ik de router, de verlichting en de koelkast?"; voor camping is dat "hoeveel dagen zonder bijladen?"; voor gereedschap is de capaciteit vaak bijzaak en de piek alles.

Twijfel je of een powerstation überhaupt het juiste product is, dan is het onderscheid met een vaste thuisbatterij de moeite van het uitzoeken waard: die twee lossen andere problemen op en verdienen zich anders terug. Dat staat uitgewerkt in [powerstation versus thuisbatterij](/posts/powerstation-vs-thuisbatterij-2026/).

## Deze tool op jouw website

Er is een compacte embed-versie van de runtime-calculator beschikbaar voor blogs, kampeersites, vanlife-pagina's en installateurs. De embed-code staat op de [embed-codes-pagina](/embed-codes/); de enige voorwaarde is dat de bronvermelding blijft staan.
