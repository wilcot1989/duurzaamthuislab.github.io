---
title: "Negatieve stroomprijzen 2026: live overzicht en wat het betekent voor zonnepanelen"
description: "Live check op negatieve stroomprijzen vandaag en morgen, plus uitleg wat negatieve uren betekenen voor je dynamische contract en voor het terugleveren van zonnestroom."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
lastmod: 2026-08-20
---

*Disclosure: dit artikel bevat affiliate-links naar energieaanbieders. Sluit je via zo'n link een contract af, dan ontvangen wij mogelijk een commissie — dit kost jou niets extra en beïnvloedt de getoonde prijzen niet: die komen rechtstreeks van de stroombeurs.*

Negatieve stroomprijzen betekenen dat de kale beursprijs voor een uur onder nul staat: wie op dat moment stroom afneemt, krijgt voor die kilowattuurprijs geld toe in plaats van dat hij betaalt. Hieronder staat de live stand voor vandaag en (na circa 15:00) morgen, op basis van de day-ahead-veiling.

<div id="neg-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:.8rem;">
    <div id="neg-vandaag" style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.9rem;"><div style="font-size:.8rem;color:#666;">Vandaag</div><div style="color:#888;font-size:.9rem;">laden…</div></div>
    <div id="neg-morgen" style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.9rem;"><div style="font-size:.8rem;color:#666;">Morgen</div><div style="color:#888;font-size:.9rem;">laden…</div></div>
  </div>
  <p style="color:#666;font-size:.85rem;margin-top:.8rem;">Kale EPEX-prijs incl. btw, excl. energiebelasting en de inkoopvergoeding van je leverancier. Bron: day-ahead-veiling. Alle tijden in Europe/Amsterdam. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

<script>
(function(){
  function uurNL(datum, uurUTC){
    var dt = new Date(datum + 'T' + String(uurUTC).padStart(2,'0') + ':00:00Z');
    return dt.toLocaleTimeString('nl-NL',{timeZone:'Europe/Amsterdam',hour:'2-digit',minute:'2-digit'});
  }
  function render(el, label, d, isMorgen){
    var box = document.getElementById(el);
    if (!d || !d.uren || !d.uren.length){
      box.innerHTML = '<div style="font-size:.8rem;color:#666;">' + label + '</div><div style="color:#888;font-size:.9rem;">' +
        (isMorgen ? 'Morgenprijzen komen rond 15:00 beschikbaar.' : 'Geen data beschikbaar.') + '</div>';
      return;
    }
    var neg = d.uren.filter(function(u){ return u.prijs < 0; });
    var prijzen = d.uren.map(function(u){ return u.prijs; });
    var min = Math.min.apply(null, prijzen);
    var minUren = d.uren.filter(function(u){ return u.prijs === min; }).map(function(u){ return uurNL(d.datum, u.uur); }).join(', ');
    var html = '<div style="font-size:.8rem;color:#666;">' + label + ' · ' + d.datum + '</div>';
    if (neg.length){
      var laagst = Math.min.apply(null, neg.map(function(u){ return u.prijs; }));
      html += '<div style="font-size:1.5rem;font-weight:700;color:#0e7490;">' + neg.length + ' uur onder nul</div>' +
        '<div style="font-size:.9rem;color:#333;margin-top:.3rem;">' + neg.map(function(u){ return uurNL(d.datum, u.uur) + ' (€ ' + u.prijs.toFixed(3) + ')'; }).join(' · ') + '</div>' +
        '<div style="font-size:.8rem;color:#666;margin-top:.4rem;">Laagste: € ' + laagst.toFixed(3) + ' per kWh (kale beursprijs)</div>';
    } else {
      html += '<div style="font-size:1.1rem;font-weight:700;">Geen negatieve uren</div>' +
        '<div style="font-size:.9rem;color:#333;margin-top:.3rem;">Laagste prijs € ' + min.toFixed(3) + ' om ' + minUren + '</div>';
    }
    box.innerHTML = html;
  }
  function laad(url, el, label, isMorgen){
    fetch(url).then(function(r){ return r.json(); }).then(function(d){ render(el, label, d, isMorgen); })
      .catch(function(){ document.getElementById(el).innerHTML = '<div style="font-size:.8rem;color:#666;">' + label + '</div><div style="color:#888;font-size:.9rem;">Kon prijzen niet laden.</div>'; });
  }
  laad('https://beheer.wtdigital.nl/api/public/stroomprijzen', 'neg-vandaag', 'Vandaag', false);
  laad('https://beheer.wtdigital.nl/api/public/stroomprijzen?dag=morgen', 'neg-morgen', 'Morgen', true);
})();
</script>

## Waarom stroom soms minder dan niets kost

Op de day-ahead-veiling wordt elk uur van de volgende dag apart verhandeld. Aanbod en vraag moeten per uur exact op elkaar aansluiten: het net kan stroom niet zelf opslaan. Staat er veel zon en wind ingepland terwijl de vraag laag is — een zonnige zondagmiddag, een windrijke nacht — dan is er meer productie beschikbaar dan afname.

Voor sommige producenten is het dan goedkoper om stroom mét een toeslag kwijt te raken dan om stil te vallen: een grote centrale afschakelen en weer opstarten kost geld en tijd, en subsidie- of contractafspraken kunnen productie lonend maken tot onder de nulgrens. De veilingprijs zakt dus onder nul totdat er genoeg vraag bijkomt of productie afvalt.

