# Plan kwerendy: aktywizacja ucznia niezaangazowanego

## Cel projektu

Zbudowac baze minimum 100 wartosciowych aktywnosci/mechanizmow na jednorazowe lekcje zastepcze w szkole ponadpodstawowej, szczegolnie dla uczniow branzowej szkoly I stopnia i technikum w wieku 15-19 lat, czesto z niska motywacja szkolna.

Najwazniejszy filtr: aktywnosc ma byc konkretna misja lub wyzwaniem, ktore konczy sie widocznym efektem, decyzja, wynikiem, rozwiazaniem, konstrukcja, prototypem, umowa, rankingiem, kodem albo testem. Nie zbieramy typowych cwiczen integracyjnych ani aktywnosci opartych glownie na rozmowie.

## Definicja dobrej aktywnosci

Dobra aktywnosc powinna przejsc przynajmniej 4 z 5 warunkow:

1. Cel jest natychmiast zrozumialy.
2. Powstaje konkretny rezultat.
3. Kilku uczniow rzeczywiscie musi wspolpracowac.
4. Da sie ja przeprowadzic w 45 minut.
5. Istnieje element ciekawosci, ograniczenia, rywalizacji, testu albo niespodzianki.

Aktywnosci spelniajace wszystkie 5 warunkow oznaczamy jako `STRONG CANDIDATE`.

## Glowny model aktywnosci

Preferowany schemat:

```text
WYZWANIE -> DZIALANIE -> KONKRETNY EFEKT -> TEST / POROWNANIE -> WYNIK
```

Najbardziej pozadane typy:

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

Utworzyc pliki robocze:

- `data/aktywnosci.csv` albo `data/aktywnosci.xlsx` - glowna baza rekordow,
- `data/zrodla.csv` - lista zrodel i typow inspiracji,
- `research/notatki_zrodlowe.md` - krotkie notatki z kwerendy,
- `rankingi/` - pliki z rankingami koncowymi.

Minimalny zestaw pol w bazie:

| Pole | Opis |
|---|---|
| `id` | Unikalny identyfikator, np. A001 |
| `robocza_nazwa` | Krotka nazwa aktywnosci |
| `krotki_opis` | 2-4 zdania o przebiegu |
| `glowny_mechanizm` | Schemat aktywnosci, np. ograniczone zasoby -> ranking -> negocjacje |
| `kategoria` | Jedna lub kilka kategorii |
| `kompetencje` | Wspolpraca, komunikacja, planowanie, logiczne myslenie itd. |
| `liczba_osob` | Sugerowana liczba uczestnikow |
| `optymalna_wielkosc_zespolu` | Najlepiej 3-6 osob |
| `czas` | Docelowo do 45 minut |
| `materialy` | Tablica, kartki, dlugopisy, wydruk itd. |
| `poziom_przygotowania` | 0-2 |
| `potencjal_zainteresowania` | 1-5, bez zawyzania |
| `konkretnosc_efektu` | 1-5 |
| `rzeczywista_wspolpraca` | 1-5 |
| `grupa_16` | TAK / WARUNKOWO / NIE |
| `grupa_30` | TAK / WARUNKOWO / NIE |
| `ryzyko_chaosu` | 1-5 |
| `zwrot_akcji_mozliwy` | TAK / NIE |
| `przykladowy_zwrot_akcji` | Np. utrata zasobu, zmiana budzetu, nowa informacja |
| `odpowiedz_po_co` | 20-sekundowa odpowiedz dla sceptycznego ucznia |
| `source_type` | Edukacja, biznes, scouting, escape room, assessment center itd. |
| `zrodlo_inspiracji` | Nazwa zrodla |
| `url` | Link do zrodla |
| `adaptacja_bs_technikum` | Jak dostosowac do BS I / technikum |
| `ryzyka` | Konflikt, zawstydzenie, prywatnosc, wykluczenie |
| `status` | Kandydat / po selekcji / odrzucone / strong candidate |

### Etap 2. Kwerenda zrodel

Szukac po polsku i angielsku. Nie ograniczac sie do stron szkolnych; brac mechanizmy z edukacji, biznesu, assessment center, scouting, gier szkoleniowych i escape roomow.

Priorytetowe zrodla i obszary:

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

Przy kazdym zrodle zapisac:

- link,
- typ zrodla,
- jakie mechanizmy sa warte adaptacji,
- czego nie kopiowac wprost,
- czy zrodlo daje legalna inspiracje do opracowania wlasnej wersji.

### Etap 3. Zbieranie kandydatow

Najpierw zebrac szerzej niz docelowe 100 rekordow, np. 140-180 kandydatow. Kazdy kandydat ma byc zapisany jako mechanizm, nie tylko temat.

Przyklad laczenia wariantow:

```text
Bezludna wyspa / katastrofa samolotu / misja na Marsie
= ograniczone zasoby -> indywidualny ranking -> negocjacje zespolu -> wspolna decyzja -> uzasadnienie -> zwrot akcji
```

