const activities = window.ACTIVITIES || [];

const grid = document.querySelector("#activityGrid");
const resultCount = document.querySelector("#resultCount");
const totalCount = document.querySelector("#totalCount");
const strongCount = document.querySelector("#strongCount");
const searchInput = document.querySelector("#searchInput");
const categoryFilter = document.querySelector("#categoryFilter");
const prepFilter = document.querySelector("#prepFilter");
const hookFilter = document.querySelector("#hookFilter");
const statusFilter = document.querySelector("#statusFilter");
const dialog = document.querySelector("#activityDialog");
const dialogContent = document.querySelector("#dialogContent");
const closeDialog = document.querySelector("#closeDialog");

const rankTop = ["A070", "A074", "A001", "A002", "A005", "A011", "A072", "A090", "A037", "A041"];
const rankZero = ["A001", "A014", "A051", "A052", "A053", "A054", "A055", "A060", "A066", "A098"];
const rankCollab = ["A070", "A072", "A074", "A075", "A041", "A037", "A023", "A061", "A083", "A084"];

const byId = new Map(activities.map((activity) => [activity.id, activity]));
let quickMode = "";

function escapeHtml(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function markdownLite(value) {
  let html = escapeHtml(value).trim();
  if (!html) return "";

  html = html
    .replace(/^### (.*)$/gm, "<h5>$1</h5>")
    .replace(/^## (.*)$/gm, "<h4>$1</h4>")
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");

  const blocks = html.split(/\n{2,}/).map((block) => {
    if (block.startsWith("<h")) return block;
    if (block.includes("\n|") || block.startsWith("|")) return `<pre>${block}</pre>`;
    if (block.startsWith("- ")) {
      const items = block
        .split("\n")
        .map((line) => line.replace(/^- /, "").trim())
        .filter(Boolean)
        .map((line) => `<li>${line}</li>`)
        .join("");
      return `<ul>${items}</ul>`;
    }
    if (/^\d+\. /.test(block)) {
      const items = block
        .split("\n")
        .map((line) => line.replace(/^\d+\. /, "").trim())
        .filter(Boolean)
        .map((line) => `<li>${line}</li>`)
        .join("");
      return `<ol>${items}</ol>`;
    }
    return `<p>${block.replace(/\n/g, "<br>")}</p>`;
  });

  return blocks.join("");
}

function activityUrl(activity) {
  return `zadanie.html?id=${encodeURIComponent(activity.id)}`;
}

function materialList(items, limit) {
  const list = Array.isArray(items) ? items : [];
  const visible = Number.isFinite(limit) ? list.slice(0, limit) : list;
  const extra = Number.isFinite(limit) && list.length > limit ? `<li>+ ${list.length - limit} więcej w szczegółach zadania</li>` : "";
  return `<ul class="materials-list">${visible.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}${extra}</ul>`;
}

function populateStats() {
  totalCount.textContent = activities.length;
  strongCount.textContent = activities.filter((item) => item.status === "STRONG CANDIDATE").length;
}

function populateCategories() {
  const categories = new Set();
  activities.forEach((activity) => {
    activity.kategoria.split("|").forEach((category) => categories.add(category.trim()));
  });
  [...categories].sort((a, b) => a.localeCompare(b, "pl")).forEach((category) => {
    const option = document.createElement("option");
    option.value = category;
    option.textContent = category;
    categoryFilter.append(option);
  });
}

function cardTemplate(activity) {
  const status = activity.status === "STRONG CANDIDATE" ? "Strong" : "Kandydat";
  const scenarioBadge = activity.scenario_path ? '<span>Scenariusz: gotowy</span>' : "";
  const actionLabel = activity.scenario_path ? "Czytaj szczegóły" : "Zobacz opis";
  return `
    <article class="card">
      <div class="card-header">
        <span class="id">${escapeHtml(activity.id)}</span>
        <span class="status">${escapeHtml(status)}</span>
      </div>
      <h3>${escapeHtml(activity.robocza_nazwa)}</h3>
      <p>${escapeHtml(activity.krotki_opis)}</p>
      <div class="card-materials">
        <strong>Lista rzeczy:</strong>
        ${materialList(activity.lista_potrzebnych_rzeczy, 3)}
      </div>
      <div class="meta-grid">
        <span>Czas: ${escapeHtml(activity.czas)}</span>
        <span>Grupa: ${escapeHtml(activity.optymalna_wielkosc_zespolu)} os.</span>
        <span>Prep: ${escapeHtml(activity.poziom_przygotowania_label)}</span>
        <span>Hook: ${escapeHtml(activity.potencjal_zainteresowania)}/5</span>
        ${scenarioBadge}
      </div>
      <a class="card-action" href="${escapeHtml(activityUrl(activity))}">${escapeHtml(actionLabel)}</a>
    </article>
  `;
}

function filterActivities() {
  const term = searchInput.value.trim().toLowerCase();
  const category = categoryFilter.value;
  const prep = prepFilter.value;
  const hook = Number(hookFilter.value || 0);
  const status = statusFilter.value;

  return activities.filter((activity) => {
    const haystack = [
      activity.id,
      activity.robocza_nazwa,
      activity.krotki_opis,
      activity.glowny_mechanizm,
      activity.kategoria,
      activity.kompetencje,
      activity.przykladowy_zwrot_akcji,
      activity.opis_aktywnosci,
      activity.podprowadzajka,
      ...(activity.lista_potrzebnych_rzeczy || []),
    ].join(" ").toLowerCase();

    return (
      (!term || haystack.includes(term)) &&
      (!category || activity.kategoria.split("|").includes(category)) &&
      (!prep || activity.poziom_przygotowania === prep) &&
      Number(activity.potencjal_zainteresowania) >= hook &&
      (!status || activity.status === status) &&
      (quickMode !== "twist" || activity.zwrot_akcji_mozliwy === "TAK")
    );
  });
}

function render() {
  const filtered = filterActivities();
  resultCount.textContent = `${filtered.length} z ${activities.length} aktywności`;
  grid.innerHTML = filtered.map(cardTemplate).join("");
}

function detailTemplate(activity) {
  const steps = activity.proponowany_przebieg
    .map((step) => `<li>${escapeHtml(step)}</li>`)
    .join("");
  const scenarioLink = activity.scenario_path
    ? `<a class="scenario-link" href="${escapeHtml(activityUrl(activity))}">Czytaj szczegóły zadania</a>`
    : "";

  if (activity.scenario_path && activity.scenario_worksheet) {
    return `
      <p class="id">${escapeHtml(activity.id)} | ${escapeHtml(activity.kategoria)}</p>
      <h2 class="dialog-title">${escapeHtml(activity.robocza_nazwa)}</h2>
      <p class="dialog-lead">${escapeHtml(activity.krotki_opis)}</p>
      ${scenarioLink}
      <div class="detail-grid">
        <section class="detail-box wide">
          <h4>Instrukcja dla uczniów</h4>
          ${markdownLite(activity.scenario_instruction)}
        </section>
        <section class="detail-box">
          <h4>Lista rzeczy do przygotowania</h4>
          ${materialList(activity.lista_potrzebnych_rzeczy)}
        </section>
        <section class="detail-box">
          <h4>Zwrot akcji</h4>
          ${markdownLite(activity.scenario_twist)}
        </section>
        <section class="detail-box wide">
          <h4>Karta pracy / zasady gry</h4>
          ${markdownLite(activity.scenario_worksheet)}
        </section>
        <section class="detail-box wide">
          <h4>Przebieg 45 minut</h4>
          ${markdownLite(activity.scenario_flow)}
        </section>
        <section class="detail-box">
          <h4>Punktacja / kryterium sukcesu</h4>
          ${markdownLite(activity.scenario_scoring)}
        </section>
        <section class="detail-box">
          <h4>Klucz lub przykład dobrego rozwiązania</h4>
          ${markdownLite(activity.scenario_key)}
        </section>
        <section class="detail-box wide">
          <h4>Uwagi dla nauczyciela</h4>
          ${markdownLite(activity.scenario_notes)}
        </section>
      </div>
    `;
  }

  return `
    <p class="id">${escapeHtml(activity.id)} | ${escapeHtml(activity.kategoria)}</p>
    <h2 class="dialog-title">${escapeHtml(activity.robocza_nazwa)}</h2>
    <p class="dialog-lead">${escapeHtml(activity.opis_aktywnosci)}</p>
    ${scenarioLink}
    <div class="detail-grid">
      <section class="detail-box wide">
        <h4>Start dla uczniów</h4>
        <p>${escapeHtml(activity.podprowadzajka)}</p>
      </section>
      <section class="detail-box">
        <h4>Cel</h4>
        <p>${escapeHtml(activity.cel_dla_uczniow)}</p>
      </section>
      <section class="detail-box">
        <h4>Co ćwiczy</h4>
        <p>${escapeHtml(activity.co_cwiczy)}</p>
      </section>
      <section class="detail-box">
        <h4>Lista rzeczy do przygotowania</h4>
        ${materialList(activity.lista_potrzebnych_rzeczy)}
      </section>
      <section class="detail-box">
        <h4>Jak dzielić klasę</h4>
        <p>${escapeHtml(activity.jak_dzielic)}</p>
      </section>
      <section class="detail-box wide">
        <h4>Przebieg</h4>
        <ol>${steps}</ol>
      </section>
      <section class="detail-box">
        <h4>Zwrot akcji</h4>
        <p>${escapeHtml(activity.przykladowy_zwrot_akcji)}</p>
      </section>
      <section class="detail-box">
        <h4>Uwagi dla BS I / technikum</h4>
        <p>${escapeHtml(activity.bezpieczenstwo_i_uwagi)}</p>
      </section>
    </div>
  `;
}

function openActivity(id) {
  const activity = byId.get(id);
  if (!activity) return;
  dialogContent.innerHTML = detailTemplate(activity);
  dialog.showModal();
}

function renderRanking(target, ids) {
  target.innerHTML = ids
    .map((id) => {
      const activity = byId.get(id);
      if (!activity) return "";
      return `<li><a href="${escapeHtml(activityUrl(activity))}">${escapeHtml(id)} ${escapeHtml(activity.robocza_nazwa)}</a></li>`;
    })
    .join("");
}

function applyQuickFilter(mode) {
  quickMode = "";
  if (mode === "reset") {
    searchInput.value = "";
    categoryFilter.value = "";
    prepFilter.value = "";
    hookFilter.value = "0";
    statusFilter.value = "";
  }
  if (mode === "zero") {
    prepFilter.value = "0";
  }
  if (mode === "strong") {
    statusFilter.value = "STRONG CANDIDATE";
  }
  if (mode === "twist") {
    searchInput.value = "";
    quickMode = "twist";
    statusFilter.value = "";
  }
  render();
}

document.querySelector("#filters").addEventListener("input", () => {
  quickMode = "";
  render();
});
document.querySelector(".quick-filters").addEventListener("click", (event) => {
  const button = event.target.closest("button[data-quick]");
  if (button) applyQuickFilter(button.dataset.quick);
});
closeDialog.addEventListener("click", () => dialog.close());
dialog.addEventListener("click", (event) => {
  if (event.target === dialog) dialog.close();
});

populateStats();
populateCategories();
renderRanking(document.querySelector("#rankTop"), rankTop);
renderRanking(document.querySelector("#rankZero"), rankZero);
renderRanking(document.querySelector("#rankCollab"), rankCollab);
render();
