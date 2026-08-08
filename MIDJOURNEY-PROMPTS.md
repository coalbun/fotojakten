# Midjourney-prompter för Fotojakten

Appens palett: mörkgrön bakgrund `#0F1A12`, kort `#1D2E22`, accentgrön `#6DC77C`, sand `#E8E3D4`.
Lägg alltid till `--v 7` sist. Bilder sparas i `photos`-bucketen och läggs in via CSS/`<img>`.

---

## 1. Hero-bakgrund (startsidan, bakom loggan)

```
misty nordic pine forest at dawn seen from above, layered silhouetted treetops fading into fog, deep forest green and dark teal palette, soft volumetric light, minimal negative space in upper third for text, cinematic, muted desaturated tones, no people, premium mobile app background --ar 9:16 --style raw --v 7
```

**Varför:** plats i övre tredjedelen för rubriken, dimman gör att text alltid är läsbar.

---

## 2. Uppdragskort-bakgrund (bakom "Fota något grönt")

```
abstract macro of wet fern leaves and moss, extreme shallow depth of field, dark moody forest greens, soft bokeh, organic curves, very dark vignette edges, subtle texture, luxurious minimal wallpaper --ar 4:5 --style raw --v 7
```

Använd med `opacity: 0.35` bakom kortet så texten står kvar tydligt.

---

## 3. Prisutdelningens bakgrund (finalen)

```
enchanted dark forest clearing at night, faint golden light rays through pine branches, floating dust particles and fireflies, deep emerald and near-black gradient, magical premium atmosphere, centered empty space for content, no people --ar 9:16 --style raw --v 7
```

---

## 4–8. Badges / medaljonger (uppdragsikoner)

Gemensam stil-svans, klistra in efter varje motiv:

> `, 3D soft-body render, rounded matte clay material, glossy highlights, floating on transparent background, centered composition, soft studio lighting from top left, vibrant green and cream color scheme, app icon style, cute premium collectible badge --ar 1:1 --style raw --v 7`

| Uppdrag | Motiv att sätta först |
|---|---|
| Vilt djur | `a plump friendly forest bird sitting on a small branch` |
| Action | `a running shoe mid-stride with motion swoosh` |
| Hjärtformat | `a smooth heart-shaped stone with moss growing on it` |
| Färgglatt | `a small rainbow arc over a rounded green hill` |
| Vinnare/pokal | `a rounded golden trophy cup with laurel leaves` |

**Tips:** kör alla fem i samma session så Midjourney håller stilen konsekvent. Lägg till `--seed 1234` (samma siffra) för ännu jämnare resultat.

---

## 9. Tomt tillstånd ("Inga bilder än")

```
single small pine sapling growing from forest floor, top-down view, dark green background, minimal, lots of empty space, soft diffused light, calm and premium --ar 1:1 --style raw --v 7
```

---

## Så lägger du in dem

1. Ladda ner PNG från Midjourney (välj **Upscale** först).
2. Skicka filerna till mig så lägger jag in dem på rätt ställe i appen.
3. För badges: be om transparent bakgrund via `--no background` eller klipp ut i Photoshop/remove.bg.
