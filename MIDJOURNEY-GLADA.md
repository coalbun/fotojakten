# Midjourney – ljusare & gladare variant

Dina tre första bilder är snygga men mörka och stämningsfulla. Här är samma tre motiv fast **soliga, varma och glada** – mer sommarpromenad, mindre skogsmystik.

**Viktigt om läsbarhet:** appen har vit text ovanpå bilderna. Därför slutar varje prompt med en formulering som håller *en del av bilden mörk eller lugn* – annars försvinner texten. Ta inte bort de orden.

Alla prompter avslutas med `--v 7`. Lägg till `--style raw` om du vill ha mindre "illustrerat" och mer foto.

---

## 1. Startsidan (hero) – solig tallskog

```
sunlit nordic pine forest in summer, warm golden sunbeams streaming between trunks, fresh vivid green foliage, lens flare, joyful and airy atmosphere, shot from a walking path, dreamy bokeh, upper third softly darkened for text overlay, no people --ar 9:16 --style raw --v 7
```

**Alternativ – ännu gladare, mer sommaräng:**
```
summer meadow at the edge of a bright birch forest, wildflowers and tall grass glowing in golden hour light, warm and cheerful, soft haze, gentle breeze feeling, darker calm area at the top for text, no people --ar 9:16 --style raw --v 7
```

---

## 2. Uppdragskort – ljusa blad

```
sunlight shining through fresh green leaves seen from below, glowing translucent foliage, warm summer light, cheerful vivid greens, soft bokeh, bright and optimistic, gentle vignette at edges --ar 4:5 --style raw --v 7
```

Lägg den bakom kortet med låg opacitet (`0.25`) så texten står kvar knivskarp.

---

## 3. Prisutdelningen – festlig men fortfarande magisk

```
golden hour sunbeams bursting through a forest clearing, warm confetti-like floating pollen and light particles, celebratory and uplifting mood, rich greens and honey gold, centered calm darker area for content, cinematic and joyful, no people --ar 9:16 --style raw --v 7
```

**Alternativ – kvällsfest utan att bli mörk:**
```
warm string lights hanging between summer trees at dusk, soft glowing bulbs, festive celebratory atmosphere, teal and warm amber palette, dreamy bokeh, calm darker centre for text, no people --ar 9:16 --style raw --v 7
```

---

## 4. Badges – glada och lekfulla

Gemensam stil-svans (klistra in efter varje motiv):

> `, 3D soft-body render, rounded matte clay material, glossy highlights, playful and cheerful, bright sunny lighting, fresh green and warm yellow palette, floating on transparent background, centered, cute premium collectible sticker --ar 1:1 --v 7`

| Uppdrag | Motiv först |
|---|---|
| Vilt djur | `a cheerful chubby songbird mid-hop, big friendly eyes` |
| Action | `a bright sneaker leaping with playful speed lines` |
| Hjärtformat | `a smooth heart-shaped pebble with a tiny daisy beside it` |
| Roligaste minen | `a smiling sun character with rosy cheeks` |
| Färgglatt | `a cheerful rainbow arc with tiny fluffy clouds` |
| Vinnare | `a shiny golden trophy with confetti bursting around it` |

Kör alla i samma session och lägg till samma `--seed 4242` för konsekvent stil.

---

## Om du vill byta hela appens känsla

Just nu är appen mörkgrön (snyggt kvällsläge, syns bra i skog). Vill du att den ska kännas ljus och solig rakt igenom – ljus bakgrund, mörk text – säg till, det är en ganska snabb ändring. Men tänk på: **mörk app syns bättre i starkt solljus utomhus** och drar mindre batteri. Mitt förslag är att behålla mörkt gränssnitt men köra ljusa, glada bilder i det – kontrasten blir fin.
