---
title: "Terugleverkosten berekenen per leverancier (rekentool)"
description: "Vul in hoeveel kWh je per jaar teruglevert en zie per energieleverancier wat je aan terugleverkosten betaalt. Alleen staffels en bedragen die de leverancier zelf publiceert, met peildatum."
layout: "single"
url: /terugleverkosten-berekenen/
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
lastmod: 2026-08-21
faq:
- q: 'Waarom staat bij sommige leveranciers geen bedrag in de uitkomst?'
  a: 'Omdat die leverancier het bedrag niet vrij toegankelijk publiceert. Eneco, ENGIE, Greenchoice en Oxxio rekenen een bedrag per teruggeleverde kWh maar noemen de hoogte alleen in je contract, de app of de mijn-omgeving; Vattenfall publiceert de staffel als los tarievendocument. Wij vullen daar geen schatting in — een verzonnen bedrag zou er in deze tool uitzien als leverancierswaarheid.'
- q: 'Waarom kan de tool bij Budget Thuis, energiedirect en Essent niet elk volume berekenen?'
  a: 'Die drie publiceren hun staffel op de eigen site als een reeks voorbeelden, niet als volledige tabel. Valt jouw teruglevering binnen een gepubliceerde schaal, dan rekent de tool exact. Valt hij ertussenin, dan laat de tool zien tussen welke twee gepubliceerde ankerpunten je zit en verzint hij geen bedrag daartussen. Alleen van Frank Energie hebben wij de volledige staffel kunnen uitlezen.'
- q: 'Hoe weet ik hoeveel ik per jaar teruglever?'
  a: 'Dat staat op je jaarafrekening als "teruggeleverd" of "invoeding", en in de app of mijn-omgeving van je leverancier. Weet je het niet, dan geeft onze opbrengsttool een indicatie op basis van je opgesteld vermogen — reken daarbij met het deel dat je niet zelf verbruikt, doorgaans grofweg de helft tot twee derde van je jaaropbrengst.'
- q: 'Waarom is de terugleververgoeding hier een invoerveld en geen vast tarief?'
  a: 'Omdat het per leverancier en per contract verschilt en regelmatig wijzigt. De startwaarde van 7 cent is een aanpasbare aanname, geen tarief dat wij als geldend presenteren. Ter vergelijking: Essent publiceert een terugleververgoeding van 15 cent per kWh (peildatum 20 augustus 2026), en bij een dynamisch contract beweegt de vergoeding per uur mee met de beursprijs. Vul in wat er in jouw contract staat.'
- q: 'Betekent nul terugleverkosten dat teruglevering bij die leverancier gratis is?'
  a: 'Nee. Bij de dynamische contracten in deze tool is er geen aparte kostenpost, maar de waarde van je teruggeleverde stroom wordt per uur bepaald — en dat is juist op zonnige middagen laag tot negatief. Bij Tibber gaat er bovendien een verkoopvergoeding per kWh van je opbrengst af. Geen terugleverkosten is dus niet hetzelfde als kosteloos terugleveren.'
- q: 'Blijven deze bedragen na 1 januari 2027 gelden?'
  a: 'Naar verwachting niet. Vattenfall en Budget Thuis melden op hun eigen site dat zij per 1 januari 2027 overgaan van een vast staffelbedrag naar een bedrag per kWh; Essent en energiedirect melden dat terugleververgoeding en terugleverkosten vanaf die datum anders worden berekend. Gebruik de uitkomst dus als momentopname voor 2026, niet als prognose voor daarna.'
---

*Disclosure: met één leverancier in deze tool hebben wij een affiliate-relatie — energiedirect. Sluit je via die gemarkeerde link een contract af, dan ontvangen wij mogelijk een commissie; dat kost jou niets extra. Alle andere leveranciers staan hier zonder vergoeding, en de rekenuitkomst wordt alleen bepaald door de gepubliceerde tarieven en jouw invoer. Zie [hoe we geld verdienen](/how-we-earn/).*

