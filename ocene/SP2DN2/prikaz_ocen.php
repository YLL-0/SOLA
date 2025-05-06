<!DOCTYPE html>
<html lang="sl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prikaz vseh ocen</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Seznam vseh ocen</h1>
        
        <?php
        $conn = mysqli_connect('fdb1032.awardspace.net', '4486437_tilen', 'Nelit.2004', '4486437_tilen');
        
        if(!$conn) {
            echo '<div class="error">Povezava z bazo ni uspela: ' . mysqli_connect_error() . '</div>';
            exit();
        }
        
        $result = mysqli_query($conn, "SELECT * FROM ocene_studentov ORDER BY datum DESC");
        
        if(mysqli_num_rows($result) > 0) {
            echo '<table>';
            echo '<tr><th>Ime študenta</th><th>Predmet</th><th>Profesor</th><th>Datum</th><th>Ocena</th><th>Komentar</th></tr>';
            
            while($row = mysqli_fetch_assoc($result)) {
                echo '<tr>';
                echo '<td>' . htmlspecialchars($row['ime_studenta']) . '</td>';
                echo '<td>' . htmlspecialchars($row['predmet']) . '</td>';
                echo '<td>' . htmlspecialchars($row['profesor']) . '</td>';
                echo '<td>' . $row['datum'] . '</td>';
                echo '<td>' . $row['ocena'] . '</td>';
                echo '<td>' . htmlspecialchars($row['komentar']) . '</td>';
                echo '</tr>';
            }
            
            echo '</table>';
        } else {
            echo '<p>Ni najdenih ocen.</p>';
        }
        
        mysqli_close($conn);
        ?>
        
        <a href="index.php" class="link-button">Nazaj na vnos ocen</a>
    </div>
</body>
</html>