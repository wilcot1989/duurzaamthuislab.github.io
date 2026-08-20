---
title: "Terugverdientijd thuisbatterij berekenen (rekentool)"
description: "Bereken de terugverdientijd van je thuisbatterij op basis van capaciteit, aanschafprijs, cycli, prijsspread, rendement en degradatie. Alle aannames zelf aanpasbaar."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
lastmod: 2026-08-20
---

*Disclosure: deze pagina bevat affiliate-links naar batterijfabrikanten. Koop je via zo'n link, dan ontvangen wij mogelijk een commissie — dit kost jou niets extra en heeft geen invloed op de rekentool: die rekent alleen met de waarden die jij invult.*

Hoe lang duurt het voordat een thuisbatterij zichzelf terugbetaalt? Dat hangt af van zes variabelen. Vul ze hieronder in — de tool rekent de jaaropbrengst uit en telt de opbrengst per jaar op tot je de investering eruit hebt, waarbij de capaciteit elk jaar afneemt door degradatie.

De startwaarden zijn **aanpasbare aannames**, geen meetresultaten. Waar ze vandaan komen staat onder elk veld en in de onderbouwing verderop.

<div id="tvt-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.1rem;">
    <div>
      <label for="tvt-cap" style="display:block;font-weight:600;margin-bottom:.3rem;">Batterijcapaciteit (kWh)</label>
      <input id="tvt-cap" type="number" min="1" max="100" step="0.5" value="10" oninput="tvtReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Aanname: 10 kWh, de meest verkochte klasse. Vul je eigen bruikbare capaciteit in.</span>
    </div>
    <div>
      <label for="tvt-prijs" style="display:block;font-weight:600;margin-bottom:.3rem;">Netto aanschafprijs (€)</label>
      <input id="tvt-prijs" type="number" min="0" max="50000" step="50" value="5000" oninput="tvtReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Aanname: € 5.000 inclusief installatie. Trek eventuele subsidie er zelf al af.</span>
    </div>
    <div>
      <label for="tvt-cycli" style="display:block;font-weight:600;margin-bottom:.3rem;">Bruikbare cycli per jaar</label>
      <input id="tvt-cycli" type="number" min="0" max="730" step="5" value="250" oninput="tvtReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Aanname: 250. Een dagelijkse volle cyclus zou 365 zijn; hier gaan vakantie, storingen en dagen met een te vlak prijsverloop eraf.</span>
    </div>
    <div>
      <label for="tvt-spread" style="display:block;font-weight:600;margin-bottom:.3rem;">Gemiddelde prijsspread (€/kWh)</label>
      <input id="tvt-spread" type="number" min="0" max="2" step="0.01" value="0.15" oninput="tvtReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Het verschil tussen het goedkoopste uur waarop je laadt en het duurste uur waarop je ontlaadt — over een heel jaar gemiddeld. Kijk zelf mee op <a href="/stroomprijzen/">dynamische stroomprijzen per uur</a>.</span>
    </div>
    <div>
      <label for="tvt-rend" style="display:block;font-weight:600;margin-bottom:.3rem;">Round-trip-rendement (%)</label>
      <input id="tvt-rend" type="number" min="50" max="100" step="1" value="90" oninput="tvtReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Aanname: 90%. Van elke kWh die je inlaadt komt er 0,9 kWh weer uit; het verschil is omvormer- en batterijverlies. Check het datasheet van je eigen systeem.</span>
    </div>
    <div>
      <label for="tvt-deg" style="display:block;font-weight:600;margin-bottom:.3rem;">Degradatie (% per jaar)</label>
      <input id="tvt-deg" type="number" min="0" max="15" step="0.1" value="2" oninput="tvtReken()" style="width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font:inherit;">
      <span style="font-size:.8rem;color:#666;">Aanname: 2% capaciteitsverlies per jaar. Fabrikanten geven dit vaak indirect op als restcapaciteit na 10 jaar — reken die om en vul in.</span>
    </div>
  </div>
  <div id="tvt-uitkomst" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.8rem;margin-top:1.4rem;"></div>
  <div id="tvt-tabel" style="margin-top:1.2rem;overflow-x:auto;"></div>
  <p style="color:#666;font-size:.85rem;margin-top:.9rem;">Deze tool rekent alleen de <strong>handelsopbrengst</strong> (laden bij een lage prijs, ontladen bij een hoge). Opslag van je eigen zonnestroom zit er niet in; dat is een aparte opbrengstbron met een eigen berekening.</p>
