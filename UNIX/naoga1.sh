#!/bin/bash


# 1. V domačem imeniku ustvarite imenik foobar in nastavite pravice
mkdir ~/foobar             # Ustvari imenik 'foobar' v domačem imeniku
chmod 700 ~/foobar         # Nastavi pravice - samo lastnik ima dostop

# 2. Ustvarite skrito datoteko skript.txt in vanjo prepišite vsebino imenika /opt
touch ~/foobar/.skript.txt      # Ustvari skrito datoteko '.skript.txt' v imeniku 'foobar'
ls /opt > ~/foobar/.skript.txt    # Izpiše vsebino imenika /opt v datoteko '.skript.txt'

# 3. Preimenujte datoteko iz '.skript.txt' v 'seznam.dat'
mv ~/foobar/.skript.txt ~/foobar/seznam.dat
ls /usr/bin >> ~/foobar/seznam.dat

# 3. Dodajte izpis vsebine imenika /usr/bin v datoteko 'seznam.dat'

# 4. Poisce vse datoteke s koncnico .jpg in jih sortira (pipe = \)
# lahok dodamo se en pipe uniqe ki poskrbi da ne izpise ponovitev 
#nato pa se lahko upodabimo > kateri izpis ukaza na levi strani zapise v datoteko na desni
#za slike ki se ponavljajo pa lahko uporabimo enak ukaz ampak pri uniq dodamo se -d ki filtrera "duplicate"

find /foto-doma /foto-izlet -name "*.jpg" | sort | uniq > vse_slike.txt
find /foto-doma /foto-izlet -name "*.jpg" | sort | uniq -d > ponovitev.txt


# 5 
ls -d ~/imenik 2> /dev/null || echo "Datoteke so bile izbrisane"

# 6
ls -la ~/imenik 2> error_report.txt
 


cat dat?.txt > datvse.txt && tail -10 datvse.txt | wc -w
