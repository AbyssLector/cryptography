#!C:\xampp\htdocs\cryptography\Env\Scripts\python.exe
from email import message
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import cgi
import cgitb
print("Content-type: text/html\n\n")
BLOCK_SIZE = 32


def encrypt(text, key):
    encrypt_des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text, BLOCK_SIZE)
    encrypted_text = encrypt_des.encrypt(padded_text)
    return encrypted_text


def decrypt(cipher, key):
    decrypt_des = DES.new(key, DES.MODE_ECB)
    decrypted_text = decrypt_des.decrypt(cipher).decode('ascii')
    # https://developer.mozilla.org/en-US/docs/Glossary/CRLF
    return decrypted_text


form = cgi.FieldStorage()
raw = form.getvalue('plain_text')
raw = raw.encode()

key = form.getvalue('key')
key = key.encode()

# key = b'QWERTYUI'
# raw = b'plain text uji coba'

# harus 8 digit, jadi global variabel

try:
    cipher_text = encrypt(raw, key)
except Exception as e:
    print(e)
# dekripsi
replain_text = decrypt(cipher_text, key)

html_text = """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text | Encryption</title>

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
            <h2>Text Encryption</h2>
        </div>
        <div class="row">
            <form class="col s12" action="text_des.py" method="post">
                <div class="row">
                    <div class="input-field col s6">
                        <input placeholder="BekantanLepas" id="input_text" type="text" name="plain_text"
                            class="validate">
                        <label for="input_text">Plain Text</label>
                    </div>
                </div>
                <div class="row">
                    <div class="input-field col s6">
                        <input placeholder="8 karakter" id="input_key" type="text" name="key" class="validate">
                        <label for="input_key">Key</label>
                    </div>
                </div>
                <div class="row">
                    <div class="col s6">
                        <input type="submit" class="btn waves-effect waves-light red">
                    </div>
                </div>
            </form>
            <h4>{}</h4>
        </div>
    </div>


    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</body>

</html>
""".format(cipher_text)
print(html_text)
