if ('serviceWorker' in navigator) {
	navigator.serviceWorker
		.register('/web-worker.js')
		.then(() => { console.log('Service Worker Registered'); });
}
function notify() {
	alert("Welcome")
}
function registerNotification() {
	Notification.requestPermission(permission => {
		if (permission === 'granted'){ notify() }
		else console.error("Permission was not granted.")
	})
}
