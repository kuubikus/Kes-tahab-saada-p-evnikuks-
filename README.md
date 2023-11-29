# Kes tahab saada päevnikuks?

Tabel, mis peab arvet, kui palju keegi on olnud päevnik. Programm võimaldab anda sõduritele motivatsioonipunkte. Osad võimalikud rikkumised ja vastavad punktid on ette antud tabelis 1. Üks päevnikuks olemise kord võrdub 10 punkti.

## Kuidas kasutada?
1. Ava kaust build/dist
2. Ava paevnikud.csv
3. Muuda esimeses tulbas nimed vastavalt oma üksusele
4. Iga päevnike vahetuse korral märgi tabelisse sõduri juurde, kes oli päevnik, "x" 
5. Vajadusel lisa punkte motivatsiooni lahtrisse
6. Sulge paevnikud.csv ja jooksuta paevnikud.exe
7. Avades uuesti paevnikud.csv on tabel uuendatud

## Märkused
1. Kui paevnikud.csv avatakse Exceli abil, võib juhtuda, et esimesel real on kuupäeva asemel #######. See tähendab, et kuupäev ei mahu kasti ära. Kasti suurendamisel viga kaob
2. Kui paevnikud.csv avatakse Exceli abil, võib juhtuda, et täpitähed ei ole korralikult šifreeritud. Probleemi põhjuseks on faili encoding. Proovige teist applicationit, nt Notepad++. paevnikud.csv on "UTF-8-sig" šifreeringuga.
3. Kuna mul puudub Signature, siis minu tehtud .exe failid tuvastatakse tihti, kui viirused. Kui soovite tarkvara kasutada, siis lubage allalaetav fail enda viiruse tõrjes (nt Windows Defenderi) 
4. Kui .exe faili ei saa mingil põhjusel kasutada, siis source code on olemas (paevnik.py.

##
Välja töötatud Eesti Mereväes, Rannikukaitse Divisjonis, nooremmaat Miku poolt
