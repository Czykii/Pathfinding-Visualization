# **Wizualizacja algorytmów A* oraz Dijkstry**

<br>
<div style="text-align: right"><b>Kacper Czykierda</b></div>

## **1. Wstęp**
Program wykonany jako projekt zaliczeniowy z kursu Język Python w roku akademickim 2022/2023.

----------
<br>

## **2. Opis programu**
Program jest wizualizacją działania heurystycznego algorytmu A* oraz algorytmu Dijkstry służących do znalezienia najkrótszej ścieżki w grafie.
<br>
<br>
Użytkownik wybiera pole startowe (zostanie oznaczone kolorem pomarańczowym) oraz końcowe (zostanie oznaczone kolorem turkusowym), następnie ustala, które pola będą stanowiły blokadę na drodze do pola końcowego (zostaną oznaczone kolorem czarnym).
<br>
<br>
Po wybraniu odpowiednich pól i włączeniu wybranego algorytmu program zaczyna szukać najktórszej ścieżki zgodnie z wybranym algorytmem oznaczając pola, które już zostały odwiedzone kolorem czerwonym (dla algorytmu A*) bądź niebieskim (dla algorytmu Dijkstry) oraz te, które potencjalnie mogą zostać odwiedzone jako następne kolorem zielonym (dla algorytmu A*) bądź żółtym (dla algorytmu Dijkstry).
<br>
<br>
W momencie znalezienia najkrótszej ścieżki z pola startowego do końcowego pola stanowiące tą ścieżkę zostaną oznaczone kolorem fioletowym.
<br>
<br>
Program został napisany z pomocą tutorialu: https://www.youtube.com/watch?v=JtiK0DOeI4A&ab_channel=TechWithTim

----------
<br>

## **3. Sposób uruchomienia**
Aby uruchomić program należy zainstalować bibliotekę pygame oraz wywołać komendę:<br>
`python3 main.py`<br>
a następnie przystąpić do wyboru odpowiednich pól.

----------
<br>

## **4. Klawiszologia**

LPM (lewy przycisk myszy) - ustawienie pola na punkt startowy, punkt końcowy oraz blokadę

PPM (prawy przycisk myszy) - cofnięcie ustawienia pola

A - rozpoczęcie działania algorytmu A*

D - rozpoczęcie działania algorytmu Dijkstry

C - zresetowanie całej planszy

----------
<br>