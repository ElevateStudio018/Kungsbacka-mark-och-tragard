#!/usr/bin/env python3
"""Bygger sajtens HTML-sidor.

Sidhuvud, meny och sidfot finns på ett ställe här nedan. Varje sidas innehåll
ligger i src/pages/<namn>.html. Kör:  python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "pages"

PHONE = "0735-23 53 16"
PHONE_TEL = "+46735235316"
EMAIL = "anders@kungsbackamark.com"
FACEBOOK = "https://www.facebook.com/Kungsbacka-Mark-Tr%C3%A4dg%C3%A5rd-AB-1606088956289043/"

VERKSAMHET = [
    ("markarbeten.html", "Markarbeten"),
    ("dranering.html", "Dränering"),
    ("stensattning.html", "Stensättning & murar"),
    ("bygg.html", "Bygg & altaner"),
    ("tradgard.html", "Trädgårdsanläggning"),
]

# fil, titel, beskrivning, aktiv menypunkt, og-bild
PAGES = [
    ("index.html", "Mark-, bygg- och trädgårdsentreprenader i Halland och Göteborg | Kungsbacka Mark & Trädgård",
     "Kungsbacka Mark & Trädgård AB utför mark-, bygg- och trädgårdsentreprenader i Varberg, Kungsbacka och Göteborg med omnejd. En kontakt från första spadtag till färdig miljö.",
     "", "p-16239805.jpg"),
    ("verksamhet.html", "Verksamhet | Kungsbacka Mark & Trädgård",
     "Våra verksamhetsområden: markarbeten, dränering, stensättning och murar, bygg och altaner samt trädgårdsanläggning.",
     "verksamhet", "p-5125783.jpg"),
    ("markarbeten.html", "Markarbeten – schaktning, grund och materialleverans | Kungsbacka Mark & Trädgård",
     "Schaktning, grundläggning, återfyllning, stenröjning samt transport och leverans av matjord, grus och makadam.",
     "verksamhet", "p-95687.jpg"),
    ("dranering.html", "Dränering av husgrund och tomt | Kungsbacka Mark & Trädgård",
     "Dränering runt husgrund och på tomt i Varberg, Kungsbacka och Göteborg med omnejd.",
     "verksamhet", "p-32112822.jpg"),
    ("stensattning.html", "Stensättning, plattläggning och murar | Kungsbacka Mark & Trädgård",
     "Plattläggning av uppfarter, parkeringar, gångar och uteplatser samt nya murar och upprustning av befintliga.",
     "verksamhet", "p-6095810.jpg"),
    ("bygg.html", "Bygg och altaner | Kungsbacka Mark & Trädgård",
     "Altanbyggen, garage, tillbyggnader och renoveringar utförda av egna snickare.",
     "verksamhet", "p-7587879.jpg"),
    ("tradgard.html", "Trädgårdsanläggning och trädgårdstjänster | Kungsbacka Mark & Trädgård",
     "Slyröjning, häckklippning, trädgårdsplanering, anläggning av rabatter och gräsmattor samt gräsklippning.",
     "verksamhet", "p-7061672.jpg"),
    ("referenser.html", "Referensprojekt | Kungsbacka Mark & Trädgård",
     "Referensprojekt inom markarbeten, stensättning, murar, bygg och trädgårdsanläggning.",
     "referenser", "p-7546775.jpg"),
    ("kvalitet-miljo.html", "Kvalitet & miljö | Kungsbacka Mark & Trädgård",
     "Så arbetar vi med kvalitet, dokumentation och miljö i våra entreprenader.",
     "kvalitet", "p-5231236.jpg"),
    ("om-oss.html", "Om oss | Kungsbacka Mark & Trädgård",
     "Kungsbacka Mark & Trädgård AB är ett mark-, bygg- och trädgårdsföretag med säte i Veddige.",
     "om", "p-7788227.jpg"),
    ("kontakt.html", "Kontakt och offertförfrågan | Kungsbacka Mark & Trädgård",
     "Kontakta Kungsbacka Mark & Trädgård AB – Veddigevägen 253, 432 66 Veddige. Telefon 0735-23 53 16.",
     "kontakt", "p-280222.jpg"),
    ("integritetspolicy.html", "Integritetspolicy | Kungsbacka Mark & Trädgård",
     "Så hanterar Kungsbacka Mark & Trädgård AB personuppgifter.",
     "", "p-280222.jpg"),
]

ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
ICON_FB = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5H16l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.4H8v3h2.6V21h2.9z"/></svg>'


def head(title, desc, image):
    return f"""<!doctype html>
<html lang="sv">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="assets/img/{image}">
  <meta name="theme-color" content="#023845">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;1,800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": "Kungsbacka Mark & Trädgård AB",
    "telephone": "{PHONE_TEL}",
    "email": "{EMAIL}",
    "address": {{"@type": "PostalAddress", "streetAddress": "Veddigevägen 253", "postalCode": "432 66", "addressLocality": "Veddige", "addressCountry": "SE"}},
    "areaServed": ["Veddige", "Varberg", "Kungsbacka", "Göteborg"]
  }}
  </script>
