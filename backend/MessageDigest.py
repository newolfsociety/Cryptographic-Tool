import hashlib

def MD5(text):
    result = hashlib.md5(text.encode())
    return  result.hexdigest()

