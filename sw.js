/* Fotojakten – service worker.
   Servern skickar en tom "väckning". Vi hämtar själva vad som gäller
   och bygger notisen här, så ingen nyttolast behöver krypteras. */

var SUPA_URL = "https://uqizcqnedzozmsmlkuhz.supabase.co";
var SUPA_KEY = "sb_publishable_p71i3T6a_SJgvyhjDEaz0w_UKC-Qxtc";

self.addEventListener("install", function (e) { self.skipWaiting(); });
self.addEventListener("activate", function (e) { e.waitUntil(self.clients.claim()); });

function api(fn, args) {
  return fetch(SUPA_URL + "/rest/v1/rpc/" + fn, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      apikey: SUPA_KEY,
      Authorization: "Bearer " + SUPA_KEY
    },
    body: JSON.stringify(args || {})
  }).then(function (r) { return r.ok ? r.json() : null; });
}

/* vilket uppdrag är öppet just nu? */
function currentMission(state) {
  var g = state.game;
  if (!g.started_at || g.ended_at) return null;
  var t = (Date.now() - g.started_at) / 1000;
  var open = null;
  state.missions.forEach(function (m) {
    if (m.open_s <= t && t < m.open_s + g.submit_min * 60) open = m;
  });
  return open;
}

self.addEventListener("push", function (event) {
  event.waitUntil(
    self.registration.pushManager.getSubscription()
      .then(function () {
        return caches.open("fotojakt").then(function (c) { return c.match("game-code"); });
      })
      .then(function (res) { return res ? res.text() : null; })
      .then(function (code) {
        if (!code) return null;
        return api("get_state", { p_code: code });
      })
      .then(function (state) {
        var title = "Nytt uppdrag!";
        var body = "Öppna Fotojakten – klockan tickar.";
        if (state) {
          var m = currentMission(state);
          if (m) body = m.title;
        }
        return self.registration.showNotification(title, {
          body: body,
          icon: "img/icon-192.png",
          badge: "img/icon-192.png",
          tag: "fotojakt-uppdrag",
          renotify: true,
          /* ligger kvar tills man tittar - lätt att missa ett pling ute på en promenad */
          requireInteraction: true,
          silent: false,
          vibrate: [400, 120, 400, 120, 600]
        });
      })
      .catch(function () {
        return self.registration.showNotification("Nytt uppdrag!", {
          body: "Öppna Fotojakten – klockan tickar.",
          tag: "fotojakt-uppdrag",
          renotify: true,
          requireInteraction: true,
          silent: false,
          vibrate: [400, 120, 400, 120, 600]
        });
      })
  );
});

self.addEventListener("notificationclick", function (event) {
  event.notification.close();
  event.waitUntil(
    caches.open("fotojakt")
      .then(function (c) { return c.match("game-code"); })
      .then(function (res) { return res ? res.text() : null; })
      .then(function (code) {
        var url = code ? "./?g=" + code : "./";
        return self.clients.matchAll({ type: "window", includeUncontrolled: true })
          .then(function (list) {
            for (var i = 0; i < list.length; i++) {
              if (list[i].url.indexOf(self.registration.scope) === 0 && "focus" in list[i]) {
                return list[i].focus();
              }
            }
            return self.clients.openWindow(url);
          });
      })
  );
});
