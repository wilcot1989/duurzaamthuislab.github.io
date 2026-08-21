---
title: "Stroomprijs-alert: gratis mail bij negatieve stroomprijzen"
description: "Ontvang automatisch een e-mail op de middag vóór een dag met negatieve stroomprijzen — met de exacte uren en wat het je oplevert. Gratis, uitschrijven kan altijd."
date: 2026-08-21
lastmod: 2026-08-21
author: Team DuurzaamThuisLab
url: /stroomprijs-alert/
affiliate: false
faq:
  - q: 'Wanneer krijg ik een mail?'
    a: 'Alleen als de day-ahead-prijzen voor morgen één of meer negatieve uren bevatten. De prijzen worden rond 15:00 gepubliceerd; de alert volgt daarna, dus je hebt de hele avond om je verbruik te plannen. Geen negatieve uren = geen mail.'
  - q: 'Verdien ik echt geld bij negatieve prijzen?'
    a: 'Meestal niet direct: de energiebelasting (€0,11085/kWh incl. btw in 2026) en de leveranciersopslag betaal je altijd. Pas als de kale prijs onder circa −€0,13 zakt, kan je totaalprijs onder nul komen. Wél is stroom op die uren het allergoedkoopst — het perfecte moment voor wasmachine, EV of thuisbatterij.'
  - q: 'Wat doen jullie met mijn e-mailadres?'
    a: 'Alleen deze alert versturen. Het adres staat in onze eigen database, gaat nergens anders heen en elke mail bevat een uitschrijflink die direct werkt. Zie ook onze privacyverklaring.'
---

> **Kort antwoord:** meld je e-mailadres aan en je krijgt automatisch bericht op de middag vóór elke dag met negatieve stroomprijzen — met de exacte uren erbij. In 2025 telde Nederland **212 uur** met een negatieve beursprijs, vooral op zonnige middagen. Gratis, geen andere mails, uitschrijven met één klik.

<div style="background:var(--cream-soft,#f6f2ea);border:1px solid var(--ink-line,#ddd);border-radius:4px;padding:1.5rem;margin:1.5rem 0;">
  <form id="alert-form" onsubmit="return alertAanmelden(event)" style="display:flex;gap:.5rem;flex-wrap:wrap;">
    <input type="email" id="alert-email" placeholder="je@email.nl" required style="flex:1;min-width:14rem;padding:.8rem 1rem;border:1px solid #ccc;border-radius:3px;font-size:1rem;">
    <input type="text" name="website" style="display:none" tabindex="-1" autocomplete="off">
    <button type="submit" style="padding:.8rem 1.5rem;background:var(--ink,#1a1a1a);color:#fff;border:none;border-radius:3px;font-size:1rem;cursor:pointer;">Zet de alert aan</button>
  </form>
  <p id="alert-status" style="margin:.75rem 0 0;font-size:.9rem;color:var(--ink-soft,#555);"></p>
</div>

<script>
function alertAanmelden(e){
  e.preventDefault();
  var el = document.getElementById("alert-status");
  el.textContent = "Bezig…";
  fetch("https://beheer.wtdigital.nl/api/public/stroomprijs-alert", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({email: document.getElementById("alert-email").value})
  }).then(function(r){ return r.json(); }).then(function(d){
    el.textContent = d.ok ? "Gelukt! Je krijgt een mail zodra er negatieve uren aankomen." : ("Dat ging mis: " + (d.error || "probeer het opnieuw"));
  }).catch(function(){ el.textContent = "Dat ging mis — probeer het later opnieuw."; });
  return false;
}
</script>

## Hoe het werkt

Elke middag rond 15:00 publiceert de EPEX-beurs de uurprijzen voor morgen. Ons systeem leest die automatisch in (dezelfde data als op [stroomprijzen morgen](/stroomprijzen-morgen/)) en controleert of er uren onder nul zitten. Zo ja, dan krijg je één mail met de exacte uren en de kanttekening wat het écht oplevert — inclusief de rekenregel dat de totaalprijs pas onder nul komt als de kale prijs dieper daalt dan circa −€0,13.

Waarom dit nuttig is: negatieve uren clusteren op zonnige dagen tussen 11:00 en 17:00. Wie een thuisbatterij, EV of gewoon een wasmachine slim inzet, pakt op zo'n dag het maximale prijsverschil. Hoeveel dat is, staat in onze [negatieve-stroomprijzen-analyse](/negatieve-stroomprijzen/).

*Aan deze informatie kunnen geen rechten worden ontleend.*
