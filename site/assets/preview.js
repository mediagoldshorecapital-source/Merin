/* Single-newsletter preview + preflight. */
(function () {
  var params = new URLSearchParams(location.search);
  var id = params.get('id');
  var detail = document.getElementById('detail');
  var titleEl = document.getElementById('title');
  var eyebrowEl = document.getElementById('eyebrow');
  var toastEl = document.getElementById('toast');

  // Rough inbox truncation points. Subject lines get cut around 40 chars on
  // narrow mobile clients; preview text past ~140 is almost never shown.
  var SUBJECT_LIMIT = 60;
  var PREVIEW_LIMIT = 140;

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function toast(msg) {
    toastEl.textContent = msg;
    toastEl.classList.add('show');
    clearTimeout(toast._t);
    toast._t = setTimeout(function () { toastEl.classList.remove('show'); }, 1800);
  }

  function counter(len, limit, unit) {
    var over = len > limit;
    return '<div class="counter' + (over ? ' warn' : '') + '">' + len + ' ' + unit +
      (over ? ' — over ' + limit + ', likely truncated in the inbox' : '') + '</div>';
  }

  function checks(n) {
    var s = n.stats;
    var rows = [
      {
        pass: !s.clipped,
        text: s.kb + ' KB message size',
        note: s.clipped
          ? 'Over Gmail’s 102 KB limit — the tail, including the unsubscribe link, gets clipped.'
          : 'Comfortably under Gmail’s 102 KB clipping threshold.'
      },
      {
        pass: s.hasUnsubscribe,
        text: 'Unsubscribe link',
        note: s.hasUnsubscribe
          ? 'Present in the footer.'
          : 'Missing — required by CAN-SPAM and GDPR before this can send.'
      },
      {
        pass: s.images === 0 || s.imagesMissingAlt === 0,
        text: s.images + ' image' + (s.images === 1 ? '' : 's'),
        note: s.images === 0
          ? 'Text-only — nothing to break when images are blocked by default.'
          : (s.imagesMissingAlt
              ? s.imagesMissingAlt + ' without alt text; those render blank when images are off.'
              : 'All images carry alt text.')
      },
      {
        pass: s.linkCount > 0,
        text: s.linkCount + ' unique link' + (s.linkCount === 1 ? '' : 's'),
        note: s.linkCount ? 'Check each destination below before sending.' : 'No outbound links — the email has no call to action.'
      }
    ];

    return '<ul class="checks">' + rows.map(function (r) {
      return '<li class="' + (r.pass ? 'pass' : 'flag') + '">' +
        '<span class="mark" aria-hidden="true">' + (r.pass ? '✓' : '!') + '</span>' +
        '<span><strong>' + esc(r.text) + '</strong><br><span class="note">' + esc(r.note) + '</span></span>' +
      '</li>';
    }).join('') + '</ul>';
  }

  function render(n) {
    document.title = n.title + ' — Forge';
    titleEl.textContent = n.title;
    eyebrowEl.textContent = n.brand + (n.date ? ' · ' + n.date : '');

    detail.innerHTML =
      '<div class="stage">' +
        '<div class="stage-bar">' +
          '<div class="seg" role="group" aria-label="Preview width">' +
            '<button type="button" data-w="desktop" aria-pressed="true">Desktop</button>' +
            '<button type="button" data-w="mobile" aria-pressed="false">Mobile</button>' +
          '</div>' +
          '<button class="btn" id="copy" type="button">Copy HTML</button>' +
          '<a class="btn" href="' + esc(n.file) + '" target="_blank" rel="noopener">Open raw</a>' +
        '</div>' +
        '<div class="frame" id="frame">' +
          '<iframe id="email" src="' + esc(n.file) + '" title="' + esc(n.title) + ' email preview"></iframe>' +
        '</div>' +
      '</div>' +

      '<aside class="panel">' +
        '<div class="box">' +
          '<h3>Inbox preview</h3>' +
          '<div class="field"><label>Subject</label><div class="value">' +
            (n.subject ? esc(n.subject) : '<span class="note">Not set</span>') + '</div>' +
            (n.subject ? counter(n.subject.length, SUBJECT_LIMIT, 'characters') : '') +
          '</div>' +
          '<div class="field"><label>Preview text</label><div class="value">' +
            (n.previewText ? esc(n.previewText) : '<span class="note">Not set</span>') + '</div>' +
            (n.previewText ? counter(n.previewText.length, PREVIEW_LIMIT, 'characters') : '') +
          '</div>' +
          '<div class="field"><label>Status</label><div class="value">' +
            '<span class="badge ' + esc(n.status) + '">' + esc(n.status) + '</span></div></div>' +
        '</div>' +

        '<div class="box"><h3>Preflight</h3>' + checks(n) + '</div>' +

        (n.stats.links.length
          ? '<div class="box"><h3>Links</h3><ul class="linklist">' +
              n.stats.links.map(function (l) {
                return '<li><a href="' + esc(l.url) + '" target="_blank" rel="noopener">' + esc(l.url) + '</a>' +
                  (l.count > 1 ? ' <span class="count">×' + l.count + '</span>' : '') + '</li>';
              }).join('') +
            '</ul></div>'
          : '') +

        (n.links.length
          ? '<div class="box"><h3>Working files</h3><ul class="linklist">' +
              n.links.map(function (l) {
                return '<li><a href="' + esc(l.url) + '" target="_blank" rel="noopener">' + esc(l.label) + '</a></li>';
              }).join('') +
            '</ul></div>'
          : '') +

        (n.checklist.length
          ? '<div class="box"><h3>Before sending</h3><ul class="todo">' +
              n.checklist.map(function (c) { return '<li>' + esc(c) + '</li>'; }).join('') +
            '</ul></div>'
          : '') +

        '<div class="box"><h3>Source</h3><div class="field"><div class="value"><code>' +
          esc(n.source) + '</code></div></div></div>' +
      '</aside>';

    var frame = document.getElementById('frame');
    var iframe = document.getElementById('email');

    detail.querySelectorAll('.seg button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        detail.querySelectorAll('.seg button').forEach(function (b) {
          b.setAttribute('aria-pressed', String(b === btn));
        });
        frame.classList.toggle('mobile', btn.dataset.w === 'mobile');
      });
    });

    // Same-origin, so we can size the frame to the email instead of guessing.
    function fit() {
      try {
        var doc = iframe.contentDocument;
        if (doc && doc.body) {
          iframe.style.height = Math.max(doc.body.scrollHeight, doc.documentElement.scrollHeight) + 'px';
        }
      } catch (e) { /* keep the CSS fallback height */ }
    }
    iframe.addEventListener('load', function () { fit(); setTimeout(fit, 120); });
    window.addEventListener('resize', fit);

    document.getElementById('copy').addEventListener('click', function () {
      fetch(n.file)
        .then(function (r) { return r.text(); })
        .then(function (html) { return navigator.clipboard.writeText(html); })
        .then(function () { toast('HTML copied to clipboard'); })
        .catch(function () { toast('Copy failed — use “Open raw” instead'); });
    });
  }

  fetch('data/newsletters.json')
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      var list = data.newsletters || [];
      var n = list.find(function (x) { return x.id === id; });
      if (!n) {
        titleEl.textContent = 'Newsletter not found';
        detail.innerHTML = '<div class="empty">No newsletter with id <code>' + esc(id || '') +
          '</code>. <a href="./">See all newsletters.</a></div>';
        return;
      }
      render(n);
    })
    .catch(function (err) {
      titleEl.textContent = 'Could not load';
      detail.innerHTML = '<div class="empty">' + esc(err.message) + '</div>';
    });
})();
