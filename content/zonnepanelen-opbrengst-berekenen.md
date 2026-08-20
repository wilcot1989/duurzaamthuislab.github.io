---
title: "Opbrengst zonnepanelen berekenen (tool + verwachting vandaag)"
description: "Bereken de opbrengst van je zonnepanelen: systeemgrootte in kWp, de verwachte opbrengst vandaag, morgen en overmorgen op basis van de instralingsverwachting, en een jaarindicatie per oriëntatie."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
lastmod: 2026-08-20
---

Wil je weten wat je zonnepanelen opleveren — vandaag, morgen of over een heel jaar? Vul hieronder je aantal panelen, het wattpiek-vermogen per paneel en de oriëntatie van je dak in. De tool rekent je systeemgrootte om naar **kWp** en combineert die met de actuele instralingsverwachting voor Nederland.

<div id="zop-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.8rem;margin-bottom:1.2rem;">
    <label style="font-size:.85rem;color:#555;">Aantal panelen
      <input id="zop-aantal" type="number" min="1" max="200" step="1" value="10" style="width:100%;margin-top:.3rem;padding:.5rem;border:1px solid #ccc;border-radius:8px;font:inherit;">
    </label>
    <label style="font-size:.85rem;color:#555;">Wattpiek per paneel (Wp)
      <input id="zop-wp" type="number" min="100" max="1000" step="5" value="440" style="width:100%;margin-top:.3rem;padding:.5rem;border:1px solid #ccc;border-radius:8px;font:inherit;">
    </label>
    <label style="font-size:.85rem;color:#555;">Oriëntatie
      <select id="zop-orient" style="width:100%;margin-top:.3rem;padding:.5rem;border:1px solid #ccc;border-radius:8px;font:inherit;">
        <option value="1.00">Zuid (×1,00)</option>
        <option value="0.95">Zuidoost of zuidwest (×0,95)</option>
        <option value="0.90">Oost-west opstelling (×0,90)</option>
        <option value="0.85">Oost of west (×0,85)</option>
        <option value="0.60">Noord (×0,60)</option>
      </select>
    </label>
  </div>
  <p style="color:#666;font-size:.8rem;margin:-.6rem 0 1.2rem;">De factoren achter de oriëntaties zijn <strong>modelaannames</strong>: ze schatten hoeveel van de zuid-opbrengst een dakrichting benadert.</p>

  <div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;margin-bottom:1.2rem;">
    <div style="font-size:.8rem;color:#666;">Systeemgrootte</div>
    <div id="zop-kwp" style="font-size:1.6rem;font-weight:700;">—</div>
    <div id="zop-kwp-sub" style="font-size:.75rem;color:#888;">piekvermogen van je installatie</div>
  </div>

  <div style="font-size:.85rem;color:#555;font-weight:600;margin-bottom:.5rem;">Verwachte opbrengst per dag</div>
  <div id="zop-dagen" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.8rem;margin-bottom:1.2rem;"><span style="color:#666;font-size:.9rem;">laden…</span></div>

  <div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;margin-bottom:1rem;">
    <div style="font-size:.8rem;color:#666;">Jaarindicatie</div>
    <div id="zop-jaar" style="font-size:1.6rem;font-weight:700;">—</div>
    <div style="font-size:.75rem;color:#888;">vuistregel ± 875–950 kWh per kWp per jaar in Nederland (modelaanname, werkelijke opbrengst hangt af van locatie, hellingshoek en schaduw)</div>
  </div>

  <p style="color:#666;font-size:.85rem;margin:0;">Modelberekening — geen garantie. Bron dagverwachting: Open-Meteo-instraling (De Bilt), performance ratio 0,85.</p>
</div>

