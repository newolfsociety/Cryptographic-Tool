# importing Flask and other modules
from flask import Flask, request, render_template
from CeasarCipher import EncryptCeasar, DecryptCeasar
from KeywordCipher import key_main, encr, decr
from AffineCipher import *
from MessageDigest import *
from SHA import *
from RSA import *
from RSA import lock, key

# Flask constructor
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def crypto():
    return render_template("HomePage.html")

@app.route('/CeasarCipher', methods=["GET", "POST"])
def crypto1():
    if request.method == "POST":
        text = request.form.get("d_string")
        k = int(request.form.get("k_value"))
        option = request.form.get('option')
        if option == 'Encrypt':
            return 'The Encrypted message is: ' + EncryptCeasar(text, k)
        elif option == 'Decrypt':
            return 'The Decrypted message is: ' + DecryptCeasar(text, k)
        else:
            pass
    return render_template("CeasarCipher.html")


@app.route('/KeywordCipher', methods=["GET", "POST"])
def crypto2():
    if request.method == "POST":
        text = request.form.get("d_string")
        key = request.form.get("k_value")
        keyf = key_main(key)
        option = request.form.get('option')
        if option == 'Encrypt':
            return 'The Encrypted message is: ' + encr(text, keyf)
        elif option == 'Decrypt':
            return 'The Decrypted message is: ' + decr(text, keyf)
        else:
            pass
    return render_template("KeywordCipher.html")


@app.route('/AffineCipher', methods=["GET", "POST"])
def crypto3():
    if request.method == "POST":
        text = request.form.get("d_string")
        option = request.form.get('option')
        if option == 'Encrypt':
            return 'The Encrypted message is: ' + affine_encrypt(text)
        elif option == 'Decrypt':
            return 'The Decrypted message is: ' + affine_decrypt(text)
        else:
            pass
    return render_template("AffineCipher.html")


@app.route('/MessageDigest', methods=["GET", "POST"])
def crypto4():
    if request.method == "POST":
        text = request.form.get("d_string")
        return 'The MD5 Equivalent of the Text entered is: ' + MD5(text)
    return render_template("MD5.html")


@app.route('/SHA', methods=["GET", "POST"])
def crypto5():
    if request.method == "POST":
        text = request.form.get("d_string")
        option = request.form.get('option')
        if option == 'SHA1':
            return 'SHA1 Equivalent of the message: ' + SHAEncrypt1(text)
        elif option == 'SHA256':
            return 'SHA256 Equivalent of the message: ' + SHAEncrypt256(text)
        elif option == 'SHA224':
            return 'SHA224 Equivalent of the message: ' + SHAEncrypt224(text)
        elif option == 'SHA384':
            return 'SHA384 Equivalent of the message: ' + SHAEncrypt384(text)
        elif option == 'SHA512':
            return 'SHA512 Equivalent of the message: ' + SHAEncrypt512(text)
        else:
            pass
    return render_template("SHA.html")


@app.route('/RSA', methods=["GET", "POST"])
def crypto6():
    if request.method == "POST":
        text = request.form.get("d_string")
        option = request.form.get('option')
        if option == 'Encrypt':
            return 'The Encrypted message is: ' + encrypt_text(text, lock)
        elif option == 'Decrypt':
            return 'The Decrypted message is: ' + decrypt_text(text, key)
        else:
            pass
    return render_template("RSA.html")


if __name__ == '__main__':
    app.run(debug=True)
