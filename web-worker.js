caches.open("pwa-assets")
.then(cache => {
	cache.addAll(["core.css", "webstyle.css", "resume.html", "index.html", "web-worker.js", "manifest.json"]); 
});
