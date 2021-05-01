# def Affine_egcd(a, b):
#     x, y, u, v = 0, 1, 1, 0
#     while a != 0:
#         q, r = b // a, b % a
#         m, n = x - u * q, y - v * q
#         b, a, x, y, u, v = a, r, u, v, m, n
#     gcd = b
#     return gcd, x, y


# def Affine_modinv(a, m):
#     gcd, x, y = Affine_egcd(a, m)
#     if gcd != 1:
#         return None
#     else:
#         return x % m


# def Affine_Encrypt(text):
#     key = [17, 20]
#     result= ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])

#     return result


# def Affine_Decrypt(text):
#     key = [17, 20]
#     result= ''.join([chr(((Affine_modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in text])
#     return result


def Affine_egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def Affine_modinv(a, m):
    gcd, x, y = Affine_egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def Affine_Encrypt(text):
    key = [17, 20]
    result= ''.join(chr((key[0] * ord(t) + key[1]) % 128) for t in text)

    return result


def Affine_Decrypt(text):
    key = [17, 20]
    result= ''.join(chr((Affine_modinv(key[0], 128) * (ord(c) - key[1])) % 128) for c in text)
    return result

# e = Affine_Encrypt('abcdefghijklmnopqrstuvwxyz')
# for i in e:
#     print(i, ord(i))
# print(Affine_Decrypt(e))