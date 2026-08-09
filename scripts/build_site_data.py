import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "aktywnosci.csv"
OUTPUT = ROOT / "site" / "activities.js"
SCENARIOS = ROOT / "scenariusze"


CATEGORY_HINTS = {
    "konstruowanie": "działanie techniczne, szybkie prototypowanie i testowanie rozwiązania",
    "STEM": "eksperymentowanie, mierzenie wyniku i wyciąganie wniosków z testu",
    "pieniądze": "podejmowanie decyzji finansowych przy ograniczonych zasobach",
    "przedsiębiorczość": "myślenie o koszcie, wartości, kliencie i sensowności pomysłu",
    "negocjacje": "słuchanie interesów, argumentowanie i szukanie warunków porozumienia",
    "information gap": "precyzyjną komunikację, bo nikt nie ma kompletu informacji",
    "dedukcja": "łączenie poszlak, eliminowanie hipotez i uzasadnianie werdyktu",
    "escape room": "koncentrację, wspólne rozwiązywanie zagadek i pracę pod presją czasu",
    "planowanie": "priorytetyzację, przewidywanie ryzyka i reagowanie na zmianę",
    "projektowanie": "tworzenie rozwiązania dla konkretnego użytkownika i szybki test",
    "życie zawodowe": "organizację pracy, odpowiedzialność za role i jakość decyzji",
    "informacja": "ocenianie wiarygodności informacji i szukanie dowodów",
    "fake news": "ostrożność wobec manipulacji i sprawdzanie przesłanek",
    "logika": "systematyczne myślenie i pracę na ograniczeniach",
    "gry": "strategię, wynik i uczenie się przez konsekwencje decyzji",
}


def split_values(value):
    return [part.strip() for part in value.replace(",", "|").split("|") if part.strip()]


def practice_sentence(row):
    tokens = split_values(row["kategoria"]) + split_values(row["kompetencje"])
    hits = []
    for token in tokens:
        if token in CATEGORY_HINTS and CATEGORY_HINTS[token] not in hits:
            hits.append(CATEGORY_HINTS[token])
    if not hits:
        hits = ["współpracę, decyzje i sprawdzanie pomysłów w praktyce"]
    if len(hits) == 1:
        return hits[0]
    return ", ".join(hits[:2]) + " oraz " + hits[2] if len(hits) >= 3 else " oraz ".join(hits)


def prep_label(level):
    return {
        "0": "bez przygotowania",
        "1": "minimalne przygotowanie",
        "2": "niewielkie przygotowanie",
    }.get(level, "do sprawdzenia")


def chaos_note(value):
    try:
        level = int(value)
    except ValueError:
        level = 3
    if level <= 2:
        return "Ryzyko chaosu jest niskie. Wystarczy pilnować czasu i jasnego kryterium wyniku."
    if level == 3:
        return "Ryzyko chaosu jest umiarkowane. Warto ustawić stoły zespołów i jedną kolejkę do testu."
    return "Ryzyko chaosu jest wysokie. Przed startem trzeba jasno wyznaczyć strefy pracy, zasady bezpieczeństwa i sposób testowania."


def materials(row):
    raw = row["materialy"].strip()
    if raw.lower() in {"brak", "brak, tylko dostępne przedmioty"}:
        return "Nic specjalnego. Wystarczy tablica lub kartka do zapisania wyniku."
    return raw[0].upper() + raw[1:] + "."


def group_instruction(row):
    size = row["optymalna_wielkosc_zespolu"]
    base = f"Najlepiej pracować w zespołach po {size} osoby."
    g16 = " Przy 16 uczniach ustaw 4 zespoły."
    g30 = " Przy 30 uczniach ustaw 5-6 zespołów i trzymaj wspólne testowanie w jednej kolejce."
    if row["grupa_30"] == "WARUNKOWO":
        g30 = " Przy 30 uczniach działa warunkowo: ogranicz ruch po sali i testuj zespoły po kolei."
    return base + g16 + g30


def steps(row):
    return [
        f"Wyjaśnij misję i kryterium wyniku: {row['odpowiedz_po_co']}",
        f"Podziel klasę na zespoły i rozdaj materiały: {row['materialy']}.",
        f"Daj 2-3 minuty na szybki plan. Potem zespoły pracują według mechanizmu: {row['glowny_mechanizm']}.",
        "W połowie czasu zapowiedz pozostały limit. Nie rozwiązuj zadania za zespoły, tylko przypominaj kryterium wyniku.",
        f"Przeprowadź test, porównanie albo prezentację efektu. Zapisz wynik i poproś o jedno zdanie uzasadnienia.",
    ]


def scenario_paths():
    if not SCENARIOS.exists():
        return {}
    return {
        path.name[:4]: str(path.relative_to(ROOT))
        for path in sorted(SCENARIOS.glob("A*.md"))
    }


def enrich(row, scenarios):
    practice = practice_sentence(row)
    intro = (
        f"Nie robimy tego jako szkolnego ćwiczenia dla samego ćwiczenia. "
        f"Waszym zadaniem jest konkretny wynik: {row['odpowiedz_po_co']} "
        "Liczy się decyzja, sposób pracy i to, czy efekt przejdzie sprawdzenie."
    )
    teacher_description = (
        f"{row['krotki_opis']} Nauczyciel prowadzi aktywność jako krótką misję z jasnym wynikiem, "
        "a nie jako rozmowę o współpracy. Najpierw uczniowie dostają ograniczenie, potem działają w zespołach, "
        "na końcu porównują rezultat z innymi zespołami albo z ustalonym kryterium."
    )
    return {
        **row,
        "poziom_przygotowania_label": prep_label(row["poziom_przygotowania"]),
        "opis_aktywnosci": teacher_description,
        "podprowadzajka": intro,
        "cel_dla_uczniow": row["odpowiedz_po_co"],
        "co_cwiczy": f"Aktywność ćwiczy {practice}.",
        "co_zabrac": materials(row),
        "jak_dzielic": group_instruction(row),
        "proponowany_przebieg": steps(row),
        "bezpieczenstwo_i_uwagi": f"{chaos_note(row['ryzyko_chaosu'])} Uwaga adaptacyjna: {row['adaptacja_bs_technikum']}. Ryzyka: {row['ryzyka']}.",
        "scenario_path": scenarios.get(row["id"], ""),
    }


def main():
    with INPUT.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter=";"))
    scenarios = scenario_paths()
    enriched = [enrich(row, scenarios) for row in rows]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = "window.ACTIVITIES = " + json.dumps(enriched, ensure_ascii=False, indent=2) + ";\n"
    OUTPUT.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
