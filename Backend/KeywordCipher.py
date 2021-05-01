# alpha =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
# 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
# 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
# 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
# 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def Keyword_key_main(key):
    keyf = ''
    for i in key:
        if i not in keyf:
            keyf += i
    for i in range(126, 31, -1):
        if chr(i) not in keyf:
            keyf += chr(i)
    return keyf


def Keyword_Encr(text, keyf):
    alpha = ['~', '}', '|', '{', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j',
             'i',
             'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '`', '_', '^', ']', '\\',
             '[', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N',
             'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', '@',
             '?', '>', '=', '<', ';', ':', '9', '8', '7', '6', '5', '4', '3', '2',
             '1', '0', '/', '.', '-', ',', '+', '*', ')', '(', "'", '&', '%', '$',
             '#', '"', '!', ' ']
    enc = ''
    for i in text:
        ind = alpha.index(i)
        enc = enc + keyf[ind]
    return enc


def Keyword_Decr(text, keyf):
    alpha = ['~', '}', '|', '{', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j',
             'i',
             'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '`', '_', '^', ']', '\\',
             '[', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N',
             'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', '@',
             '?', '>', '=', '<', ';', ':', '9', '8', '7', '6', '5', '4', '3', '2',
             '1', '0', '/', '.', '-', ',', '+', '*', ')', '(', "'", '&', '%', '$',
             '#', '"', '!', ' ']
    dec = ''
    for i in text:
        ind = keyf.index(i)
        dec = dec + alpha[ind]
    return dec



