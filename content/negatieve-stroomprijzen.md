---
title: "Negatieve stroomprijzen 2026: live overzicht en wat het betekent voor zonnepanelen"
description: "Live check op negatieve stroomprijzen vandaag en morgen, plus uitleg wat negatieve uren betekenen voor je dynamische contract en voor het terugleveren van zonnestroom."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
faq:
- q: 'Krijg ik echt geld toe bij een negatieve stroomprijs?'
  a: 'Alleen als de kale beursprijs zo diep onder nul staat dat de energiebelasting en de inkoopvergoeding van je leverancier erdoor gecompenseerd worden. Bij een licht negatieve beursprijs betaal je nog steeds iets per kWh, alleen minder dan gebruikelijk.'
- q: 'Wanneer komen negatieve uren het vaakst voor?'
  a: 'Vooral rond het middaguur op zonnige dagen met een lage vraag — weekenden en feestdagen in het voor- en najaar — en soms ''s nachts bij veel wind. Of het vandaag speelt, zie je in het blok bovenaan deze pagina.'
- q: 'Moet ik mijn zonnepanelen uitzetten bij negatieve prijzen?'
  a: 'Handmatig uitschakelen is zelden nodig en zelden verstandig. Effectiever is de stroom zelf gebruiken of opslaan; wie het invoeden echt wil beperken, regelt dat via de instellingen van de omvormer of een terugleverbegrenzing in plaats van via de schakelaar.'
- q: 'Hoeveel negatieve uren zijn er per jaar eigenlijk?'
  a: 'In ons eigen archief van day-ahead-uurdata komen in 2025 in totaal 212 negatieve uren voor, met mei als drukste maand (59 uur). Vrijwel alles valt tussen maart en september; van oktober tot en met februari staat de teller op nul. De actuele maandtelling staat in de grafiek [hierboven](#negatieve-uren-per-maand-ons-archief) en loopt met elke nieuwe dag mee.'
- q: 'Betalen alle dynamische leveranciers hetzelfde bij negatieve uren?'
  a: 'De uurprijs zelf is voor iedereen dezelfde beursprijs, en alle acht leveranciers in de tabel hierboven geven die in beide richtingen door. Het verschil zit in de opslagen: de inkoop- en verkoopvergoeding per kWh, en of de aanbieder je omvormer automatisch kan uitschakelen bij negatieve uren (Frank Energie en Zonneplan bieden daar een dienst voor). Dat laatste bepaalt in de praktijk meer dan het tarief.'
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

## Negatieve uren per maand (ons archief)

Eén dag zegt weinig. Sinds we de day-ahead-uurdata dagelijks vastleggen, kunnen we tellen hoeveel uren per maand daadwerkelijk onder nul stonden. De staafgrafiek hieronder wordt automatisch bijgewerkt met elke nieuwe dag in ons archief.

<div id="neg-arch" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div id="neg-arch-body" style="color:#888;font-size:.9rem;">laden…</div>
  <p style="color:#666;font-size:.85rem;margin-top:.8rem;">Bron: eigen DuurzaamThuisLab-archief van EPEX day-ahead-uurdata (via EnergyZero), dagelijks bijgewerkt. Aan deze informatie kunnen geen rechten worden ontleend.</p>
</div>

