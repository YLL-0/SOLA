<?php
// Vzpostavi povezavo s podatkovno bazo
$conn = mysqli_connect('fdb1032.awardspace.net', '4486437_tilen', 'Nelit.2004', '4486437_tilen');

// Preveri, če je povezava uspela
if(!$conn) {
    // Če povezava ni uspela, preusmeri nazaj na index.php z napako
    header("Location: index.php?error=" . urlencode(mysqli_connect_error()));
    exit();
}

// Preveri, če so vsa obvezna polja izpolnjena
if(empty($_POST['ime_studenta']) || empty($_POST['predmet']) || 
   empty($_POST['profesor']) || empty($_POST['datum']) || empty($_POST['ocena'])) {
    // Če kateri od podatkov manjka, preusmeri nazaj z napako
    header("Location: index.php?error=Vsa obvezna polja so potrebna");
    exit();
}

// Pripravi podatke za vnos v bazo in prepreči SQL vrivanje z mysqli_real_escape_string
$ime_studenta = mysqli_real_escape_string($conn, $_POST['ime_studenta']);
$predmet = mysqli_real_escape_string($conn, $_POST['predmet']);
$profesor = mysqli_real_escape_string($conn, $_POST['profesor']);
$datum = mysqli_real_escape_string($conn, $_POST['datum']);
$ocena = (int)$_POST['ocena']; // Pretvori v celo število
$komentar = mysqli_real_escape_string($conn, $_POST['komentar'] ?? '');

// Dodatno preveri veljavnost ocene
if($ocena < 1 || $ocena > 10) {
    header("Location: index.php?error=Ocena mora biti med 1 in 10");
    exit();
}

// Sestavi SQL stavek za vstavljanje podatkov
$sql = "INSERT INTO ocene_studentov (ime_studenta, predmet, profesor, datum, ocena, komentar) 
        VALUES ('$ime_studenta', '$predmet', '$profesor', '$datum', $ocena, '$komentar')";

// Izvedi poizvedbo in preusmeri z ustreznim sporočilom
if(mysqli_query($conn, $sql)) {
    header("Location: index.php?success=1"); // Uspeh
} else {
    header("Location: index.php?error=" . urlencode(mysqli_error($conn))); // Napaka
}

// Zapri povezavo z bazo
mysqli_close($conn);
?>