<div id="sc-blok" style="background:#fff6ec;border:1px solid #f0d3b4;border-left:5px solid #c66e3f;border-radius:0 10px 10px 0;padding:1rem 1.1rem;margin:1.5rem 0;">
  <div style="font-size:.8rem;color:#8a5a34;letter-spacing:.04em;text-transform:uppercase;">Aftellen naar het einde van de saldering</div>
  <div id="sc-dagen" style="font-size:1.6rem;font-weight:700;line-height:1.2;margin:.15rem 0;">—</div>
  <p style="margin:.3rem 0 0;font-size:.9rem;color:#444;">Op 1 januari 2027 stopt de salderingsregeling in één keer; vanaf dat moment bepaalt het verschil tussen je afnameprijs en je terugleververgoeding wat een teruggeleverde kWh je nog waard is. <a href="/posts/saldering-stopt-2027-volledige-gids/">Wat er precies verandert →</a></p>
</div>

<script>
(function(){
  var el = document.getElementById('sc-dagen');
  if (!el) return;
  var nu = new Date();
  var vandaag = Date.UTC(nu.getFullYear(), nu.getMonth(), nu.getDate());
  var einde = Date.UTC(2027, 0, 1);
  var dagen = Math.round((einde - vandaag) / 86400000);
  if (dagen > 1) el.textContent = 'nog ' + dagen.toLocaleString('nl-NL') + ' dagen';
  else if (dagen === 1) el.textContent = 'nog 1 dag';
  else if (dagen === 0) el.textContent = 'vandaag is de laatste dag';
  else el.textContent = 'de saldering is gestopt';
})();
</script>

Lever je stroom terug aan het net, dan rekenen de meeste leveranciers daar sinds 2024 kosten voor. Hoeveel dat is, hangt af van je leverancier én van hoeveel kWh je per jaar teruglevert. Vul je jaarlijkse teruglevering in en de tool zet de leveranciers naast elkaar.

Wat je hieronder ziet, zijn **uitsluitend bedragen die de leverancier zelf publiceert**, met peildatum. Waar een leverancier geen bedrag publiceert, staat dat er ook zo. Aan de uitkomsten kunnen geen rechten worden ontleend.

<div id="tlk-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.1rem;">
    <div>
      <label for="tlk-kwh" style="display:block;font-weight:600;margin-bottom:.3rem;">Teruglevering per jaar (kWh)</label>
      <input id="tlk-kwh" type="number" min="0" max="30000" step="50" value="3500" oninput="tlkReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Het aantal kWh dat je aan het net teruglevert, niet je totale opwek. Staat op je jaarafrekening; een indicatie krijg je met de <a href="/zonnepanelen-opbrengst-berekenen/">opbrengsttool</a>.</span>
    </div>
    <div>
      <label for="tlk-verg" style="display:block;font-weight:600;margin-bottom:.3rem;">Terugleververgoeding (€/kWh)</label>
      <input id="tlk-verg" type="number" min="0" max="1" step="0.005" value="0.07" oninput="tlkReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Aanpasbare aanname: € 0,07. Alleen om de kosten in verhouding te zetten. Essent publiceert € 0,15/kWh (peildatum 20 aug 2026); bij dynamisch beweegt de vergoeding per uur mee. Vul in wat in jouw contract staat.</span>
    </div>
  </div>
  <div id="tlk-context" style="margin-top:1.3rem;"></div>
  <div id="tlk-tabel" style="margin-top:1.1rem;overflow-x:auto;"></div>
  <p style="color:#666;font-size:.85rem;margin-top:.9rem;">Staffelbedragen per dag zijn omgerekend met 365 dagen, Frank Energie met 12 maanden. De rangschikking is alfabetisch op leveranciersnaam — geen commissie, geen redactionele voorkeur. Alle tarieven komen van de site van de leverancier zelf, peildatum per rij. Tarieven wijzigen regelmatig; de leverancierssite is leidend. Aan deze uitkomsten kunnen geen rechten worden ontleend.</p>
