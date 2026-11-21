(function(){
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('js');

  // Revelar ao rolar
  var els = document.querySelectorAll('[data-reveal]');
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    }, {threshold: .14, rootMargin: '0px 0px -40px 0px'});
    els.forEach(function(el, i){
      var d = el.getAttribute('data-delay'); if (d) el.style.transitionDelay = d + 'ms';
      io.observe(el);
    });
  } else { els.forEach(function(el){ el.classList.add('in'); }); }

  // Contadores
  var nums = document.querySelectorAll('[data-count]');
  function run(el){
    var end = parseFloat(el.getAttribute('data-count')), dec = (el.getAttribute('data-count').split('.')[1]||'').length;
    if (reduce){ el.textContent = end.toFixed(dec).replace('.', ','); return; }
    var t0 = null, dur = 1400;
    function step(t){ if(!t0) t0 = t; var p = Math.min((t - t0)/dur, 1); var v = end * (1 - Math.pow(1 - p, 3));
      el.textContent = v.toFixed(dec).replace('.', ','); if (p < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window) {
    var io2 = new IntersectionObserver(function(entries){ entries.forEach(function(e){ if(e.isIntersecting){ run(e.target); io2.unobserve(e.target);} }); }, {threshold: .6});
    nums.forEach(function(n){ io2.observe(n); });
  } else nums.forEach(run);

  // Barra fixa de agendamento (celular) e topo com sombra
  var bar = document.querySelector('.stickybar'), top = document.querySelector('.top');
  function onScroll(){
    var y = window.scrollY || 0;
    if (bar) bar.classList.toggle('show', y > 420);
    if (top) top.classList.toggle('scrolled', y > 8);
  }
  window.addEventListener('scroll', onScroll, {passive: true}); onScroll();

  // Parallax suave nas formas do topo
  var par = document.querySelectorAll('[data-par]');
  if (!reduce && par.length){
    window.addEventListener('scroll', function(){
      var y = window.scrollY || 0;
      par.forEach(function(p){ p.style.transform = 'translate3d(0,' + (y * parseFloat(p.getAttribute('data-par'))) + 'px,0)'; });
    }, {passive: true});
  }

  // Serviço pré-selecionado a partir do botão clicado
  document.querySelectorAll('[data-svc]').forEach(function(a){
    a.addEventListener('click', function(){
      var s = document.getElementById('servico'); if (s) s.value = a.getAttribute('data-svc');
    });
  });
})();
document.querySelectorAll('input[name="pagina"]').forEach(function(i){ i.value = location.pathname; });
/* Conversões: clique no WhatsApp ou no telefone */
(function () {
  function conv(tipo) {
    /* A conversão do Google Ads ([A31] Clique botão Whats) é disparada pelo Tag Manager no clique em links wa.me */
    try { if (window.gtag) gtag('event', 'generate_lead', { method: tipo, page_path: location.pathname }); } catch (e) {}
    try { if (window.fbq) fbq('track', 'Contact'); } catch (e) {}
  }
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[href]'); if (!a) return;
    var h = a.getAttribute('href');
    if (h.indexOf('wa.me') > -1) conv('whatsapp'); else if (h.indexOf('tel:') === 0) conv('telefone');
  });
})();
