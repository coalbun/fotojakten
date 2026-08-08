import base64, pathlib, re

src = pathlib.Path("index.html").read_text(encoding="utf-8")
css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
js  = re.search(r"<script>\n(.*)</script>", src, re.S).group(1)

def data_uri(name):
    b64 = base64.b64encode(pathlib.Path(f"img/{name}.jpg").read_bytes()).decode()
    return f"data:image/jpeg;base64,{b64}"

for _name in ["hero", "finale"]:
    css = css.replace(f"url('img/{_name}.jpg')", f"url('{data_uri(_name)}')")

MISSION_KEYS = ["m-djur", "m-korv", "m-trick", "m-natur", "m-album", "m-alg", "m-film"]
MISSION_URI_JS = "var PREVIEW_IMG = {" + ",".join(
    f'"{k}":"{data_uri(k)}"' for k in MISSION_KEYS) + "};"

_boot = re.search(r"\(function boot\(\).*?\)\(\);", js, re.S)
js = js.replace(_boot.group(0), "/* boot disabled */")

# fyra kandidater: nuvarande + tre mörkare/grönare
VARIANTS = [
    ("Nuvarande",      "#0F1A12", "#16241A", "#1D2E22", "#26382B",
     "Dagens färg. Mörk men ganska neutral – gröntonen är svag."),
    ("Djupare grön",   "#0A1B11", "#102418", "#182E20", "#213829",
     "Samma mörkhet, mer mättad grön. Känns mer skog utan att bli svartare."),
    ("Mörkare",        "#0A1310", "#101B15", "#16241B", "#1E2E23",
     "Ett steg mörkare rakt av. Bilderna lyfter mer, men gröntonen tappar närvaro."),
    ("Mörkare + grönare", "#071410", "#0D1D15", "#132619", "#1B3122",
     "Både mörkare och mer mättad. Djupast känsla, men svagast kontrast mot korten."),
]

frames = []
for i, (name, bg, bgsoft, card, cardhi, note) in enumerate(VARIANTS):
    frames.append(f"""
    <figure class="shot">
      <h3>{name}</h3>
      <p class="n">{note}</p>
      <p class="hex">{bg}</p>
      <div class="frame v{i}"><div class="screen" id="scr{i}"></div></div>
    </figure>""")

overrides = "\n".join(
    f""".frame.v{i} {{ --bg: {bg}; --bg-soft: {bgsoft}; --card: {card}; --card-hi: {cardhi};
        background-color: {bg};
        background-image:
          radial-gradient(ellipse 700px 520px at 78% -6%, rgba(78,158,95,0.22), transparent 62%),
          radial-gradient(ellipse 620px 460px at 6% 32%, rgba(45,92,58,0.20), transparent 60%); }}"""
    for i, (_, bg, bgsoft, card, cardhi, _n) in enumerate(VARIANTS))

WRAP = """
  body.pv { background:#050906; padding:34px 20px 70px; display:block; }
  .pv-head { max-width:1180px; margin:0 auto 30px; text-align:center; }
  .pv-head h1 { font-size:2rem; letter-spacing:-0.03em; }
  .pv-head p { color:#9BAE9E; margin-top:8px; }
  .pv-grid { max-width:1180px; margin:0 auto; display:grid; gap:34px 26px;
             grid-template-columns:repeat(auto-fill, minmax(300px,1fr)); }
  .shot h3 { font-size:1.1rem; margin-bottom:4px; color:#F2F5EF; }
  .shot .n { color:#9BAE9E; font-size:0.86rem; line-height:1.4; min-height:3.4em; }
  .shot .hex { color:#6DC77C; font-size:0.8rem; font-weight:700; margin:6px 0 12px; letter-spacing:0.04em; }
  .frame { position:relative; overflow:hidden; width:100%; max-width:320px;
           aspect-ratio:375/812; border-radius:30px; border:1px solid rgba(255,255,255,.16);
           box-shadow:0 18px 48px rgba(0,0,0,.55); }
  .frame .heroimg, .frame .tabs, .frame .mutebtn { position:absolute !important; }
  .frame .screen { position:absolute; inset:0; overflow:hidden; padding:16px 14px 40px; z-index:0; }
  .frame .screen > .heroimg { height:52%; }
"""

SEED = MISSION_URI_JS + r"""
isMuted = function(){ return true; }; buzz = function(){};
missionImg = function(t){ var k = MISSION_IMG[t]; return k ? PREVIEW_IMG[k] : null; };
S.code="K7XM"; S.playerId=null; S.teamId=null; S.hostKey=null; S.offset=0;
S.data = { now:Date.now(),
  game:{ id:"g1", code:"K7XM", name:"Skogsrundan", duration_min:90, submit_min:3, started_at:null, ended_at:null },
  teams:[], players:[], missions:[], submissions:[], votes:[] };
VIEW="home"; render();
var homeHtml = document.getElementById("app").innerHTML;
for (var i=0;i<4;i++) {
  var el = document.getElementById("scr"+i);
  if (el) el.innerHTML = homeHtml;
}
document.getElementById("app").innerHTML = "";
var mb = document.getElementById("mutebtn"); if (mb) mb.remove();
"""

html = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fotojakten – välj bakgrundsfärg</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{css}
{WRAP}
{overrides}
</style>
<body class="pv">
<div class="pv-head">
  <h1>Vilken grön ska bära appen?</h1>
  <p>Samma startsida i fyra bakgrundsfärger. Titta helst i mobilen och utomhus – det är där den ska fungera.</p>
</div>
<div class="pv-grid">{''.join(frames)}</div>
<div id="app"></div><div id="ovl"></div><div id="toast"></div>
<button id="mutebtn" class="mutebtn"></button>
<script>
{js}
</script>
<script>
{SEED}
</script>
"""

pathlib.Path("valj-farg.html").write_text(html, encoding="utf-8")
print("wrote valj-farg.html", len(html))