<script>
(function(){
  var zopData = null;
  function nl(x, d){ return x.toLocaleString('nl-NL', {minimumFractionDigits:d, maximumFractionDigits:d}); }
  function zopReken(){
    var aantal = parseFloat(document.getElementById('zop-aantal').value);
    var wp = parseFloat(document.getElementById('zop-wp').value);
    var f = parseFloat(document.getElementById('zop-orient').value);
    var kwpEl = document.getElementById('zop-kwp'), jaarEl = document.getElementById('zop-jaar'), dagenEl = document.getElementById('zop-dagen');
    if (!(aantal > 0) || !(wp > 0)) {
      kwpEl.textContent = '—'; jaarEl.textContent = '—';
      dagenEl.innerHTML = '<span style="color:#666;font-size:.9rem;">Vul een aantal panelen en een wattpiek in.</span>';
      return;
    }
    var kwp = aantal * wp / 1000;
    kwpEl.textContent = nl(kwp, 2) + ' kWp';
    document.getElementById('zop-kwp-sub').textContent = aantal + ' × ' + wp + ' Wp — piekvermogen van je installatie';
    var jaar = kwp * 900 * f;
    jaarEl.textContent = nl(Math.round(jaar), 0) + ' kWh per jaar';
    if (!zopData || !zopData.dagen || !zopData.dagen.length) return;
    var namen = ['Vandaag', 'Morgen', 'Overmorgen'];
    dagenEl.innerHTML = zopData.dagen.map(function(dag, i){
      var opbrengst = kwp * dag.opbrengst_kwh_per_kwp * f;
      var zon = dag.opbrengst_kwh_per_kwp >= 4 ? '☀️☀️☀️' : (dag.opbrengst_kwh_per_kwp >= 2.5 ? '☀️☀️' : '☀️');
      return '<div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.8rem;">' +
        '<div style="font-size:.8rem;color:#666;">' + (namen[i] || dag.datum) + ' ' + zon + '</div>' +
        '<div style="font-size:1.4rem;font-weight:700;">' + nl(opbrengst, 1) + ' kWh</div>' +
        '<div style="font-size:.75rem;color:#888;">' + nl(dag.opbrengst_kwh_per_kwp, 1) + ' kWh per kWp · ' + nl(dag.zonuren, 1) + ' zonuren</div></div>';
    }).join('');
  }
  ['zop-aantal','zop-wp','zop-orient'].forEach(function(id){
    var el = document.getElementById(id);
    el.addEventListener('input', zopReken);
    el.addEventListener('change', zopReken);
  });
  zopReken();
  fetch('https://beheer.wtdigital.nl/api/public/zonverwachting').then(function(r){ return r.json(); }).then(function(d){
    zopData = d;
    if (!d.dagen || !d.dagen.length) { document.getElementById('zop-dagen').innerHTML = '<span style="color:#666;font-size:.9rem;">Geen dagverwachting beschikbaar.</span>'; return; }
    zopReken();
  }).catch(function(){
    document.getElementById('zop-dagen').innerHTML = '<span style="color:#666;font-size:.9rem;">Kon de verwachting niet laden — probeer het later opnieuw.</span>';
  });
})();
</script>

## Hoe de berekening werkt

De opbrengst van zonnepanelen komt neer op drie stappen.

**Stap 1 — instraling.** De zon levert per vierkante meter energie aan, uitgedrukt in kWh/m². Die waarde verschilt sterk per dag: bewolking, seizoen en daglengte bepalen hoeveel er binnenkomt. De dagverwachting in de tool komt uit de instralingsverwachting van Open-Meteo voor De Bilt en geldt dus voor Nederland als geheel, niet voor jouw postcode.

**Stap 2 — performance ratio.** Niet alle ingestraalde energie wordt stroom. Verliezen in de panelen zelf (temperatuur, spectrum), de kabels en de omvormer worden samengevat in de performance ratio. In de berekening hierboven staat die vast op 0,85, een gangbare aanname voor een normaal functionerende installatie.

**Stap 3 — oriëntatie.** Een dak op het zuiden vangt over de dag de meeste instraling. Andere richtingen vangen minder, en dat drukken we uit als een factor ten opzichte van zuid. Die factoren zijn modelaannames: ze geven de orde van grootte, geen exacte uitkomst voor jouw dak.

### Wat betekent kWp?

kWp staat voor kilowattpiek: het vermogen dat je installatie levert onder gestandaardiseerde testomstandigheden. Tel simpelweg het wattpiek-vermogen van al je panelen op en deel door 1.000. Tien panelen van 440 Wp zijn dus 4,4 kWp. kWp is een vermogensmaat en zegt niets over de jaaropbrengst; die komt pas in beeld als je het vermogen combineert met instraling en verliezen — precies wat de tool doet.

### Waarom je werkelijke opbrengst afwijkt

