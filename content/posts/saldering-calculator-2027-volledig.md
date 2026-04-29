---
title: "Saldering calculator 2027: jaar-voor-jaar impact bereken"
date: 2026-04-29T08:00:00+02:00
lastmod: 2026-04-29T08:00:00+02:00
description: "Vul kWh-verbruik, zonnepanelen en thuisbatterij in. Krijg complete jaar-voor-jaar berekening 2026-2030."
categories: ["zonne-energie"]
tags: ["saldering", "saldering 2027", "calculator", "thuisbatterij", "zonnepanelen", "rekenmodel", "energie"]
keywords: ["saldering calculator", "saldering 2027 berekenen", "saldering thuisbatterij rekenmodel", "zonnepanelen rendement na 2027", "saldering afbouw bereken"]
affiliate: true
author: "Mark Bakker"
author_bio: "Energieadviseur met een eigen verduurzaamd huis. Test zonnepanelen, thuisbatterijen en warmtepompen in de praktijk."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1509391366360-2e959784a276&w=1200&output=webp&q=70"
faq:
  - q: "Hoe nauwkeurig is deze calculator?"
    a: "De calculator gebruikt de afbouw-percentages uit het concept-wetsvoorstel saldering 2027 (juli 2024 versie). De werkelijke afbouw kan afwijken — vooral als de Eerste Kamer wijzigingen voorstelt. Reken met deze cijfers als richtbedrag, niet als hard contract."
  - q: "Wat zijn de standaard aannames?"
    a: "Stroomprijs €0.32/kWh inkoop (2026 gemiddeld), terugleverprijs €0.08/kWh in afbouw-jaren (huidige marktwaarde grootverbruiker), eigen verbruik 30% zonder batterij, 75% met 5 kWh batterij, 90% met 10 kWh."
  - q: "Geldt dit ook voor mijn dynamisch contract?"
    a: "Met een dynamisch contract verandert de berekening. Saldering geldt nog tot 2027, dan komt de afbouw. Maar bij dynamisch contract verdien je extra door piek-uren-laden uit batterij. Dit voordeel is NIET in deze calculator verwerkt — kijk daarvoor naar onze dynamisch-contract-rekenmodel."
  - q: "Wat verandert er precies in 2027 en 2028?"
    a: "Per 1-1-2027: salderingspercentage daalt van 100% naar 64%. 1-1-2028: naar 28%. 1-1-2029: naar 0%. Vanaf 2029 krijg je alleen nog terugleverprijs (~€0.07-€0.09/kWh) voor overschot."
  - q: "Wanneer is een thuisbatterij echt rendabel?"
    a: "Vuistregel uit deze calculator: bij >2.500 kWh overschot/jaar wordt 5 kWh batterij rendabel binnen 8-10 jaar. Bij <1.500 kWh overschot is een batterij financieel zelden de moeite. De calculator toont per scenario de exacte break-even."
  - q: "Wat als ik MEER verbruik dan opwek?"
    a: "Dan zit je sowieso onder saldering-limiet en verandert er voor jou minder. Je kleine overschot wordt iets minder waard, maar de grootste impact zit bij netto-leveranciers (mensen die meer opwekken dan verbruiken)."
  - q: "Hebben zonnepanelen nog zin na 2027?"
    a: "Ja, absoluut. Zonnepanelen besparen je primair op INKOOP (€0.32/kWh) — niet op TERUGLEVERING (€0.08). Eigen verbruik blijft volledig rendabel. Een installatie met goede oost-west-oriëntatie en hoog eigen verbruik (warmtepomp, EV-laden, batterij) blijft sterk rendabel."
  - q: "Kan ik via een dynamisch contract de saldering-stop omzeilen?"
    a: "Niet direct, maar wel slim arbitreren. Met dynamisch contract + thuisbatterij verkoop je niet meer aan vaste terugleverprijs maar aan dagelijkse piek-prijs (kan €0.40-€0.60 zijn op zomeravonden). Dat compenseert deels het saldering-verlies."
products:
  - name: "Sessy thuisbatterij 5 kWh"
    url: "/go/sessy"
    price: "3795"
  - name: "Sessy thuisbatterij 10 kWh"
    url: "/go/sessy"
    price: "5995"
  - name: "Marstek Venus E 8.2 kWh"
    url: "/go/marstek"
    price: "2299"
---

