const activities = window.ACTIVITIES || [];
const params = new URLSearchParams(window.location.search);
const activityId = params.get("id") || "";
const activity = activities.find((item) => item.id === activityId);
const page = document.querySelector("#taskPage");

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
    .replace(/^### (.*)$/gm, "<h3>$1</h3>")
    .replace(/^## (.*)$/gm, "<h2>$1</h2>")
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");

  return html
    .split(/\n{2,}/)
    .map((block) => {
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
    })
    .join("");
}

function detailSection(title, content, wide = false) {
  if (!content) return "";
  return `
    <section class="detail-box ${wide ? "wide" : ""}">
      <h2>${escapeHtml(title)}</h2>
      ${markdownLite(content)}
    </section>
  `;
}

function renderNotFound() {
  page.innerHTML = `
    <section class="task-hero">
      <p class="eyebrow">Nie znaleziono zadania</p>
      <h1>Brak takiej aktywności</h1>
      <p>Wróć do katalogu i wybierz zadanie z listy.</p>
      <a class="scenario-link" href="index.html#katalog">Wróć do katalogu</a>
    </section>
  `;
}

function renderTask(item) {
  document.title = `${item.id} | ${item.robocza_nazwa}`;
  const fullScenario = item.scenario_path && item.scenario_worksheet;

  page.innerHTML = `
    <section class="task-hero">
      <p class="eyebrow">${escapeHtml(item.id)} | ${escapeHtml(item.kategoria)}</p>
      <h1>${escapeHtml(item.robocza_nazwa)}</h1>
      <p>${escapeHtml(item.krotki_opis)}</p>
      <div class="task-actions">
        <a class="button primary" href="index.html#katalog">Wróć do katalogu</a>
      </div>
      <div class="task-meta">
        <span>Czas: ${escapeHtml(item.czas)}</span>
        <span>Grupa: ${escapeHtml(item.optymalna_wielkosc_zespolu)} os.</span>
        <span>Przygotowanie: ${escapeHtml(item.poziom_przygotowania_label)}</span>
        <span>Co zabrać: ${escapeHtml(item.co_zabrac)}</span>
      </div>
    </section>

    <section class="task-content">
      ${fullScenario ? `
        ${detailSection("Instrukcja dla uczniów", item.scenario_instruction, true)}
        ${detailSection("Materiały", item.scenario_materials)}
        ${detailSection("Zwrot akcji", item.scenario_twist)}
        ${detailSection("Karta pracy / zasady gry", item.scenario_worksheet, true)}
        ${detailSection("Przebieg 45 minut", item.scenario_flow, true)}
        ${detailSection("Punktacja / kryterium sukcesu", item.scenario_scoring)}
        ${detailSection("Klucz lub przykład dobrego rozwiązania", item.scenario_key)}
        ${detailSection("Uwagi dla nauczyciela", item.scenario_notes, true)}
      ` : `
        ${detailSection("Start dla uczniów", item.podprowadzajka, true)}
        ${detailSection("Cel", item.cel_dla_uczniow)}
        ${detailSection("Przebieg", item.proponowany_przebieg.map((step, index) => `${index + 1}. ${step}`).join("\n"), true)}
        ${detailSection("Zwrot akcji", item.przykladowy_zwrot_akcji)}
        ${detailSection("Uwagi dla BS I / technikum", item.bezpieczenstwo_i_uwagi)}
      `}
    </section>
  `;
}

if (!activity) {
  renderNotFound();
} else {
  renderTask(activity);
}