- **Schaduw.** Een schoorsteen, dakkapel of boom die een deel van de dag over de panelen valt kost meer dan je op basis van het beschaduwde oppervlak zou verwachten, vooral bij strings zonder optimizers.
- **Hellingshoek.** Een vrij vlak of juist heel steil dak verzamelt over het jaar anders dan de hoek waarop de vuistregel is gebaseerd. Zomer- en winterprestaties schuiven daarmee ook onderling.
- **Omvormer.** Een omvormer die kleiner is gedimensioneerd dan het paneelvermogen kapt de pieken op heldere dagen af. Dat kost weinig op jaarbasis, maar wel juist op de dagen die de tool als zonnig aangeeft.
- **Degradatie en vervuiling.** Panelen leveren over de jaren geleidelijk iets minder, en vuil of mos op een flauw hellend dak verlaagt de opbrengst.
- **Locatie.** De kust ontvangt gemiddeld meer instraling dan het oosten van het land; de dagverwachting is één landelijk cijfer.

Gebruik de uitkomst dus als richtsnoer voor planning, niet als toezegging.

## Wat je met de dagverwachting kunt

De opbrengstverwachting is vooral bruikbaar om **verbruik te verschuiven naar de uren waarin je eigen stroom er is**. Op een dag met een hoge verwachting is de middag het moment voor de wasmachine, de droger, de vaatwasser, het opwarmen van de boiler of het laden van de elektrische auto. Wat je op dat moment zelf verbruikt, hoef je later niet uit het net te halen.

Dat weegt zwaarder sinds de vergoeding voor teruglevering onder druk staat. Veel leveranciers rekenen inmiddels [terugleverkosten](/posts/terugleverkosten-zonnepanelen-2026/), en met het [einde van de salderingsregeling per 2027](/posts/saldering-stopt-2027-volledige-gids/) verschuift het rendement van "alles terugleveren" naar "zoveel mogelijk zelf gebruiken". Een hoge zonverwachting is dan geen reden om achterover te leunen, maar een signaal om apparaten aan te zetten.

Tegelijk drukt veel zonnestroom de beursprijs. Op zonnige middagen zakken de uurtarieven, soms tot onder nul. Wie een dynamisch contract heeft, kan de [actuele stroomprijzen per uur](/stroomprijzen/) naast deze verwachting leggen: goedkope of negatieve uren zijn juist de momenten om extra te verbruiken of een thuisbatterij te laden. Op de pagina [dynamische energiecontracten vergelijken](/dynamisch-energiecontract-vergelijken/) staat welke aanbieders die uurprijzen doorgeven en welke voorwaarden daarbij horen.

Overweeg je nog panelen bij te leggen of anders te plaatsen? Dan is de dakrichting belangrijker dan de factor in de tool suggereert: een [oost-west-opstelling levert over de dag een vlakker profiel](/posts/oost-west-zonnepanelen-vs-zuid-2026/) dan zuid, met een lagere piek maar een langere productieperiode — wat bij minder gunstige terugleververgoedingen anders uitpakt dan puur op jaartotaal kijken.

## Veelgestelde vragen

**Hoeveel levert 1 kWp per jaar op?**
Als vuistregel wordt in Nederland ongeveer 875 tot 950 kWh per kWp per jaar gerekend bij een gunstige oriëntatie zonder schaduw. De tool hierboven gebruikt 900 kWh per kWp als middenwaarde. Het is een vuistregel, geen norm: locatie, hellingshoek, schaduw en de staat van de installatie bepalen waar je binnen (of buiten) die bandbreedte uitkomt.

**Waarom wijkt de dagverwachting soms sterk af van wat mijn omvormer laat zien?**
De verwachting gebruikt één landelijk instralingscijfer en een vaste performance ratio. Lokale bewolking, schaduw op jouw dak en de dimensionering van je omvormer zorgen voor afwijkingen in beide richtingen. Over een langere periode lopen model en werkelijkheid doorgaans dichter bij elkaar dan op een enkele dag.

**Kan ik met deze tool berekenen of zonnepanelen zich terugverdienen?**
Niet direct: de tool rekent opbrengst in kWh, geen euro's. Wat een kWh je waard is, hangt af van je contractvorm, hoeveel je zelf verbruikt, eventuele terugleverkosten en de afbouw van de saldering. Voor de financiële kant zijn de pagina's over [terugleverkosten](/posts/terugleverkosten-zonnepanelen-2026/) en [het einde van de saldering](/posts/saldering-stopt-2027-volledige-gids/) het startpunt.