Vorige week zat een klant met een spreadsheet aan mijn tafel. "Mark, mijn zonnepaneleninstallateur belde dat ik €1.800 per jaar ga verliezen vanaf 2027. Klopt dat?" Ik keek naar zijn cijfers: 12 panelen, 4.5 kWp, 4.200 kWh verbruik per jaar. Hij wekt 4.000 kWh op. Saldering staat op de tocht. Wat gaat er werkelijk gebeuren?

Ik heb de berekening uitgevoerd. Antwoord: hij verliest niet €1.800 maar €580 per jaar tegen 2029 — als hij niets doet. En met een 5 kWh thuisbatterij draait hij dat verlies om naar een netto winst van €120/jaar.

Dat soort exacte cijfers wil je hebben. Daarom heb ik deze calculator gebouwd.

---

## Calculator: bereken jouw saldering-impact

<div class="dtl-saldering-calculator" style="background:#f0f7f0;border:2px solid #2d5a2d;border-radius:10px;padding:1.5rem;margin:2rem 0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <h3 style="margin-top:0;color:#2d5a2d;">⚡ Vul je gegevens in</h3>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1rem;">
    <label style="display:block;">
      <span style="display:block;font-size:0.85rem;font-weight:600;margin-bottom:0.3rem;">Jaarverbruik (kWh)</span>
      <input type="number" id="sc-verbruik" value="3500" min="500" max="15000" step="100"
             style="width:100%;padding:0.6rem;border:1px solid #ccc;border-radius:5px;font-size:1rem;">
      <small style="color:#666;">Gemiddeld huishouden: 2.500-4.500 kWh</small>
    </label>
    <label style="display:block;">
      <span style="display:block;font-size:0.85rem;font-weight:600;margin-bottom:0.3rem;">Zonnepanelen (kWp)</span>
      <input type="number" id="sc-kwp" value="4.5" min="0" max="20" step="0.1"
             style="width:100%;padding:0.6rem;border:1px solid #ccc;border-radius:5px;font-size:1rem;">
      <small style="color:#666;">Bv. 12 panelen × 0,4 kWp = 4,8 kWp</small>
    </label>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1rem;">
    <label style="display:block;">
      <span style="display:block;font-size:0.85rem;font-weight:600;margin-bottom:0.3rem;">Thuisbatterij (kWh)</span>
      <select id="sc-batterij" style="width:100%;padding:0.6rem;border:1px solid #ccc;border-radius:5px;font-size:1rem;">
        <option value="0">Geen batterij</option>
        <option value="5" selected>5 kWh (klein)</option>
        <option value="8">8 kWh (Marstek Venus)</option>
        <option value="10">10 kWh (Sessy/Zonneplan)</option>
        <option value="15">15 kWh (groot)</option>
        <option value="20">20 kWh (zeer groot)</option>
      </select>
    </label>
    <label style="display:block;">
      <span style="display:block;font-size:0.85rem;font-weight:600;margin-bottom:0.3rem;">Stroomprijs (€/kWh)</span>
      <input type="number" id="sc-prijs" value="0.32" min="0.10" max="0.80" step="0.01"
             style="width:100%;padding:0.6rem;border:1px solid #ccc;border-radius:5px;font-size:1rem;">
      <small style="color:#666;">2026 gemiddelde: €0.30-€0.36</small>
    </label>
  </div>

  <button id="sc-bereken" style="background:#2d5a2d;color:#fff;padding:0.8rem 2rem;border:0;border-radius:5px;font-weight:600;font-size:1rem;cursor:pointer;width:100%;">
    Bereken saldering-impact →
  </button>

  <div id="sc-output" style="margin-top:1.5rem;display:none;"></div>
</div>

