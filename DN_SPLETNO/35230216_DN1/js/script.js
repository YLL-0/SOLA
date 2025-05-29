// Seznam slovenskih praznikov za leta 2023-2025
const prazniki = {
  '2023-1-1': 'Novo leto',
  '2023-1-2': 'Novo leto',
  '2023-2-8': 'Prešernov dan',
  '2023-4-9': 'Velika noč',
  '2023-4-10': 'Velikonočni ponedeljek',
  '2023-4-27': 'Dan upora proti okupatorju',
  '2023-5-1': 'Praznik dela',
  '2023-5-2': 'Praznik dela',
  '2023-6-25': 'Dan državnosti',
  '2023-8-15': 'Marijino vnebovzetje',
  '2023-10-31': 'Dan reformacije',
  '2023-11-1': 'Dan spomina na mrtve',
  '2023-12-25': 'Božič',
  '2023-12-26': 'Dan samostojnosti in enotnosti',

  '2024-1-1': 'Novo leto',
  '2024-1-2': 'Novo leto',
  '2024-2-8': 'Prešernov dan',
  '2024-3-31': 'Velika noč',
  '2024-4-1': 'Velikonočni ponedeljek',
  '2024-4-27': 'Dan upora proti okupatorju',
  '2024-5-1': 'Praznik dela',
  '2024-5-2': 'Praznik dela',
  '2024-6-25': 'Dan državnosti',
  '2024-8-15': 'Marijino vnebovzetje',
  '2024-10-31': 'Dan reformacije',
  '2024-11-1': 'Dan spomina na mrtve',
  '2024-12-25': 'Božič',
  '2024-12-26': 'Dan samostojnosti in enotnosti',

  '2025-1-1': 'Novo leto',
  '2025-1-2': 'Novo leto',
  '2025-2-8': 'Prešernov dan',
  '2025-4-20': 'Velika noč',
  '2025-4-21': 'Velikonočni ponedeljek',
  '2025-4-27': 'Dan upora proti okupatorju',
  '2025-5-1': 'Praznik dela',
  '2025-5-2': 'Praznik dela',
  '2025-6-25': 'Dan državnosti',
  '2025-8-15': 'Marijino vnebovzetje',
  '2025-10-31': 'Dan reformacije',
  '2025-11-1': 'Dan spomina na mrtve',
  '2025-12-25': 'Božič',
  '2025-12-26': 'Dan samostojnosti in enotnosti'
};

// Seznam okrajšav za dni v tednu
const dneviVTednu = ["Pon", "Tor", "Sre", "Čet", "Pet", "Sob", "Ned"];

// Začetek izvajanja aplikacije
inicializirajKoledar();

// Funkcija za inicializacijo koledarja ob nalaganju strani
function inicializirajKoledar() {
  if (document.readyState === 'loading') {
    // Če se dokument še vedno nalaga, počakaj na dogodek DOMContentLoaded
    document.addEventListener('DOMContentLoaded', function() {
      nastaviPoslusalce();
      nastaviTrenutniDatumVIzbirniku();
      posodobiKoledar();
    });
  } else {
    // Če je dokument že naložen, takoj nastavi poslušalce in prikaži koledar
    nastaviPoslusalce();
    nastaviTrenutniDatumVIzbirniku();
    posodobiKoledar();
  }
}

// Funkcija za nastavitev poslušalcev dogodkov na kontrolne elemente
function nastaviPoslusalce() {
  document.getElementById('mesec').addEventListener('change', posodobiKoledar);
  document.getElementById('leto').addEventListener('change', posodobiKoledar);
  document.getElementById('gumbDanes').addEventListener('click', nastaviDanes);
}

// Funkcija za nastavitev trenutnega datuma v izbirnikih za mesec in leto
function nastaviTrenutniDatumVIzbirniku() {
  try {
    // Pridobi trenutni datum
    const danes = new Date();

    // Nastavi izbrani mesec na trenutni mesec
    const mesecIzbirnik = document.getElementById('mesec');
    if (mesecIzbirnik) {
      mesecIzbirnik.value = danes.getMonth();
    }

    // Nastavi izbrano leto na trenutno leto
    const letoIzbirnik = document.getElementById('leto');
    if (letoIzbirnik) {
      const leto = danes.getFullYear().toString();

      // Preveri, če je trenutno leto na voljo v izbirniku
      let najdenoLeto = false;
      for (let i = 0; i < letoIzbirnik.options.length; i++) {
        if (letoIzbirnik.options[i].value === leto) {
          letoIzbirnik.value = leto;
          najdenoLeto = true;
          break;
        }
      }

      // Če leto ni na voljo, izberi prvo leto v izbirniku
      if (!najdenoLeto && letoIzbirnik.options.length > 0) {
        letoIzbirnik.selectedIndex = 0;
      }
    }
  } catch (err) {
    console.error("Napaka pri nastavljanju datuma:", err);
  }
}

