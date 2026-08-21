---
title: "Onze rekentools op jouw site — gratis, met bronvermelding"
date: 2026-04-29
description: "Plaats de rekentools en live prijswidgets van DuurzaamThuisLab gratis op jouw site — de enige voorwaarde is een zichtbare bronvermelding met link."
draft: false
---

## Onze rekentools gratis op jouw site

Hieronder vind je iframe-codes voor onze rekentools en widgets. Gebruik ze vrij op jouw site **mits**:
- Bronvermelding zichtbaar onder de embed
- Een gewone link naar de calculatorpagina, dus zonder `rel="nofollow"` (er bestaat geen waarde `rel="dofollow"`; een link zonder `rel` volstaat)
- Geen aanpassing aan de rekenlogica of vormgeving

---

### Saldering 2027 calculator

Rekent twee situaties door en zet ze naast elkaar: t/m 31 december 2026 met volledige saldering, en vanaf 1 januari 2027 zonder. Je bezoeker vult zelf verbruik, opgesteld vermogen (kWp), stroomprijs, terugleververgoeding, batterijcapaciteit en investering in. Er zitten géén afbouwpercentages in — de saldering stopt in één keer, er is geen afbouwpad — en de terugleververgoeding is een invoerveld met een gelabelde aanname, geen tarief dat wij als vaststaand presenteren.

```html
<iframe src="https://duurzaamthuislab.nl/posts/saldering-calculator-2027-volledig/?embed=1"
        width="100%" height="700"
        style="border:1px solid #ddd;border-radius:8px;"
        title="Saldering 2027 calculator">
</iframe>
<p style="font-size:.85rem;color:#666;margin-top:.5rem;">
  Calculator door <a href="https://duurzaamthuislab.nl/posts/saldering-calculator-2027-volledig/">DuurzaamThuisLab</a>
</p>
```

### Energiebesparing 2027 calculator

Rekent per maatregel door wat die in jouw situatie oplevert, op basis van je eigen invoer. Ook hier: expliciete aannames, geen beloofde bedragen.

```html
<iframe src="https://duurzaamthuislab.nl/posts/energiebesparing-calculator-2027/?embed=1"
        width="100%" height="600"
        style="border:1px solid #ddd;border-radius:8px;"
        title="Energiebesparing 2027 calculator">
</iframe>
<p style="font-size:.85rem;color:#666;margin-top:.5rem;">
  Calculator door <a href="https://duurzaamthuislab.nl/posts/energiebesparing-calculator-2027/">DuurzaamThuisLab</a>
</p>
```

---

## Voor wie is dit geschikt?

- **Energie-blogs** die saldering-content hebben maar geen eigen calculator
- **Installatiebedrijven** die klanten een ROI-tool willen tonen
- **Adviseurs** voor verduurzaming
- **Gemeente-portals** voor energietransitie-pagina's

## Let op bij de twee calculator-embeds

Beide calculators staan in een artikelpagina; wij hebben (nog) geen aparte, kale embed-weergave. In het iframe zie je dus de pagina met de calculator erin, en de hoogtes hierboven zijn een praktische ondergrens — zet ze ruimer als je bezoekers niet in het iframe willen scrollen. De twee widgets hieronder (powerstation-runtime en live stroomprijzen) zijn wél losse, kale pagina's en passen zonder scrollen.

## Disclaimer

We tracken geen embeds. Je hoeft niets aan te vragen — gewoon embedden + credit. Als je een prominente embed plaatst (homepage of gids-pagina), [laat het ons weten](mailto:info@duurzaamthuislab.nl) — dan weten wij dat we die tool niet zomaar mogen verplaatsen of uitzetten.

## Contact

[info@duurzaamthuislab.nl](mailto:info@duurzaamthuislab.nl)


## Powerstation-runtime-widget

Laat bezoekers uitrekenen hoe lang een powerstation hun apparaten voedt — handig voor camping-, vanlife- en klussites:

```html
<iframe src="https://duurzaamthuislab.nl/widget-powerstation/"
        title="Powerstation-runtime berekenen — DuurzaamThuisLab"
        width="100%" height="290" loading="lazy"
        style="border:1px solid #e0e0e0;border-radius:10px;max-width:520px;"></iframe>
```

## Live stroomprijzen-widget

Toon de actuele dynamische stroomprijzen per uur op je eigen site — automatisch elke dag ververst:

```html
<iframe src="https://duurzaamthuislab.nl/widget-stroomprijzen/"
  width="100%" height="200" frameborder="0" loading="lazy"
  title="Stroomprijzen vandaag — DuurzaamThuisLab"></iframe>
```

Voorwaarde voor gebruik: de bronvermelding met link naar duurzaamthuislab.nl blijft zichtbaar.
