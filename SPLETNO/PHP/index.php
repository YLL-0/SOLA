<html>

<body>

    <?php
    pre_p($_POST);
    pre_p($_GET);
    pre_p($_REQUEST);
    if (isset($_GET['submit'])) {
    
    echo "First name: ".$_GET['name'].'<br/>';
    echo'Gmail: '.$_GET['last'].'<br/>';

    };

    ?>

    <form action="" method="GET">
        Name: <input type="text" name="name" value=""><br>
        E-mail: <input type="text" name="last" value=""><br>
        Submit: <input type="submit" name="submit" value="submit"><br>

    </form>


</body>

</html>

<?php
function pre_p($array)
{
    echo '<pre>';
    print_r($array);
    echo '</pre>';
};
