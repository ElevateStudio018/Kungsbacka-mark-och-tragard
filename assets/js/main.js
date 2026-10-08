(function () {
  var body = document.body;

  // Mobilmeny
  var toggle = document.querySelector('.menu-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.mobile-menu a').forEach(function (a) {
      a.addEventListener('click', function () {
        body.classList.remove('menu-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Till toppen
  var top = document.querySelector('.to-top');
  if (top) {
    var onScroll = function () { top.classList.toggle('show', window.scrollY > 600); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    top.addEventListener('click', function () { window.scrollTo({ top: 0 }); });
  }

  // Intoning
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  // Referensfilter
  var filters = document.querySelectorAll('.filter');
  var refs = document.querySelectorAll('.ref');
  filters.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var cat = btn.dataset.filter;
      filters.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
      refs.forEach(function (r) {
        r.hidden = !(cat === 'alla' || (r.dataset.cat || '').split(' ').indexOf(cat) > -1);
      });
    });
  });

  // Lightbox
  var lb = document.querySelector('.lightbox');
  if (lb && refs.length) {
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('.lightbox-caption');
    var current = 0;
    var visible = function () { return Array.prototype.filter.call(refs, function (r) { return !r.hidden; }); };
    var show = function (i) {
      var list = visible();
      current = (i + list.length) % list.length;
      var card = list[current];
      var img = card.querySelector('img');
      lbImg.src = card.dataset.full || img.src;
      lbImg.alt = img.alt;
      var h = card.querySelector('h3');
      lbCap.textContent = h ? h.textContent : '';
    };
    var open = function (card) {
      show(visible().indexOf(card));
      lb.classList.add('open');
      body.style.overflow = 'hidden';
      lb.querySelector('.lb-close').focus();
    };
    var close = function () { lb.classList.remove('open'); body.style.overflow = ''; };
    refs.forEach(function (card) {
      card.setAttribute('tabindex', '0');
      card.addEventListener('click', function () { open(card); });
      card.addEventListener('keydown', function (e) { if (e.key === 'Enter') open(card); });
    });
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(current - 1);
      if (e.key === 'ArrowRight') show(current + 1);
    });
  }

  // Offertformulär — öppnar e-postprogrammet med ifylld förfrågan.
  // Byt gärna mot Formspree/Netlify Forms för att ta emot förfrågningar direkt.
  var form = document.querySelector('#offert-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var tjanster = d.getAll('tjanst').join(', ') || 'Ej angivet';
      var text =
        'Namn: ' + d.get('namn') + '\n' +
        (d.get('foretag') ? 'Företag/förening: ' + d.get('foretag') + '\n' : '') +
        'Telefon: ' + d.get('telefon') + '\n' +
        'E-post: ' + (d.get('epost') || '-') + '\n' +
        'Ort: ' + (d.get('ort') || '-') + '\n' +
        'Gäller: ' + tjanster + '\n\n' +
        (d.get('meddelande') || '');
      window.location.href = 'mailto:anders@kungsbackamark.com?subject=' +
        encodeURIComponent('Offertförfrågan – ' + tjanster) + '&body=' + encodeURIComponent(text);
      var status = form.querySelector('.form-status');
      if (status) status.textContent = 'Tack! Ditt e-postprogram öppnas med förfrågan ifylld – tryck skicka så hör vi av oss.';
    });
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
