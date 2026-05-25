self.addEventListener("install", event => {
    console.log("Service Worker: zainstalowany");
});

self.addEventListener("activate", event => {
    console.log("Service Worker: aktywny");
});

self.addEventListener("fetch", event => {
    // Możesz dodać cache, ale na razie zostawiamy minimalnie
});
