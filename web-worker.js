caches.open("pwa-assets")
.then(cache => {
	cache.addAll(); 
});


self.addEventListener('install', (e) => {
  e.waitUntil(
      caches.open('fox-store').then((cache) => cache.addAll(
		  ["core.css",
		   "webstyle.css",
		   "resume.html",
		   "index.html",
		   "web-worker.js",
		   "app.js",
		   "manifest.json",
		   "images/android-chrome-192x192.png",
		   "images/apple-touch-icon.png",
		   "images/favicon-32x32.png",
		   "images/android-chrome-512x512.png",
		   "images/favicon-16x16.png",
		   "images/favicon.ico"]
   )),
  );
});

self.addEventListener('fetch', (e) => {
  console.log(e.request.url);
  e.respondWith(
    caches.match(e.request).then((response) => response || fetch(e.request)),
  );
});
