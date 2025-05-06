<?php

$conn = mysqli_connect('fdb1032.awardspace.net', '4486437_tilen', 'Nelit.2004', '4486437_tilen');

if(!$conn) {
    header("Location: index.php?error=" . urlencode(mysqli_connect_error()));
    exit();
}


if(empty($_POST['ime_studenta']) || empty($_POST['predmet']) || 
   empty($_POST['profesor']) || empty($_POST['datum']) || empty($_POST['ocena'])) {
    header("Location: index.php?error=Vsa obvezna polja so potrebna");
    exit();
}

$ime_studenta = mysqli_real_escape_string($conn, $_POST['ime_studenta']);
$predmet = mysqli_real_escape_string($conn, $_POST['predmet']);
$profesor = mysqli_real_escape_string($conn, $_POST['profesor']);
$datum = mysqli_real_escape_string($conn, $_POST['datum']);
$ocena = (int)$_POST['ocena'];
$komentar = mysqli_real_escape_string($conn, $_POST['komentar'] ?? '');


if($ocena < 1 || $ocena > 10) {
    header("Location: index.php?error=Ocena mora biti med 1 in 10");
    exit();
}


$sql = "INSERT INTO ocene_studentov (ime_studenta, predmet, profesor, datum, ocena, komentar) 
        VALUES ('$ime_studenta', '$predmet', '$profesor', '$datum', $ocena, '$komentar')";

if(mysqli_query($conn, $sql)) {
    header("Location: index.php?success=1");
} else {
    header("Location: index.php?error=" . urlencode(mysqli_error($conn)));
}

mysqli_close($conn);
?>