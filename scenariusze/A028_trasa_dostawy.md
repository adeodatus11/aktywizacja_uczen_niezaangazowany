# A028 | Trasa dostawy

## Status
Gotowe do użycia po wydruku / bez wydruku. FALA 1.

## Cel dla uczniów
Uczniowie planują trasę dostaw przy ograniczonym czasie i paliwie, porównują koszt z priorytetem paczek oraz uzasadniają wybór kolejności dostaw.

## Materiały
- Wydruk jednej karty pracy na zespół albo przepisanie mapy i tabeli na tablicę.
- Kartka A4 dla każdego zespołu.
- Długopis, kalkulator opcjonalnie.
- Zegar widoczny dla klasy.

## Instrukcja dla uczniów (do odczytania)
Jesteście dyspozytorami małej firmy kurierskiej w fikcyjnym mieście. Macie jeden pojazd, limit czasu i paliwa. Nie musicie dostarczyć wszystkiego, ale macie zdobyć jak najwięcej punktów za dobrze wybrane paczki i sensowną trasę. Najpierw policzcie koszt przejazdu, potem zdecydujcie, które dostawy są warte ryzyka. Po 12 minutach pojawi się zmiana w sieci dróg i będziecie musieli poprawić plan.

## Karta pracy / materiały uczniowskie
Start i koniec trasy: magazyn `M`.

Limit przed zwrotem akcji: maksymalnie 55 minut jazdy i 18 jednostek paliwa.

Zasady:
- Każdą ulicą można jechać w obie strony.
- Czas i paliwo z odcinka liczą się za każdy przejazd.
- Paczkę można dostarczyć tylko wtedy, gdy pojazd odwiedzi jej punkt.
- Trasa musi wrócić do magazynu `M`.
- Jeżeli przekroczycie limit czasu lub paliwa, plan jest nieważny.

Mapa tekstowa:

```text
        [A]----8/3----[B]
       /  \           /  \
   7/2    6/2     5/2    9/3
     /      \       /      \
   [M]--10/4--[C]--7/3----[D]
     \        /  \         /
    9/3    4/1   6/2    8/3
       \    /       \   /
        [E]----5/2---[F]
```

Opis odcinka: `czas w minutach / paliwo`.

Paczki:

| Punkt | Paczka | Punkty bazowe | Najpóźniej do minuty | Kara za spóźnienie |
|---|---:|---:|---:|---:|
| A | P1 | 12 | 22 | -4 |
| B | P2 | 18 | 35 | -6 |
| C | P3 | 10 | 28 | -3 |
| D | P4 | 24 | 45 | -8 |
| E | P5 | 14 | 30 | -4 |
| F | P6 | 16 | 40 | -5 |

Zadania zespołu:
1. Wypiszcie trasę w formie `M-C-F-D-C-M`.
2. Policzcie całkowity czas i paliwo.
3. Zaznaczcie, które paczki dostarczacie i w której minucie.
4. Policzcie punkty po ewentualnych karach.
5. Zapiszcie jedno zdanie uzasadnienia: dlaczego ta trasa jest lepsza niż dostarczenie wszystkich paczek.

## Przebieg 45 minut
| Czas | Działanie |
|---:|---|
| 0-4 min | Nauczyciel odczytuje instrukcję, dzieli klasę na zespoły 4-5 osobowe. |
| 4-12 min | Zespoły analizują mapę i wybierają pierwszą trasę. |
| 12 min | Nauczyciel ogłasza zwrot akcji. |
| 12-25 min | Zespoły poprawiają trasę, liczą wynik i zapisują uzasadnienie. |
| 25-35 min | Zespoły wpisują finalną trasę na kartce lub tablicy. |
| 35-42 min | Krótkie porównanie 3-4 rozwiązań: koszt, punkty, ryzyko. |
| 42-45 min | Podsumowanie: czym różni się trasa najkrótsza od trasy najlepszej. |

## Zwrot akcji
Po 12 minutach droga `C-D` zostaje zamknięta. Nie wolno jej używać w finalnym planie. Dodatkowo paczka `P4` w punkcie `D` dostaje premię +5 punktów, jeżeli zostanie dostarczona przed 45 minutą.

## Punktacja / kryterium sukcesu
Maksymalnie 40 punktów:

| Kryterium | Punkty |
|---|---:|
| Trasa jest poprawna, wraca do `M` i nie używa zamkniętej drogi | 8 |
| Czas i paliwo policzone bez błędów większych niż 1 jednostka | 8 |
| Dobór paczek uwzględnia wartość, termin i koszt dojazdu | 10 |
| Wynik punktowy obliczony poprawnie | 6 |
| Uzasadnienie pokazuje realny kompromis, a nie tylko "bo najwięcej" | 5 |
| Czytelny zapis trasy i minut dostawy | 3 |

Kryterium sukcesu: zespół ma ważną trasę, minimum 45 punktów za paczki przed karami oraz logiczne uzasadnienie priorytetów.

## Klucz lub przykład dobrego rozwiązania
Przykładowa dobra trasa po zwrocie akcji:

`M-E-C-F-D-F-C-M`

Obliczenia:
- `M-E` 9 min / 3 paliwa, dostawa P5 w minucie 9.
- `E-C` 4 min / 1 paliwa, dostawa P3 w minucie 13.
- `C-F` 6 min / 2 paliwa, dostawa P6 w minucie 19.
- `F-D` 8 min / 3 paliwa, dostawa P4 w minucie 27.
- `D-F` 8 min / 3 paliwa.
- `F-C` 6 min / 2 paliwa.
- `C-M` 10 min / 4 paliwa.

Suma: 51 minut, 18 paliwa. Paczki: P5 14 pkt, P3 10 pkt, P6 16 pkt, P4 24 + 5 premii = 29 pkt. Razem 69 punktów, bez kar za spóźnienie.

Dlaczego to dobre rozwiązanie: zespół rezygnuje z A i B, bo po zamknięciu `C-D` dojazd do D wymaga objazdu, a limit paliwa jest ciasny. Trasa wybiera paczki o wysokiej wartości i mieści się dokładnie w paliwie.

## Uwagi dla nauczyciela
- Jeżeli klasa ma trudność z liczeniem, pozwól najpierw szukać tras bez terminów, a terminy dolicz dopiero przy finalizacji.
- Nie oceniaj jednej jedynej "optymalnej" trasy. Ważne są poprawne limity, wynik i obrona decyzji.
- Przy pracy bez wydruku przepisz mapę i tabelę paczek na tablicę, a zespoły przepisują tylko wybraną trasę.