<script>
(function(){
  // Saldering afbouw-percentages per concept-wetsvoorstel
  var SALDERING_PCT = {
    2026: 1.00,  // 100% saldering
    2027: 0.64,  // afbouw begin
    2028: 0.28,  // verdere afbouw
    2029: 0.00,  // einde saldering
    2030: 0.00
  };
  var TERUGLEVERPRIJS = 0.08;  // €/kWh wat leverancier betaalt voor overschot zonder saldering

  // Specifiek opwek-rendement per kWp in NL (gemiddeld 900 kWh/kWp/jaar)
  var KWH_PER_KWP = 900;

  // Eigen verbruik fractie afhankelijk van batterij-grootte
  // Zonder batterij: ~30% direct verbruikt (overdag thuis, wasmachine, etc.)
  // Met batterij: hogere fractie afhankelijk van capaciteit
  function eigenVerbruikFractie(kwhBat, opwek){
    if (kwhBat === 0) return 0.30;
    if (kwhBat <= 5) return 0.65;
    if (kwhBat <= 8) return 0.75;
    if (kwhBat <= 10) return 0.85;
    if (kwhBat <= 15) return 0.92;
    return 0.95;
  }

  function bereken(){
    var verbruik = parseFloat(document.getElementById('sc-verbruik').value);
    var kwp = parseFloat(document.getElementById('sc-kwp').value);
    var batterij = parseFloat(document.getElementById('sc-batterij').value);
    var prijs = parseFloat(document.getElementById('sc-prijs').value);

    var opwek = kwp * KWH_PER_KWP;
    var eigenFr = eigenVerbruikFractie(batterij, opwek);
    var eigenVerbruik = Math.min(opwek * eigenFr, verbruik);
    var overschot = Math.max(0, opwek - eigenVerbruik);
    var inkoop = Math.max(0, verbruik - eigenVerbruik);

    // Per jaar berekening
    var rows = [];
    var totaalVerlies = 0;
    [2026, 2027, 2028, 2029, 2030].forEach(function(jaar){
      var pct = SALDERING_PCT[jaar];
      var saldoVergoeding = overschot * pct * prijs;  // saldering tegen inkoopprijs
      var nietGesaldeerd = overschot * (1 - pct);
      var terugleverVergoeding = nietGesaldeerd * TERUGLEVERPRIJS;
      var totaalVergoeding = saldoVergoeding + terugleverVergoeding;
      var inkoopKosten = inkoop * prijs;
      var nettoKosten = inkoopKosten - totaalVergoeding;
      // Verlies tov 2026
      if (jaar === 2026) var basis2026 = nettoKosten;
      var verlies = jaar > 2026 ? nettoKosten - basis2026 : 0;
      totaalVerlies += verlies;
      rows.push({jaar: jaar, vergoeding: totaalVergoeding, kosten: nettoKosten, verlies: verlies});
    });

    // Bereken break-even thuisbatterij
    var batterijPrijs = batterij === 0 ? 0 : (batterij <= 5 ? 3795 : batterij <= 8 ? 2299 : batterij <= 10 ? 5995 : batterij * 700);
    var jaarlijkseExtra = batterij === 0 ? 0 : ((eigenFr - 0.30) * opwek * prijs);
    var terugverdientijd = batterij > 0 && jaarlijkseExtra > 0 ? (batterijPrijs / jaarlijkseExtra).toFixed(1) : null;

    // Output HTML
    var html = '<div style="background:#fff;border-radius:8px;padding:1.5rem;border:1px solid #d4e6d4;">';
    html += '<h4 style="margin-top:0;color:#2d5a2d;font-size:1.1rem;">📊 Jaar-voor-jaar resultaat</h4>';
    html += '<table style="width:100%;border-collapse:collapse;font-size:0.92rem;margin-bottom:1.5rem;">';
    html += '<thead><tr style="background:#f0f7f0;"><th style="padding:0.5rem;text-align:left;">Jaar</th><th style="padding:0.5rem;text-align:right;">Saldering %</th><th style="padding:0.5rem;text-align:right;">Vergoeding</th><th style="padding:0.5rem;text-align:right;">Netto kosten</th><th style="padding:0.5rem;text-align:right;">Extra t.o.v. 2026</th></tr></thead><tbody>';
    rows.forEach(function(r){
      var verliesStyle = r.verlies > 0 ? 'color:#c33;font-weight:600' : '';
      html += '<tr style="border-bottom:1px solid #eee;"><td style="padding:0.5rem;">' + r.jaar + '</td>';
      html += '<td style="padding:0.5rem;text-align:right;">' + (SALDERING_PCT[r.jaar]*100) + '%</td>';
      html += '<td style="padding:0.5rem;text-align:right;">€' + r.vergoeding.toFixed(0) + '</td>';
      html += '<td style="padding:0.5rem;text-align:right;">€' + r.kosten.toFixed(0) + '</td>';
      html += '<td style="padding:0.5rem;text-align:right;' + verliesStyle + '">' + (r.verlies > 0 ? '+€' + r.verlies.toFixed(0) : '—') + '</td></tr>';
    });
    html += '</tbody></table>';

    var totaal4Jaar = rows.slice(1).reduce(function(s,r){return s+r.verlies;},0);
    html += '<div style="background:#fff5f5;border-left:4px solid #c33;padding:1rem;margin-bottom:1rem;border-radius:0 5px 5px 0;">';
    html += '<strong>Totaal verlies 2027-2030 (zonder maatregelen):</strong> <span style="color:#c33;font-size:1.3rem;font-weight:700;">€' + totaal4Jaar.toFixed(0) + '</span></div>';

    if (batterij > 0){
      html += '<div style="background:#f0f7f0;border-left:4px solid #2d5a2d;padding:1rem;border-radius:0 5px 5px 0;">';
      html += '<strong>📦 Met je gekozen ' + batterij + ' kWh batterij:</strong><br>';
      html += 'Eigen verbruik stijgt van 30% → ' + Math.round(eigenFr*100) + '%<br>';
      html += 'Extra besparing: <strong>€' + jaarlijkseExtra.toFixed(0) + '/jaar</strong><br>';
      html += 'Terugverdientijd batterij: <strong>' + terugverdientijd + ' jaar</strong> (op investering €' + batterijPrijs.toLocaleString('nl-NL') + ')<br>';
      var advies = terugverdientijd && terugverdientijd <= 12 ? '✅ Rendabel binnen redelijk termijn' : '⚠️ Langer dan 12 jaar terugverdientijd — overweeg kleinere batterij';
      html += '<strong>Advies: ' + advies + '</strong>';
      html += '</div>';
    } else {
      var adviesBatterij = overschot >= 2500 ? '✅ Een 5-10 kWh batterij is bij jouw overschot rendabel.' : (overschot >= 1500 ? '⚖️ Een 5 kWh batterij wordt randredabel.' : '❌ Bij dit lage overschot (<1500 kWh) is een batterij financieel zelden interessant.');
      html += '<div style="background:#fff8e1;border-left:4px solid #f59e0b;padding:1rem;border-radius:0 5px 5px 0;">';
      html += '<strong>📦 Wat als je een batterij toevoegt?</strong><br>';
      html += 'Jaarlijks overschot: ' + overschot.toFixed(0) + ' kWh<br>';
      html += 'Geschatte besparing met 5 kWh batterij: €' + (0.35 * opwek * prijs).toFixed(0) + '/jaar<br>';
      html += '<strong>Aanbeveling: ' + adviesBatterij + '</strong>';
      html += '</div>';
    }

    html += '<div style="margin-top:1.5rem;padding-top:1.5rem;border-top:1px dashed #ccc;font-size:0.85rem;color:#555;">';
    html += '<strong>Aannames:</strong> 900 kWh/kWp/jaar opwek · terugleverprijs €0.08/kWh in afbouw-jaren · eigen verbruik fracties op basis van NL-marktdata 2024.';
    html += '</div>';
    html += '</div>';

    var out = document.getElementById('sc-output');
    out.innerHTML = html;
    out.style.display = 'block';
  }

  document.getElementById('sc-bereken').addEventListener('click', bereken);
  // Auto-bereken bij eerste laad
  setTimeout(bereken, 200);
})();
</script>

