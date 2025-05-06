<!DOCTYPE html>
<html lang="sl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistem za beleženje študentskih ocen</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Vpis ocene studenta</h1>
        
        <?php
        if(isset($_GET['success'])) {
            echo '<div class="success">Ocena je bila uspešno shranjena.</div>';
        }
        if(isset($_GET['error'])) {
            echo '<div class="error">Napaka: ' . $_GET['error'] . '</div>';
        }
        ?>
        
        <form action="obdelava.php" method="post">
            <label for="ime_studenta">Ime in priimek študenta:</label>
            <input type="text" id="ime_studenta" name="ime_studenta" required>
            
            <label for="predmet">Predmet:</label>
            <input type="text" id="predmet" name="predmet" required>
            
            <label for="profesor">Profesor:</label>
            <input type="text" id="profesor" name="profesor" required>
            
            <label for="datum">Datum:</label>
            <input type="date" id="datum" name="datum" required>
            
            <label for="ocena">Ocena (1-10):</label>
            <input type="number" id="ocena" name="ocena" min="1" max="10" required>
            
            <label for="komentar">Komentar:</label>
            <textarea id="komentar" name="komentar" rows="3"></textarea>
            
            <button type="submit">Shrani oceno</button>
        </form>
        
        <a href="prikaz_ocen.php" class="link-button">Prikaži vse ocene</a>
    </div>
</body>
</html>