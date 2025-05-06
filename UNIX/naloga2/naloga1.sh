#!/bin/bash

imenik=$(pwd)
echo "Trenutni imenik je $imenik"

# Dobimo trenutnega uporabnika sistema
uporabnik=$(whoami)
echo "Trenutni uporabnik sistema je $uporabnik"

# Ustvarimo nov imenik za procese
mkdir -p Procesi

echo "PID-i procesov uporabnika root:"
# Poiscemo vse procese od root uporabnika - prikaz v terminalu in zapis v datoteko
ps -u root -o pid | grep -v PID | tee Procesi/rootProcesi.txt
rootProcesi=$(cat Procesi/rootProcesi.txt)

echo -e "\nPID-i procesov uporabnika $uporabnik:"
# Poiscemo vse procese od našega uporabnika - prikaz v terminalu in zapis v datoteko
ps -u $uporabnik -o pid | grep -v PID | tee Procesi/userProcesi.txt
userProcesi=$(cat Procesi/userProcesi.txt)

# Izpis statusa zadnjega ukaza
echo -e "\nIzhodno stanje zadnjega izvrsenega programa je $?"

echo -e "\nDrevo procesov uporabnika root:"
# Ustvari in prikaži drevo procesov za root uporabnika
pstree root | tee Procesi/Drevo.txt

echo -e "\nPodatki so shranjeni v imeniku Procesi/"
