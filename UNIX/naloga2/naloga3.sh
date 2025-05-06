#!/bin/bash

# Preveri ce je parameter podan
if [ $# -ne 1 ]; then
    echo "Napaka: Manjka parameter z imenom imenika."
    echo "Uporaba: $0 pot_do_imenika"
    exit 1
fi

# Shrani parameter
imenik=$1

# Preveri ali imenik sploh obstaja
if [ ! -d "$imenik" ]; then
    echo "Napaka: Imenik $imenik ne obstaja."
    exit 1
fi

echo "Začenjam preimenovanje datotek v imeniku $imenik..."

# Poisce vse datoteke v imeniku
find "$imenik" -maxdepth 1 -type f | while read datoteka; do
# Ime datoteke brez poti
    ime_datoteke=$(basename "$datoteka")
    
# Samo pot do datoteke
    pot_do_datoteke=$(dirname "$datoteka")
    
   
    novo_ime=$(echo "$ime_datoteke" | tr ' -' '_')

# Preimenovanje kadar je potrebno   
    if [[ "$ime_datoteke" != "$novo_ime" ]]; then
        mv "$datoteka" "$pot_do_datoteke/$novo_ime"
        echo "Datoteka $ime_datoteke preimenovana v $novo_ime"
    fi
done
# Izpis
echo "Preimenovanje zaključeno."
