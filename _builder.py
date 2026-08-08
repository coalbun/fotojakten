import base64, pathlib, re

src = pathlib.Path("index.html").read_text(encoding="utf-8")
css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
js  = re.search(r"<script>\n(.*)</script>", src, re.S).group(1)

def data_uri(name):
    b64 = base64.b64encode(pathlib.Path(f"img/{name}.webp").read_bytes()).decode()
    return f"data:image/webp;base64,{b64}"

# inline the two CSS-referenced photos so the preview page stands on its own
for _name in ["hero", "finale"]:
    css = css.replace(f"url('img/{_name}.webp')", f"url('{data_uri(_name)}')")

# the mission photos are referenced from JS, so hand the preview a lookup table
MISSION_KEYS = ["m-djur", "m-korv", "m-trick", "m-natur", "m-album", "m-alg", "m-film"]
MISSION_URI_JS = "var PREVIEW_IMG = {" + ",".join(
    f'"{k}":"{data_uri(k)}"' for k in MISSION_KEYS
) + "};"

# neutralise the boot IIFE so the preview never auto-loads a game or starts polling
_boot = re.search(r"\(function boot\(\).*?\)\(\);", js, re.S)
assert _boot, "boot IIFE not found in index.html"
js = js.replace(_boot.group(0), "/* boot disabled in preview */")

WRAP_CSS = """
  body.pv {
    background: #0B140E;
    padding: 34px 20px 70px;
    display: block;
  }
  .pv-head { max-width: 1180px; margin: 0 auto 30px; text-align: center; }
  .pv-head h1 { font-size: 2.1rem; letter-spacing: -0.035em; }
  .pv-head p { color: var(--muted); margin-top: 8px; }
  .pv-grid {
    max-width: 1180px; margin: 0 auto;
    display: grid; gap: 40px 30px;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  }
  .pv-section {
    grid-column: 1 / -1;
    padding: 26px 0 4px;
    border-top: 1px solid var(--line-strong);
    margin-top: 20px;
  }
  .pv-section h2 { font-size: 1.5rem; }
  .pv-section p { color: var(--muted); font-size: 0.9rem; margin-top: 6px; max-width: 620px; }
  .shot { display: block; }
  .shot h3 { font-size: 1.05rem; margin-bottom: 3px; }
  .shot .n { color: var(--muted); font-size: 0.85rem; min-height: 2.6em; margin-bottom: 12px; line-height: 1.4; }
  .frame {
    position: relative; overflow: hidden;
    width: 100%; max-width: 330px; aspect-ratio: 375 / 812;
    border-radius: 30px; border: 1px solid var(--line-strong);
    background-color: var(--bg);
    background-image:
      radial-gradient(ellipse 700px 520px at 78% -6%, rgba(78,158,95,0.22), transparent 62%),
      radial-gradient(ellipse 620px 460px at 6% 32%, rgba(45,92,58,0.20), transparent 60%);
    box-shadow: 0 18px 48px rgba(0,0,0,0.5);
  }
  /* the app pins things to the viewport; inside a frame they must pin to the frame */
  .frame .tabs, .frame .heroimg, .frame .finale, .frame .dropfx,
  .frame .mutebtn, .frame .overlay, .frame .checkfx, .frame .lightbox {
    position: absolute !important;
  }
  .frame .tabs { left: 12px; right: 12px; bottom: 12px; margin: 0; max-width: none; }
  .frame .finale .hint { position: absolute !important; bottom: 16px; }
  .frame .screen {
    position: absolute; inset: 0; overflow: hidden;
    padding: 16px 14px 100px;
    z-index: 0;            /* own stacking context so the hero image sits behind content, not behind the frame */
  }
  .frame .screen > .heroimg { height: 62%; }
"""

