const RICE_INDEX = [
  { type: "Essay", title: "Crowley Modernism", author: "C. Sandbatch", href: "essay-template.html", meta: "Acadia Parish · Vol. 1" },
  { type: "Essay", title: "Against Cotton Memory", author: "J. T. Miller", href: "essays.html", meta: "Delta memory · Vol. 1" },
  { type: "Fiction", title: "The Pump House", author: "L. Doucet", href: "fiction-template.html", meta: "Vermilion Parish · Vol. 1" },
  { type: "Poetry", title: "Crawfish Pond with Saints", author: "C. Sandbatch", href: "poem-template.html", meta: "Wetland modernism · Vol. 1" },
  { type: "Archive", title: "Mill Ledger, 1911", author: "Crowley Rice Mill", href: "archive-template.html", meta: "RC-ACD-1911-004" },
  { type: "Field Page", title: "About RICE", author: "St. Expedite Press", href: "about.html", meta: "New Orleans, LA" },
  { type: "Call", title: "Submissions", author: "RICE Editors", href: "submissions.html", meta: "Reading period open" }
];

function buildUtilities() {
  const masthead = document.querySelector(".masthead");
  if (!masthead || masthead.querySelector(".masthead-tools")) return;

  const tools = document.createElement("div");
  tools.className = "masthead-tools";
  tools.innerHTML = `
    <a href="index.html" class="issue-switcher" aria-label="Current issue">ISSUE 01 / 2026</a>
    <button class="search-trigger" type="button" aria-haspopup="dialog">SEARCH /</button>
  `;
  masthead.append(tools);

  const dialog = document.createElement("dialog");
  dialog.className = "search-dialog";
  dialog.innerHTML = `
    <form method="dialog" class="search-shell">
      <div class="search-heading">
        <label for="site-search">SEARCH THE FIELD</label>
        <button value="cancel" aria-label="Close search">CLOSE ×</button>
      </div>
      <input id="site-search" type="search" autocomplete="off" placeholder="TITLE / AUTHOR / PARISH">
      <div class="search-results" aria-live="polite"></div>
    </form>
  `;
  document.body.append(dialog);

  const input = dialog.querySelector("input");
  const results = dialog.querySelector(".search-results");
  const render = value => {
    const query = value.trim().toLowerCase();
    const matches = RICE_INDEX.filter(item => !query || Object.values(item).join(" ").toLowerCase().includes(query));
    results.innerHTML = matches.length
      ? matches.map(item => `
          <a href="${item.href}" class="search-result">
            <span>${item.type}</span>
            <strong>${item.title}</strong>
            <small>${item.author} · ${item.meta}</small>
          </a>`).join("")
      : `<p class="empty-state">NO RECORDS FOUND / TRY ANOTHER TERM</p>`;
  };
  render("");
  input.addEventListener("input", event => render(event.target.value));
  tools.querySelector(".search-trigger").addEventListener("click", () => {
    dialog.showModal();
    input.focus();
  });
}

function enableReadingMode() {
  document.querySelectorAll("[data-reading-mode]").forEach(button => {
    button.addEventListener("click", () => {
      const active = document.body.classList.toggle("reading-mode");
      button.textContent = active ? "EXIT READING MODE" : "READING MODE";
      button.setAttribute("aria-pressed", String(active));
    });
  });
}

function enableArchiveFilters() {
  const grid = document.querySelector("[data-archive-grid]");
  if (!grid) return;
  document.querySelectorAll("[data-archive-filter]").forEach(button => {
    button.addEventListener("click", () => {
      const filter = button.dataset.archiveFilter;
      document.querySelectorAll("[data-archive-filter]").forEach(item => item.setAttribute("aria-pressed", "false"));
      button.setAttribute("aria-pressed", "true");
      grid.querySelectorAll("[data-tags]").forEach(item => {
        item.hidden = filter !== "all" && !item.dataset.tags.includes(filter);
      });
    });
  });
}

function enableArchiveZoom() {
  document.querySelectorAll("[data-zoom-image]").forEach(button => {
    button.addEventListener("click", () => {
      const dialog = document.createElement("dialog");
      dialog.className = "image-dialog";
      dialog.innerHTML = `
        <button aria-label="Close image">CLOSE ×</button>
        <img src="${button.dataset.zoomImage}" alt="${button.dataset.zoomAlt || ""}">
      `;
      document.body.append(dialog);
      dialog.querySelector("button").addEventListener("click", () => dialog.close());
      dialog.addEventListener("close", () => dialog.remove());
      dialog.showModal();
    });
  });
}

function enableDemoForms() {
  document.querySelectorAll(".signup-form").forEach(form => {
    form.addEventListener("submit", event => {
      if (form.getAttribute("action")) return;
      event.preventDefault();
      const status = form.querySelector(".form-status");
      if (status) status.textContent = "MAILING SERVICE CONNECTION PENDING / ADDRESS NOT SENT";
    });
  });
}

buildUtilities();
enableReadingMode();
enableArchiveFilters();
enableArchiveZoom();
enableDemoForms();
