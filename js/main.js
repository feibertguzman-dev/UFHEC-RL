(function () {
  "use strict";

  var root = document.documentElement;
  var themeButton = document.querySelector("[data-theme-toggle]");
  var savedTheme = localStorage.getItem("housing-theme");
  if (savedTheme) {
    root.setAttribute("data-theme", savedTheme);
  }
  updateThemeLabel();

  if (themeButton) {
    themeButton.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      localStorage.setItem("housing-theme", next);
      updateThemeLabel();
    });
  }

  function updateThemeLabel() {
    if (!themeButton) return;
    var dark = root.getAttribute("data-theme") === "dark";
    themeButton.setAttribute("aria-label", dark ? "Activar modo claro" : "Activar modo oscuro");
    themeButton.innerHTML = dark ? sunIcon() : moonIcon();
  }

  function sunIcon() {
    return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>';
  }

  function moonIcon() {
    return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  }

  var navToggle = document.querySelector("[data-nav-toggle]");
  var navLinks = document.querySelector("[data-nav-links]");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
      var open = navLinks.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", String(open));
    });
    navLinks.addEventListener("click", function (event) {
      if (event.target.tagName === "A") {
        navLinks.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  var sections = Array.prototype.slice.call(document.querySelectorAll("main section[id]"));
  var links = Array.prototype.slice.call(document.querySelectorAll(".nav-links a[href^='#']"));
  if ("IntersectionObserver" in window && sections.length) {
    var navObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          links.forEach(function (link) {
            var active = link.getAttribute("href") === "#" + entry.target.id;
            link.setAttribute("aria-current", active ? "true" : "false");
          });
        });
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0.01 }
    );
    sections.forEach(function (section) {
      navObserver.observe(section);
    });
  }

  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var revealObserver = new IntersectionObserver(
      function (entries, observer) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    reveals.forEach(function (element) {
      revealObserver.observe(element);
    });
  } else {
    reveals.forEach(function (element) {
      element.classList.add("is-visible");
    });
  }

  document.querySelectorAll("[data-copy]").forEach(function (button) {
    button.addEventListener("click", function () {
      var target = document.getElementById(button.getAttribute("data-copy"));
      if (!target) return;
      var text = target.innerText;
      var done = function () {
        var original = button.textContent;
        button.textContent = "Copiado";
        window.setTimeout(function () {
          button.textContent = original;
        }, 1400);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(function () {});
      } else {
        var area = document.createElement("textarea");
        area.value = text;
        document.body.appendChild(area);
        area.select();
        document.execCommand("copy");
        area.remove();
        done();
      }
    });
  });

  var lightbox = document.querySelector("[data-lightbox]");
  var lightboxImage = lightbox ? lightbox.querySelector("img") : null;
  document.querySelectorAll("[data-zoom]").forEach(function (image) {
    image.addEventListener("click", function () {
      if (!lightbox || !lightboxImage) return;
      lightboxImage.src = image.src;
      lightboxImage.alt = image.alt;
      lightbox.classList.add("is-open");
    });
  });
  if (lightbox) {
    lightbox.addEventListener("click", function (event) {
      if (event.target === lightbox || event.target.hasAttribute("data-lightbox-close")) {
        lightbox.classList.remove("is-open");
      }
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") lightbox.classList.remove("is-open");
    });
  }

  var income = document.getElementById("income-range");
  var incomeOut = document.getElementById("income-value");
  var prediction = document.getElementById("quick-prediction");
  if (income && prediction) {
    var intercept = Number(prediction.getAttribute("data-intercept"));
    var coef = Number(prediction.getAttribute("data-coef"));
    var render = function () {
      var value = Number(income.value);
      if (incomeOut) incomeOut.textContent = value.toFixed(2) + " × $10,000 = $" + Math.round(value * 10000).toLocaleString("en-US");
      var estimate = Math.max(0, intercept + coef * value);
      prediction.textContent = "$" + Math.round(estimate).toLocaleString("en-US");
    };
    income.addEventListener("input", render);
    render();
  }

  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());
})();