Takie warianty laczyc w jeden rekord mechanizmu, a nie mnozyc jako osobne aktywnosci.

### Etap 4. Filtr odrzucajacy

Odrzucic aktywnosci, ktore:

- sa infantylne albo wygladaja jak zabawy dla dzieci,
- opieraja sie glownie na "powiedz cos o sobie", imionach lub autoprezentacji,
- wymagaja specjalistycznej wiedzy przedmiotowej,
- wymagaja duzego przygotowania lub sprzetu,
- maja instrukcje trudna do wyjasnienia w 2-3 minuty,
- sa ryzykowne pod wzgledem zawstydzenia, prywatnosci lub wykluczenia,
- przy 30 uczniach latwo wymykaja sie spod kontroli jednego nauczyciela,
- moga zostac wykonane przez jedna dominujaca osobe, gdy reszta grupy patrzy.

### Etap 5. Scoring

Dla kazdej aktywnosci policzyc roboczy wynik priorytetu:

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

Wynik nie ma zastapic oceny eksperckiej, tylko pomoc w sortowaniu kandydatow.

### Etap 6. Kategorie robocze

Startowe kategorie:

- logika i dedukcja,
- wspolpraca,
- komunikacja,
- negocjacje,
- kreatywnosc,
- projektowanie,
- podejmowanie decyzji,
- zycie codzienne,
- pieniadze i przedsiebiorczosc,
- informacja i fake news,
- planowanie,
- problemy spoleczne,
- konstruowanie,
- zagadki,
- gry i rywalizacja.

Dodatkowe kategorie do rozważenia podczas kwerendy:

- misje detektywistyczne,
- optymalizacja,
- logistyka,
- handel i wymiana,
- awarie i zarzadzanie kryzysem,
- komunikacja z ograniczeniami,
- prototypowanie,
- test fizyczny.

### Etap 7. Zwroty akcji

Przy kazdym kandydacie sprawdzic, czy mozna dodac jeden z mechanizmow:

- zmiana budzetu,
- ograniczenie czasu,
- utrata zasobu,
- nowa informacja,
- zmiana celu,
- konflikt interesow,
- dodatkowy klient/interesariusz,
- nieoczekiwane wydarzenie,
- awaria,
- zmiana kryteriow wygranej,
- zakaz uzycia jednego rozwiazania,
- koniecznosc wymiany zasobow z innym zespolem.

Zwrot akcji ma wzmacniac zadanie, a nie robic chaos.

### Etap 8. Kontrola skalowalnosci

Kazda aktywnosc musi zostac oceniona dla:

- malej grupy: ok. 16 uczniow, najlepiej 4 zespoly po 4 osoby,
- duzej grupy: ok. 30 uczniow, najlepiej 5-6 zespolow po 5-6 osob,
- pracy rownoleglej kilku zespolow,
- kontroli przez jednego nauczyciela,
- ryzyka chaosu przy 30 osobach.

Priorytet maja aktywnosci, ktore dzialaja rownolegle w zespolach 4-6 osob i maja prosty, mierzalny wynik.

### Etap 9. Weryfikacja i deduplikacja

Po zebraniu kandydatow:

1. Usunac duplikaty.
2. Polaczyc aktywnosci o tym samym mechanizmie.
3. Odrzucic rekordy slabiej dopasowane do BS I / technikum.
4. Oznaczyc `STRONG CANDIDATE`.
5. Oznaczyc ryzyka.
6. Zostawic minimum 100 sensownych rekordow.

### Etap 10. Rankingi koncowe

Przygotowac:

- TOP 20 najbardziej obiecujacych aktywnosci dla BS I / technikum,
- TOP 10 bez zadnego przygotowania,
- TOP 10 najbardziej angazujacych,
- TOP 10 rozwijajacych wspolprace,
- TOP 10 rozwijajacych myslenie,
- TOP 10 wykorzystujacych zwroty akcji.

Kazdy ranking powinien zawierac krotkie uzasadnienie, a nie tylko liste nazw.

## Kryteria gotowosci pierwszej wersji

Pierwsza wersja kwerendy jest gotowa, gdy:

- baza ma minimum 100 rekordow po deduplikacji,
- kazdy rekord ma wypelnione pola obowiazkowe,
- kazda aktywnosc miesci sie w 45 minutach,
- kazda aktywnosc ma jasny konkretny efekt,
- aktywnosci z duzym ryzykiem chaosu albo zawstydzenia sa oznaczone,
- TOP 20 zawiera glownie rekordy `STRONG CANDIDATE`,
- mozna od razu wybrac aktywnosc na zastepstwo bez czytania calej bazy.

## Najblizsze zadania

1. Utworzyc strukture katalogow i puste szablony bazy.
2. Przygotowac liste zapytan PL/EN do kwerendy.
3. Zebrac pierwsza pule 30-40 kandydatow z roznorodnych zrodel.
4. Przetestowac format rekordu na kilku przykladach.
5. Dopiero potem skalowac baze do 100+ rekordow.

