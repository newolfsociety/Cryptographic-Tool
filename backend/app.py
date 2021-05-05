from flask import Flask, redirect, url_for, request, render_template
from RSA import *
from CeasarCipher import *
from SHA import *
from AffineCipher import *
from KeywordCipher import *
from MessageDigest import *
from AffineCipher import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    return render_template('home.html')


@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form['opt'] == 'caeserc':
            return render_template('caeser.html')
        elif request.form['opt'] == 'keywordc':
            return render_template('keyword.html')
        elif request.form['opt'] == 'affinec':
            return render_template('affine.html')
        elif request.form['opt'] == 'rsaa':
            return render_template('rsa.html')
        elif request.form['opt'] == 'shah':
            return render_template('sha.html')
        elif request.form['opt'] == 'md5h':
            return render_template('messagedigest.html')


@app.route('/display/<alg>/<value>/<e>')
def display(value, alg, e):
    return render_template('value.html', value=value, alg=alg, e=e)


@app.route('/rsa', methods=['POST', 'GET'])
def RSA():
    if request.method == 'POST':

        resm = request.form  # A dictionary of key value pairs. Key = name and value = entered value or defined value in the html input tag

        if request.form['option'] == 'encrypt':
            given = request.form['given']
            enc = RSA_Encrypt_Text(given, RSA_Lock)
            algo = 'RSA'
            e = 'encrypted'
            return redirect(url_for('display', value=enc, alg=algo, e=e))

        elif request.form['option'] == 'decrypt':
            given = request.form['given']
            dec = RSA_Decrypt_Text(given, RSA_Key)
            algo = 'RSA'
            e = 'decrypted'
            return redirect(url_for('display', value=dec, alg=algo, e=e))


@app.route('/caeser', methods=['POST', 'GET'])
def caeser():
    if request.method == 'POST':
        if request.form['option'] == 'encrypt':
            given = request.form['given']
            key = int(request.form['caeser_key'])
            enc = EncryptCeasar(given, key)
            algo = 'Caeser'
            e = 'encrypted'
            return redirect(url_for('display', value=enc, alg=algo, e=e))

        elif request.form['option'] == 'decrypt':
            given = request.form['given']
            key = int(request.form['caeser_key'])
            dec = DecryptCeasar(given, key)
            algo = 'Caeser'
            e = 'decrypted'
            return redirect(url_for('display', value=dec, alg=algo, e=e))


@app.route('/sha', methods=['POST', 'GET'])
def sha():
    if request.method == 'POST':
        if request.form['option'] == 'SHA1':
            given = request.form['given']
            hashsha = SHAEncrypt1(given)
            algo = 'SHA'
            e = 'sha1'
            return redirect(url_for('display', value=hashsha, alg=algo, e=e))

        elif request.form['option'] == 'SHA224':
            given = request.form['given']
            hashsha = SHAEncrypt224(given)
            algo = 'SHA'
            e = 'sha224'
            return redirect(url_for('display', value=hashsha, alg=algo, e=e))

        elif request.form['option'] == 'SHA256':
            given = request.form['given']
            hashsha = SHAEncrypt256(given)
            algo = 'SHA'
            e = 'sha256'
            return redirect(url_for('display', value=hashsha, alg=algo, e=e))

        elif request.form['option'] == 'SHA384':
            given = request.form['given']
            hashsha = SHAEncrypt384(given)
            algo = 'SHA'
            e = 'sha384'
            return redirect(url_for('display', value=hashsha, alg=algo, e=e))

        elif request.form['option'] == 'SHA512':
            given = request.form['given']
            hashsha = SHAEncrypt512(given)
            algo = 'SHA'
            e = 'sha512'
            return redirect(url_for('display', value=hashsha, alg=algo, e=e))


@app.route('/affine', methods=['POST', 'GET'])
def affine():
    if request.method == 'POST':

        if request.form['option'] == 'encrypt':
            given = request.form['given']
            enc = Affine_Encrypt(given)
            algo = 'Affine'
            e = 'encrypted'
            return redirect(url_for('display', value=enc, alg=algo, e=e))

        elif request.form['option'] == 'decrypt':
            given = request.form['given']
            dec = Affine_Decrypt(given)
            algo = 'Affine'
            e = 'decrypted'
            return redirect(url_for('display', value=dec, alg=algo, e=e))


@app.route('/keyword', methods=['POST', 'GET'])
def keyword():
    if request.method == 'POST':

        if request.form['option'] == 'encrypt':
            given = request.form['given']
            key = Keyword_key_main(request.form['key'])
            enc = Keyword_Encr(given, key)
            algo = 'Keyword'
            e = 'encrypted'
            return redirect(url_for('display', value=enc, alg=algo, e=e))

        elif request.form['option'] == 'decrypt':
            given = request.form['given']
            key = Keyword_key_main(request.form['key'])
            dec = Keyword_Decr(given, key)
            algo = 'Keyword'
            e = 'decrypted'
            return redirect(url_for('display', value=dec, alg=algo, e=e))


@app.route('/md5', methods=['POST', 'GET'])
def md5():
    if request.method == 'POST':
        given = request.form['given']
        hashmd5 = MD5(given)
        algo = 'MD5'
        e = "Nothing"
        return redirect(url_for('display', value=hashmd5, alg=algo, e=e))


if __name__ == '__main__':
    app.run(debug=True)