import hashlib

def MD5(text):
    result = hashlib.md5(text.encode())
    return "The hexadecimal equivalent of MD5 is : " + result.hexdigest()
text = input("Enter text: ")
encrypted_data=MD5(text)
print(encrypted_data)
