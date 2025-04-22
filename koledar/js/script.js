// Slovenski prazniki
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

// Dnevi v tednu
const dneviVTednu = ["Pon", "Tor", "Sre", "Čet", "Pet", "Sob", "Ned"];

// IMMEDIATE EXECUTION - Create calendar as soon as possible
// This ensures the table appears immediately on page load
inicializirajKoledar();

/**
 * Funkcija za inicializacijo koledarja
 */
function inicializirajKoledar() {
  // Check if document is already loaded
  if (document.readyState === 'loading') {
    // If not loaded, wait for DOMContentLoaded event
    document.addEventListener('DOMContentLoaded', function() {
      nastaviPoslusalce();
      nastaviTrenutniDatumVIzbirniku();
      posodobiKoledar(); // Generate calendar immediately
    });
  } else {
    // If already loaded, run initialization immediately
    nastaviPoslusalce();
    nastaviTrenutniDatumVIzbirniku();
    posodobiKoledar(); // Generate calendar immediately
  }
}

/**
 * Nastavi poslušalce za gumbe in izbirnike
 */
function nastaviPoslusalce() {
  document.getElementById('mesec').addEventListener('change', posodobiKoledar);
  document.getElementById('leto').addEventListener('change', posodobiKoledar);
  document.getElementById('gumbDanes').addEventListener('click', nastaviDanas);
}

/**
 * Funkcija za nastavitev trenutnega datuma v izbirniku
 */
function nastaviTrenutniDatumVIzbirniku() {
  try {
    const danes = new Date();

    // Nastavi mesec
    const mesecIzbirnik = document.getElementById('mesec');
    if (mesecIzbirnik) {
      mesecIzbirnik.value = danes.getMonth();
    }

    // Nastavi leto
    const letoIzbirnik = document.getElementById('leto');
    if (letoIzbirnik) {
      const leto = danes.getFullYear().toString();

      // Preveri, če izbrano leto obstaja v izbirniku
      let najdenoLeto = false;
      for (let i = 0; i < letoIzbirnik.options.length; i++) {
        if (letoIzbirnik.options[i].value === leto) {
          letoIzbirnik.value = leto;
          najdenoLeto = true;
          break;
        }
      }

      // Če leto ne obstaja, izberi najbližje
      if (!najdenoLeto && letoIzbirnik.options.length > 0) {
        // Default to first option if current year not found
        letoIzbirnik.selectedIndex = 0;
      }
    }
  } catch (err) {
    console.error("Napaka pri nastavljanju datuma:", err);
  }
}

/**
 * Funkcija za nastavitev današnjega datuma
 */
function nastaviDanas() {
  nastaviTrenutniDatumVIzbirniku();
  posodobiKoledar();
}

/**
 * Glavna funkcija za posodabljanje koledarja
 */
function posodobiKoledar() {
  try {
    // Preberi izbrani mesec in leto
    const mesecElement = document.getElementById('mesec');
    const letoElement = document.getElementById('leto');

    if (!mesecElement || !letoElement) {
      console.error("Manjkajoči elementi za izbor meseca ali leta");
      return;
    }

    const mesec = parseInt(mesecElement.value);
    const leto = parseInt(letoElement.value);

    // Pridobi podatke o dnevih
    const stDni = pridobiSteviloDni(leto, mesec);
    const prviDan = pridobiPrviDanVMesecu(leto, mesec);

    // Ustvari HTML za tabelo
    let html = '<table>';

    // Glava tabele
    html += '<tr>';
    for (let i = 0; i < dneviVTednu.length; i++) {
      html += '<th>' + dneviVTednu[i] + '</th>';
    }
    html += '</tr>';

    // Pridobi podatek o današnjem datumu
    const danes = new Date();
    const danasnjiDan = danes.getDate();
    const danasnjiMesec = danes.getMonth();
    const danasnjeGleto = danes.getFullYear();

    // Telo tabele
    let dan = 1;
    const stVrstic = Math.ceil((stDni + prviDan) / 7);

    for (let i = 0; i < stVrstic; i++) {
      html += '<tr>';

      for (let j = 0; j < 7; j++) {
        if ((i === 0 && j < prviDan) || dan > stDni) {
          html += '<td class="prazno"></td>';
        } else {
          let razred = [];

          // Preveri če je vikend
          if (j === 5 || j === 6) {
            razred.push('vikend');
          }

          // Preveri če je praznik
          const kljucPraznika = leto + '-' + (mesec + 1) + '-' + dan;
          if (prazniki[kljucPraznika]) {
            razred.push('praznik');
          }

          // Preveri če je današnji dan
          if (dan === danasnjiDan && mesec === danasnjiMesec && leto === danasnjeGleto) {
            razred.push('danes');
          }

          // Ustvari atribut za razred
          const razredStr = razred.length > 0 ? ' class="' + razred.join(' ') + '"' : '';

          // Dodaj naslov za praznik
          let title = '';
          if (prazniki[kljucPraznika]) {
            title = ' title="' + prazniki[kljucPraznika] + '"';
          }

          html += '<td' + razredStr + title + '>' + dan + '</td>';
          dan++;
        }
      }

      html += '</tr>';
    }

    html += '</table>';

    // Vstavi HTML v DOM
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

/**
 * Funkcija za pridobivanje števila dni v mesecu
 */
function pridobiSteviloDni(leto, mesec) {
  return new Date(leto, mesec + 1, 0).getDate();
}

/**
 * Funkcija za pridobivanje prvega dne v mesecu
 */
function pridobiPrviDanVMesecu(leto, mesec) {
  // V JavaScript je prvi dan nedelja (0), mi pa želimo, da je ponedeljek (0)
  const prviDan = new Date(leto, mesec, 1).getDay();
  return prviDan === 0 ? 6 : prviDan - 1;
}
