import hashlib

def SHAEncrypt256(str):
    result = hashlib.sha256(str.encode())
    return result.hexdigest()

def SHAEncrypt384(str):
    result = hashlib.sha384(str.encode())
    return result.hexdigest()

def SHAEncrypt224(str):
    result = hashlib.sha224(str.encode())
    return result.hexdigest()

def SHAEncrypt512(str):
    result = hashlib.sha512(str.encode())
    return result.hexdigest()

def SHAEncrypt1(str):
    result = hashlib.sha1(str.encode())
    return result.hexdigest()

