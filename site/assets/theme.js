/* Theme toggle: light -> dark -> follow system, remembered per browser. */
(function () {
  var KEY = 'forge-theme';
  var order = ['light', 'dark', 'system'];

  function stored() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }

  function apply(mode) {
    if (mode === 'light' || mode === 'dark') {
      document.documentElement.setAttribute('data-theme', mode);
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
  }

  var current = stored() || 'system';
  apply(current);

  document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('theme');
    if (!btn) return;
    var label = function () {
      btn.textContent = current === 'system' ? 'Theme: auto' : 'Theme: ' + current;
    };
    label();
    btn.addEventListener('click', function () {
      current = order[(order.indexOf(current) + 1) % order.length];
      apply(current);
      try { localStorage.setItem(KEY, current); } catch (e) { /* private mode */ }
      label();
    });
  });
})();