SEED_JS = MISSION_URI_JS + r"""
isMuted = function () { return true; };   // silence audio in the preview
buzz = function () {};
// relative image paths can't resolve on the artifact host, so serve them inline
missionImg = function (title) {
  var key = MISSION_IMG[title];
  return key ? PREVIEW_IMG[key] : null;
};

function fakePhoto(c1, c2, label) {
  var svg = "<svg xmlns='http://www.w3.org/2000/svg' width='300' height='400'>" +
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>" +
    "<stop offset='0' stop-color='" + c1 + "'/><stop offset='1' stop-color='" + c2 + "'/>" +
    "</linearGradient></defs><rect width='300' height='400' fill='url(#g)'/>" +
    "<text x='150' y='215' font-family='sans-serif' font-size='30' font-weight='bold' " +
    "fill='rgba(255,255,255,.85)' text-anchor='middle'>" + label + "</text></svg>";
  return "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
}
BUCKET_PUB = "";

var T1="t1",T2="t2",T3="t3",P1="p1",P2="p2",P3="p3",M1="m1",M2="m2",M3="m3";
function SEED(startedOffsetSec, ended) {
  S.code="K7XM"; S.playerId=P1; S.teamId=T1; S.hostKey="host"; S.offset=0;
  S.data = {
    now: Date.now(),
    game: { id:"g1", code:"K7XM", name:"Skogsrundan", duration_min:90, submit_min:3,
      started_at: startedOffsetSec===null ? null : Date.now()-startedOffsetSec*1000,
      ended_at: ended ? Date.now()-1000 : null },
    teams: [
      { id:T1, name:"Grodorna", avatar_path:null },
      { id:T2, name:"Ugglorna", avatar_path:null },
      { id:T3, name:"Rävarna",  avatar_path:null }
    ],
    players: [
      { id:P1, team_id:T1, name:"Per" },
      { id:P2, team_id:T2, name:"Anna" },
      { id:P3, team_id:T3, name:"Kalle" }
    ],
    missions: [
      { id:M1, idx:0, title:DEFAULT_MISSIONS[0], open_s:120 },
      { id:M2, idx:1, title:DEFAULT_MISSIONS[1], open_s:1800 },
      { id:M3, idx:2, title:DEFAULT_MISSIONS[5], open_s:3600 }
    ],
    submissions: [
      { id:"s1", mission_id:M1, player_id:P1, team_id:T1, photo_path:fakePhoto("#2F6B3A","#14361D","Grodorna"), thumb_path:fakePhoto("#2F6B3A","#14361D","Grodorna") },
      { id:"s2", mission_id:M1, player_id:P2, team_id:T2, photo_path:fakePhoto("#7B4E9E","#3A2350","Ugglorna"), thumb_path:fakePhoto("#7B4E9E","#3A2350","Ugglorna") },
      { id:"s3", mission_id:M1, player_id:P3, team_id:T3, photo_path:fakePhoto("#B5642F","#5C2F14","Rävarna"),  thumb_path:fakePhoto("#B5642F","#5C2F14","Rävarna") }
    ],
    votes: [
      { mission_id:M1, voter_player_id:P1, submission_id:"s2" },
      { mission_id:M1, voter_player_id:P2, submission_id:"s1" },
      { mission_id:M1, voter_player_id:P3, submission_id:"s2" }
    ]
  };
  S.lastSig=""; S.finaleOpen=false; S.finaleClosed=false; S.votePick={};
}

var GRID = document.getElementById("pvgrid");
function frame(label, note, html, isOverlay) {
  var fig = document.createElement("figure");
  fig.className = "shot";
  var inner = isOverlay ? html : '<div class="screen">' + html + "</div>";
  fig.innerHTML = "<h3></h3><p class='n'></p><div class='frame'>" + inner + "</div>";
  fig.querySelector("h3").textContent = label;
  fig.querySelector(".n").textContent = note;
  GRID.appendChild(fig);
}
function shot(label, note) { frame(label, note, document.getElementById("app").innerHTML, false); }
function shotOvl(label, note) { frame(label, note, document.getElementById("ovl").innerHTML, true); }

/* ---- every screen, in the order you meet them ---- */
SEED(null,false); VIEW="home"; render();
shot("1 · Startsidan", "Det första alla ser när de öppnar länken.");

VIEW="create"; render();
shot("2 · Skapa ny fotojakt", "Bara spelledaren ser den här. Här sätts promenadens längd.");

SEED(null,false); S.hostKey=null; S.playerId=null; S.teamId=null; VIEW="lobby"; render();
shot("3 · Lobbyn – ny spelare", "Så här ser det ut för den som precis klickat på länken.");

SEED(null,false); VIEW="lobby"; render();
shot("4 · Lobbyn – spelledaren", "Koden delas, lagen dyker upp, du startar när alla är med.");

SEED(60,false); VIEW="game"; S.tab="mission"; render();
shot("5 · Jakten är igång", "Mellan uppdragen. Ingen vet när nästa dyker upp.");

var mp = mParts(S.data.missions[0].title);
frame("6 · Nytt uppdrag!", "Fullskärm med uppdragets egen bild, ljud och vibration.",
  '<div class="dropfx photo" style="background-image:' +
    "linear-gradient(180deg, rgba(8,18,11,0.30) 0%, rgba(8,18,11,0.18) 28%, rgba(8,18,11,0.72) 55%, rgba(8,18,11,0.94) 76%, rgba(8,18,11,0.98) 100%), url('" +
    missionImg(S.data.missions[0].title) + "')\">" +
  '<span class="label dlabel">Nytt uppdrag</span>' +
  '<div class="dtitle">' + esc(mp.text) + "</div></div>", true);

SEED(130,false); S.data.submissions=[]; VIEW="game"; S.tab="mission"; render();
shot("7 · Dags att fota", "Kameraknappen syns direkt – ingen scroll behövs.");

SEED(130,false); S.data.submissions=S.data.submissions.slice(0,1); VIEW="game"; S.tab="mission"; render();
shot("8 · Bilden är inne", "Vem som helst i laget kan byta eller ta bort den.");

SEED(300,false); VIEW="game"; S.tab="mission"; render();
shot("9 · Röstning", "Alla bilder anonymt. Ert eget lag är nedtonat och går inte att rösta på.");

SEED(3700,false); VIEW="game"; showRevealOverlay(S.data.missions[0]);
shotOvl("10 · Trumvirvel", "Spänningen byggs upp innan vinnaren visas.");

renderRevealResult(S.data.missions[0]); stopConfetti();
shotOvl("11 · Resultatet", "Konfetti och fanfar. Övriga bilder ligger under.");

SEED(3700,false); VIEW="game"; S.tab="gallery"; render();
shot("12 · Bilder", "Alla bilder från avklarade uppdrag, med röster och vinnarmarkering.");

SEED(3700,false); VIEW="game"; S.tab="score"; render();
shot("13 · Topplista", "Poäng = röster på lagets bilder.");

SEED(5000,false); VIEW="game"; S.tab="mission"; render();
shot("14 · Alla uppdrag klara", "Spelledaren startar prisutdelningen härifrån.");

SEED(5000,true); VIEW="game";
var slides = finaleSlides();
var titles = { intro:"15 · Prisutdelning", mission:"16 · Vinnarbild per uppdrag",
               podium:"17 · Pallplats", winner:"18 · Vinnaren", table:"19 · Slutställning" };
var notes  = { intro:"Samla alla runt en telefon och tryck er igenom.",
               mission:"En slide per uppdrag med den vinnande bilden.",
               podium:"Räknar ner från tredje plats.",
               winner:"Konfetti och fanfar.",
               table:"Alla bilder finns kvar under Bilder efteråt." };
var seen = {};
slides.forEach(function (sl, i) {
  if (seen[sl.type]) return;
  seen[sl.type] = 1;
  S.finaleStep = i; S.finaleOpen = true; renderFinale(); stopConfetti();
  shotOvl(titles[sl.type], notes[sl.type]);
});
/* ---- alla sju uppdrag med sina egna bilder ---- */
function sectionHeading(title, note) {
  var h = document.createElement("div");
  h.className = "pv-section";
  h.innerHTML = "<h2></h2><p></p>";
  h.querySelector("h2").textContent = title;
  h.querySelector("p").textContent = note;
  GRID.appendChild(h);
}
sectionHeading("De sju hemliga uppdragen",
  "Så här ser varje uppdrag ut när det plötsligt släpps. Ordningen slumpas – ingen vet vilket som kommer när.");

var DROP_GRAD = "linear-gradient(180deg, rgba(8,18,11,0.30) 0%, rgba(8,18,11,0.18) 28%, " +
                "rgba(8,18,11,0.72) 55%, rgba(8,18,11,0.94) 76%, rgba(8,18,11,0.98) 100%)";
DEFAULT_MISSIONS.forEach(function (title, i) {
  var img = missionImg(title);
  frame("Uppdrag " + (i + 1), title,
    '<div class="dropfx photo" style="background-image:' + DROP_GRAD +
      (img ? ", url('" + img + "')" : "") + '">' +
      '<span class="label dlabel">Nytt uppdrag</span>' +
      '<div class="dtitle">' + esc(title) + "</div></div>", true);
});

document.getElementById("app").innerHTML = "";
document.getElementById("ovl").innerHTML = "";
var mb = document.getElementById("mutebtn"); if (mb) mb.remove();
"""

html = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fotojakten – alla skärmar</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{css}
{WRAP_CSS}
</style>
<body class="pv">
<div class="pv-head">
  <h1>Fotojakten – alla skärmar</h1>
  <p>Varje vy i den ordning ni möter dem. Riktig kod och riktig design, med påhittade lag och bilder.</p>
</div>
<div class="pv-grid" id="pvgrid"></div>
<div id="app"></div>
<div id="ovl"></div>
<div id="toast"></div>
<button id="mutebtn" class="mutebtn" aria-label="Ljud"></button>
<script>
{js}
</script>
<script>
{SEED_JS}
</script>
"""

pathlib.Path("alla-skarmar.html").write_text(html, encoding="utf-8")
print("wrote alla-skarmar.html", len(html), "chars")
