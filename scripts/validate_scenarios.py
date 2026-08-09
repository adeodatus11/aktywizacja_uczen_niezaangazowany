from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "scenariusze"

REQUIRED_SCENARIOS = {
    "A014", "A016", "A017", "A018", "A019", "A020", "A021", "A022", "A023", "A024",
    "A025", "A026", "A027", "A028", "A029", "A030", "A031", "A032", "A033", "A034",
    "A035", "A036", "A037", "A038", "A039", "A040", "A041", "A042", "A043", "A044",
    "A045", "A046", "A047", "A048", "A049", "A050", "A051", "A052", "A053", "A054",
    "A055", "A056", "A057", "A058", "A059", "A060", "A061", "A062", "A063", "A064",
    "A065", "A066", "A067", "A068", "A071", "A072", "A073", "A075", "A076", "A077",
    "A078", "A079", "A081", "A082", "A084", "A085", "A086", "A087", "A088", "A089",
    "A091", "A092", "A093", "A094", "A095", "A096", "A097", "A098", "A099", "A100",
}

REQUIRED_SECTIONS = [
    "## Status",
    "## Cel dla uczniów",
    "## Materiały",
    "## Instrukcja dla uczniów (do odczytania)",
    "## Karta pracy / materiały uczniowskie",
    "## Przebieg 45 minut",
    "## Zwrot akcji",
    "## Punktacja / kryterium sukcesu",
    "## Klucz lub przykład dobrego rozwiązania",
    "## Uwagi dla nauczyciela",
]


def main():
    files = sorted(SCENARIOS.glob("A*.md")) if SCENARIOS.exists() else []
    by_id = {}
    duplicates = {}
    for path in files:
        activity_id = path.name[:4]
        if activity_id in by_id:
            duplicates.setdefault(activity_id, [by_id[activity_id]]).append(path)
        else:
            by_id[activity_id] = path

    missing_ids = sorted(REQUIRED_SCENARIOS - set(by_id))
    extra_ids = sorted(set(by_id) - REQUIRED_SCENARIOS)
    section_errors = []

    for activity_id in sorted(REQUIRED_SCENARIOS & set(by_id)):
        text = by_id[activity_id].read_text(encoding="utf-8")
        missing_sections = [section for section in REQUIRED_SECTIONS if section not in text]
        if missing_sections:
            section_errors.append((activity_id, missing_sections))

    if missing_ids:
        print("Missing scenario files:", ", ".join(missing_ids))
    if extra_ids:
        print("Extra scenario files:", ", ".join(extra_ids))
    for activity_id, paths in sorted(duplicates.items()):
        print(f"{activity_id} duplicate files: {', '.join(path.name for path in paths)}")
    for activity_id, sections in section_errors:
        print(f"{activity_id} missing sections: {', '.join(sections)}")

    if missing_ids or extra_ids or duplicates or section_errors:
        raise SystemExit(1)

    print(f"OK: {len(REQUIRED_SCENARIOS)} scenario files with required sections.")


if __name__ == "__main__":
    main()