</div>

<script>
function tvtGetal(id, min, max){
  var v = parseFloat(document.getElementById(id).value.replace(',', '.'));
  if (isNaN(v) || v < min || v > max) return null;
  return v;
}

function tvtOpbrengstJaar(cap, cycli, spread, rend, deg, jaar){
  // Bruikbare capaciteit in dit jaar na (jaar-1) jaren degradatie
  var capJaar = cap * Math.pow(1 - deg / 100, jaar - 1);
  return capJaar * cycli * spread * (rend / 100);
}

function tvtTerugverdientijd(cap, prijs, cycli, spread, rend, deg){
  var cum = 0, maxJaren = 30;
  for (var jaar = 1; jaar <= maxJaren; jaar++){
    var opbrengst = tvtOpbrengstJaar(cap, cycli, spread, rend, deg, jaar);
    if (opbrengst <= 0) return null;
    if (cum + opbrengst >= prijs){
      // lineair interpoleren binnen het jaar
      return jaar - 1 + (prijs - cum) / opbrengst;
    }
    cum += opbrengst;
  }
  return null;
}

function tvtReken(){
  var cap    = tvtGetal('tvt-cap', 0.1, 100);
  var prijs  = tvtGetal('tvt-prijs', 0, 50000);
  var cycli  = tvtGetal('tvt-cycli', 0, 730);
  var spread = tvtGetal('tvt-spread', 0, 2);
  var rend   = tvtGetal('tvt-rend', 1, 100);
  var deg    = tvtGetal('tvt-deg', 0, 15);
  var uit = document.getElementById('tvt-uitkomst');
  var tab = document.getElementById('tvt-tabel');

  if (cap === null || prijs === null || cycli === null || spread === null || rend === null || deg === null){
    uit.innerHTML = '<div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.9rem;grid-column:1/-1;color:#b03a3a;">Vul alle velden in met een geldige waarde.</div>';
    tab.innerHTML = '';
    return;
  }

  var jaar1 = tvtOpbrengstJaar(cap, cycli, spread, rend, deg, 1);
  var tvt = tvtTerugverdientijd(cap, prijs, cycli, spread, rend, deg);
  var perCyclus = cap * spread * (rend / 100);

  var tvtTekst = tvt === null
    ? 'niet binnen 30 jaar'
    : tvt.toFixed(1).replace('.', ',') + ' jaar';
  var tvtKleur = (tvt !== null && tvt <= 10) ? '#e8f5ee' : '#fdeeee';
  var tvtRand  = (tvt !== null && tvt <= 10) ? '#b7dfc9' : '#f0c4c4';

  uit.innerHTML =
    '<div style="background:#fff;border-radius:8px;padding:.9rem;border:1px solid #e0e0e0;"><div style="font-size:.8rem;color:#666;">Opbrengst per cyclus</div><div style="font-size:1.3rem;font-weight:700;">€ ' + perCyclus.toFixed(2).replace('.', ',') + '</div><div style="font-size:.75rem;color:#888;">bij volle cyclus</div></div>' +
    '<div style="background:#fff;border-radius:8px;padding:.9rem;border:1px solid #e0e0e0;"><div style="font-size:.8rem;color:#666;">Opbrengst jaar 1</div><div style="font-size:1.3rem;font-weight:700;">€ ' + Math.round(jaar1).toLocaleString('nl-NL') + '</div><div style="font-size:.75rem;color:#888;">per jaar</div></div>' +
    '<div style="background:' + tvtKleur + ';border-radius:8px;padding:.9rem;border:1px solid ' + tvtRand + ';"><div style="font-size:.8rem;color:#444;">Terugverdientijd</div><div style="font-size:1.3rem;font-weight:700;">' + tvtTekst + '</div><div style="font-size:.75rem;color:#666;">incl. degradatie</div></div>';

  // Cumulatief overzicht, eerste 12 jaar
  var rijen = '', cum = 0;
  for (var j = 1; j <= 12; j++){
    var o = tvtOpbrengstJaar(cap, cycli, spread, rend, deg, j);
    cum += o;
    var terug = cum >= prijs;
    rijen += '<tr style="background:' + (terug ? '#e8f5ee' : 'transparent') + ';">' +
      '<td style="padding:.35rem .6rem;border-bottom:1px solid #eee;">' + j + '</td>' +
      '<td style="padding:.35rem .6rem;border-bottom:1px solid #eee;">€ ' + Math.round(o).toLocaleString('nl-NL') + '</td>' +
      '<td style="padding:.35rem .6rem;border-bottom:1px solid #eee;">€ ' + Math.round(cum).toLocaleString('nl-NL') + '</td>' +
      '<td style="padding:.35rem .6rem;border-bottom:1px solid #eee;">' + (terug ? 'terugverdiend' : '€ ' + Math.round(prijs - cum).toLocaleString('nl-NL') + ' te gaan') + '</td></tr>';
  }
  tab.innerHTML = '<table style="width:100%;border-collapse:collapse;font-size:.9rem;background:#fff;border:1px solid #e0e0e0;border-radius:8px;">' +
    '<thead><tr style="background:#f1f3f5;text-align:left;"><th style="padding:.45rem .6rem;">Jaar</th><th style="padding:.45rem .6rem;">Opbrengst</th><th style="padding:.45rem .6rem;">Cumulatief</th><th style="padding:.45rem .6rem;">Status</th></tr></thead><tbody>' +
    rijen + '</tbody></table>';
}
tvtReken();
</script>