<script>
(function(){
  var MAAND = ['jan','feb','mrt','apr','mei','jun','jul','aug','sep','okt','nov','dec'];
  fetch('https://beheer.wtdigital.nl/api/public/energie-archief?dagen=400')
    .then(function(r){ return r.json(); })
    .then(function(d){
      var dagen = (d && d.dagen) || [];
      if (!dagen.length) throw new Error('leeg');
      var orde = [], som = {};
      dagen.forEach(function(x){
        var k = String(x.datum).slice(0,7);
        if (!(k in som)) { som[k] = 0; orde.push(k); }
        som[k] += (x.stroom_negatieve_uren || 0);
      });
      orde.sort();
      var waarden = orde.map(function(k){ return som[k]; });
      var max = Math.max.apply(null, waarden);
      var totaal = waarden.reduce(function(a,b){ return a+b; }, 0);
      var html = '<div style="font-size:.8rem;color:#666;">Negatieve uren per maand · ' + orde.length + ' maanden · ' + totaal + ' uur totaal</div>';
      html += '<div style="display:flex;flex-direction:column;gap:.35rem;margin-top:.7rem;">';
      orde.forEach(function(k){
        var v = som[k];
        var jr = k.slice(0,4), mnd = MAAND[parseInt(k.slice(5,7),10)-1];
        var breedte = max > 0 ? Math.round(v / max * 100) : 0;
        var kleur = (v === max && max > 0) ? '#0e7490' : (v === 0 ? '#d4d4d4' : '#67a9bb');
        html += '<div style="display:flex;align-items:center;gap:.5rem;font-size:.85rem;">' +
          '<div style="width:74px;color:#666;flex:0 0 74px;">' + mnd + ' ' + jr + '</div>' +
          '<div style="flex:1;background:#eceff1;border-radius:4px;height:16px;overflow:hidden;">' +
            '<div style="width:' + breedte + '%;background:' + kleur + ';height:100%;border-radius:4px;"></div>' +
          '</div>' +
          '<div style="width:64px;text-align:right;color:#333;font-weight:' + (v === max && max > 0 ? '700' : '400') + ';">' + v + ' uur</div>' +
        '</div>';
      });
      html += '</div>';
      document.getElementById('neg-arch-body').innerHTML = html;
    })
    .catch(function(){ document.getElementById('neg-arch-body').innerHTML = '<span style="color:#888;font-size:.9rem;">Kon het archief niet laden.</span>'; });
})();
</script>

Het patroon in die reeks is consistenter dan de dagkoppen suggereren: negatieve uren zijn een lente- en zomerverschijnsel. In de maanden oktober tot en met februari staat de teller in ons archief op nul — de zonproductie is dan te laag om het aanbod door de nulgrens te duwen, ook op windrijke dagen. Vanaf maart loopt het op, met een piek in het voorjaar, en tegen het najaar zakt het weer weg. Over heel 2025 gaat het om 212 negatieve uren, met mei als piekmaand (59 uur); vrijwel alles viel tussen maart en september.

Voor je eigen planning betekent dat twee dingen. Ten eerste: als je een dynamisch contract afsluit om negatieve uren te benutten, gebeurt dat voordeel in een half jaar — de winter draait op gewone prijsverschillen tussen dag en nacht. Ten tweede: precies in die voorjaars- en zomermaanden produceren je zonnepanelen het meest, dus het risico bij teruglevering en de kans bij afname vallen op hetzelfde moment samen.

## Wat doet jouw leverancier met negatieve uren?

Niet elke aanbieder legt dit even duidelijk uit, en de details verschillen. In de tabel hieronder staat per leverancier wat het bedrijf zelf publiceert over negatieve uurprijzen bij afname en bij teruglevering. Peildatum: 20 augustus 2026; controleer de tarieven altijd op de site van de leverancier zelf.

