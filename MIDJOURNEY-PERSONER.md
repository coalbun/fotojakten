# Midjourney – med människor, äventyr och känsla

Mål: ett gäng i 25–30-årsåldern ute på en skogsled, mitt i ett uppdrag. Äventyrligt, spännande, roligt, realistiskt – men **personerna ska vara små eller sedda bakifrån** så de inte konkurrerar med knappar och text. Mörkare med kontrast, inte ljust och glättigt.

---

## Stil-svansen (klistras in sist i varje prompt)

```
, candid documentary photography, unposed natural moment, shot on 35mm film, Kodak Portra 400, moody low-key lighting, deep shadows and high contrast, muted desaturated greens, cinematic, no eye contact with camera --no text, watermark, logo, faces looking at camera
```

Den här svansen gör tre saker: **candid/unposed + no eye contact** dödar stockfoto-känslan, **low-key + deep shadows** ger det mörka du vill ha, och **--no** stoppar text och logotyper som MJ annars slänger in.

Avsluta alltid med `--ar 9:16 --style raw --v 7` för bakgrunder (stående), `--ar 4:5` för uppdragskort, `--ar 1:1` för närbilder.

---

## 1. Startsidan – helkropp, på avstånd

**A – gänget på leden (mest "äventyr")**
```
four young friends in their late twenties walking away from camera along a narrow forest trail, small figures in the lower third of the frame, tall dark pines towering above them, misty depth, backpacks and casual outdoor clothing, sense of setting off on an adventure [STIL-SVANS] --ar 9:16 --style raw --v 7
```

**B – en person stannar och fotar**
```
a young woman crouching on a forest trail photographing something on the ground with her phone, seen from behind at a distance, friends waiting further up the path in soft focus, dark green forest, dappled light [STIL-SVANS] --ar 9:16 --style raw --v 7
```

**C – siluetter, mest subtil (bäst för text ovanpå)**
```
silhouettes of a small group of friends hiking single file through dense misty forest, seen from far away, tiny figures against luminous fog, dramatic backlight, most of the frame is empty atmospheric forest [STIL-SVANS] --ar 9:16 --style raw --v 7
```

> **C är den säkraste** om du vill ha garanterat läsbar text – personerna blir små och resten är dimma.

---

## 2. Uppdragskortet – händer och närbilder

Här funkar närbilder bäst, för då tar personen inte plats i bild alls.

**A – händer som fotar**
```
close-up of hands holding a phone photographing a fern, shallow depth of field, forest floor blurred behind, natural skin tones, dark moody greens [STIL-SVANS] --ar 4:5 --style raw --v 7
```

**B – händer som bygger/skapar något**
```
close-up of two pairs of hands arranging pinecones and stones into a shape on a mossy log, collaborative and playful, warm skin against cold green forest tones, shallow focus [STIL-SVANS] --ar 4:5 --style raw --v 7
```

**C – hand som sträcks fram med ett fynd**
```
a hand holding out a heart-shaped stone toward the camera, forest trail blurred in the background, intimate and tactile, dark natural palette [STIL-SVANS] --ar 4:5 --style raw --v 7
```

---

## 3. Action – fart och skratt

**A – hopp mitt i luften**
```
young man mid-jump over a fallen log on a forest trail, caught mid-air, motion blur in the limbs, friends laughing out of focus behind, dynamic low angle, energetic [STIL-SVANS] --ar 9:16 --style raw --v 7
```

**B – springer mot kameran genom skogen**
```
two friends running along a forest path toward camera at a distance, slight motion blur, joyful energy, dark pines closing in on both sides, shaft of light ahead [STIL-SVANS] --ar 9:16 --style raw --v 7
```

---

## 4. Prisutdelningen – halvkropp, gemenskap

**A – gänget samlat runt en telefon**
```
small group of friends in their late twenties gathered in a circle looking down at a phone together, seen from slightly above and behind, faces obscured, forest clearing at dusk, warm phone glow lighting them from below, dark surroundings [STIL-SVANS] --ar 9:16 --style raw --v 7
```

**B – firande i motljus**
```
group of young friends raising their arms in celebration on a forest ridge at golden hour, seen as dark silhouettes against glowing haze, small in frame, triumphant and joyful [STIL-SVANS] --ar 9:16 --style raw --v 7
```

---

## 5. Väntar-läget ("håll telefonen redo")

```
a young person standing still on a forest trail looking up and around expectantly, seen from behind at medium distance, phone held loosely at their side, anticipation, quiet dark forest surrounding them [STIL-SVANS] --ar 9:16 --style raw --v 7
```

---

## Praktiska tips

**Kör flera varianter samtidigt.** Skicka 2–3 prompter, välj sedan. MJ ger dig fyra bilder per prompt – ta den där personerna är *minst* framträdande, inte den snyggaste porträttmässigt.

**Om personerna blir för stora:** lägg till `extreme wide shot` eller `tiny figures in vast forest` i början av prompten.

**Om det blir för ljust:** lägg till `underexposed, dark shadows, moody` – MJ tenderar att ljusa upp.

**Ett ärligt råd:** bilder med människor är svårare att lägga text ovanpå än ren natur, eftersom ögat dras till ansikten och rörelse. Jag lägger på en mörk gradient över bilden i appen så texten alltid är läsbar – men välj gärna bilder där **övre tredjedelen är lugn** (himmel, dimma, mörk skog), där hamnar rubrikerna.

**Filnamn när du sparar** i `Fotojakten-bilder` på skrivbordet:
- `1-startsida` · `2-uppdrag` · `3-prisutdelning` · `4-vantar` (valfri)
