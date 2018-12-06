if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register('/serviceworker.js')
        .then(function() {
            console.log('ServiceWorker registrado!');
        })
        .catch(function(err) {
            console.log('ServiceWorker Error al registrar :(', err);
        });
    });
  }