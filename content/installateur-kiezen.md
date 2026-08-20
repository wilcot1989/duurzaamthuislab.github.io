---
title: "Zonnepanelen- of warmtepomp-installateur kiezen: keuzehulp"
description: "Interactieve keuzehulp: vink af wat je installateur aantoonbaar op orde heeft en zie direct waar het risico zit. Zeven criteria die je allemaal zelf kunt controleren."
layout: "single"
author: Team DuurzaamThuisLab
author_bio: Team DuurzaamThuisLab schrijft datagedreven over zonnepanelen, thuisbatterijen en warmtepompen — op basis van specificaties, publieke data en narekenbare modelberekeningen.
faq:
- q: 'Is een erkenning wettelijk verplicht?'
  a: 'Erkenningsregelingen zijn in de regel vrijwillig, maar niet zonder gevolgen: verzekeraars en subsidieregelingen kunnen als voorwaarde stellen dat het werk door een erkend bedrijf is uitgevoerd. Controleer daarom vóór de opdracht welke eis er in jouw geval geldt — bij de subsidieverstrekker en bij je woonverzekering.'
- q: 'Wat als een installateur geen referentieadressen wil geven?'
  a: 'Dat mag hij weigeren met een beroep op privacy van klanten. Vraag dan om een geanonimiseerd opleveringsdossier of foto''s van vergelijkbare projecten met datum. Wie helemaal niets kan laten zien, geeft daarmee zelf het antwoord.'
- q: 'Hoeveel aanbetaling is te veel?'
  a: 'Er is geen wettelijk maximum voor particuliere opdrachten van dit type, dus het is een onderhandelpunt. Het principe dat je vasthoudt: het bedrag dat je vooruitbetaalt is het bedrag dat je kunt kwijtraken. Zorg dat een substantieel deel pas na oplevering wordt betaald.'
- q: 'Moet ik de installatie zelf opleveren?'
  a: 'Ja, en leg vast wat "opgeleverd" betekent: systeem werkt, monitoring gekoppeld en uitleesbaar, documentatie en garantiebewijzen overhandigd, en bij een warmtepomp de inregelgegevens vastgelegd. Zonder die laatste heb je later geen referentiepunt als het rendement tegenvalt.'
lastmod: 2026-08-20
---

*Disclosure: deze pagina bevat affiliate-links naar een offerteplatform. Vraag je daar een offerte aan, dan ontvangen wij mogelijk een vergoeding — dit kost jou niets extra en heeft geen invloed op de criteria in de checklist: die zijn allemaal zelfstandig verifieerbaar.*

De meeste klachten over zonnepanelen- en warmtepompinstallaties gaan niet over het product, maar over de installatie: een verkeerd gedimensioneerd systeem, werk dat niet volgens de normen is aangesloten, of een bedrijf dat na de aanbetaling niet meer opneemt. Het goede nieuws is dat je de belangrijkste risico's vóór het ondertekenen kunt uitsluiten — met vragen waarop het antwoord controleerbaar is.

Vink hieronder aan wat je installateur **aantoonbaar** heeft. Niet wat hij zegt: wat je zelf kunt narekenen in een register, in de offerte of bij een referentie.

<div id="ik-tool" style="background:#f8f9fa;border:1px solid #e0e0e0;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
  <div id="ik-lijst"></div>
  <div id="ik-uitkomst" style="margin-top:1.3rem;"></div>
  <button onclick="ikReset()" style="margin-top:1rem;padding:.45rem 1rem;border-radius:8px;border:1px solid #0e7490;background:#fff;color:#0e7490;cursor:pointer;font:inherit;">Opnieuw beginnen</button>
</div>

