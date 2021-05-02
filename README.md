# Cryptographer
Cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it.

# Brief Description
This project contains some of the commonly used or were commonly used cryptographic algorithms. 
There are three symmetric algorithms, one assymetric algorithm and two hashing algorithms.

# Symmetric, Asymmetric and Hashing:
Symmetric-key algorithms are algorithms for cryptography that use the same cryptographic keys for both the encryption of plaintext and the decryption of ciphertext. While symmetric encryption is an older method of encryption, it is faster and more efficient than asymmetric encryption.Unfortunately, symmetric encryption does come with its own drawbacks. Its weakest point is its aspects of key management.

Asymmetric encryption, also known as Public-Key cryptography, is an example of one type. Unlike “normal” (symmetric) encryption, asymmetric encryption encrypts and decrypts the data using two separate yet mathematically-connected cryptographic keys. These keys are known as a 'Public Key' and a 'Private Key. The generation of such key pairs depends on cryptographic algorithms which are based on mathematical problems termed one-way functions.

Hashing is the transformation of a string of characters into a usually shorter fixed-length value or key that represents the original string. Hashing is used to index and retrieve items in a database.Encryption is a two-way function; what is encrypted can be decrypted with the proper key. Hashing, however, is a one-way function that scrambles plain text to produce a unique message digest. With a properly designed algorithm, there is no way to reverse the hashing process to reveal the original password.

# Cryptographic Algorithms:

# 1. Caeser Cipher
It is a type of substitution cipher in which each character in the plaintext is replaced by a letter some fixed number of positions down the ASCII table. There is a provision for the user to enter the text to be encypted and the key (the number of positions to be shifted), using which every character in the text entered will be replaced by a character which is key number of ASCII values ahead. For Decryption, every character in the cipher text is replaced by a character which is key number of ASCII values behind.

# 2. Keyword Cipher
It is a type of monoalphabetic or monocharacter substitution where every character of the entered text is replaced by a character which occupies the same index in the key. There is a provision for the user to enter the text to be encypted and also the key using which a keyword will be generated. The key will have the rest of the character set appended to it which becomes the keyword. Encryption and Decryption are both done by matching the index of given text with keyword.

# 3. Affine Cipher
The Affine cipher is a type of monoalphabetic substitution cipher, wherein each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter. 
<img width="946" alt="Screenshot1" src="https://www.tutorialspoint.com/cryptography_with_python/images/affine_cipher.jpg">

# 4. RSA Algorithm
It is an assymetric algorithm, meaning it uses a public key for encryption and a private key for decryption. Two prime numbers, p and q are selected. The product of these prime numbers is taken as n. (p-1)*(q-1) is taken as pn. A number e is then calculated which is co-prime with both n and pn and less than pn. [e,n] is the publc key. If t is the ASCII value of a character, then its encrypted form will be (t^e)%n. For private key, multiples of e which satisfy en%pn == 1, where en is a multiple of e, calculated. [en,n] is the private key. If t is the ASCII value of the encrypted character then, (t^en)%n will be the ASCII value of the decrypted character.

# 5. Secure Hashing Algorithms(SHA)
SHA is a family of cryptographic hashing algorithms. It takes the text entered by the user and uses random hex values, bitwise operations, modular additions, and compression functions on it and generates an encrypted text. It is mainly used for storing passwords and since it is a one way encryption, the original message cannot be retrieved from the hashed text. The Federal Information Processing Standard (FIPS 180-2) specifies four secure hash algorithms – SHA-1, SHA-256, SHA-384, and SHA-512 – all of which are iterative, one-way hash functions that can process a message with a maximum length of 264 – to 2128 – bits to produce a 160- to 512-bit condensed representation called a message digest.

#6. MD5
It is a cryptographic hashing algorithm from the message digest family. The MD5 hashing algorithm takes a message of arbitrary length as input and produces as output a 128-bit “fingerprint” or “message digest” of the input message.It is a complex sequence of simple binary operations, such as exclusive OR (XORs) and rotations, that are performed on input data and produce a 128-bit digest. It is faster than SHA but not as secure.
# Web app:
<img width="946" alt="Screenshot1" src="https://github.com/charvibannur/Cryptographic-Tool/blob/main/Screenshot%202021-05-01%20185300.png">
 
 
 # Team Members:
 
 Charvi Bannur: https://github.com/charvibannur
 
 Vishnu Bharadwaj: https://github.com/Vishnu1426