</div>

<script>
var TLK_LEV = [
  {
    naam: 'ANWB Energie',
    contract: 'Dynamisch',
    soort: 'nul',
    peil: '20 aug 2026',
    noot: 'Eigen site: geen extra terugleverkosten of -boetes. De prijs zit in de uurtarieven: je ontvangt per uur het tarief dat je op dat moment voor afname zou betalen.'
  },
  {
    naam: 'Budget Thuis',
    contract: 'Vast en variabel',
    soort: 'ankers-dag',
    peil: 'tarieven per 16 dec 2025',
    ankers: [ [5, 500, 0.07], [2000, 2500, 0.59], [4500, 5000, 1.38], [20000, Infinity, 7.73] ],
    noot: 'Staffel met een vast bedrag per dag. Budget Thuis publiceert vier van de 25 schalen als voorbeeld; per 1 jan 2027 gaat het naar een bedrag per kWh.'
  },
  {
    naam: 'Budget Thuis Dynamisch',
    contract: 'Dynamisch',
    soort: 'nul',
    peil: '20 aug 2026',
    noot: 'Eigen site: je betaalt geen terugleverkosten. De prijs zit in de uurtarieven.'
  },
  {
    naam: 'Eneco',
    contract: 'Vast, variabel en VoordeelMomenten',
    soort: 'onbekend',
    peil: 'model 20 aug 2026',
    noot: 'Vast tarief per teruggeleverde kWh. Het bedrag staat alleen in de app en Mijn Eneco, dus niet te berekenen.'
  },
  {
    naam: 'Eneco Dynamisch',
    contract: 'Dynamisch',
    soort: 'nul',
    peil: '20 aug 2026',
    noot: 'Geen terugleverkosten; je krijgt per uur hetzelfde leveringstarief als voor afname. Let op: wel een verkoopvergoeding over wat je meer teruglevert dan afneemt, waarvan het bedrag niet publiek is.'
  },
  {
    naam: 'energiedirect',
    contract: 'Vast en variabel',
    soort: 'ankers-dag',
    peil: 'staffel per 1 jun / 1 jul 2024',
    affiliate: true,
    ankers: [ [0, 250, 0], [251, 500, 0.13367], [1001, 1250, 0.40059], [10000, Infinity, 3.65069] ],
    noot: 'Staffel met een vast bedrag per dag; vier schalen gepubliceerd als voorbeeld. Een vast contract dat vóór 1 jun 2024 startte valt er pas onder na het aflopen van dat contract.'
  },
  {
    naam: 'energiedirect Dynamisch',
    contract: 'Dynamisch',
    soort: 'nul',
    peil: '20 aug 2026',
    affiliate: true,
    noot: 'Eigen klantenservicepagina: bij dynamisch geen extra kosten voor teruglevering. De prijs zit in de uurtarieven.'
  },
  {
    naam: 'ENGIE',
    contract: 'Vast en variabel',
    soort: 'onbekend',
    peil: 'model 20 aug 2026',
    noot: 'Vast bedrag per teruggeleverde kWh. De hoogte staat volgens ENGIE in je leveringsovereenkomst, MijnENGIE of de app — niet publiek, dus niet te berekenen.'
  },
  {
    naam: 'Essent',
    contract: 'Vast en variabel',
    soort: 'ankers-dag',
    peil: 'tarievenblad per 1 jan 2025',
    ankers: [ [0, 250, 0], [251, 500, 0.13367], [10000, Infinity, 3.65069] ],
    noot: 'Staffel met een vast bedrag per dag incl. btw; drie schalen gepubliceerd als voorbeeld. Essent noemt daarnaast een terugleververgoeding van € 0,15/kWh en meldt een andere berekening vanaf 1 jan 2027.'
  },
  {
    naam: 'Frank Energie',
    contract: 'Vast en variabel',
    soort: 'staffel-maand',
    peil: 'staffel uitgelezen 21 aug 2026',
    staffel: [
      [5, 0], [500, 5.06], [1000, 10.12], [1500, 15.18], [2000, 20.23],
      [2500, 25.29], [3000, 30.35], [3500, 35.41], [4000, 40.47], [4500, 45.53],
      [5000, 50.58], [6000, 60.70], [7000, 70.82], [8000, 80.93], [9000, 91.05],
      [10000, 101.17], [11500, 116.34], [13000, 131.52], [14500, 146.69], [16000, 161.87],
      [17500, 177.05], [19000, 192.22], [20500, 207.40], [Infinity, 217.48]
    ],
    noot: 'Volledige staffel per maand incl. btw, geldt bij vaste en variabele contracten sinds 1 jun 2025. Wij hebben de tabel (op de Frank-pagina een afbeelding) op 21 aug 2026 uitgelezen; controleer de actuele tabel vóór je tekent.'
  },
  {
    naam: 'Greenchoice',
    contract: 'Vast en variabel',
    soort: 'onbekend',
    peil: 'model 20 aug 2026',
    noot: 'Tarief per teruggeleverde kWh, bedrag niet vrij toegankelijk gepubliceerd. Geldt voor nieuwe vaste of variabele contracten vanaf 20 jun 2024.'
  },
  {
    naam: 'Oxxio',
    contract: 'Vast, variabel, dynamisch en hybride',
    soort: 'onbekend',
    peil: 'model 20 aug 2026',
    noot: 'Een vast bedrag per teruggeleverde kilowattuur. Je persoonlijke tarief staat volgens Oxxio in de app of Mijn Oxxio; Oxxio maakt in de gepubliceerde uitleg geen onderscheid per contracttype.'
  },
  {
    naam: 'Tibber',
    contract: 'Dynamisch',
    soort: 'per-kwh',
    tarief: 0.0248,
    peil: '20 aug 2026',
    noot: 'Geen aparte terugleverkosten, wél een verkoopvergoeding van € 0,0248 per kWh incl. btw die van je opbrengst af gaat. Dat bedrag rekent de tool hier als kostenpost, zodat het vergelijkbaar is.'
  },
  {
    naam: 'Vattenfall',
    contract: 'Variabel en vast vanaf 1 jul 2024',
    soort: 'drempel-onbekend',
    drempel: 500,
    peil: 'staffel per 1 mei 2026, los document',
    noot: 'Vaste terugleverkosten volgens staffel. Onder 500 kWh teruglevering betaal je volgens Vattenfall geen vaste terugleverkosten; de staffelbedragen daarboven staan alleen in een los tarievendocument. Per 1 jan 2027 gaat Vattenfall over op een bedrag per kWh.'
  },
  {
    naam: 'Vattenfall FlexPrijs',
    contract: 'Dynamisch',
    soort: 'nul',
    peil: '20 aug 2026',
    noot: 'Eigen site: bij FlexPrijs betaal je nu geen vaste terugleverkosten. De prijs zit in de uurtarieven.'
  },
  {
    naam: 'Zonneplan',
    contract: 'Dynamisch',
    soort: 'nul',
    peil: '20 aug 2026',
    noot: 'Eigen site: Zonneplan rekent geen terugleverkosten, nu en in de toekomst. De prijs zit in de kwartiertarieven; daarnaast noemt Zonneplan een Zonnebonus bovenop de kale marktprijs.'
  }
];