| Leverancier | Negatief uur bij afname | Negatief uur bij teruglevering | Wat de leverancier zelf vermeldt |
|---|---|---|---|
| Tibber | Uurprijs 1-op-1 door: "je krijgt in theorie dan geld toe als je stroom verbruikt" | Ja: "op het moment dat je teruglevert en de beursprijs negatief is, betaal je dat tarief ook" | Verkoopvergoeding € 0,0248/kWh; energiebelasting wordt gesaldeerd, bij teruglevering boven je jaarverbruik geen recht op de energiebelasting ([support.tibber.com](https://support.tibber.com/nl/articles/4669873-salderen-en-terugleveren-bij-tibber)) |
| Frank Energie | Day-ahead-uurprijs 1-op-1 door: "je [betaalt] elk uur het actuele tarief" | Ja: "tijdens negatieve prijzen [moet] je juist betalen voor teruggeleverde stroom" | Dienst Slim Terugleveren schakelt panelen uit bij negatieve marktprijs; op het dynamische contract geen terugleverkosten, de staffelprijzen gelden voor vaste/variabele contracten — bedragen: zie site ([kennisbank](https://www.frankenergie.nl/nl/kennisbank/dynamisch-energiecontract/negatieve-stroomprijzen), [terugleverkosten](https://www.frankenergie.nl/nl/terugleverkosten)) |
| Zonneplan | Uurprijs (kwartierprijs) door | Ja: "bij negatieve uren betalen voor elke kilowattuur (kWh) die je teruglevert" | Zelfde prijs voor teruglevering als voor afname, incl. inkoopvergoeding en belastingen; "bij een dynamisch contract betaal je geen terugleverkosten"; met een Zonneplan-omvormer schakelt die automatisch uit bij negatieve uurprijzen ([zonneplan.nl](https://www.zonneplan.nl/energie/zonnepanelen-en-negatieve-stroomprijzen)) |
| ANWB Energie | Uurprijs door; "je krijgt alsnog geld toe als de stroomprijs lager ligt dan de belasting en de inkoopkosten die je betaalt" | Ja: "op het moment dat de stroomprijs negatief is, betaal je dat tarief ook voor teruggeleverde stroom" | Werkt met het werkelijke uurtarief voor teruggeleverde kWh; rekenvoorbeeld met energiebelasting van 12 cent (2025) waarbij het saldo per saldo positief blijft ([anwb.nl](https://www.anwb.nl/energie/negatieve-stroomprijzen)) |
| easyEnergy | Uurprijs door: "bij een flink negatieve prijs kun je soms echt geld toe krijgen" | Ja: "als de prijs negatief is en jij levert stroom terug, kan het zijn dat je voor teruglevering betaalt" | Noemt als omslagpunt dat je, zolang saldering nog geldt, "eigenlijk pas vanaf 14 cent negatief echt [gaat] betalen" ([easyenergy.com](https://www.easyenergy.com/negatieve-stroomprijzen-uitgelegd)) |
| Eneco Dynamisch | Uurprijs door | Ja: "je ontvangt de actuele marktprijs per uur. Dat tarief kan positief of negatief zijn, afhankelijk van de uurprijzen" | Daarnaast een verkoopvergoeding per kWh over teruggeleverde stroom; vanaf 2027 geldt die over alle teruggeleverde kWh — bedrag: zie site ([eneco.nl klantenservice](https://www.eneco.nl/klantenservice/dynamisch-energiecontract/dynamisch-en-terugleveren/)) |
| Vattenfall FlexPrijs | Uurprijs door: "wanneer het tarief negatief is, ontvang je geld voor de stroom die je verbruikt" | Ja: "lever je tijdens deze uren stroom terug, dan betaal je voor je teruglevering het tarief" | Afname en teruglevering worden per uur tegen elkaar weggestreept (waardesaldering op de jaarafrekening); verkoopvergoeding per kWh geldt als je op jaarbasis méér teruglevert dan verbruikt ([vattenfall.nl](https://www.vattenfall.nl/klantenservice/alles-over-je-dynamische-contract/)) |
| energiedirect | Uurprijs door | Ja | "De negatieve stroomprijs geldt voor zowel afname als teruglevering. Je krijgt dus op dat moment betaald om stroom af te nemen en je moet betalen als je stroom teruglevert." ([energiedirect.nl](https://www.energiedirect.nl/blog/negatieve-stroomprijs)) |

Wat er netto overblijft, hangt niet alleen van dat uur af. Bij **afname** komen energiebelasting en de inkoopvergoeding boven op de beursprijs, dus een licht negatief uur maakt stroom goedkoop maar zelden gratis — je moet flink onder nul zitten voordat er echt geld bij komt. Bij **teruglevering** werkt het omgekeerd: daar is de negatieve uurprijs een kostenpost, terwijl saldering (zolang die geldt) de energiebelasting nog terugbrengt. Dat is precies waarom Tibber, easyEnergy en ANWB in hun voorbeelden op een netto positief bedrag uitkomen bij een licht negatief uur: de gesaldeerde belasting is groter dan het negatieve tarief. Zakt de beursprijs diep genoeg, dan kantelt dat wel.

Heb je een **vast of variabel contract**, dan bestaan uurprijzen voor jou niet: je merkt niets van negatieve uren, in geen van beide richtingen. Het vergelijkbare risico zit daar in de terugleverkosten — een vast bedrag of een staffel op basis van hoeveel je invoedt. Die staffels lopen per leverancier flink uiteen; we hebben ze naast elkaar gezet in [terugleverkosten vergelijken](/terugleverkosten-vergelijken/).

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