// Funkcija za nastavitev današnjega datuma in prikaz koledarja
function nastaviDanes() {
  nastaviTrenutniDatumVIzbirniku();
  posodobiKoledar();
}

// Funkcija za posodobitev prikaza koledarja glede na izbrani mesec in leto
function posodobiKoledar() {
  try {
    // Pridobi izbrani mesec in leto
    const mesecElement = document.getElementById('mesec');
    const letoElement = document.getElementById('leto');

    // Preveri, če sta elementa na voljo
    if (!mesecElement || !letoElement) {
      console.error("Manjkajoči elementi za izbor meseca ali leta");
      return;
    }

    const mesec = parseInt(mesecElement.value);
    const leto = parseInt(letoElement.value);

    // Pridobi število dni v mesecu in prvi dan v mesecu (0=ponedeljek, 6=nedelja)
    const stDni = pridobiSteviloDni(leto, mesec);
    const prviDan = pridobiPrviDanVMesecu(leto, mesec);

    // Začni graditi HTML za tabelo koledarja
    let html = '<table>';

    // Dodaj vrstico z imeni dni v tednu
    html += '<tr>';
    for (let i = 0; i < dneviVTednu.length; i++) {
      html += '<th>' + dneviVTednu[i] + '</th>';
    }
    html += '</tr>';

    // Pridobi podatke o današnjem datumu za posebno označevanje
    const danes = new Date();
    const danasnjiDan = danes.getDate();
    const danasnjiMesec = danes.getMonth();
    const danasnjeGleto = danes.getFullYear();

    // Pripravi spremenljivke za generiranje dni v mesecu
    let dan = 1;
    const stVrstic = Math.ceil((stDni + prviDan) / 7); // Izračunaj število potrebnih vrstic

    // Generiraj vrstice koledarja
    for (let i = 0; i < stVrstic; i++) {
      html += '<tr>';

      // Generiraj celice v vsaki vrstici
      for (let j = 0; j < 7; j++) {
        if ((i === 0 && j < prviDan) || dan > stDni) {
          // Prazna celica, če je pred prvim dnem meseca ali po zadnjem dnevu
          html += '<td class="prazno"></td>';
        } else {
          // Določi razrede za celico (vikend, praznik, danes)
          let razred = [];

          // Sobota in nedelja sta vikend
          if (j === 5 || j === 6) {
            razred.push('vikend');
          }

          // Preveri, če je dan praznik
          const kljucPraznika = leto + '-' + (mesec + 1) + '-' + dan;
          if (prazniki[kljucPraznika]) {
            razred.push('praznik');
          }

          // Preveri, če je to današnji dan
          if (dan === danasnjiDan && mesec === danasnjiMesec && leto === danasnjeGleto) {
            razred.push('danes');
          }

          // Združi razrede v niz za HTML
          const razredStr = razred.length > 0 ? ' class="' + razred.join(' ') + '"' : '';

          // Dodaj naslov z imenom praznika, če obstaja
          let title = '';
          if (prazniki[kljucPraznika]) {
            title = ' title="' + prazniki[kljucPraznika] + '"';
          }

          // Dodaj celico za dan
          html += '<td' + razredStr + title + '>' + dan + '</td>';
          dan++;
        }
      }

      html += '</tr>';
    }

    html += '</table>';

    // Vstavi generirano HTML tabelo v DOM
    const koledarElement = document.getElementById('koledar');
    if (koledarElement) {
      koledarElement.innerHTML = html;
    } else {
      console.error("Element koledarja ni bil najden");
    }
  } catch (err) {
    console.error("Napaka pri posodabljanju koledarja:", err);
  }
}

// Funkcija za pridobitev števila dni v izbranem mesecu in letu
function pridobiSteviloDni(leto, mesec) {
  return new Date(leto, mesec + 1, 0).getDate();
}

// Funkcija za pridobitev prvega dne v mesecu (0=ponedeljek, 6=nedelja)
function pridobiPrviDanVMesecu(leto, mesec) {
  const prviDan = new Date(leto, mesec, 1).getDay();
  // Pretvorba iz 0=nedelja, 6=sobota v 0=ponedeljek, 6=nedelja
  return prviDan === 0 ? 6 : prviDan - 1;
}