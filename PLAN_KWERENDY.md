# Plan kwerendy: Misje na 45 minut

## Cel projektu

Zbudować bazę minimum 100 wartościowych aktywności/mechanizmów na jednorazowe lekcje zastępcze w szkole ponadpodstawowej, szczególnie dla uczniów branżowej szkoły I stopnia i technikum w wieku 15-19 lat, często z niską motywacją szkolną.

Najważniejszy filtr: aktywność ma być konkretną misją lub wyzwaniem, które kończy się widocznym efektem, decyzją, wynikiem, rozwiązaniem, konstrukcją, prototypem, umową, rankingiem, kodem albo testem. Nie zbieramy typowych ćwiczeń integracyjnych ani aktywności opartych głównie na rozmowie.

## Definicja dobrej aktywności

Dobra aktywność powinna przejść przynajmniej 4 z 5 warunków:

1. Cel jest natychmiast zrozumiały.
2. Powstaje konkretny rezultat.
3. Kilku uczniów rzeczywiście musi współpracować.
4. Da się ją przeprowadzić w 45 minut.
5. Istnieje element ciekawości, ograniczenia, rywalizacji, testu albo niespodzianki.

Aktywności spełniające wszystkie 5 warunków oznaczamy jako `STRONG CANDIDATE`.

## Główny model aktywności

Preferowany schemat:

```text
WYZWANIE -> DZIAŁANIE -> KONKRETNY EFEKT -> TEST / PORÓWNANIE -> WYNIK
```

Najbardziej pożądane typy:

- konstrukcje i engineering challenges,
- paper challenges,
- team problem-solving challenges,
- escape room mechanics,
- mystery / detective games,
- information gap activities,
- survival simulations,
- resource allocation games,
- negotiation simulations,
- trading games,
- business simulations,
- design / prototyping challenges,
- optimization problems,
- logistics challenges,
- communication construction games,
- real-world simulations.

## Etapy pracy

### Etap 1. Przygotowanie struktury bazy

Utworzyć pliki robocze:

- `data/aktywnosci.csv` albo `data/aktywnosci.xlsx` - główna baza rekordów,
- `data/zrodla.csv` - lista źródeł i typów inspiracji,
- `research/notatki_zrodlowe.md` - krótkie notatki z kwerendy,
- `rankingi/` - pliki z rankingami końcowymi.

Minimalny zestaw pól w bazie:

| Pole | Opis |
|---|---|
| `id` | Unikalny identyfikator, np. A001 |
| `robocza_nazwa` | Krótka nazwa aktywności |
| `krotki_opis` | 2-4 zdania o przebiegu |
| `glowny_mechanizm` | Schemat aktywności, np. ograniczone zasoby -> ranking -> negocjacje |
| `kategoria` | Jedna lub kilka kategorii |
| `kompetencje` | Współpraca, komunikacja, planowanie, logiczne myślenie itd. |
| `liczba_osob` | Sugerowana liczba uczestników |
| `optymalna_wielkosc_zespolu` | Najlepiej 3-6 osób |
| `czas` | Docelowo do 45 minut |
| `materialy` | Tablica, kartki, długopisy, wydruk itd. |
| `poziom_przygotowania` | 0-2 |
| `potencjal_zainteresowania` | 1-5, bez zawyżania |
| `konkretnosc_efektu` | 1-5 |
| `rzeczywista_wspolpraca` | 1-5 |
| `grupa_16` | TAK / WARUNKOWO / NIE |
| `grupa_30` | TAK / WARUNKOWO / NIE |
| `ryzyko_chaosu` | 1-5 |
| `zwrot_akcji_mozliwy` | TAK / NIE |
| `przykladowy_zwrot_akcji` | Np. utrata zasobu, zmiana budżetu, nowa informacja |
| `odpowiedz_po_co` | 20-sekundowa odpowiedź dla sceptycznego ucznia |
| `source_type` | Edukacja, biznes, scouting, escape room, assessment center itd. |
| `zrodlo_inspiracji` | Nazwa źródła |
| `url` | Link do źródła |
| `adaptacja_bs_technikum` | Jak dostosować do BS I / technikum |
| `ryzyka` | Konflikt, zawstydzenie, prywatność, wykluczenie |
| `status` | Kandydat / po selekcji / odrzucone / strong candidate |

### Etap 2. Kwerenda źródeł

Szukać po polsku i angielsku. Nie ograniczać się do stron szkolnych; brać mechanizmy z edukacji, biznesu, assessment center, scouting, gier szkoleniowych i escape roomów.

Priorytetowe źródła i obszary:

- Harvard Project Zero / Thinking Routines,
- Stanford d.school,
- IDEO,
- Edutopia,
- Facing History,
- TeachThought,
- CASEL,
- cooperative learning,
- problem-based learning,
- experiential learning,
- design thinking,
- team-building i szkolenia biznesowe,
- assessment center,
- scouting / harcerstwo,
- escape rooms,
- zagadki logiczne,
- gry negocjacyjne i decyzyjne,
- financial literacy games,
- vocational education activities.

Przy każdym źródle zapisać:

- link,
- typ źródła,
- jakie mechanizmy są warte adaptacji,
- czego nie kopiować wprost,
- czy źródło daje legalną inspirację do opracowania własnej wersji.

### Etap 3. Zbieranie kandydatów

Najpierw zebrać szerzej niż docelowe 100 rekordów, np. 140-180 kandydatów. Każdy kandydat ma być zapisany jako mechanizm, nie tylko temat.