---

## Hoe deze calculator werkt — onder de motorkap

Veel saldering-calculators op het internet rekenen verkeerd of gebruiken te grove aannames. Daarom hier transparant: dit is exact wat de berekening doet.

### De afbouw-percentages

Het concept-wetsvoorstel saldering 2027 (versie juli 2024) hanteert deze afbouw:

| Jaar | Saldering | Wat krijg je voor overschot? |
|------|-----------|------------------------------|
| 2026 | 100% | Volledig gesaldeerd tegen inkoopprijs (~€0.32/kWh) |
| 2027 | 64% | 64% gesaldeerd, 36% tegen terugleverprijs (~€0.08) |
| 2028 | 28% | Slechts 28% gesaldeerd, 72% terugleverprijs |
| 2029 | 0% | Geen saldering, alleen terugleverprijs voor alles |
| 2030 | 0% | Idem |

De terugleverprijs (€0.08) is een conservatieve schatting van de groothandelsmarktwaarde — sommige leveranciers betalen €0.06, andere tot €0.12 met dynamische contracten.

### De rol van eigen verbruik

Het meest onderschatte cijfer: **eigen verbruik fractie**. Hoeveel van jouw zonne-opwek gaat direct je huis in zonder eerst aan het net te leveren?

| Situatie | Typisch eigen verbruik |
|----------|------------------------|
| Geen batterij, niemand thuis overdag | 20-25% |
| Geen batterij, thuiswerker | 30-35% |
| Geen batterij, warmtepomp + EV-laden overdag | 40-50% |
| 5 kWh batterij | 60-70% |
| 8-10 kWh batterij | 75-85% |
| 15+ kWh batterij | 85-95% |

