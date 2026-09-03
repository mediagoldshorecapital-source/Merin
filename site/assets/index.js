/* Newsletter gallery. */
(function () {
  var grid = document.getElementById('grid');

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function card(n) {
    var flags = [];
    if (n.stats.clipped) flags.push('Gmail clipping');
    if (!n.stats.hasUnsubscribe) flags.push('no unsubscribe');
    if (n.stats.imagesMissingAlt) flags.push(n.stats.imagesMissingAlt + ' missing alt');

    return (
      '<a class="card" href="preview.html?id=' + encodeURIComponent(n.id) + '">' +
        '<div class="thumb"><iframe src="' + esc(n.file) + '" title="" tabindex="-1" loading="lazy" scrolling="no" aria-hidden="true"></iframe></div>' +
        '<div class="card-body">' +
          '<h2>' + esc(n.title) + '</h2>' +
          (n.subject ? '<div class="subject">' + esc(n.subject) + '</div>' : '') +
          (n.previewText ? '<p class="preview-text">' + esc(n.previewText) + '</p>' : '') +
          '<div class="meta-row">' +
            '<span class="badge ' + esc(n.status) + '">' + esc(n.status) + '</span>' +
            '<span>' + n.stats.kb + ' KB</span>' +
            '<span>' + n.stats.linkCount + ' link' + (n.stats.linkCount === 1 ? '' : 's') + '</span>' +
            (flags.length ? '<span class="counter warn">' + esc(flags.join(' · ')) + '</span>' : '') +
          '</div>' +
        '</div>' +
      '</a>'
    );
  }

  fetch('data/newsletters.json')
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      grid.removeAttribute('aria-busy');
      var list = data.newsletters || [];
      if (!list.length) {
        grid.outerHTML = '<div class="empty">No newsletters yet. Add a folder under <code>newsletters/</code> containing an <code>email.html</code> and rebuild.</div>';
        return;
      }
      grid.innerHTML = list.map(card).join('');
      var built = document.getElementById('built');
      if (built && data.builtAt) {
        built.textContent = 'Built ' + new Date(data.builtAt).toLocaleString();
      }
    })
    .catch(function (err) {
      grid.removeAttribute('aria-busy');
      grid.outerHTML = '<div class="empty">Could not load newsletter data (' + esc(err.message) + ').</div>';
    });
})();
