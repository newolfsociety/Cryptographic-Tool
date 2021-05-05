def RSA_Factors(a):
    fact = set()
    for i in range(1, a + 1):
        if a % i == 0:
            fact.add(i)
    return fact


def RSA_Multiples(a):
    m = []
    for i in range(500, 600):
        m.append(a * i)
    return m


def RSA_Encrypt(t, lock):
    enc = (t ** lock[0]) % lock[1]
    return enc


def RSA_Decrypt(t, key):
    dec = (t ** key[0]) % key[1]
    return dec


def RSA_Encrypt_Text(t, lock):
    encrypted = []
    encr_m = ''
    for i in t:
        encrypted.append(RSA_Encrypt(ord(i), lock))
    for i in encrypted:
        encr_m = encr_m + chr(i)
    return encr_m


def RSA_Decrypt_Text(t, key):
    decrypted = ''
    encr_n = []
    for i in t:
        encr_n.append(ord(i))
    for i in encr_n:
        decrypted = decrypted + chr(RSA_Decrypt(i, key))
    return decrypted


p = 11
q = 23
n = p * q
pn = (p - 1) * (q - 1)

fact1 = RSA_Factors(n)
fact2 = RSA_Factors(pn)

e = 0
el = []

for i in range(2, pn):
    facte = RSA_Factors(i)
    if facte & fact1 == {1}:
        if facte & fact2 == {1}:
            e = i
            el.append(e)

e = el[-3]
RSA_Lock = [e, n]

# gen e multiples
ed = RSA_Multiples(e)

# mod_1 numbers
mods = []

for i in ed:
    if i % pn == 1:
        mods.append(i)
print(mods)

d = int(max(mods) / e)
RSA_Key = [d, n]