<script>
var ikCriteria = [
  {
    id: 'kvk',
    gewicht: 2,
    titel: 'Inschrijving bij de KvK én aantoonbare vergelijkbare projecten',
    uitleg: 'Vraag het KvK-nummer en zoek het op in het Handelsregister: bestaat het bedrijf, hoe lang, en klopt de bedrijfsactiviteit? Vraag daarnaast twee of drie adressen van vergelijkbare installaties uit de afgelopen twee jaar en bel er minstens één na.'
  },
  {
    id: 'certificering',
    gewicht: 2,
    titel: 'Een erkenning of certificering die je zélf in een register kunt terugvinden',
    uitleg: 'In Nederland beheert de stichting InstallQ erkenningsregelingen voor onder meer zonnestroomsystemen (pv) en warmtepompinstallaties; voor het bovengrondse deel van een bodemgebonden warmtepomp geldt de certificering BRL 6000-21. Vraag om de exacte naam van de regeling waaronder het bedrijf valt en zoek dat bedrijf op in het register van de betreffende regeling. Ook lidmaatschap van een branchevereniging zoals Techniek Nederland is te controleren. Wat níet controleerbaar is — een logo op de website zonder registratienummer — telt hier niet mee.'
  },
  {
    id: 'garantie',
    gewicht: 2,
    titel: 'Garantie op het installatiewerk, schriftelijk en los van de productgarantie',
    uitleg: 'Productgarantie komt van de fabrikant en geldt voor het paneel, de omvormer of de warmtepomp. Garantie op het werk — montage, bekabeling, meterkast, waterzijdig inregelen — komt van de installateur en staat er vaak niet automatisch bij. Laat beide termijnen apart en op papier benoemen, inclusief wat er gebeurt als het installatiebedrijf ophoudt te bestaan.'
  },
  {
    id: 'offerte',
    gewicht: 2,
    titel: 'Gespecificeerde offerte in plaats van één totaalbedrag',
    uitleg: 'Een bruikbare offerte noemt per post: merk en type van alle hoofdcomponenten met aantallen, montagemateriaal, arbeid, eventueel meterkast- of groepenkastwerk, en de btw-behandeling. Zonder specificatie kun je twee offertes niet vergelijken en kun je later niet aantonen wat je hebt gekocht.'
  },
  {
    id: 'aanbetaling',
    gewicht: 3,
    titel: 'Aanbetaling van maximaal circa 30%, rest na oplevering',
    uitleg: 'Een beperkte aanbetaling voor materiaalinkoop is gebruikelijk. Volledige vooruitbetaling betekent dat jij het hele risico draagt als het bedrijf niet levert of failliet gaat. Spreek af dat het slotbedrag pas na een geslaagde oplevering betaald wordt — en leg dat vast in de opdrachtbevestiging, niet mondeling.'
  },
  {
    id: 'reviews',
    gewicht: 1,
    titel: 'Reviews die controleerbaar zijn buiten de eigen website',
    uitleg: 'Beoordelingen op de eigen site zijn geselecteerd. Zoek de bedrijfsnaam op onafhankelijke reviewplatforms en let vooral op hoe het bedrijf reageert op klachten en op wat er in de één- en tweesterrenreviews staat — daar zit de informatie.'
  },
  {
    id: 'schouw',
    gewicht: 1,
    titel: 'Een fysieke of onderbouwde schouw vóór de definitieve prijs',
    uitleg: 'Bij zonnepanelen gaat het om dakconstructie, schaduw en de staat van de meterkast; bij een warmtepomp om de warmtevraag, de afgiftetemperatuur en de isolatiestand. Een prijs die zonder enige inventarisatie tot stand komt, is een schatting die tijdens de installatie nog kan veranderen.'
  }
];

var ikMax = ikCriteria.reduce(function(a, c){ return a + c.gewicht; }, 0);

function ikRender(){
  document.getElementById('ik-lijst').innerHTML = ikCriteria.map(function(c){
    return '<label for="ik-' + c.id + '" style="display:block;background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:.9rem 1rem;margin-bottom:.7rem;cursor:pointer;">' +
      '<span style="display:flex;gap:.7rem;align-items:flex-start;">' +
      '<input id="ik-' + c.id + '" type="checkbox" onchange="ikReken()" style="margin-top:.25rem;width:1.1rem;height:1.1rem;flex:0 0 auto;">' +
      '<span><strong>' + c.titel + '</strong><br><span style="color:#555;font-size:.9rem;">' + c.uitleg + '</span></span>' +
      '</span></label>';
  }).join('');
}

function ikReken(){
  var score = 0, ontbreekt = [];
  ikCriteria.forEach(function(c){
    if (document.getElementById('ik-' + c.id).checked) score += c.gewicht;
    else ontbreekt.push(c);
  });

  var pct = Math.round((score / ikMax) * 100);
  var aanbetalingOk = document.getElementById('ik-aanbetaling').checked;

  var kop, tekst, bg, rand;
  if (score === ikMax){
    kop = 'Alles controleerbaar op orde';
    tekst = 'Elk punt in deze lijst is aantoonbaar geregeld. Vraag alsnog een tweede offerte aan om de prijs en de systeemdimensionering te kunnen ijken — een goede installateur is niet automatisch de scherpste aanbieding.';
    bg = '#e8f5ee'; rand = '#b7dfc9';
  } else if (!aanbetalingOk){
    kop = 'Eerst de betaalafspraak regelen';
    tekst = 'Zolang de aanbetaling niet begrensd is en het slotbedrag niet aan oplevering hangt, draag jij het financiële risico van de hele opdracht. Dit punt weegt daarom het zwaarst: los dit eerst op voordat je naar de rest kijkt.';
    bg = '#fdeeee'; rand = '#f0c4c4';
  } else if (pct >= 70){
    kop = 'Grotendeels in orde, met open punten';
    tekst = 'De basis staat. Leg de ontbrekende punten hieronder schriftelijk voor aan de installateur en laat het antwoord in de opdrachtbevestiging opnemen — mondelinge toezeggingen zijn later niet aantoonbaar.';
    bg = '#fff8e6'; rand = '#f0dfae';
  } else {
    kop = 'Te veel onbekend om te ondertekenen';
    tekst = 'Er is nog te weinig verifieerbaar om een opdracht van deze omvang te gunnen. Vraag de ontbrekende gegevens op en leg er minimaal twee andere offertes naast.';
    bg = '#fdeeee'; rand = '#f0c4c4';
  }

  var lijst = ontbreekt.length
    ? '<div style="margin-top:.8rem;"><strong style="font-size:.9rem;">Nog uit te zoeken:</strong><ul style="margin:.4rem 0 0 1.2rem;font-size:.9rem;">' +
      ontbreekt.map(function(c){ return '<li>' + c.titel + '</li>'; }).join('') + '</ul></div>'
    : '';

  document.getElementById('ik-uitkomst').innerHTML =
    '<div style="background:' + bg + ';border:1px solid ' + rand + ';border-radius:10px;padding:1.1rem;">' +
    '<div style="font-size:.85rem;color:#555;">Score ' + score + ' van ' + ikMax + ' punten (' + pct + '%)</div>' +
    '<div style="height:8px;background:#fff;border-radius:4px;margin:.5rem 0 .8rem;overflow:hidden;"><div style="height:100%;width:' + pct + '%;background:#0e7490;"></div></div>' +
    '<div style="font-size:1.05rem;font-weight:700;margin-bottom:.35rem;">' + kop + '</div>' +
    '<div style="font-size:.95rem;color:#333;">' + tekst + '</div>' + lijst + '</div>';
}

