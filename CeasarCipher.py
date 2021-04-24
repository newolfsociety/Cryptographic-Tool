def EncryptCeasar(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return "Cipher: " + result

def DecryptCeasar(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return "Text: " + result

text = input("Enter the string: ")
key = int(input("Enter the key: "))
print(EncryptCeasar(text,key))
text = input("Enter the string: ")
key = int(input("Enter the key: "))
print(DecryptCeasar(text,key))

