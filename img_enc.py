#!C:\xampp\htdocs\cryptography\Env\Scripts\python.exe
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import cgi
print("Content-type: text/html\n\n")

def encrypt_image(filename, key, iv):

    BLOCKSIZE = 16
    encrypted_filename = "encrypted_" + filename

    with open(filename, "rb") as file1:
        data = file1.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))

        with open(encrypted_filename, "wb") as file2:
            file2.write(ciphertext)

    return encrypted_filename



filename = "plain_img.jpg"

form = cgi.FieldStorage()
key = form.getvalue('key')

key = key.encode()
iv = b'0000000000000000'

encrypted_filename = encrypt_image(filename, key, iv)

html = """
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
            <h4>Decrypted Image</h4>
        </div>
        <div class="row">
            <div class="col">Output: </div>
        </div>
        <div class="row">
            <div class="col s6">
                <div class="card-panel">
                    <a href="encrypted_plain_img.jpg">Output</a>
                </div>
            </div>
        </div>
    </div>

    <script src="js/displayImg.js"></script>

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</body>

</html>
"""
print(html)