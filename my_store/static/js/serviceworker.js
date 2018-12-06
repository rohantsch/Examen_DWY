var CACHE_NAME = 'examen-cache';

var urlsToCache = [
    '/',
    '/static/icons/fuse-icon-font/style.css',
    '/static/node_modules/animate.css/animate.min.css',
    '/static/node_modules/pnotify/src/PNotifyBrightTheme.css',
    '/static/node_modules/nvd3/build/nv.d3.min.css',
    '/static/node_modules/perfect-scrollbar/css/perfect-scrollbar.css',
    '/static/fuse-html/fuse-html.min.css',
    '/static/node_modules/jquery/dist/jquery.min.js',
    '/static/node_modules/mobile-detect/mobile-detect.min.js',
    '/static/node_modules/perfect-scrollbar/dist/perfect-scrollbar.min.js',
    '/static/node_modules/popper.js/dist/umd/popper.min.js',
    '/static/node_modules/bootstrap/dist/js/bootstrap.min.js',
    '/static/node_modules/nvd3/build/nv.d3.min.js',
    '/static/node_modules/datatables.net/js/jquery.dataTables.js',
    '/static/node_modules/datatables-responsive/js/dataTables.responsive.js',
    '/static/node_modules/pnotify/dist/iife/PNotify.js',
    '/static/node_modules/pnotify/dist/iife/PNotifyStyleMaterial.js',
    '/static/node_modules/pnotify/dist/iife/PNotifyButtons.js',
    '/static/node_modules/pnotify/dist/iife/PNotifyCallbacks.js',
    '/static/node_modules/pnotify/dist/iife/PNotifyMobile.js',
    '/static/node_modules/pnotify/dist/iife/PNotifyHistory.js',
    '/static/node_modules/pnotify/dist/iife/PNotifyDesktop.js',
    '/static/node_modules/pnotify/dist/iife/PNotifyConfirm.js',
    '/static/node_modules/pnotify/dist/iife/PNotifyReference.js',
    '/static/fuse-html/fuse-html.min.js',
    '/static/js/main.js',

    //Registrar
    '/static/favicon.ico',
    '/static/css/main.css',
];


self.addEventListener('install', function(event) {
// Perform install steps
	event.waitUntil(
		caches.open(CACHE_NAME)
			.then(function(cache) {
				console.log('Cache Abierto!');
				return cache.addAll(urlsToCache);
			})
	);
});

self.addEventListener('activate', function(event) {
  console.log('Finally active. Ready to start serving content!');  
});


self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
        .then(function(response) {
            // Cache hit - return response
        if (response) {
            return response;
        }
        return fetch(event.request);
        })
    );
});
