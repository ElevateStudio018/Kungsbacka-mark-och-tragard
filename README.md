# Kungsbacka Mark & Trädgård – ny webbplats

Statisk sajt (HTML/CSS/JS, inga byggsteg). Öppna `index.html` direkt eller kör en lokal server:

```
python3 -m http.server 8000
```

## Sidor
- `index.html` – startsida: hero, om oss, tjänster, arbetsgång, urval av referenser, område, offertformulär
- `referenser.html` – referensgalleri med filter och bildvisning (lightbox)

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
3. Kontrollera orterna under "Område" och att ROT/RUT-texten stämmer för era tjänster.

## Pexels-bilder som används
95687, 5125783, 129544, 16239805, 6095810, 7587879, 24595771, 36866669, 7061672,
7546775, 280222, 5231236, 3575827, 7813043, 34400606, 32112822
(`https://www.pexels.com/photo/<id>/`)
