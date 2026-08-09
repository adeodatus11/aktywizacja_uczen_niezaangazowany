# A030 | Awaria w warsztacie

## Status
Gotowe do użycia po wydruku / bez wydruku. FALA 1.

## Cel dla uczniów
Uczniowie ustalają kolejność napraw w fikcyjnym warsztacie, liczą skutki przestoju i bronią priorytetów przy ograniczonej liczbie pracowników.

## Materiały
- Karta scenariusza na zespół albo tabela na tablicy.
- Kartka A4, długopis, kalkulator opcjonalnie.

## Instrukcja dla uczniów (do odczytania)
Jesteście zespołem organizującym pracę fikcyjnego warsztatu "Delta". W jednym dniu pojawiło się pięć awarii, a ludzi i części nie wystarczy na wszystko naraz. Macie wybrać kolejność napraw, żeby warsztat stracił jak najmniej czasu, pieniędzy i zaufania klienta. Po 10 minutach dojdzie pilne zamówienie.

## Karta pracy / materiały uczniowskie
Zasoby warsztatu:
- 2 techników mechanicznych: T1, T2.
- 1 technik elektryk: E1.
- 1 stanowisko podnośnikowe.
- Dzień pracy: 6 godzin.
- Jedna naprawa może być robiona tylko wtedy, gdy dostępni są wymagani ludzie i stanowisko.

Awaria i dane:

| Kod | Awaria | Czas naprawy | Wymaga | Koszt przestoju za godzinę | Termin / ryzyko |
|---|---|---:|---|---:|---|
| W1 | Podnośnik nie blokuje pozycji | 2 h | T1 + podnośnik | 300 zł | bez tego wolniej idą inne naprawy |
| W2 | Kompresor przerywa pracę | 1 h | T2 | 180 zł | potrzebny do zamówienia o 13:00 |
| W3 | Błąd czujnika w pojeździe klienta | 2 h | E1 | 250 zł | klient czeka do 12:00 |
| W4 | Wymiana uszkodzonego przewodu | 1 h | E1 + T1 | 120 zł | niskie ryzyko |
| W5 | Hamulce w pojeździe dostawczym | 3 h | T2 + podnośnik | 400 zł | pojazd ma wyjechać do 14:00 |

Godzina startu: 8:00.

Kryteria priorytetu:
1. Bezpieczeństwo i blokowanie innych prac.
2. Termin klienta.
3. Koszt przestoju.
4. Czas naprawy i dostępność ludzi.

Zadania zespołu:
1. Ułóżcie harmonogram od 8:00 do 14:00.
2. Przy każdej awarii zapiszcie godzinę startu i końca.
3. Wypiszcie 2 awarie, które mają najwyższy priorytet, i dlaczego.
4. Policzcie szacunkowy koszt opóźnień: każda awaria zakończona po terminie liczy pełne godziny opóźnienia razy koszt przestoju.

## Przebieg 45 minut
| Czas | Działanie |
|---:|---|
| 0-4 min | Odczytanie roli i zasad. |
| 4-10 min | Zespoły układają pierwszy harmonogram. |
| 10 min | Zwrot akcji: pilne zamówienie. |
| 10-24 min | Przebudowa harmonogramu i liczenie kosztów. |
| 24-34 min | Zapis finalnej tabeli i uzasadnienia. |
| 34-42 min | Porównanie rozwiązań: gdzie powstał przestój i dlaczego. |
| 42-45 min | Podsumowanie priorytetów: pilne nie zawsze znaczy najważniejsze. |

## Zwrot akcji
O 10:00 pojawia się zlecenie Z1: przygotowanie narzędzi do wysyłki serwisowej. Trwa 1 godzinę, wymaga T1 albo T2, nie wymaga podnośnika. Jeżeli nie skończy się do 12:00, warsztat traci 200 zł. Z1 nie może przerwać trwającej naprawy, ale może wejść jako następne zadanie.

## Punktacja / kryterium sukcesu
Maksymalnie 40 punktów:

| Kryterium | Punkty |
|---|---:|
| Harmonogram używa tylko dostępnych ludzi i jednego podnośnika | 10 |
| Priorytety odnoszą się do podanych kryteriów, nie do zgadywania | 8 |
| Uwzględniono zwrot akcji Z1 | 6 |
| Koszt opóźnień policzony logicznie | 6 |
| Plan minimalizuje przestoje stanowiska podnośnikowego | 5 |
| Zapis jest czytelny i możliwy do wykonania | 5 |

Kryterium sukcesu: zespół ma realny harmonogram, żadna osoba nie robi dwóch prac naraz, a uzasadnienie pokazuje kompromis między terminem, kosztem i bezpieczeństwem.

## Klucz lub przykład dobrego rozwiązania
Przykładowy harmonogram:

| Czas | T1 | T2 | E1 | Podnośnik |
|---|---|---|---|---|
| 8:00-10:00 | W1 | W2 8:00-9:00, przerwa 9:00-10:00 | W3 | W1 |
| 10:00-11:00 | Z1 | przygotowanie W5 | W3 do 10:00, potem W4 z T1 nie może jeszcze wejść | wolny |
| 11:00-12:00 | W4 | W5 | W4 | W5 |
| 12:00-14:00 | wsparcie organizacyjne | W5 | dokumentacja / rezerwa | W5 |

Wynik:
- W1 kończy się o 10:00 i odblokowuje bezpieczne użycie podnośnika.
- W3 kończy się o 10:00, przed terminem 12:00.
- Z1 kończy się o 11:00, przed terminem 12:00.
- W5 trwa 11:00-14:00, mieści się w terminie 14:00.
- W4 kończy się o 12:00, ma niskie ryzyko.
- Koszt opóźnień: 0 zł.

Uwaga: To nie jest jedyne dobre rozwiązanie. Plan, który zaczyna od W5, może stracić punkty, jeśli blokuje podnośnik przed naprawą W1 albo opóźnia W3.

## Uwagi dla nauczyciela
- Jeśli uczniowie nie zauważą konfliktu o podnośnik, poproś ich o dopisanie kolumny "stanowisko".
- Nie wymagaj idealnej optymalizacji. Ważniejsza jest logika priorytetów i brak sprzeczności w harmonogramie.
- Przy klasie zawodowej można dodać pytanie: które zadanie wymaga najpierw zabezpieczenia miejsca pracy.
