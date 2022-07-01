import hashlib
import binascii
import string
import base64

#from pycipher import SimpleSubstitution
import rsa


def RSA_text(string):
    public, private = rsa.newkeys(512)
    message = string.encode('utf-8')
    m_string = rsa.encrypt(message, public)
    print(m_string)
    m = 0
    for i in m_string:
        m += ord(i)
    return m


'''
def substitution_text(string, key):
    alpha = string.ascii_lowercase
    def make_alphabet(key):
        key = list(key)
        for i in key:
            alpha.remove(i)
        alphabet = str(key) + str(alpha)
        return alphabet
    alphabet = make_alphabet(key)
    ss = SimpleSubstitution(alphabet)
    return ss.encipher(string)
'''


def MD5(string):
    string = str.encode(string)
    m = hashlib.md5(string)
    return m.hexdigest()


def SHA256(string):
    string = str.encode(string)
    m = hashlib.sha256(string)
    return m.hexdigest()


def fixnonalpha(str1, str2):
    listt = list(str1)
    for i in range(len(str2)):
        if not (str2[i].isalpha()):
            listt.insert(i, str2[i])
    str1 = ""
    for i in listt:
        str1 += i
    return str1


def encrypt_vigenere_text(plaintext, key):
    plaintext2 = ''.join([i for i in plaintext if i.isalpha()])
    plaintext2 = plaintext2.lower()
    plaintext2 = plaintext2.strip()
    ciphertext = ""
    keylen = len(key)
    for i in range(len(plaintext2)):
        letter = plaintext2[i]
        if (letter.isalpha()):
            keyindex = i % keylen
            letterval = ord(letter) - 96

            keyval = ord(key[keyindex]) - 96
            shift = letterval + keyval + 95
            if (shift > 122):
                shift = shift - 26
            ciphertext = ciphertext + chr(shift)
        else:
            ciphertext = ciphertext + letter
    return fixnonalpha(ciphertext, plaintext)


def decode_vigenere_text(string, key):
    # TODO: assume key isnt known
    key = generateKey(string, key)
    orig_text = []
    for i in range(len(string)):
        x = (ord(string[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


def ceasar_text(plaintext, shift=None):
    if shift is None:
        shift = 13
    '''
    return ''.join([
            (lambda c, is_upper: c.upper() if is_upper else c)
                (
                  (plain.lower()*2)[ord(char.lower()) - ord('a') + shift % 26],
                  char.isupper()
                )
            if char.isalpha() else char
            for char in plain
        ])
    '''
    plaintext = plaintext.lower()
    plaintext = plaintext.strip()
    ciphertext = ""
    for letter in plaintext:
        if (letter.isalpha()):
            asciival = ord(letter)
            lettershift = asciival + shift
            if (lettershift > 122):
                lettershift = lettershift - 26
            ciphertext = ciphertext + chr(lettershift)
        else:
            ciphertext = ciphertext + letter
    return ciphertext


def decode_ceasar_text(string, shift=None):
    if shift is None:
        shift = 13
    pass


def hex_text(text):
    text = text.encode('utf-8')
    return text.hex()


def decode_hex_text(text):
    bin = binascii.a2b_hex(text)
    return decode_binary_text(bin)


def base64_text(text):
    return base64.b64encode(bytes(text, 'utf-8')).decode('utf-8')


def decode_base64_text(text):
    return base64.b64decode(bytes(text, 'utf-8'))


def binary_text(text):
    return " ".join([bin(ord(c))[2:].zfill(8) for c in text])


def decode_binary_text(text):
    return "".join([int(text[i:i+8], 2) for i in range(0, len(text), 8)])


def encryptDecrypt(inpString, xorKey):

    # calculate length of input string
    length = len(inpString)

    # perform XOR operation of key
    # with every caracter in string
    for i in range(length):
        inpString = (inpString[:i] +
                     chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:])
        #print(inpString[i], end="");

    return hex_text(inpString)


def xor_text(string, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(string, key*(len(string) / len(key) + 1))])


text_transforms = {
    'hex': {
        'encode': hex_text,
        'decode': decode_hex_text
    },
    'base64': {
        'encode': base64_text,
        'decode': decode_base64_text
    },
    'binary': {
        'encode': binary_text,
        'decode': decode_binary_text
    },
    'ceasar':  {
        'encode': ceasar_text,
        'decode': decode_ceasar_text
    }
}
