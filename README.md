# **Wizualizacja algorytmu A-star**

<br>
<div style="text-align: right"><b>Kacper Czykierda</b></div>

## **1. Wstęp**
Program wykonany jako projekt zaliczeniowy z kursu Język Python w roku akademickim 2022/2023

----------
<br>

## **2. Opis programu**
Program jest wizualizacją działania heurystycznego algorytmu A* służącego do znalezienia najkrótszej ścieżki w grafie.
<br>
<br>
Użytkownik wybiera pole startowe (zostanie oznaczone kolorem pomarańczowym) oraz końcowe (zostanie oznaczone kolorem turkusowym), następnie ustala, które pola będą stanowiły blokadę na drodze do pola końcowego (zostaną oznaczone kolorem czarnym).
<br>
<br>
Po wybraniu odpowiednich pól i włączeniu algorytmu program zaczyna szukać najktórszej ścieżki oznaczając pola, które już zostały odwiedzone kolorem czerwonym oraz te, które potencjalnie mogą zostać odwiedzone jako następne kolorem zielonym.
<br>
<br>
W momencie znalezienia najkrótszej ścieżki z pola startowego do końcowego pola stanowiące tą ścieżkę zostaną oznaczone kolorem fioletowym.
<br>
<br>
Program napisany z pomocą tutorialu: https://www.youtube.com/watch?v=JtiK0DOeI4A&ab_channel=TechWithTim

----------
<br>

## **3. Sposób uruchomienia**
Aby uruchomić program należy wywołać komendę:<br>
`python3 main.py`<br>
a następnie przystąpić do wyboru odpowiednich pól.

----------
<br>

## **4. Klawiszologia**

LPM (lewy przycisk myszy) - ustawienie pola na punkt startowy, punkt końcowy oraz blokadę

PPM (prawy przycisk myszy) - cofnięcie ustawienia pola

Spacja - rozpoczęcie działania algorytmu

C - zresetowanie całej planszy

----------
<br>