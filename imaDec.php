<?php
if (isset($_POST['submit'])) {
    $info = pathinfo($_FILES['plain_img']['name']);
    $ext = $info['extension']; // get the extension of the file
    $newname = "cipher_img." . $ext;

    // $target = 'images/' . $newname;
    move_uploaded_file($_FILES['plain_img']['tmp_name'], $newname);
    header("location: imadec2.html");
}

?>
<!-- Buat page awal -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image | Decryption</title>

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <link rel="stylesheet" href="style.css">
</head>

<body>

    <nav>
        <div class="nav-wrapper">
            <div class="container">
                <a href="index.html" class="brand-logo">Cryptography</a>
                <ul class="right hide-on-med-and-down">
                    <li><a href="text.html">Text</a></li>
                    <li><a href="image.html">Image</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        <div class="row">
            <h4>Image Decryption</h4>
        </div>
        <div class="row">
            <form class="col s12" action="#" method="post" enctype="multipart/form-data">
                <div class="row">
                    <div class="col s6">
                        <!-- <input type="file" name="plain_img"> -->
                        <input type="file" accept="image/*" name="plain_img" id="plain_img" onchange="loadFile(event)">
                        <img id="output" width="200" />
                    </div>
                </div>
                <div class="row">
                    <div class="col s6">
                        <input type="submit" name="submit" class="btn waves-effect waves-light red">
                    </div>
                </div>
            </form>
        </div>
    </div>

    <script src="js/displayImg.js"></script>

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</body>

</html>