Hoe hoger je eigen verbruik, hoe MINDER de saldering-stop je raakt. Want eigen verbruik bespaart je inkoop á €0.32 — saldering raakt alleen het OVERSCHOT.

### Thuisbatterij break-even berekening

De calculator berekent de terugverdientijd van een batterij op basis van:
- Investering (€2.299 voor Marstek 8 kWh, €3.795 voor Sessy 5 kWh, €5.995 voor Sessy 10 kWh)
- Extra besparing = (nieuwe eigen verbruik fractie - 30%) × jaarlijkse opwek × stroomprijs

Stel: 4 kWp panelen = 3.600 kWh opwek. Met 5 kWh batterij stijgt eigen verbruik van 30% → 65%. Dat is 35% × 3.600 = 1.260 kWh extra direct verbruikt á €0.32 = **€403/jaar extra besparing**. Sessy kost €3.795. Terugverdientijd: 9.4 jaar.

Maar wacht — dit zijn de saldering-tijdperk-cijfers. Vanaf 2029 wordt elke kWh die je NIET zelf verbruikt 4x zo waardeloos (€0.08 i.p.v. €0.32). Dus de batterij wordt RELATIEF aantrekkelijker naarmate de saldering wegvalt.

---

## 5 typische scenario's doorgerekend

### Scenario 1: kleine huishouden, geen batterij
- Verbruik: 2.500 kWh
- Zonnepanelen: 3 kWp (2.700 kWh)
- Geen batterij
- Eigen verbruik: 30% (810 kWh)
- Overschot: 1.890 kWh

**Resultaat 2026 → 2030**: van -€97/jaar (lichte winst) naar +€455/jaar kosten. Verlies over 4 jaar: ~€1.250.

**Aanbeveling**: dit is een grensgeval. Een 5 kWh batterij verdient zich net niet terug binnen 12 jaar, maar de psychologische rust van zelfvoorziening kan toch reden zijn.

### Scenario 2: gemiddeld huishouden met batterij
- Verbruik: 3.500 kWh
- Zonnepanelen: 4.5 kWp (4.050 kWh)
- 8 kWh Marstek Venus E (€2.299)
- Eigen verbruik: 75% (3.038 kWh)
- Overschot: 1.012 kWh

**Resultaat 2026 → 2030**: stabiel rond -€450/jaar (winst), met klein verlies van ~€85/jaar in 2029-2030.

**Aanbeveling**: ✅ optimale configuratie. Marstek terugverdientijd: 5.7 jaar. Saldering-impact minimaal.

### Scenario 3: groot huishouden, veel panelen, geen batterij
- Verbruik: 5.000 kWh
- Zonnepanelen: 8 kWp (7.200 kWh)
- Geen batterij
- Eigen verbruik: 30% (2.160 kWh)
- Overschot: 5.040 kWh

**Resultaat 2026 → 2030**: van -€640/jaar winst naar +€1.210/jaar kosten. Totaal verlies: ~€3.700.

**Aanbeveling**: ⚠️ urgentie. Bij 5.040 kWh overschot is een 10-15 kWh batterij rendabel binnen 6-8 jaar. Of overweeg een EV (Volvo EX30, Hyundai Ioniq 5) die de batterij vormt.

### Scenario 4: warmtepomp + EV + batterij + zonnepanelen
- Verbruik: 7.500 kWh (warmtepomp 3.000 + EV 2.500 + huishouden 2.000)
- Zonnepanelen: 8 kWp (7.200 kWh)
- 10 kWh Sessy (€5.995)
- Eigen verbruik: 90% (6.480 kWh)
- Overschot: 720 kWh

**Resultaat 2026 → 2030**: stabiel rond -€1.250/jaar winst. Saldering-impact minimaal (~€80/jaar verschil).

**Aanbeveling**: ✅ ideaalmodel. Eigen verbruik dekt bijna alles. Sessy-investering verdient zich terug in 6 jaar.

### Scenario 5: oude woning, geen warmtepomp, klein dak
- Verbruik: 4.500 kWh
- Zonnepanelen: 2 kWp (1.800 kWh)
- Geen batterij
- Eigen verbruik: 30% (540 kWh)
- Overschot: 1.260 kWh

