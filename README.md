# Misje na 45 minut

Projekt roboczy dotyczący misji i wyzwań na jednorazowe lekcje zastępcze.

## Cel

Zebranie materiałów, koncepcji i narzędzi wspierających nauczycieli w pracy z uczniami o niskim poziomie zaangażowania.

## Dokumenty robocze

- [Strona www katalogu](index.html)
- [Plan kwerendy](PLAN_KWERENDY.md)
- [Baza aktywności CSV](data/aktywnosci.csv)
- [Rejestr źródeł CSV](data/zrodla.csv)
- [Notatki źródłowe](research/notatki_zrodlowe.md)
- [Rankingi](rankingi/TOP.md)

## Strona

Strona katalogu jest statyczna i działa lokalnie po otwarciu `index.html` albo przez prosty serwer HTTP. Dane strony generuje skrypt:

```bash
python3 scripts/build_site_data.py
```
