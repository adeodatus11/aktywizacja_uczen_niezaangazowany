# A078 | Misja: naprawić szkolny automat

## Status
Gotowe do użycia po wydruku / bez wydruku. FALA 2.

## Cel dla uczniów
Uczniowie analizują fikcyjne skargi użytkowników, wybierają trzy najważniejsze poprawki automatu i projektują prosty test sprawdzający, czy poprawki działają.

## Materiały
- Karta skarg i danych albo tabela przepisana na tablicę.
- Kartka A4 dla zespołu.
- Długopis.

## Instrukcja dla uczniów (do odczytania)
Jesteście zespołem, który ma poprawić fikcyjny automat z przekąskami w centrum szkoleniowym. Nie chodzi o narzekanie, tylko o decyzję projektową: które problemy naprawić najpierw, bo najbardziej przeszkadzają użytkownikom. Macie ograniczony budżet, dane ze skarg i obowiązek zaplanowania testu.

## Karta pracy / materiały uczniowskie
Dane automatu "Snack-7":
- Dziennie korzysta około 120 osób.
- Automat ma ekran, czytnik płatności i spiralne podajniki.
- Budżet początkowy: 1000 zł.
- Można wybrać maksymalnie 3 poprawki.

Skargi z ostatnich 10 dni:

| Kod | Treść skargi | Liczba zgłoszeń | Skutek dla użytkownika |
|---|---|---:|---|
| S1 | Produkt zawiesza się po zapłacie | 18 | użytkownik traci czas i zgłasza zwrot |
| S2 | Ekran jest nieczytelny przy mocnym świetle | 11 | trudniej wybrać produkt |
| S3 | Automat nie pokazuje, że produkt się skończył | 15 | płatność za niedostępny produkt |
| S4 | Płatność kartą czasem trzeba powtórzyć | 9 | kolejka i irytacja |
| S5 | Produkty zdrowe są w dolnym rzędzie i słabo widoczne | 7 | mniejsza sprzedaż tych produktów |
| S6 | Instrukcja zwrotu pieniędzy jest niejasna | 12 | więcej pytań do obsługi |

Możliwe poprawki:

| Poprawka | Koszt | Efekt |
|---|---:|---|
| P1: czujnik wydania produktu | 450 zł | ogranicza S1 o 70% |
| P2: lepsza osłona ekranu | 250 zł | ogranicza S2 o 80% |
| P3: blokada sprzedaży pustych przegródek | 350 zł | ogranicza S3 o 90% |
| P4: aktualizacja płatności | 500 zł | ogranicza S4 o 60% |
| P5: zmiana układu półek | 150 zł | ogranicza S5 o 70% |
| P6: nowa instrukcja zwrotów na ekranie | 100 zł | ogranicza S6 o 75% |

Kryteria priorytetu:
1. Liczba zgłoszeń.
2. Skutek dla użytkownika: utrata pieniędzy/czasu jest ważniejsza niż wygoda.
3. Koszt poprawki.
4. Możliwość sprawdzenia efektem w teście.

Zadania zespołu:
1. Wybierzcie 3 poprawki.
2. Uzasadnijcie wybór przy użyciu danych.
3. Zapiszcie, z których problemów świadomie rezygnujecie.
4. Zaprojektujcie test: kto testuje, przez ile dni, co mierzycie, jaki wynik oznacza sukces.

## Przebieg 45 minut
| Czas | Działanie |
|---:|---|
| 0-5 min | Instrukcja i wyjaśnienie kryteriów priorytetu. |
| 5-10 min | Zespoły czytają skargi i zaznaczają najpoważniejsze. |
| 10 min | Zwrot akcji. |
| 10-25 min | Wybór poprawek po zmianie budżetu. |
| 25-35 min | Projekt testu rozwiązania. |
| 35-42 min | Prezentacja decyzji i testów. |
| 42-45 min | Podsumowanie: dobra poprawka ma mierzalny efekt. |

## Zwrot akcji
Po 10 minutach budżet spada z 1000 zł do 500 zł. Nadal można wybrać maksymalnie 3 poprawki, ale suma kosztów nie może przekroczyć 500 zł.

## Punktacja / kryterium sukcesu
Maksymalnie 40 punktów:

| Kryterium | Punkty |
|---|---:|
| Wybrane poprawki mieszczą się w budżecie 500 zł | 6 |
| Priorytety wynikają z liczby skarg i skutku dla użytkownika | 10 |
| Zespół wskazuje świadome rezygnacje | 5 |
| Test ma konkretne mierniki i próg sukcesu | 10 |
| Uzasadnienie odnosi się do danych, nie opinii | 6 |
| Zapis jest czytelny | 3 |

Kryterium sukcesu: zespół wybiera maksymalnie 3 poprawki do 500 zł i potrafi sprawdzić po wdrożeniu, czy skargi realnie spadły.

## Klucz lub przykład dobrego rozwiązania
Przykładowy wybór po spadku budżetu:
- P3: blokada sprzedaży pustych przegródek, 350 zł.
- P6: nowa instrukcja zwrotów, 100 zł.
- Razem: 450 zł. Trzeciej poprawki nie trzeba wybierać, bo budżet nie pozwala na sensowny dodatek poza P5, ale P5 dotyczy mniejszej szkody.

Alternatywa:
- P2 za 250 zł, P5 za 150 zł, P6 za 100 zł. Razem 500 zł.
- Ta opcja rozwiązuje trzy problemy, ale pomija S1 i S3, które dotyczą zapłaty i niewydania produktu.

Lepsze uzasadnienie dla pierwszej opcji:
- S3 ma 15 zgłoszeń i dotyczy płatności za niedostępny produkt, więc jest poważniejsze niż widoczność produktów.
- S6 ma 12 zgłoszeń i zwiększa chaos przy zwrotach, a koszt poprawki jest niski.
- Zespół świadomie rezygnuje z P1, bo P1 + P3 przekracza budżet. Rezygnacja jest bolesna, ale po P3 spada część sytuacji, w których użytkownik płaci za coś, czego nie ma.

Plan testu:
- Czas: 10 dni przed zmianą i 10 dni po zmianie.
- Mierniki: liczba zgłoszeń S3, liczba pytań o zwrot, liczba transakcji anulowanych.
- Próba: wszystkie transakcje z automatu, bez danych osobowych.
- Sukces: S3 spada z 15 do maksymalnie 3 zgłoszeń w 10 dni, a pytania o zwrot spadają z 12 do maksymalnie 4.

## Uwagi dla nauczyciela
- Pilnuj, aby uczniowie nie używali realnych nazw sklepów, osób ani szkolnych sytuacji.
- Jeżeli grupa chce wydać cały budżet "bo trzeba", przypomnij, że niewydanie pieniędzy też może być decyzją.
- Dobre pytanie podsumowujące: czy wybraliście problem najgłośniejszy, najdroższy, czy najważniejszy dla użytkownika.
