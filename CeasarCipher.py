def EncryptCeasar(text, key):
    result = ""
    for i in text:
        result += chr((ord(i) + key - 32) % 95 + 32)

    return result


def DecryptCeasar(text, key):
    result = ""
    for i in text:
        result += chr((ord(i) - key - 32) % 95 + 32)
    return result