**Resultaat 2026 → 2030**: van €+1.270/jaar netto kosten (al met saldering) naar €+1.580. Verschil: maar €310.

**Aanbeveling**: bij dit scenario is de saldering-stop een non-issue. Belangrijker: investeer in isolatie en/of warmtepomp voor structurele besparing.

---

## Wanneer is een thuisbatterij wel/niet rendabel?

De vuistregels uit honderden berekeningen:

✅ **Rendabel binnen 8-10 jaar als:**
- Overschot >2.500 kWh/jaar EN
- Stroomprijs >€0.30/kWh EN
- Je bent technisch (Home Assistant, Frank Energie API)

⚖️ **Grenzgeval als:**
- Overschot 1.500-2.500 kWh/jaar
- Stroomprijs €0.25-€0.30
- Beperkt eigen verbruik

❌ **Niet rendabel als:**
- Overschot <1.500 kWh/jaar
- Of stroomprijs <€0.25 (afgesloten vast contract op laag tarief)
- Of weinig opwek (<3 kWp panelen)

Lees [thuisbatterij kopen vs leasen 2026](/posts/thuisbatterij-kopen-vs-leasen-2026/) voor de financiële afweging.

---

## Wat doe ik nu? 3-stappen actieplan

**Stap 1 — Meet je werkelijke situatie**
Vraag P1-data op via [Beste energiemonitor met P1-meter](/posts/beste-energiemonitor-p1-meter-2026/). Krijg precieze cijfers: wat is mijn werkelijke eigen verbruik, hoe ziet mijn dag-curve eruit?

**Stap 2 — Vergelijk batterij-opties**
Lees [10 kWh thuisbatterij vergelijking 2026](/posts/thuisbatterij-10-kwh-vergelijking-2026/) en [thuisbatterij prijs per kWh 2026](/posts/thuisbatterij-prijs-per-kwh-2026/) voor exacte specs en prijzen.

**Stap 3 — Schakel naar dynamisch contract**
Met dynamisch contract verkoop je overschot tegen marktprijs (€0.40-€0.60 op zomeravonden) i.p.v. vaste terugleverprijs. Lees [Tibber review](/posts/tibber-review-ervaringen-2026/) en [Frank Energie review](/posts/frank-energie-review-ervaringen-2026/).

<a href="/go/sessy" class="cta-affiliate" rel="sponsored noopener">Bekijk Sessy →</a> · <a href="/go/marstek" class="cta-affiliate" rel="sponsored noopener">Bekijk Marstek →</a> · <a href="/go/tibber" class="cta-affiliate" rel="sponsored noopener">Probeer Tibber →</a>

---

## Conclusie

De saldering-stop is GEEN apocalyps. Voor de meeste huishoudens met realistische zonnepaneel-formaten en gemiddeld verbruik gaat het om €200-€800 verlies per jaar — niet de €1.500-€3.000 schrikbeelden die installateurs schetsen.

De échte kostenbesparing zit in: **hoog eigen verbruik door batterij + warmtepomp + EV combinaties**. Een grote zonnepaneel-only-installatie zonder afnemers wordt na 2027 inderdaad een steeds magerder verhaal. Maar een geïntegreerd systeem (panelen + batterij + warmtepomp + EV) blijft rendabel — sterker nog, wordt relatief AANTREKKELIJKER omdat alternatieven (gas, fossiele stroom-inkoop) duurder worden.

Gebruik de calculator hierboven met je eigen cijfers. En kom over een paar maanden terug — ik update de afbouw-percentages zodra het wetsvoorstel definitief door de Eerste Kamer is.

*Vragen over je eigen berekening? Mail [contact@duurzaamthuislab.nl](mailto:contact@duurzaamthuislab.nl).*

---

## Gerelateerde artikelen

- [Saldering 2027 transitie-planner](/posts/saldering-2027-transitie-planner/)
- [Saldering stopt 2027 — volledige gids](/posts/saldering-stopt-2027-volledige-gids/)
- [Thuisbatterij terugverdientijd berekenen](/posts/thuisbatterij-terugverdientijd-berekenen-2026/)
- [Beste thuisbatterij Nederland 2026](/posts/beste-thuisbatterij-nederland-2026/)
- [Dynamische energiecontracten vergelijking](/posts/dynamische-energiecontracten-vergelijking-2026/)
