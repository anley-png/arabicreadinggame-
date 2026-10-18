const C='ali-v3';
self.addEventListener('install',e=>e.waitUntil(caches.open(C).then(c=>c.addAll(['./','index.html','manifest.webmanifest']))));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;
 e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(x=>{const k=x.clone();if(x.ok)caches.open(C).then(c=>c.put(e.request,k));return x}).catch(()=>r)))});
