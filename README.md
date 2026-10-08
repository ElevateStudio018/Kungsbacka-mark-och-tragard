# Kungsbacka Mark & Trädgård – ny webbplats

Statisk sajt (HTML/CSS/JS). Sidorna byggs från `src/pages/` med ett litet skript:

```
python3 build.py          # bygger alla .html-filer i roten
python3 -m http.server 8000
```

Redigera **aldrig** `.html`-filerna i roten direkt – de skrivs över. Ändra i stället:
- `build.py` – sidhuvud, meny, sidfot, kontaktuppgifter och sidlista (titlar/beskrivningar)
- `src/pages/<sida>.html` – respektive sidas innehåll (`{{PHONE}}`, `{{PHONE_TEL}}`, `{{EMAIL}}` ersätts vid bygget)

Designen utgår från anlab.se: Montserrat, skiffergrönt (#173a35), salviagröna och varmgrå
sektioner, vita kort, fyrkantiga knappar och mörk footer – med en
koncernstruktur: informationsrad, helskärms-hero med verksamhetsrad, verksamhetsområden med egna sidor, faktablad för
referensprojekt, bolagsfakta och kontaktpersonkort.

## Sidor
- `index.html` – startsida
- `verksamhet.html` – översikt, samt `markarbeten`, `dranering`, `stensattning`, `bygg`, `tradgard`
- `referenser.html` – referensprojekt med filter och bildvisning
- `kvalitet-miljo.html`, `om-oss.html`, `kontakt.html` (offertformulär), `integritetspolicy.html`

## Innehåll
Texter och kontaktuppgifter kommer från markarbetevarberg.com / kungsbackamark.com
(Veddigevägen 253, 432 66 Veddige · 0735-23 53 16 · anders@kungsbackamark.com).

## Att göra innan publicering
1. **Byt bilder.** Alla bilder i `assets/img/p-*.jpg` är exempelbilder från Pexels (fri licens).
   Ersätt referensbilderna med egna projektbilder – riktiga jobb konverterar betydligt bättre.
   Varje bild finns i två storlekar: `namn.jpg` (1600 px) och `namn-sm.jpg` (800 px).
2. **Formulär.** Offertformuläret öppnar besökarens e-postprogram med förfrågan ifylld
   (`assets/js/main.js`). För att ta emot förfrågningar direkt, koppla formuläret till
   t.ex. Formspree eller Netlify Forms.
3. Kontrollera texterna: ROT/RUT, F-skatt, Anders som kontaktperson, tjänstelistorna per
   verksamhetsområde och "Moment" i referensprojektens faktablad (de beskriver exempelbilderna).
4. Har ni certifikat, medlemskap eller kreditrating – byt ut de tre symbolerna i förtroenderaden mot riktiga logotyper.

## Pexels-bilder som används
95687, 5125783, 16239805, 6095810, 7587879, 24595771, 36866669, 7061672,
7546775, 280222, 5231236, 3575827, 32112822, 7788227
(`https://www.pexels.com/photo/<id>/`)
