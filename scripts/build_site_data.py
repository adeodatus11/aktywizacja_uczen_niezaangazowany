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


def readable_mechanism(value):
    return value.replace("->", "→")


def student_start(row):
    categories = set(split_values(row["kategoria"]))
    materials_text = row["materialy"].strip()
    if materials_text.lower() in {"brak", "brak, tylko dostępne przedmioty"}:
        materials_text = "kartka lub tablica do zapisania wyniku"

    if categories & {"konstruowanie", "STEM", "konstrukcje", "optymalizacja"}:
        opener = "Na stole macie prosty zestaw materiałów i test, który od razu pokaże, czy pomysł działa."
    elif categories & {"pieniądze", "przedsiębiorczość"}:
        opener = "Dostajecie sytuację z budżetem, kosztami i wyborem, którego nie da się rozwiązać samym przeczuciem."
    elif categories & {"dedukcja", "escape room", "logika"}:
        opener = "Dostajecie tropy, ograniczenia i limit czasu. Trzeba dojść do rozwiązania bez zgadywania."
    elif categories & {"informacja", "fake news", "argumentacja"}:
        opener = "Dostajecie materiały, które trzeba sprawdzić przed podjęciem decyzji albo podaniem ich dalej."
    elif categories & {"negocjacje"}:
        opener = "Każdy zespół ma interes do obrony, ale zasoby albo warunki nie wystarczą wszystkim po równo."
    elif categories & {"planowanie", "życie zawodowe"}:
        opener = "Dostajecie zadanie organizacyjne, w którym kolejność decyzji ma znaczenie."
    elif categories & {"projektowanie", "problem solving"}:
        opener = "Projektujecie rozwiązanie dla konkretnego użytkownika, a potem sprawdzacie, czy ono naprawdę działa."
    elif categories & {"gry", "rywalizacja"}:
        opener = "To krótka gra decyzyjna: wynik zależy od wyborów zespołu i reakcji na ruchy innych."
    else:
        opener = "Dostajecie zadanie z jasnym wynikiem i krótkim limitem czasu."

    return (
        f"{opener} Wasz cel: {row['odpowiedz_po_co']} "
        f"Do pracy potrzebne będą: {materials_text}. "
        "Na końcu zespół pokazuje wynik i jedno konkretne uzasadnienie swojej decyzji."
    )


def steps(row):
    mechanism = readable_mechanism(row["glowny_mechanizm"])
    return [
        f"0-5 min: przedstaw wyzwanie i powiedz, jak będzie sprawdzany wynik: {row['odpowiedz_po_co']}",
        f"5-8 min: podziel klasę na zespoły, rozdaj materiały i poproś o szybki plan pierwszego ruchu.",
        f"8-25 min: zespoły pracują według rytmu: {mechanism}. Nauczyciel pilnuje czasu i limitów.",
        f"25-32 min: wprowadź zmianę warunków: {row['przykladowy_zwrot_akcji']}. Zespoły poprawiają decyzję albo projekt.",
        "32-42 min: zespoły testują, porównują albo prezentują wynik. Każdy wynik musi mieć krótkie uzasadnienie.",
        "42-45 min: zapisz 1-2 najlepsze strategie na tablicy i nazwij, co zadziałało w praktyce.",
    ]


def scenario_paths():
    if not SCENARIOS.exists():
        return {}
    return {
        path.name[:4]: str(path.relative_to(ROOT))
        for path in sorted(SCENARIOS.glob("A*.md"))
    }


def scenario_sections(path):
    if not path:
        return {}
    scenario_file = ROOT / path
    if not scenario_file.exists():
        return {}

    sections = {}
    current = None
    buffer = []
    for line in scenario_file.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            if current:
                sections[current] = "\n".join(buffer).strip()
            current = line[3:].strip()
            buffer = []
            continue
        if current:
            buffer.append(line)
    if current:
        sections[current] = "\n".join(buffer).strip()
    return sections


def enrich(row, scenarios):
    practice = practice_sentence(row)
    scenario_path = scenarios.get(row["id"], "")
    scenario = scenario_sections(scenario_path)
    teacher_description = (
        f"{row['krotki_opis']} Prowadzenie opiera się na krótkim briefie, pracy zespołowej, "
        "zwrocie akcji i sprawdzeniu wyniku pod koniec lekcji."
    )
    return {
        **row,
        "poziom_przygotowania_label": prep_label(row["poziom_przygotowania"]),
        "opis_aktywnosci": teacher_description,
        "podprowadzajka": student_start(row),
        "cel_dla_uczniow": row["odpowiedz_po_co"],
        "co_cwiczy": f"Aktywność ćwiczy {practice}.",
        "co_zabrac": materials(row),
        "jak_dzielic": group_instruction(row),
        "proponowany_przebieg": steps(row),
        "bezpieczenstwo_i_uwagi": f"{chaos_note(row['ryzyko_chaosu'])} Uwaga adaptacyjna: {row['adaptacja_bs_technikum']}. Ryzyka: {row['ryzyka']}.",
        "scenario_path": scenario_path,
        "scenario_instruction": scenario.get("Instrukcja dla uczniów (do odczytania)", ""),
        "scenario_materials": scenario.get("Materiały", ""),
        "scenario_worksheet": scenario.get("Karta pracy / materiały uczniowskie", ""),
        "scenario_flow": scenario.get("Przebieg 45 minut", ""),
        "scenario_twist": scenario.get("Zwrot akcji", ""),
        "scenario_scoring": scenario.get("Punktacja / kryterium sukcesu", ""),
        "scenario_key": scenario.get("Klucz lub przykład dobrego rozwiązania", ""),
        "scenario_notes": scenario.get("Uwagi dla nauczyciela", ""),
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
