#!/bin/bash

(
# Preveri ce so 3je parametri
if [ $# -ne 3 ]; then
    echo "Napaka: Skripta potrebuje točno 3 parametre."
    echo "Uporaba: $0 prvi_parameter(1/2) drugi_parameter(1-10) tretji_parameter(1-10)"
    exit 1
fi

# Shranimo parametre 
prvi_param=$1
drugi_param=$2
tretji_param=$3

# Preveri ce so vrednosti med 1 in 10
if [ $drugi_param -lt 1 ] || [ $drugi_param -gt 10 ] || [ $tretji_param -lt 1 ] || [ $tretji_param -gt 10 ]; then
    echo "Napaka: Drugi in tretji parameter morata biti med 1 in 10."
    echo "Konec skripte."
    exit 1
fi

# Prvi parameter mora biti 1 ali 2
if [ $prvi_param -ne 1 ] && [ $prvi_param -ne 2 ]; then
    echo "Ne poznam vrednosti prvega parametra."
    echo "Konec skripte."
    exit 1
fi

# Ce je prvi parameter 1, primerjamo drugi in tretji parameter
if [ $prvi_param -eq 1 ]; then
    echo "Prvi parameter ima vrednost 1."
    
    if [ $drugi_param -ge $tretji_param ]; then
        echo "Drugi parameter je vecji ali enak tretjemu parametru."
    else
        echo "Drugi parameter ni vecji ali enak tretjemu parametru."
    fi
fi

# Ce je prvi parameter 2, računamo zmnožke in seštevke
if [ $prvi_param -eq 2 ]; then
    echo "Prvi parameter ima vrednost 2."
    
    sestevek=0
    
    # Izracun mnozenja in sestevanja
    for ((i=1; i<=$drugi_param; i++)); do
        zmnozek=$((tretji_param * i))
        echo "$tretji_param * $i = $zmnozek"
        sestevek=$((sestevek + zmnozek))
    done
    
    echo "Skupni seštevek je = $sestevek"
fi
) | tee rezultati2-2-TilenDelicVerstovsek.txt

# Potrditveni izpis shranjevanja
echo "Rezultati so bili tudi shranjeni v datoteko rezultati2-2-TilenDelicVerstovsek.txt"