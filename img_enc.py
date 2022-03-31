#!C:\xampp\htdocs\cryptography\Env\Scripts\python.exe
import numpy as np
import random
from Crypto.Cipher import AES
from Crypto import Random
import cv2
import cgi
print("Content-type: text/html\n\n")

form = cgi.FieldStorage()

key = form.getvalue('key')
# print(img)

img=cv2.imread('plain_img.jpg',1)#read image
na = np.array(img)#conver it to array
x, y ,pp= img.shape[:3]#size of 3d
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blue= np.array(range(x*y), int).reshape((x, y))
enc_blue= np.array(range(x*y), int).reshape((x, y))
blue[:,:]=gray[:, :]
key = key.encode()
iv=b'0000000000000000'
cipher = AES.new(key, AES.MODE_CFB, iv)
L2=[]
blue1 = np.array(range(x),int)
for i in range(x):
    blue1=blue[i,:].tolist()
    blue2=bytes(blue1)
    msg =  cipher.encrypt(blue2)
    for p in msg:
        L2 += [(p)]
    enc_blue[i,:]=L2[:]
    L2=[]



cv2.imwrite('cipher_img.jpg', enc_blue)

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
                    <img src="cipher_img.jpg">
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
# cipher_image = cv2.imread("enc_img.jpg")
# cv2.imshow('win', cipher_image) 
# cv2.waitKey(0)
# # # and finally destroy/close all open windows
# cv2.destroyAllWindows()