Przykład łączenia wariantów:

```text
Bezludna wyspa / katastrofa samolotu / misja na Marsie
= ograniczone zasoby -> indywidualny ranking -> negocjacje zespołu -> wspólna decyzja -> uzasadnienie -> zwrot akcji
```

Takie warianty łączyć w jeden rekord mechanizmu, a nie mnożyć jako osobne aktywności.

### Etap 4. Filtr odrzucający

Odrzucić aktywności, które:

- są infantylne albo wyglądają jak zabawy dla dzieci,
- opierają się głównie na "powiedz coś o sobie", imionach lub autoprezentacji,
- wymagają specjalistycznej wiedzy przedmiotowej,
- wymagają dużego przygotowania lub sprzętu,
- mają instrukcję trudną do wyjaśnienia w 2-3 minuty,
- są ryzykowne pod względem zawstydzenia, prywatności lub wykluczenia,
- przy 30 uczniach łatwo wymykają się spod kontroli jednego nauczyciela,
- mogą zostać wykonane przez jedną dominującą osobę, gdy reszta grupy patrzy.

### Etap 5. Scoring

Dla każdej aktywności policzyć roboczy wynik priorytetu:

```text
score =
  2 x konkretnosc_efektu
+ 2 x potencjal_zainteresowania
+ 2 x rzeczywista_wspolpraca
+ 1 x zwrot_akcji_mozliwy
+ 1 x dopasowanie_do_45_min
+ 1 x dziala_w_grupie_30
- 1 x poziom_przygotowania
- 1 x ryzyko_chaosu
```

Wynik nie ma zastąpić oceny eksperckiej, tylko pomóc w sortowaniu kandydatów.

### Etap 6. Kategorie robocze

Startowe kategorie:

- logika i dedukcja,
- współpraca,
- komunikacja,
- negocjacje,
- kreatywność,
- projektowanie,
- podejmowanie decyzji,
- życie codzienne,
- pieniądze i przedsiębiorczość,
- informacja i fake news,
- planowanie,
- problemy społeczne,
- konstruowanie,
- zagadki,
- gry i rywalizacja.

Dodatkowe kategorie do rozważenia podczas kwerendy:

- misje detektywistyczne,
- optymalizacja,
- logistyka,
- handel i wymiana,
- awarie i zarządzanie kryzysem,
- komunikacja z ograniczeniami,
- prototypowanie,
- test fizyczny.

### Etap 7. Zwroty akcji

Przy każdym kandydacie sprawdzić, czy można dodać jeden z mechanizmów:

- zmiana budżetu,
- ograniczenie czasu,
- utrata zasobu,
- nowa informacja,
- zmiana celu,
- konflikt interesów,
- dodatkowy klient/interesariusz,
- nieoczekiwane wydarzenie,
- awaria,
- zmiana kryteriów wygranej,
- zakaz użycia jednego rozwiązania,
- konieczność wymiany zasobów z innym zespołem.

Zwrot akcji ma wzmacniać zadanie, a nie robić chaos.

### Etap 8. Kontrola skalowalności

Każda aktywność musi zostać oceniona dla:

- małej grupy: ok. 16 uczniów, najlepiej 4 zespoły po 4 osoby,
- dużej grupy: ok. 30 uczniów, najlepiej 5-6 zespołów po 5-6 osób,
- pracy równoległej kilku zespołów,
- kontroli przez jednego nauczyciela,
- ryzyka chaosu przy 30 osobach.

Priorytet mają aktywności, które działają równolegle w zespołach 4-6 osób i mają prosty, mierzalny wynik.

### Etap 9. Weryfikacja i deduplikacja

Po zebraniu kandydatów:

1. Usunąć duplikaty.
2. Połączyć aktywności o tym samym mechanizmie.
3. Odrzucić rekordy słabiej dopasowane do BS I / technikum.
4. Oznaczyć `STRONG CANDIDATE`.
5. Oznaczyć ryzyka.
6. Zostawić minimum 100 sensownych rekordów.

### Etap 10. Rankingi końcowe

Przygotować:

- TOP 20 najbardziej obiecujących aktywności dla BS I / technikum,
- TOP 10 bez żadnego przygotowania,
- TOP 10 najbardziej angażujących,
- TOP 10 rozwijających współpracę,
- TOP 10 rozwijających myślenie,
- TOP 10 wykorzystujących zwroty akcji.

Każdy ranking powinien zawierać krótkie uzasadnienie, a nie tylko listę nazw.

## Kryteria gotowości pierwszej wersji

Pierwsza wersja kwerendy jest gotowa, gdy:

- baza ma minimum 100 rekordów po deduplikacji,
- każdy rekord ma wypełnione pola obowiązkowe,
- każda aktywność mieści się w 45 minutach,
- każda aktywność ma jasny konkretny efekt,
- aktywności z dużym ryzykiem chaosu albo zawstydzenia są oznaczone,
- TOP 20 zawiera głównie rekordy `STRONG CANDIDATE`,
- można od razu wybrać aktywność na zastępstwo bez czytania całej bazy.

## Najbliższe zadania

1. Utworzyć strukturę katalogów i puste szablony bazy.
2. Przygotować listę zapytań PL/EN do kwerendy.
3. Zebrać pierwszą pulę 30-40 kandydatów z różnorodnych źródeł.
4. Przetestować format rekordu na kilku przykładach.
5. Dopiero potem skalować bazę do 100+ rekordów.