function tlkEuro(v){
  return '€ ' + v.toLocaleString('nl-NL', {minimumFractionDigits: 2, maximumFractionDigits: 2});
}

function tlkEuroFijn(v, cijfers){
  return '€ ' + v.toLocaleString('nl-NL', {minimumFractionDigits: cijfers, maximumFractionDigits: cijfers});
}

function tlkTarief(v){
  return tlkEuroFijn(v, Math.round(v * 100) / 100 === v ? 2 : 5);
}

function tlkKwh(v){
  return v.toLocaleString('nl-NL') + ' kWh';
}

function tlkStaffelMaand(staffel, kwh){
  for (var i = 0; i < staffel.length; i++){
    if (kwh <= staffel[i][0]) return staffel[i][1];
  }
  return staffel[staffel.length - 1][1];
}

function tlkAnker(ankers, kwh){
  for (var i = 0; i < ankers.length; i++){
    if (kwh >= ankers[i][0] && kwh <= ankers[i][1]) return ankers[i];
  }
  return null;
}

function tlkAnkerTekst(ankers, kwh){
  var onder = null, boven = null;
  for (var i = 0; i < ankers.length; i++){
    if (ankers[i][1] < kwh) onder = ankers[i];
    if (boven === null && ankers[i][0] > kwh) boven = ankers[i];
  }
  var d = [];
  if (onder) d.push('bij ' + tlkKwh(onder[1]) + ' is het ' + tlkTarief(onder[2]) + ' per dag');
  if (boven) d.push('vanaf ' + tlkKwh(boven[0]) + ' is het ' + tlkTarief(boven[2]) + ' per dag');
  if (!d.length) return 'geen gepubliceerd ankerpunt in de buurt van dit volume';
  return 'tussen de gepubliceerde schalen: ' + d.join(', ') + '. Het bedrag daartussen publiceert deze leverancier niet.';
}

