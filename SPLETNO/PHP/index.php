<html>

<body>

    <?php
    pre_p($_POST);
    if (isset($_POST['submit'])) {
    };

    ?>

    <form action="" method="POST">
        Name: <input type="text" name="name" value=""><br>
        E-mail: <input type="text" name="last" value=""><br>
        Submit: <input type="submit" name="submit" value="submit"><br>

                </form>


</body>

</html>

<?php
function pre_p($array)
{
    echo '<ore>';
    print_r($array);
    echo '</pre>';
};