## Hoe de tool rekent

De formule is bewust simpel, zodat je hem met de hand kunt controleren:

**Opbrengst in jaar n = capaciteit × (1 − degradatie)^(n−1) × cycli per jaar × prijsspread × round-trip-rendement**

Met de startwaarden: 10 kWh × 250 cycli × € 0,15 × 0,90 = **€ 338 in jaar 1**. Elk volgend jaar is de capaciteit 2% lager, dus de opbrengst ook. De terugverdientijd is het moment waarop de opgetelde opbrengst gelijk is aan de netto aanschafprijs.

Wat er *niet* in zit: rente of inflatie, de kosten van een HEMS of extra hardware, en de opbrengst van het opslaan van eigen zonnestroom. Die laatste is voor veel huishoudens de grootste post — het volledige model met beide opbrengstbronnen naast elkaar staat in [dynamisch energiecontract + thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

## Waar de startwaarden vandaan komen

| Veld | Startwaarde | Herkomst |
|---|---|---|
| Capaciteit | 10 kWh | De meest gangbare klasse voor een gezinswoning; zie onze [vergelijking van 10 kWh-thuisbatterijen](/posts/thuisbatterij-10-kwh-vergelijking-2026/) |
| Netto aanschafprijs | € 5.000 | Aanpasbare aanname voor systeem plus installatie, vóór of ná subsidie afhankelijk van wat jij invult |
| Cycli per jaar | 250 | Aanpasbare aanname: 365 dagen minus vakantie, storingen en dagen met een te vlak prijsverloop |
| Prijsspread | € 0,15/kWh | Het prijsverschil dat wij als uitgangspunt gebruiken in ons [arbitrage-rekenmodel](/posts/dynamische-energiecontracten-thuisbatterij-2026/); controleer het zelf op de [uurprijzen van vandaag](/stroomprijzen/) |
| Round-trip-rendement | 90% | Aanpasbare aanname; het exacte cijfer staat in het datasheet van je batterij en omvormer |
| Degradatie | 2%/jaar | Aanpasbare aanname; fabrikanten geven meestal een restcapaciteit na 10 jaar op, waaruit je dit percentage kunt herleiden |

Geen van deze waarden is een gemeten resultaat van ons. Ze zijn er om mee te beginnen — de uitkomst wordt pas bruikbaar als je ze vervangt door de cijfers uit je eigen offerte, datasheet en energiecontract.

## De eerlijke kanttekening: de spread is de dominante en onzekerste variabele

Verdubbel de prijsspread en de terugverdientijd halveert bijna. Verdubbel het rendement of halveer de degradatie en er verandert relatief weinig. De spread is dus de variabele die alles bepaalt — en het is precies de variabele die je niet vooraf weet.

Waarom die onzekerheid zo groot is:

- **De spread verschilt sterk per seizoen.** Koude, windstille winterdagen leveren forse avondpieken en soms negatieve nachtprijzen; zonnige zomerweken zijn juist vlak. Eén maand meten zegt niets over een jaar.
- **De spread verschilt sterk per jaar.** De volatiliteit op de day-ahead-markt hangt af van gasprijzen, weer en de opgestelde wind- en zoncapaciteit. Dat is geen voorspelbare grootheid.
- **Je haalt nooit de volle theoretische spread.** Je sturing moet het goedkoopste uur vooraf raken, en de belastingen en inkoopvergoeding bovenop de kale beursprijs verkleinen de marge. Kijk daarom naar de all-in prijzen in de app van je leverancier, niet alleen naar de kale EPEX-prijs op onze [stroomprijzenpagina](/stroomprijzen/).

Reken daarom liever met een lage spread als ondergrens en een hoge als bovengrens, en beschouw het verschil als je risicomarge.

## Waarom de saldering-afbouw dit plaatje verandert

De rekentool hierboven gaat alleen over handelen op prijsverschillen. Maar het tweede been van een thuisbatterij — je eigen zonnestroom opslaan in plaats van terugleveren — wordt juist waardevoller naarmate de salderingsregeling verdwijnt. Zolang je onbeperkt kunt salderen, is het net feitelijk een gratis batterij; zonder saldering is het verschil tussen de afnameprijs en de terugleververgoeding pure winst voor elke kWh die je zelf opslaat.

Wie na 2027 rekent, moet dus twee sommen maken: deze arbitragesom, plus de waarde van verhoogd eigen verbruik. Bij elkaar vallen ze aanzienlijk gunstiger uit dan de arbitrage alleen. De uitwerking van beide opbrengstbronnen staat in [dynamisch energiecontract + thuisbatterij](/posts/dynamische-energiecontracten-thuisbatterij-2026/).

## Batterijen die op deze manier te gebruiken zijn

Handelen op uurprijzen kan alleen als je batterij extern aanstuurbaar is — via het platform van de leverancier, een eigen API of Home Assistant. Twee merken met een modulair systeem en een uitleesbare API:

<a href="https://go.duurzaamthuislab.nl/zendure?ref=/terugverdientijd-thuisbatterij/" target="_blank" rel="noopener nofollow sponsored" class="cta-affiliate" style="display:inline-block;background:#0e7490;color:#fff;padding:.7rem 1.4rem;border-radius:8px;text-decoration:none;font-weight:600;margin:.5rem .5rem .5rem 0;">Bekijk Zendure thuisbatterijen →</a>

<a href="https://go.duurzaamthuislab.nl/ecoflow?ref=/terugverdientijd-thuisbatterij/" target="_blank" rel="noopener nofollow sponsored" class="cta-affiliate" style="display:inline-block;background:#0e7490;color:#fff;padding:.7rem 1.4rem;border-radius:8px;text-decoration:none;font-weight:600;margin:.5rem 0;">Bekijk EcoFlow thuisbatterijen →</a>

Vergelijk vóór aankoop altijd de bruikbare capaciteit (niet de bruto), het round-trip-rendement en de garantievoorwaarden op restcapaciteit — dat zijn precies de drie velden die deze rekentool nodig heeft. Onze [vergelijking van 10 kWh-thuisbatterijen](/posts/thuisbatterij-10-kwh-vergelijking-2026/) zet die specificaties naast elkaar.

## Veelgestelde vragen

**Waarom komt de terugverdientijd hier langer uit dan in reclames van leveranciers?**
Omdat deze tool alleen de arbitrageopbrengst rekent en degradatie meeneemt. Verkooprekenvoorbeelden tellen vaak ook de opslag van eigen zonnestroom mee en rekenen met een constante capaciteit.

**Moet ik subsidie van de aanschafprijs aftrekken?**
Ja, vul de prijs in die je uiteindelijk zelf betaalt. Subsidieregelingen en hun voorwaarden veranderen per jaar; controleer de actuele stand bij RVO voordat je een bedrag invult.

**Hoeveel cycli kan een batterij aan?**
Dat staat in het datasheet als aantal volledige cycli of als restcapaciteit na een aantal jaren. Rekent de tool een terugverdientijd uit die langer is dan de gegarandeerde levensduur, dan is dat het signaal: het systeem verdient zich in dit scenario niet terug.

**Kan de spread ook negatief uitpakken?**
Op een dag met een volledig vlak prijsverloop levert een cyclus door het rendementsverlies netto geld op *kosten*. Een goede sturing slaat zulke dagen over — dat is precies waarom het aantal bruikbare cycli lager ligt dan 365.
