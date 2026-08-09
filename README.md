# Misje na 45 minut

Projekt roboczy dotyczacy misji i wyzwan na jednorazowe lekcje zastepcze.

## Cel

Zebranie materialow, koncepcji i narzedzi wspierajacych nauczycieli w pracy z uczniami o niskim poziomie zaangazowania.

## Dokumenty robocze

- [Strona www katalogu](index.html)
- [Plan kwerendy](PLAN_KWERENDY.md)
- [Baza aktywnosci CSV](data/aktywnosci.csv)
- [Rejestr zrodel CSV](data/zrodla.csv)
- [Notatki zrodlowe](research/notatki_zrodlowe.md)
- [Rankingi](rankingi/TOP.md)

## Strona

Strona katalogu jest statyczna i dziala lokalnie po otwarciu `index.html` albo przez prosty serwer HTTP. Dane strony generuje skrypt:

```bash
python3 scripts/build_site_data.py
```
