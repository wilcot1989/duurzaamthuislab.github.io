#!/usr/bin/env python3
"""
Energietarieven-wijzigingsdetector voor DuurzaamThuisLab.nl

Doel: dagelijks de tariefpagina's van energieleveranciers volgen (terugleverkosten,
inkoopvergoedingen, voorwaarden) en bij een wezenlijke wijziging een WARNING printen —
de workflow maakt daar een GitHub Issue van, mét de beursprijs van die dag ernaast.
Patroon overgenomen van bedrijfssoftwaregids/scripts/check-pricing-pages.py.

Gebruik:
    python3 scripts/check-energietarieven.py [--update]
    --update : sla de huidige staat op als nieuwe snapshot
"""
import json
import re
import sys
import time
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).parent
SNAP_FILE = ROOT / "tarieven-snapshots.json"

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

# Pagina's waar tarieven/voorwaarden staan die onze content raakt.
# Bij een wijziging: betreffende artikelen + /terugleverkosten-vergelijken/ nalopen.
WATCHLIST = {
    "frank-terugleverkosten": "https://www.frankenergie.nl/nl/terugleverkosten",
    "frank-leeswijzer": "https://www.frankenergie.nl/nl/leeswijzer-afrekening",
    "tibber-energiecontract": "https://tibber.com/nl/energiecontract",
    "tibber-app": "https://tibber.com/nl/app",
    "zonneplan-dynamisch": "https://www.zonneplan.nl/energie/dynamisch-energiecontract",
    "zonneplan-batterij-uitleg": "https://www.zonneplan.nl/thuisbatterij/hoe-werkt-het/extra-uitleg",
    "anwb-tarieven": "https://www.anwb.nl/energie/actuele-tarieven",
    "eneco-dynamisch-terugleveren": "https://www.eneco.nl/klantenservice/dynamisch-energiecontract/dynamisch-en-terugleveren/",
    "vattenfall-dynamisch": "https://www.vattenfall.nl/klantenservice/alles-over-je-dynamische-contract/",
    "easyenergy-negatief": "https://www.easyenergy.com/negatieve-stroomprijzen-uitgelegd",
    "sessy-bestellen": "https://www.sessy.nl/bestellen",
    "homewizard-plugin-battery": "https://www.homewizard.com/nl/plug-in-battery/",
}

PRICE_RE = re.compile(r"€\s?\d{1,4}(?:[.,]\d{1,4})?|(?<![\w,.])\d{1,2},\d{2,4}\s?(?:ct|cent|€)?/?\s?(?:kWh|m3|m³)", re.I)


def fetch(url, timeout=25):
    req = Request(url, headers={"User-Agent": UA, "Accept-Language": "nl-NL,nl;q=0.9"})
    with urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def extract_signature(html):
    """Alle unieke prijs-achtige tekstfragmenten op de pagina, genormaliseerd en gesorteerd."""
    text = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    sig = sorted({re.sub(r"\s+", "", m.group(0)) for m in PRICE_RE.finditer(text)})
    if not sig:
        # JS-gerenderde pagina zonder prijzen in de HTML: val terug op een tekst-hash,
        # zodat structurele wijzigingen alsnog gesignaleerd worden.
        import hashlib
        sig = ["hash:" + hashlib.sha256(re.sub(r"\s+", " ", text).strip().encode()).hexdigest()[:16]]
    return sig


def beurscontext():
    """Actuele kale beursprijzen als context voor het Issue (eigen beheer-API)."""
    ctx = []
    try:
        d = json.loads(fetch("https://beheer.wtdigital.nl/api/public/stroomprijzen"))
        prijzen = [u["prijs"] for u in d.get("uren", [])]
        if prijzen:
            ctx.append(f"stroom {d['datum']}: gem €{sum(prijzen)/len(prijzen):.3f}/kWh (min €{min(prijzen):.3f}, max €{max(prijzen):.3f})")
    except Exception:
        pass
    try:
        d = json.loads(fetch("https://beheer.wtdigital.nl/api/public/gasprijs"))
        if isinstance(d.get("prijs_m3"), (int, float)):
            ctx.append(f"gas {d['datum']}: €{d['prijs_m3']:.3f}/m³")
    except Exception:
        pass
    return " | ".join(ctx) or "beursdata niet beschikbaar"


def main():
    update = "--update" in sys.argv
    snaps = json.loads(SNAP_FILE.read_text(encoding="utf-8")) if SNAP_FILE.exists() else {}
    warnings = 0

    for key, url in WATCHLIST.items():
        try:
            sig = extract_signature(fetch(url))
        except Exception as e:
            print(f"INFO: {key} niet opgehaald ({type(e).__name__}) — overgeslagen")
            continue
        oud = snaps.get(key)
        if oud is None:
            print(f"INFO: {key} — eerste snapshot ({len(sig)} prijsfragmenten)")
            snaps[key] = sig
        elif sig != oud:
            weg = [p for p in oud if p not in sig][:8]
            nieuw = [p for p in sig if p not in oud][:8]
            print(f"WARNING: {key} gewijzigd — verdwenen: {weg or '—'} | nieuw: {nieuw or '—'} | {url}")
            warnings += 1
            if update:
                snaps[key] = sig
        time.sleep(1)

    if update or not SNAP_FILE.exists():
        SNAP_FILE.write_text(json.dumps(snaps, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"\nBeurscontext: {beurscontext()}")
    print(f"Klaar: {warnings} wijziging(en) gedetecteerd over {len(WATCHLIST)} pagina's.")


if __name__ == "__main__":
    main()
