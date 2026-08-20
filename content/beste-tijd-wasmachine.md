---
title: "Beste tijd om je wasmachine aan te zetten (live uurprijzen)"
description: "Wanneer is het goedkoopst om je wasmachine te draaien? Hieronder het goedkoopste (en duurste) tweeuursblok van vandaag en morgen, rechtstreeks uit de dynamische uurprijzen."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
lastmod: 2026-08-20
---

*Disclosure: dit artikel bevat affiliate-links naar energieaanbieders. Sluit je via zo'n link een contract af, dan ontvangen wij mogelijk een commissie — dit kost jou niets extra en beïnvloedt de getoonde prijzen niet: die komen rechtstreeks van de stroombeurs.*

Heb je een **dynamisch energiecontract**, dan bepaalt de beursprijs per uur wanneer wassen het goedkoopst is. Dat moment verschuift elke dag. Hieronder staat het goedkoopste aaneengesloten tweeuursblok van vandaag — en zodra de veiling van morgen bekend is (doorgaans rond 15:00) ook dat van morgen.

<div id="bw-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div id="bw-kaarten" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.8rem;"><span style="color:#666;font-size:.9rem;">laden…</span></div>
  <p id="bw-noot" style="color:#666;font-size:.85rem;margin-top:.8rem;">Kale EPEX-prijs incl. btw, excl. energiebelasting en de inkoopvergoeding van je leverancier. Een tweeuursblok is gekozen omdat een gemiddeld wasprogramma daarbinnen valt; controleer de looptijd van jouw programma. Bron: day-ahead-veiling.</p>
</div>

<script>
(function(){
  function uurNL(datum, uurUTC){
    var dt = new Date(datum + 'T' + String(uurUTC).padStart(2,'0') + ':00:00Z');
    return dt.toLocaleTimeString('nl-NL',{timeZone:'Europe/Amsterdam',hour:'2-digit',minute:'2-digit'});
  }
  function blok(d, n, duurste){
    var best = null, bestSom = duurste ? -Infinity : Infinity;
    for (var i = 0; i + n <= d.uren.length; i++){
      var som = 0;
      for (var j = i; j < i + n; j++) som += d.uren[j].prijs;
      if (duurste ? (som > bestSom) : (som < bestSom)){ bestSom = som; best = i; }
    }
    if (best === null) return null;
    return {
      van: uurNL(d.datum, d.uren[best].uur),
      tot: uurNL(d.datum, d.uren[Math.min(best+n, d.uren.length-1)].uur),
      gem: bestSom / n
    };
  }
  function kaart(kleurBg, kleurRand, kleurTxt, label, tijd, sub){
    return '<div style="background:' + kleurBg + ';border:1px solid ' + kleurRand + ';border-radius:8px;padding:.9rem;">' +
      '<div style="font-size:.8rem;color:' + kleurTxt + ';">' + label + '</div>' +
      '<div style="font-size:1.25rem;font-weight:700;">' + tijd + '</div>' +
      '<div style="font-size:.75rem;color:#888;">' + sub + '</div></div>';
  }
  function haal(url){ return fetch(url).then(function(r){ return r.json(); }).catch(function(){ return null; }); }
  Promise.all([
    haal('https://beheer.wtdigital.nl/api/public/stroomprijzen'),
    haal('https://beheer.wtdigital.nl/api/public/stroomprijzen?dag=morgen')
  ]).then(function(res){
    var vandaag = res[0], morgen = res[1], html = '';
    if (vandaag && vandaag.uren && vandaag.uren.length){
      var goed = blok(vandaag, 2, false), slecht = blok(vandaag, 2, true);
      if (goed) html += kaart('#e8f5ee','#b7dfc9','#1a7a4a','🧺 Beste moment vandaag', goed.van + ' – ' + goed.tot, 'gem. € ' + goed.gem.toFixed(3) + ' per kWh');
      if (slecht) html += kaart('#fdeeee','#f0c4c4','#b03a3a','⛔ Vermijd vandaag', slecht.van + ' – ' + slecht.tot, 'gem. € ' + slecht.gem.toFixed(3) + ' per kWh');
      if (goed && slecht) html += kaart('#fff','#e0e0e0','#666','Verschil per kWh', '€ ' + (slecht.gem - goed.gem).toFixed(3), 'duurste min goedkoopste blok (kale prijs)');
    } else {
      html += '<span style="color:#666;font-size:.9rem;">Kon de uurprijzen van vandaag niet laden — probeer het later opnieuw.</span>';
    }
    if (morgen && morgen.uren && morgen.uren.length){
      var goedM = blok(morgen, 2, false);
      if (goedM) html += kaart('#e8f5ee','#b7dfc9','#1a7a4a','🧺 Beste moment morgen', goedM.van + ' – ' + goedM.tot, 'gem. € ' + goedM.gem.toFixed(3) + ' per kWh');
    } else {
      html += kaart('#fff','#e0e0e0','#666','🧺 Morgen', 'nog niet bekend', 'de veiling voor morgen komt rond 15:00');
    }
    document.getElementById('bw-kaarten').innerHTML = html;
  });
})();
</script>

## Het korte antwoord

Met een dynamisch contract is er geen vast "beste uur": de day-ahead-veiling zet elke dag nieuwe prijzen per uur. Voor vandaag zie je het goedkoopste blok hierboven. Structureel zijn er wel twee patronen die vaak terugkomen:

