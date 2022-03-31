### Cryptography B. Enkrispsi text dan Image

#### List anggota:

- Muhammad Ihsanul Afkar (5027201024)
- Rafif Naufaldi Wibowo (5027201010)
- Muhammad Faris Anwari (5027201008)
- Nadine Haninta (5027201014)
- Fatih Rian Hibatul Hakim (5027201066)

#### Setup/Requirements

- Masukkan folder ke `htdocs/www/dll` tergantung pake apa (gw pake xampp)
- Config pada `Apache`, file `httpd.conf` terus tambahin di line paling bawah 

```
AddHandler cgi-script .py 
ScriptInterpreterSource Registry-Strict
```

- Start Apache buat pake localhost
- Tambahin di setiap line awal ekstensi `.py`. <br>
`#PATH_TO_PYTHON` <br>
contoh : <br>
`#!C:\xampp\htdocs\cryptography\Env\Scripts\python.exe`
<br>

***Masukkan path python yang sudah ada dalam folder `Env`***


Trus kalo mau install packages python, kasih tau terminal (vscode) kalo kita mau installnya di python `Env` <br>
Pake syntax `Env\Scripts\activate`. Nanti bakal ada `(Env)` di terminal. <br>
Baru install pake `pip install nama_package`

### Yang kurang

- Form input buat crypt & decrypt gambar AES
- Controller (proses enkripsinya) buat crypt & decrypt gambar AES 