Dat dit vaker voorkomt, is structureel: het opgestelde vermogen aan zon en wind is de afgelopen jaren sterk gegroeid, terwijl flexibele afname (batterijen, elektrolyse, slim laden) achterblijft. Zolang die twee uit balans zijn, blijven negatieve uren terugkomen — vooral in het voor- en najaar rond het middaguur.

## De nuance die vaak wegvalt: negatief op de beurs is niet negatief op je rekening

Op de meeste nieuwspagina's zie je alleen de kale beursprijs. Wat jij per kWh betaalt, is die beursprijs plus twee vaste opslagen:

1. **Energiebelasting** — een wettelijk tarief per kWh dat de overheid jaarlijks vaststelt. Dat tarief blijft gewoon staan als de beursprijs onder nul duikt. De actuele bedragen staan bij de Belastingdienst.
2. **Inkoopvergoeding van je leverancier** — de opslag per kWh die je dynamische aanbieder rekent.

Als vuistregel: de kale prijs moet flink onder nul zitten voordat je totaalprijs per kWh onder nul komt. Een uur van min één cent kaal levert dus geen geld op — je betaalt alleen minder dan normaal. Hoe diep het moet zakken, hangt af van het belastingtarief van dat jaar en de opslag in je contract; die twee getallen kun je optellen bij de kale prijs uit het blok hierboven.

Voor teruglevering werkt het spiegelbeeldig: op een dynamisch contract krijg je de beursprijs voor wat je invoedt, en is die negatief, dan betaal jij voor het invoeden — precies op het moment dat je panelen het hardst werken.

## Wat negatieve uren betekenen voor zonnepaneelbezitters

Wie zonnepanelen heeft, merkt negatieve prijzen op twee manieren:

- **Dynamisch contract:** teruglevering in een negatief uur kost geld in plaats van dat het opbrengt. Het gaat om beperkte bedragen per uur, maar het draait de logica om: op de zonnigste momenten is invoeden het minst aantrekkelijk.
- **Vast of variabel contract:** veel leveranciers rekenen terugleverkosten, meestal als een bedrag per maand dat meebeweegt met hoeveel je invoedt. Daar zie je de beursprijs niet, maar zit het risico in dat tarief verwerkt. Wat de aanbieders rekenen, staat in [terugleverkosten zonnepanelen 2026](/posts/terugleverkosten-zonnepanelen-2026/).

Daar komt bij dat de salderingsregeling verdwijnt. Vanaf dat moment bepaalt niet meer je meterstand maar het moment van je verbruik wat een kilowattuur waard is — en dan wegen negatieve middaguren zwaarder mee. De opzet en de gevolgen staan in [saldering stopt in 2027](/posts/saldering-stopt-2027-volledige-gids/).

## Wat je er concreet aan kunt doen

**Verbruik verschuiven.** De eenvoudigste stap kost niets: was, vaatwas, boiler, warmtepomp en het laden van een auto naar de goedkoopste uren van de dag. Welke uren dat zijn, staat per dag op de [live stroomprijzen-pagina](/stroomprijzen/). In negatieve uren is extra verbruik het minst duur — dan is het opladen van de auto letterlijk het beste moment.

**Zelf opslaan in plaats van invoeden.** Een thuisbatterij vangt de middagpiek van je panelen op en gebruikt die stroom in de avond, wanneer de prijs meestal hoog is. Op een dynamisch contract kan dezelfde batterij ook goedkoop (of tegen een toeslag) laden uit het net. Of dat in jouw situatie uitkomt, hangt af van je verbruikspatroon en de spreiding tussen uren; het rekenmodel staat in [dynamisch contract plus thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

**Teruglevering begrenzen.** Veel moderne omvormers kunnen het invoedvermogen beperken of de productie tijdelijk terugregelen, soms automatisch op basis van de uurprijs. Dat kost opbrengst op momenten dat die opbrengst toch niets waard is — vraag je installateur wat jouw omvormer ondersteunt ([waar je op let bij het kiezen](/installateur-kiezen/)).

**Contractvorm heroverwegen.** Een dynamisch contract maakt negatieve uren zichtbaar en bruikbaar, maar legt het uurrisico wel bij jou. Zonder automatisering (batterij, slimme laadsessies, apparaten die je echt verschuift) is het voordeel klein. De aanbieders en hun opbouw staan naast elkaar in onze [vergelijker van dynamische energiecontracten](/dynamisch-energiecontract-vergelijken/).

<a href="https://go.duurzaamthuislab.nl/frank-energie?ref=/negatieve-stroomprijzen/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Bekijk Frank Energie (dynamisch contract) →</a>

## Veelgestelde vragen

**Krijg ik echt geld toe bij een negatieve stroomprijs?**
Alleen als de kale beursprijs zo diep onder nul staat dat de energiebelasting en de inkoopvergoeding van je leverancier erdoor gecompenseerd worden. Bij een licht negatieve beursprijs betaal je nog steeds iets per kWh, alleen minder dan gebruikelijk.

**Wanneer komen negatieve uren het vaakst voor?**
Vooral rond het middaguur op zonnige dagen met een lage vraag — weekenden en feestdagen in het voor- en najaar — en soms 's nachts bij veel wind. Of het vandaag speelt, zie je in het blok bovenaan deze pagina.

**Moet ik mijn zonnepanelen uitzetten bij negatieve prijzen?**
Handmatig uitschakelen is zelden nodig en zelden verstandig. Effectiever is de stroom zelf gebruiken of opslaan; wie het invoeden echt wil beperken, regelt dat via de instellingen van de omvormer of een terugleverbegrenzing in plaats van via de schakelaar.
