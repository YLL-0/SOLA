<script type="text/javascript">
    function getcontent() {
        // Creating intens of HTTP request object
        var xmlHttp = new XMLHttpRequest();
        // Specify the method and the url
        xmlHttp.open("GET", "game-list.php", false);

        xmlHttp.send(null);

        //xmlHttp.responseText = game-list.php
        var element = document.getElementById("content");
        element.innerHTML = xmlHttp.responseText;


    }

</script>

<form>
    <input onclick="getcontent()" name="button" id="get content" />
</form>

<div id="content">

</div>