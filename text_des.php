<?php
// untuk back-end (API) enkripsi text DSA
// https://sheerapps.com/stories/article/encryption-and-decryption-using-des-algorithm-in-php
class Encryption
{
    public function convertHex($text)
    {
        $result = '';
        for ($i = 0; $i < strlen($text); $i++) {
            echo decbin(ord($text[$i])) . '<br>';
            $result .= decbin(ord($text[$i]));
            // switch ($text[$i]) {
            //     case '1':
            //         $result .= '0001';
            //         break;
            //     case '2':
            //         $result .= '0010';
            //         break;
            //     case '3':
            //         $result .= '0011';
            //         break;
            //     case '4':
            //         $result .= '0100';
            //         break;
            //     case '5':
            //         $result .= '0101';
            //         break;
            //     case '6':
            //         $result .= '0110';
            //         break;
            //     case '7':
            //         $result .= '0111';
            //         break;
            // }
        }
        return $result;
    }
}
$enc = new Encryption();
echo "berhasil\n";
$plain_text = $_POST['plain_text'];
$key = $_POST['key'];
$chiper_text = $enc->convertHex($plain_text);
// $chiper_text = crypt($plain_text, $key);
// echo $plain_text;
// echo $key;
echo $chiper_text;
