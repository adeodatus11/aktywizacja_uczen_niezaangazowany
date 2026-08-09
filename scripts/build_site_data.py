import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "aktywnosci.csv"
OUTPUT = ROOT / "site" / "activities.js"


CATEGORY_HINTS = {
    "konstruowanie": "dzialanie techniczne, szybkie prototypowanie i testowanie rozwiazania",
    "STEM": "eksperymentowanie, mierzenie wyniku i wyciaganie wnioskow z testu",
    "pieniadze": "podejmowanie decyzji finansowych przy ograniczonych zasobach",
    "przedsiebiorczosc": "myslenie o koszcie, wartosci, kliencie i sensownosci pomyslu",
    "negocjacje": "sluchanie interesow, argumentowanie i szukanie warunkow porozumienia",
    "information gap": "precyzyjna komunikacje, bo nikt nie ma kompletu informacji",
    "dedukcja": "laczenie poszlak, eliminowanie hipotez i uzasadnianie werdyktu",
    "escape room": "koncentracje, wspolne rozwiazywanie zagadek i prace pod presja czasu",
    "planowanie": "priorytetyzacje, przewidywanie ryzyka i reagowanie na zmiane",
    "projektowanie": "tworzenie rozwiazania dla konkretnego uzytkownika i szybki test",
    "zycie zawodowe": "organizacje pracy, odpowiedzialnosc za role i jakosc decyzji",
    "informacja": "ocenianie wiarygodnosci informacji i szukanie dowodow",
    "fake news": "ostroznosc wobec manipulacji i sprawdzanie przeslanek",
    "logika": "systematyczne myslenie i prace na ograniczeniach",
    "gry": "strategie, wynik i uczenie sie przez konsekwencje decyzji",
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
        hits = ["wspolprace, decyzje i sprawdzanie pomyslow w praktyce"]
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
        return "Ryzyko chaosu jest niskie. Wystarczy pilnowac czasu i jasnego kryterium wyniku."
    if level == 3:
        return "Ryzyko chaosu jest umiarkowane. Warto ustawic stoly zespolow i jedna kolejke do testu."
    return "Ryzyko chaosu jest wysokie. Przed startem trzeba jasno wyznaczyc strefy pracy, zasady bezpieczenstwa i sposob testowania."


def materials(row):
    raw = row["materialy"].strip()
    if raw.lower() in {"brak", "brak, tylko dostepne przedmioty"}:
        return "Nic specjalnego. Wystarczy tablica lub kartka do zapisania wyniku."
    return raw[0].upper() + raw[1:] + "."


def group_instruction(row):
    size = row["optymalna_wielkosc_zespolu"]
    base = f"Najlepiej pracowac w zespolach po {size} osoby."
    g16 = " Przy 16 uczniach ustaw 4 zespoly."
    g30 = " Przy 30 uczniach ustaw 5-6 zespolow i trzymaj wspolne testowanie w jednej kolejce."
    if row["grupa_30"] == "WARUNKOWO":
        g30 = " Przy 30 uczniach dziala warunkowo: ogranicz ruch po sali i testuj zespoly po kolei."
    return base + g16 + g30


def steps(row):
    return [
        f"Wyjasnij misje i kryterium wyniku: {row['odpowiedz_po_co']}",
        f"Podziel klase na zespoly i rozdaj materialy: {row['materialy']}.",
        f"Daj 2-3 minuty na szybki plan. Potem zespoly pracuja wedlug mechanizmu: {row['glowny_mechanizm']}.",
        "W polowie czasu zapowiedz pozostaly limit. Nie rozwiazuj zadania za zespoly, tylko przypominaj kryterium wyniku.",
        f"Przeprowadz test, porownanie albo prezentacje efektu. Zapisz wynik i popros o jedno zdanie uzasadnienia.",
    ]


def enrich(row):
    practice = practice_sentence(row)
    intro = (
        f"Nie robimy tego jako szkolnego cwiczenia dla samego cwiczenia. "
        f"Waszym zadaniem jest konkretny wynik: {row['odpowiedz_po_co']} "
        "Liczy sie decyzja, sposob pracy i to, czy efekt przejdzie sprawdzenie."
    )
    teacher_description = (
        f"{row['krotki_opis']} Nauczyciel prowadzi aktywnosc jako krotka misje z jasnym wynikiem, "
        "a nie jako rozmowe o wspolpracy. Najpierw uczniowie dostaja ograniczenie, potem dzialaja w zespolach, "
        "na koncu porownuja rezultat z innymi zespolami albo z ustalonym kryterium."
    )
    return {
        **row,
        "poziom_przygotowania_label": prep_label(row["poziom_przygotowania"]),
        "opis_aktywnosci": teacher_description,
        "podprowadzajka": intro,
        "cel_dla_uczniow": row["odpowiedz_po_co"],
        "co_cwiczy": f"Aktywnosc cwiczy {practice}.",
        "co_zabrac": materials(row),
        "jak_dzielic": group_instruction(row),
        "proponowany_przebieg": steps(row),
        "bezpieczenstwo_i_uwagi": f"{chaos_note(row['ryzyko_chaosu'])} Uwaga adaptacyjna: {row['adaptacja_bs_technikum']}. Ryzyka: {row['ryzyka']}.",
    }


def main():
    with INPUT.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter=";"))
    enriched = [enrich(row) for row in rows]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = "window.ACTIVITIES = " + json.dumps(enriched, ensure_ascii=False, indent=2) + ";\n"
    OUTPUT.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()