- **Midden op de dag** is stroom op zonnige dagen goedkoop, omdat al het zonnevermogen tegelijk het net op komt. Op zulke dagen zakt de beursprijs regelmatig richting nul of eronder.
- **'s Nachts** is de vraag laag en de prijs meestal onder het daggemiddelde, al is het verschil met de zonnige middag op heldere dagen vaak klein.
- **De ochtendpiek (ongeveer 07:00–09:00) en avondpiek (ongeveer 17:00–21:00)** zijn doorgaans de duurste uren: veel vraag, weinig zon.

Heb je zonnepanelen én een dynamisch contract, dan is de middag dubbel interessant: je wast dan zoveel mogelijk op je eigen stroom, en wat je van het net haalt is op zulke uren goedkoop.

## Met een vast contract verschuiven: verandert niets aan de kWh-prijs

Bij een vast of variabel contract met één tarief betaal je elk uur van het etmaal hetzelfde per kWh. Om 03:00 wassen kost dan precies zoveel als om 19:00. Verschuiven levert daar dus geen besparing op je stroomkosten op — alleen minder druk op het net.

Eén uitzondering: heb je een **dubbele meter met dag- en nachttarief**, dan geldt buiten de daguren een lager tarief (in de regel 's nachts en in het weekend). Of dat in jouw geval voordelig uitpakt, hangt af van de tarieven in je eigen contract; die staan op je jaarafrekening of in de app van je leverancier. Controleer dat voordat je je waspatroon omgooit.

## Hoeveel scheelt het echt?

Reken het als model, niet als belofte. **Stel** dat je wasprogramma 1 kWh verbruikt. Dan is het verschil per wasbeurt simpelweg:

> verschil per beurt = (gemiddelde prijs duurste blok − gemiddelde prijs goedkoopste blok) × verbruik in kWh

Voor vandaag staat dat prijsverschil per kWh in de derde kaart hierboven. Bij een verbruik van 1 kWh is dat het bedrag per wasbeurt; verbruikt jouw programma meer of minder, dan schaalt het bedrag mee. Het verbruik van jouw machine vind je op het energielabel of in de handleiding — wij vullen daar geen getal voor je in.

De bedragen hierboven zijn **kale beursprijzen**. Energiebelasting en inkoopvergoeding komen erbij, maar zijn per kWh gelijk voor elk uur — ze veranderen het *verschil* tussen uren niet. En één wasbeurt verschuiven levert centen op, geen euro's: de winst zit in het patroon over alle apparaten en alle weken van het jaar.

## Praktisch: zo verschuif je zonder erbij te zitten

- Gebruik de **startuitstel- of timerfunctie** van je machine. Vrijwel elke machine van de laatste tien jaar heeft die; je stelt het aantal uren uitstel in en de machine start zelf.
- Slimme machines en slimme stekkers kunnen starten op basis van de uurprijs. Let op: een wasmachine mag je niet met een gewone tijdschakelaar in de stroom onderbreken — gebruik de eigen timer van het apparaat.
- **Laat de machine niet 's nachts of tijdens je afwezigheid onbeheerd draaien.** De brandweer adviseert wasmachines en drogers alleen te gebruiken als er iemand thuis en wakker is; drogers en de pluizen daarin vormen een reëel brandrisico. Kies dan liever een goedkoop blok in de middag of vroege avond dat je zelf meemaakt.
- Zet vaste wasmomenten op de structurele patronen in plaats van dagelijks de prijzen te checken; dat haalt het meeste voordeel binnen zonder moeite.

## Dezelfde logica geldt voor vaatwasser, droger en EV

Wassen is het bekendste voorbeeld, maar de rekenregel is identiek voor de vaatwasser, de droger, het laden van een elektrische auto en het laden van een thuisbatterij — alleen het aantal uren dat je aaneengesloten nodig hebt verschilt. Voor de EV kijk je bijvoorbeeld naar het goedkoopste blok van vier uur.

Alle uurprijzen van vandaag en morgen, plus de actiemomenten voor die langere blokken, staan op onze pagina [stroomprijzen vandaag](/stroomprijzen/). Overweeg je de overstap naar een dynamisch contract, dan zetten we de aanbieders naast elkaar in de [vergelijking van dynamische energiecontracten](/dynamisch-energiecontract-vergelijken/).

<a href="https://go.duurzaamthuislab.nl/frank-energie?ref=/beste-tijd-wasmachine/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk Frank Energie (dynamisch contract) →</a>

## Veelgestelde vragen

**Is 's nachts wassen altijd het goedkoopst?**
Nee. Op zonnige dagen is het middaguur vaak goedkoper dan de nacht, en op stille winterdagen kan het omgekeerd zijn. Daarom staat het goedkoopste blok van vandaag bovenaan deze pagina in plaats van een vast tijdstip.

**Loont het om mijn wasmachine te verschuiven bij een vast contract?**
Voor je stroomkosten niet: bij één tarief betaal je elk uur dezelfde prijs per kWh. Heb je een dubbele meter met nachttarief, dan kan verschuiven wél iets opleveren — check de twee tarieven in je eigen contract.

**Kan ik geld terugkrijgen als de prijs negatief is?**
Bij een dynamisch contract wordt een negatieve beursprijs doorgegeven, maar energiebelasting en inkoopvergoeding blijven staan. Je totale kWh-prijs kan dan heel laag worden en in uitzonderlijke gevallen negatief; hoe dat in jouw contract wordt afgerekend, verschilt per leverancier.
