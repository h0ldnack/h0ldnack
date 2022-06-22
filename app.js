if ('serviceWorker' in navigator) {
	navigator.serviceWorker
		.register('/web-worker.js')
		.then(() => { console.log('Service Worker Registered'); });
}