function tlkBereken(lev, kwh){
  if (lev.soort === 'nul'){
    return {jaar: 0, bekend: true, label: tlkEuro(0), extra: 'geen aparte kostenpost'};
  }
  if (lev.soort === 'per-kwh'){
    var j = kwh * lev.tarief;
    return {jaar: j, bekend: true, label: tlkEuro(j), extra: tlkEuroFijn(lev.tarief, 4) + ' per kWh (verkoopvergoeding)'};
  }
  if (lev.soort === 'onbekend'){
    return {jaar: null, bekend: false, label: 'niet gepubliceerd', extra: 'check je contract, de app of de mijn-omgeving'};
  }
  if (lev.soort === 'drempel-onbekend'){
    if (kwh < lev.drempel){
      return {jaar: 0, bekend: true, label: tlkEuro(0), extra: 'onder de gepubliceerde drempel van ' + tlkKwh(lev.drempel)};
    }
    return {jaar: null, bekend: false, label: 'niet gepubliceerd', extra: 'boven ' + tlkKwh(lev.drempel) + ' geldt een staffel die alleen in een los tarievendocument staat — check je contract'};
  }
  if (lev.soort === 'staffel-maand'){
    var maand = tlkStaffelMaand(lev.staffel, kwh);
    return {jaar: maand * 12, bekend: true, label: tlkEuro(maand * 12), extra: tlkEuro(maand) + ' per maand'};
  }
  if (lev.soort === 'ankers-dag'){
    var a = tlkAnker(lev.ankers, kwh);
    if (a){
      return {jaar: a[2] * 365, bekend: true, label: tlkEuro(a[2] * 365), extra: tlkTarief(a[2]) + ' per dag (schaal ' + tlkKwh(a[0]) + (a[1] === Infinity ? ' en hoger)' : ' – ' + tlkKwh(a[1]) + ')')};
    }
    return {jaar: null, bekend: false, label: 'schaal niet gepubliceerd', extra: tlkAnkerTekst(lev.ankers, kwh)};
  }
  return {jaar: null, bekend: false, label: 'onbekend', extra: ''};
}

function tlkGetal(id, min, max){
  var v = parseFloat(document.getElementById(id).value.replace(',', '.'));
  if (isNaN(v) || v < min || v > max) return null;
  return v;
}

