# A033 | Pustynny konwój

## Status
Gotowe do użycia po wydruku / bez wydruku. FALA 2.

## Cel dla uczniów
Uczniowie wybierają trasę i podział zapasów dla fikcyjnego konwoju, oceniając ryzyko, zużycie zasobów i wartość dotarcia do celu.

## Materiały
- Karta pracy albo mapa i tabela przepisane na tablicę.
- Kartka A4 na zespół, długopis.
- Kalkulator opcjonalnie.

## Instrukcja dla uczniów (do odczytania)
To fikcyjna misja logistyczna. Wasz konwój ma przewieźć sprzęt do stacji badawczej na pustyni. Macie ograniczoną wodę, paliwo i czas. Celem nie jest "bohaterstwo", tylko plan, który daje najlepszy bilans bezpieczeństwa i skuteczności. Po 12 minutach jeden pojazd odpadnie z trasy i plan trzeba będzie zmienić.

## Karta pracy / materiały uczniowskie
Konwój startuje w `Baza` i ma dotrzeć do `Stacja`.

Mapa:

```text
 Baza
  |  2h / 2p / 1w / ryzyko 1
 Oaza A ---- 3h / 3p / 2w / ryzyko 2 ---- Wąwóz
  | \                                      / |
  |  \ 4h / 4p / 2w / ryzyko 3           /  | 2h / 2p / 1w / ryzyko 2
  |   \                                  /   |
  |    Płaskowyż ---- 3h / 3p / 1w ---- Punkt C
  |         \                            /
  |          \ 2h / 2p / 1w / ryzyko 1 /
  +----------- Punkt B ----------------+
              3h / 3p / 2w / ryzyko 2

 Punkt C ---- 2h / 2p / 1w / ryzyko 1 ---- Stacja
 Wąwóz  ---- 4h / 4p / 2w / ryzyko 4 ---- Stacja
```

Opis odcinka: czas / paliwo / woda / ryzyko.

Zasoby początkowe:
- 2 pojazdy.
- 12 jednostek paliwa.
- 7 jednostek wody.
- Maksymalnie 10 godzin jazdy.

Ładunki:

| Ładunek | Wartość punktowa | Warunek |
|---|---:|---|
| L1: części do generatora | 25 | musi dotrzeć do Stacji |
| L2: sprzęt pomiarowy | 15 | może jechać jednym pojazdem |
| L3: zapas narzędzi | 10 | można zostawić w punkcie pośrednim |

Ryzyko:
- Suma ryzyka trasy 1-4: brak kary.
- Suma ryzyka 5-7: -5 punktów.
- Suma ryzyka 8 lub więcej: -12 punktów.

Zadania zespołu:
1. Wybierzcie trasę przed zwrotem akcji.
2. Policzcie czas, paliwo, wodę i ryzyko.
3. Zdecydujcie, które ładunki zabieracie do Stacji.
4. Po zwrocie akcji poprawcie trasę i wynik.

## Przebieg 45 minut
| Czas | Działanie |
|---:|---|
| 0-5 min | Instrukcja, podział na zespoły. |
| 5-12 min | Pierwszy wybór trasy i zasobów. |
| 12 min | Zwrot akcji. |
| 12-26 min | Korekta trasy, zasobów i ładunków. |
| 26-35 min | Zapis finalnego planu. |
| 35-42 min | Prezentacja wybranych tras i porównanie ryzyka. |
| 42-45 min | Wniosek: najkrótsza trasa może mieć zbyt wysokie ryzyko. |

## Zwrot akcji
Po 12 minutach jeden pojazd odpada w `Oaza A`. Od tej chwili konwój ma tylko 1 pojazd i może zabrać maksymalnie 2 ładunki dalej. Ładunek L3 można bez kary zostawić w `Oaza A` albo `Punkt B`.

## Punktacja / kryterium sukcesu
Maksymalnie 40 punktów:

| Kryterium | Punkty |
|---|---:|
| Trasa jest spójna i kończy się w Stacji | 6 |
| Czas, paliwo i woda mieszczą się w limitach | 9 |
| Plan poprawnie uwzględnia utratę pojazdu | 8 |
| Dobór ładunków ma uzasadnienie punktowe i praktyczne | 7 |
| Ryzyko jest policzone i świadomie ograniczone | 6 |
| Zapis planu jest czytelny | 4 |

Kryterium sukcesu: zespół dowozi L1, mieści się w zasobach po utracie pojazdu i potrafi wskazać, z czego rezygnuje oraz dlaczego.

## Klucz lub przykład dobrego rozwiązania
Przykładowy dobry plan po zwrocie akcji:

Trasa: `Baza - Oaza A - Punkt B - Punkt C - Stacja`.

Obliczenia:
- Baza-Oaza A: 2 h, 2 paliwa, 1 wody, ryzyko 1.
- Oaza A-Punkt B: 3 h, 3 paliwa, 2 wody, ryzyko 2.
- Punkt B-Punkt C: 3 h, 3 paliwa, 2 wody, ryzyko 2.
- Punkt C-Stacja: 2 h, 2 paliwa, 1 wody, ryzyko 1.

Suma: 10 h, 10 paliwa, 6 wody, ryzyko 6. Kara za ryzyko: -5.

Ładunki: L1 i L2 jadą do Stacji, L3 zostaje w Oaza A. Punkty: 25 + 15 - 5 = 35.

Uzasadnienie: Plan mieści się dokładnie w czasie, oszczędza wodę i unika ryzyka 4 z drogi przez Wąwóz do Stacji. Rezygnacja z L3 jest racjonalna, bo po utracie pojazdu ma najniższą wartość.

## Uwagi dla nauczyciela
- Jeżeli uczniowie wybiorą ryzykowną trasę przez Wąwóz, nie poprawiaj od razu. Poproś o policzenie kary ryzyka.
- To ćwiczenie działa bez specjalistycznej wiedzy; chodzi o bilans zasobów.
- Przy braku wydruku uprość mapę do listy połączeń i tabeli kosztów.