</head>
<body>
"""


def cur(file, target):
    return ' aria-current="page"' if file == target else ""


def header(file, active):
    def top(key):
        return ' aria-current="page"' if active == key else ""
    sub = "\n".join(f'          <li><a href="{f}"{cur(file, f)}>{n}</a></li>' for f, n in VERKSAMHET)
    msub = "\n".join(f'        <li class="child"><a href="{f}">{n}</a></li>' for f, n in VERKSAMHET)
    return f"""
<div class="topbar">
  <div class="wrap">
    <div class="topbar-left"><span>{ICON_PIN}Huvudkontor Veddige · Verksamma i Varberg, Kungsbacka och Göteborg</span></div>
    <div class="topbar-right">
      <a href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE}</a>
      <a href="mailto:{EMAIL}">{ICON_MAIL}E-post</a>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="index.html" aria-label="Kungsbacka Mark & Trädgård – startsida">
      <b>KUNGSBACKA</b>
      <small>MARK &amp; TRÄDGÅRD</small>
    </a>
    <ul class="nav" aria-label="Huvudmeny">
      <li class="has-sub">
        <a href="verksamhet.html"{top("verksamhet")}>Verksamhet</a>
        <ul class="sub">
{sub}
        </ul>
      </li>
      <li><a href="referenser.html"{top("referenser")}>Referensprojekt</a></li>
      <li><a href="kvalitet-miljo.html"{top("kvalitet")}>Kvalitet & miljö</a></li>
      <li><a href="om-oss.html"{top("om")}>Om oss</a></li>
      <li><a href="kontakt.html"{top("kontakt")}>Kontakt</a></li>
      <li class="nav-cta"><a href="kontakt.html#offert">Begär offert</a></li>
    </ul>
    <button class="menu-toggle" aria-label="Meny" aria-expanded="false" aria-controls="mobilmeny">
      <span></span><span></span><span></span>
    </button>
    <nav class="mobile-menu" id="mobilmeny" aria-label="Mobilmeny">
      <ul>
        <li class="parent"><a href="verksamhet.html">Verksamhet</a></li>
{msub}
        <li><a href="referenser.html">Referensprojekt</a></li>
        <li><a href="kvalitet-miljo.html">Kvalitet & miljö</a></li>
        <li><a href="om-oss.html">Om oss</a></li>
        <li><a href="kontakt.html">Kontakt</a></li>
      </ul>
      <a class="btn" href="kontakt.html#offert">Begär offert</a>
    </nav>
  </div>
</header>
"""


def footer():
    vlinks = "\n".join(f'        <li><a href="{f}">{n}</a></li>' for f, n in VERKSAMHET)
    return f"""
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Bildvisning">
  <img src="" alt="">
  <button class="lb-btn lb-close" aria-label="Stäng"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
  <button class="lb-btn lb-prev" aria-label="Föregående bild"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 6l-6 6 6 6"/></svg></button>
  <button class="lb-btn lb-next" aria-label="Nästa bild"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg></button>
  <p class="lightbox-caption"></p>
</div>

<footer class="site-footer">
  <div class="wrap footer-cols four">
    <div class="footer-col">
      <a class="logo footer-logo" href="index.html"><b>KUNGSBACKA</b><small>MARK &amp; TRÄDGÅRD</small></a>
      <h4>Huvudkontor Veddige</h4>
      <p>Veddigevägen 253<br>432 66 Veddige<br><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <div class="social">
        <a href="{FACEBOOK}" aria-label="Facebook" rel="noopener" target="_blank">{ICON_FB}</a>
      </div>
    </div>
    <div class="footer-col">
      <h4>Verksamhet</h4>
      <ul>
{vlinks}
      </ul>
    </div>
    <div class="footer-col">
      <h4>Bolaget</h4>
      <ul>
        <li><a href="om-oss.html">Om oss</a></li>
        <li><a href="referenser.html">Referensprojekt</a></li>
        <li><a href="kvalitet-miljo.html">Kvalitet & miljö</a></li>
        <li><a href="kontakt.html">Kontakt</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Verksamma i</h4>
      <p>Veddige<br>Varberg<br>Kungsbacka<br>Göteborg med omnejd</p>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>© <span id="year">2026</span> Kungsbacka Mark &amp; Trädgård AB · Org.nr 559006-9687</span>
    <span><a href="integritetspolicy.html">Integritetspolicy</a> · Exempelbilder: Pexels</span>
  </div>
</footer>

<a class="call-fab" href="tel:{PHONE_TEL}" aria-label="Ring {PHONE}">
  {ICON_PHONE}
</a>
<button class="to-top" aria-label="Till toppen">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 15l6-6 6 6"/></svg>
</button>

<script src="assets/js/main.js"></script>
</body>
</html>
"""


def build():
    for file, title, desc, active, image in PAGES:
        body = (SRC / file).read_text(encoding="utf-8")
        body = (body.replace("{{PHONE}}", PHONE).replace("{{PHONE_TEL}}", PHONE_TEL)
                    .replace("{{EMAIL}}", EMAIL))
        html = head(title, desc, image) + header(file, active) + "\n<main>\n" + body + "\n</main>\n" + footer()
        (ROOT / file).write_text(html, encoding="utf-8")
        print("byggde", file)


if __name__ == "__main__":
    build()