function tlkReken(){
  var kwh  = tlkGetal('tlk-kwh', 0, 30000);
  var verg = tlkGetal('tlk-verg', 0, 1);
  var ctx = document.getElementById('tlk-context');
  var tab = document.getElementById('tlk-tabel');

  if (kwh === null || verg === null){
    ctx.innerHTML = '<div style="background:#fff;border:1px solid #f0c4c4;border-radius:8px;padding:.9rem;color:#b03a3a;">Vul een teruglevering tussen 0 en 30.000 kWh in en een vergoeding tussen € 0 en € 1 per kWh.</div>';
    tab.innerHTML = '';
    return;
  }

  var opbrengst = kwh * verg;
  var rijen = [];
  var laagste = null, hoogste = null;

  for (var i = 0; i < TLK_LEV.length; i++){
    var lev = TLK_LEV[i];
    var r = tlkBereken(lev, kwh);
    rijen.push({lev: lev, r: r});
    if (r.bekend){
      if (laagste === null || r.jaar < laagste.r.jaar) laagste = {lev: lev, r: r};
      if (hoogste === null || r.jaar > hoogste.r.jaar) hoogste = {lev: lev, r: r};
    }
  }

  var deel = (opbrengst > 0 && hoogste) ? Math.round((hoogste.r.jaar / opbrengst) * 100) : null;
  var ctxHtml =
    '<div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:1rem;">' +
    '<div style="font-size:.8rem;color:#666;">In context</div>' +
    '<p style="margin:.35rem 0 0;">Bij <strong>' + tlkKwh(kwh) + '</strong> teruglevering en een vergoeding van <strong>' + tlkEuroFijn(verg, 3) + ' per kWh</strong> is je terugleveropbrengst circa <strong>' + tlkEuro(opbrengst) + ' per jaar</strong>.';
  if (hoogste && hoogste.r.jaar > 0){
    ctxHtml += ' De duurste leverancier in deze lijst — <strong>' + hoogste.lev.naam + '</strong> — houdt daar <strong>' + tlkEuro(hoogste.r.jaar) + '</strong> van in' + (deel !== null ? ' (' + deel + '% van je opbrengst)' : '') + '.';
  }
  if (laagste){
    ctxHtml += ' Bij de goedkoopste optie in deze lijst (' + laagste.lev.naam + ') is dat ' + tlkEuro(laagste.r.jaar) + '.';
  }
  ctxHtml += '</p><p style="margin:.5rem 0 0;font-size:.85rem;color:#666;">De vergoeding is jouw invoer, geen tarief van ons. Leveranciers zonder gepubliceerd bedrag zitten niet in deze vergelijking van hoogste en laagste — die staan als <em>niet gepubliceerd</em> in de tabel.</p></div>';
  ctx.innerHTML = ctxHtml;

  var body = '';
  for (var j = 0; j < rijen.length; j++){
    var L = rijen[j].lev, R = rijen[j].r;
    var netto = R.bekend ? opbrengst - R.jaar : null;
    var kleur = !R.bekend ? '#fbfbfb' : (R.jaar === 0 ? '#e8f5ee' : (R.jaar > opbrengst && opbrengst > 0 ? '#fdeeee' : '#fff'));
    var naam = L.naam + (L.affiliate ? ' <span style="font-size:.7rem;color:#8a5a34;">(affiliate-partner)</span>' : '');
    body += '<tr style="background:' + kleur + ';border-bottom:1px solid #e2e8f0;">' +
      '<td style="padding:.6rem;vertical-align:top;"><strong>' + naam + '</strong><div style="font-size:.78rem;color:#666;">' + L.contract + '</div></td>' +
      '<td style="padding:.6rem;vertical-align:top;white-space:nowrap;"><strong>' + R.label + '</strong>' + (R.bekend && R.jaar > 0 ? ' <span style="font-size:.78rem;color:#666;">per jaar</span>' : '') + '<div style="font-size:.78rem;color:#666;">' + R.extra + '</div></td>' +
      '<td style="padding:.6rem;vertical-align:top;white-space:nowrap;">' + (netto === null ? '<span style="color:#888;">—</span>' : tlkEuro(netto)) + '</td>' +
      '<td style="padding:.6rem;vertical-align:top;font-size:.82rem;color:#444;">' + L.noot + '<div style="color:#777;margin-top:.2rem;">Peildatum: ' + L.peil + '</div></td>' +
      '</tr>';
  }

  tab.innerHTML = '<table style="width:100%;border-collapse:collapse;font-size:.9rem;background:#fff;border:1px solid #e0e0e0;min-width:780px;">' +
    '<thead><tr style="background:#0e7490;color:#fff;text-align:left;">' +
    '<th style="padding:.6rem;">Leverancier</th><th style="padding:.6rem;">Terugleverkosten</th><th style="padding:.6rem;">Netto over</th><th style="padding:.6rem;">Wat de leverancier publiceert</th>' +
    '</tr></thead><tbody>' + body + '</tbody></table>';
}
tlkReken();
</script>