function ikReset(){
  ikCriteria.forEach(function(c){ document.getElementById('ik-' + c.id).checked = false; });
  ikReken();
}

ikRender();
ikReken();
</script>

## Waarom de criteria zo zijn gewogen

De zeven punten wegen niet even zwaar. De betaalafspraak weegt het zwaarst (3 punten) omdat dat het enige punt is waarbij je bij een misstap je geld kwijt bent en geen installatie hebt. KvK plus referenties, een controleerbare erkenning, garantie op het werk en een gespecificeerde offerte wegen elk 2 punten: die bepalen of je achteraf iets kunt afdwingen. Reviews en een schouw wegen 1 punt — belangrijk, maar herstelbaar.

Wat je in deze lijst níet aantreft, is een bedrag of een percentage dat wij als "normaal" bestempelen. Prijzen voor zonnepanelen en warmtepompen bewegen te snel en verschillen te sterk per woning om er hier een norm aan te hangen. De enige betrouwbare prijsijking is meerdere offertes voor jóuw dak en jóuw warmtevraag.

## Meerdere offertes aanvragen

Eén offerte is een getal; drie offertes zijn informatie. Pas met meerdere aanbiedingen zie je of een prijs afwijkt, of een systeem ruimer of krapper gedimensioneerd is dan de rest, en welke installateur daadwerkelijk naar jouw situatie heeft gekeken in plaats van een standaardpakket te sturen.

Praktische aanpak:

1. **Vraag drie tot vier offertes aan** en verstrek alle aanbieders dezelfde uitgangsgegevens: dakvlak en oriëntatie, jaarverbruik, bouwjaar en isolatiestand, huidige verwarmingsinstallatie.
2. **Vergelijk op systeem, niet op prijs.** Verschilt het geadviseerde vermogen of de capaciteit sterk, laat dan elke aanbieder onderbouwen waaróm — daar zit vaker het verschil dan in het uurtarief.
3. **Loop de zeven punten hierboven per aanbieder na** en bewaar de antwoorden schriftelijk.
4. **Laat de laagste prijs niet automatisch winnen.** Een lagere prijs die de meterkastaanpassing of het waterzijdig inregelen buiten de opdracht laat, is geen lagere prijs.

<a href="https://go.duurzaamthuislab.nl/slimster?ref=/installateur-kiezen/" target="_blank" rel="noopener nofollow sponsored" class="cta cta-affiliate">Offertes van installateurs in je regio vergelijken →</a>

Ook via een offerteplatform blijft de checklist hierboven je eigen werk: een platform selecteert bedrijven op zijn eigen voorwaarden, niet op de jouwe.

## Verder lezen per techniek

De criteria hierboven gelden voor beide technieken. De techniekspecifieke vragen — welk vermogen past bij jouw dak, welke afgiftetemperatuur je woning aankan — staan uitgewerkt in deze artikelen:

- [Beste zonnepanelen-installateur kiezen](/posts/beste-zonnepanelen-installateur-kiezen-2026/) — dakschouw, omvormerkeuze en wat er in een pv-offerte thuishoort
- [Een goede warmtepomp-installateur vinden](/posts/best-warmtepomp-installateur-vinden-2026/) — warmteverliesberekening, dimensionering en inregelen
- [Warmtepomp-installateur checklist](/posts/warmtepomp-installateur-checklist-2026/) — de volledige vragenlijst voor het gesprek aan tafel
