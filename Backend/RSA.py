def factors(a):
    fact = set()
    for i in range(1, a + 1):
        if a % i == 0:
            fact.add(i)
    return fact


def multiples(a):
    m = []
    for i in range(1, 400):
        m.append(a * i)
    return m


def encrypt(t, lock):
    enc = (t ** lock[0]) % lock[1]
    return enc


def decrypt(t, key):
    dec = (t ** key[0]) % key[1]
    return dec


def encrypt_text(t, lock):
    encrypted = []
    encr_m = ''
    for i in t:
        encrypted.append(encrypt(ord(i), lock))
    for i in encrypted:
        encr_m = encr_m + chr(i)
    return encr_m


def decrypt_text(t, key):
    decrypted = ''
    encr_n = []
    for i in t:
        encr_n.append(ord(i))
    for i in encr_n:
        decrypted = decrypted + chr(decrypt(i, key))
    return decrypted


p = 11
q = 19
n = p * q
pn = (p - 1) * (q - 1)
fact1 = factors(n)
fact2 = factors(pn)
e = 0
for i in range(2, pn):
    facte = factors(i)
    if facte & fact1 == {1}:
        if facte & fact2 == {1}:
            e = i
lock = [e, n]


# gen e multiples
ed = multiples(e)

# mod_1 numbers
mods = []
for i in ed:
    if i % pn == 1:
        mods.append(i)

d = int(max(mods) / e)
key = [d, n]