## Het korte antwoord

Terugleverkosten verschillen geen paar procent maar een factor tien tussen leveranciers, en het **model** bepaalt dat verschil:

- **Een staffel per dag of per maand** (Budget Thuis, energiedirect, Essent, Frank Energie, Vattenfall bij vaste en variabele contracten) betaal je ongeacht wat je op een dag daadwerkelijk teruglevert. Je jaarlijkse teruglevering bepaalt alleen in welke schaal je valt.
- **Een bedrag per teruggeleverde kWh** (Eneco, ENGIE, Greenchoice, Oxxio) beweegt mee met je opbrengst — maar geen van deze vier publiceert de hoogte, dus je kunt het vooraf niet narekenen.
- **Bij dynamische contracten** (ANWB Energie, Budget Thuis Dynamisch, Eneco Dynamisch, energiedirect Dynamisch, Tibber, Vattenfall FlexPrijs, Zonneplan) is er geen aparte kostenpost. De prijs zit in de uur- of kwartiertarieven: op een zonnige middag is een teruggeleverde kWh simpelweg weinig waard, en bij Tibber gaat er nog een verkoopvergoeding van je opbrengst af.

De volledige uitleg per leverancier, met bron en peildatum per cel, staat in onze [vergelijking van terugleverkosten per leverancier](/terugleverkosten-vergelijken/).

## Waarom de tool niet elk bedrag kan uitrekenen

Dit is de belangrijkste beperking, en die zit niet aan onze kant: **de meeste leveranciers publiceren hun bedrag niet volledig.**

| Wat we hebben | Bij wie | Wat de tool dan doet |
|---|---|---|
| Volledige staffel | Frank Energie | Rekent elk volume exact uit |
| Losse ankerpunten uit de staffel | Budget Thuis, energiedirect, Essent | Rekent exact binnen een gepubliceerde schaal; daarbuiten laat hij zien tussen welke twee ankerpunten je zit |
| Alleen een drempel | Vattenfall (onder 500 kWh geen vaste terugleverkosten) | Rekent nul onder de drempel, daarboven: niet gepubliceerd |
| Alleen het model, geen bedrag | Eneco, ENGIE, Greenchoice, Oxxio | Meldt "niet gepubliceerd — check je contract" |
| Expliciete nul | ANWB Energie, Zonneplan en de andere dynamische contracten | Rekent nul, met de kanttekening dat de prijs in de uurtarieven zit |

Wij vullen die gaten niet met schattingen of met cijfers van vergelijkingssites. In een rekentool ziet een geschat bedrag eruit als een tarief van de leverancier, en dat is het dan niet.

## Hoe de tool rekent

Drie regels, allemaal met de hand te controleren:

