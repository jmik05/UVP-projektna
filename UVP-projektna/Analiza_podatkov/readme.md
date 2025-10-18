# Analiza podatkov o najboljših powerlifterjih

## Projektna naloga pri predmetu UVP

Avtor: Januš Miklavčič<br>
Datum: 18. 10. 2025

V svojem projektu sem zajel podatke o najboljših powerlifterjih v kategoriji raw do 75 kg. Podatki so bili pobrani s spletne strani *Openpowerlifting.org*. Cilj je bil analizirati tekmovalce po disciplinah, narodnosti, starosti in datumu postavljenega rekorda.

## Viri
Za analizo je bili uporabljena spletna stran:
 - https://www.openpowerlifting.org/rankings/ipf

## Knjižnice
Za projekt sem za python program uporabil:
 - re (za uporabo regularnih izrazov);
 - csv (za ustvarjanje csv datotek);
 - request (za zajem podatkov);
 - os (za pot do datotek).

Za del projekta s Jupyternoteboob pa:
 - pandas (za analizo podatkov);
 - matplotlib.pyplot (za risanje grafov).

## Struktura projekta
V glavni mapi projekta se nahajata 2 podmapi: *Analiza_podatkov* in *Pridobitev_podatkov*. V mapi *Pridobitev_podatkov* je datoteka *Openpowerlifting.py*, ki se požene s pomočjo datoteke *main.py*. V *Openpowerlifting.py* so definirane naslednje funkcije: *poberi_podatke()*, ki iz spletne strani pobere podatke in iz njih filtrira uporabne, *slovar()*, ki iz podatkov, zbranih v *poberi_podatke*, naredi seznam in *usvari_csv*, ki iz slovarja usvari csv datoteko. V mapi *Analiza_podatkov* pa se nahajata datoteki *readme.md*, v kateri je navodilo, kako zagnati program, in *analiza_podatkov.ipynb*, v kateri se s pomočjo datoteke *podatki.csv*, ki jo ustvari prej omenjena *Openpowerlifting.py* datoteka, izvede analiza.

## Zagon programa
Uporabnik naj požene *main.py* in v *Pridobitev_podatkov* se bo usvarila  datoteka *podatki.csv*. Odpremo *Analiza_podatkov.ipynb* in poženemo celice v datoteki.