- **Staffel per dag:** bedrag per dag × 365 = kosten per jaar.
- **Staffel per maand** (Frank Energie): bedrag per maand × 12 = kosten per jaar.
- **Bedrag per kWh** (bij Tibber de verkoopvergoeding): tarief × jouw teruglevering.

De kolom *netto over* is je terugleveropbrengst (teruglevering × jouw ingevulde vergoeding) minus de terugleverkosten. Die opbrengst is dus geen tarief van ons: het is de aanname die jij in het tweede veld zet. Een schrikkeljaar, een contract dat halverwege het jaar begint of een tariefwijziging halverwege een jaar zitten er niet in — dat zijn correcties van enkele procenten op een uitkomst waarvan de grootste post toch al per leverancier verschilt.

## Wat dit betekent voor je keuze

De uitkomst zegt iets anders dan "kies de goedkoopste rij". Drie dingen om mee te nemen:

**1. Bij een staffel is elke kWh die je zelf verbruikt dubbel waardevol.** Je kosten dalen namelijk niet mee met minder teruglevering — behalve als je een schaal lager komt. Zit je net boven een schaalgrens, dan kan een paar honderd kWh minder teruglevering een sprong in de kosten schelen. Verhogen van je eigen verbruik lukt met apparaten op de zonnige uren (zie [beste tijd om je wasmachine aan te zetten](/beste-tijd-wasmachine/)) of met een thuisbatterij, waarvan je de rekensom kunt maken met onze [terugverdientijd-tool](/terugverdientijd-thuisbatterij/).

**2. Geen terugleverkosten is niet hetzelfde als een goede vergoeding.** Bij dynamische contracten verdwijnt de kostenpost, maar je opbrengst per teruggeleverde kWh beweegt mee met de markt en is juist op zonnige middagen laag. Reken beide kanten door voordat je overstapt; welke aanbieders er zijn staat in onze [vergelijking van dynamische energiecontracten](/dynamisch-energiecontract-vergelijken/).

**3. Reken niet op deze bedragen voor 2027 en later.** Vattenfall en Budget Thuis melden zelf dat zij per 1 januari 2027 van staffel naar een bedrag per kWh gaan; Essent en energiedirect melden een andere berekening vanaf die datum. Wie nu in een hoge staffel zit, kan er dan relatief op vooruitgaan; kleine terugleveraars die nu onder een drempel vallen, gaan juist betalen.

Hoeveel je teruglevert weet je pas als je weet wat je opwekt en wat je zelf verbruikt. Die eerste helft reken je uit met onze [opbrengsttool voor zonnepanelen](/zonnepanelen-opbrengst-berekenen/); wat er in 2027 verandert staat in de [volledige gids over het einde van de saldering](/posts/saldering-stopt-2027-volledige-gids/).

## Bij welke leverancier je nu kunt kijken

Bij energiedirect staat op de eigen klantenservicepagina dat je met een dynamisch contract geen extra kosten voor teruglevering betaalt, terwijl het variabele contract onder de dagstaffel valt. Dat verschil binnen één leverancier is precies wat deze tool zichtbaar maakt.

<p style="margin:1.4rem 0;"><a class="cta cta-affiliate" href="https://go.duurzaamthuislab.nl/energiedirect?ref=/terugleverkosten-berekenen/" target="_blank" rel="noopener nofollow sponsored">Bekijk energiedirect →</a></p>

Wil je de staffel van Frank Energie zelf controleren — de enige waarvan wij de volledige tabel hebben kunnen uitlezen — dan staat die op hun eigen pagina over terugleverkosten. Wij ontvangen voor die verwijzing geen vergoeding.

<p style="margin:1.4rem 0;"><a class="cta" href="https://go.duurzaamthuislab.nl/frank-energie?ref=/terugleverkosten-berekenen/" target="_blank" rel="noopener nofollow">Bekijk Frank Energie →</a></p>

De veelgestelde vragen over deze rekentool staan hieronder.
