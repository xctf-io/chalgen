"""
(C) 2010 - Marcin Wielgoszewski (Gotham Digital Science)

CSAW 2010 Cryptography Challenges
"""
from Crypto.Cipher import AES, DES
import base64
import hashlib
import hmac
import os
import struct
import time


__all__ = ['InvalidSignatureError',
           'BadPaddingError',
           'IllegalBlockSizeError',
           'sign_then_aes_decrypt',
           'aes_encrypt_then_sign',
           'aes_decrypt',
           'aes_encrypt',
           'des_decrypt',
           'des_encrypt',
           'authorize',
           'sign',
           'is_equal',
           'is_equal2',
           'e_html',
           'd_b64',
           'e_b64',
          ]


ALNUMS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


class InvalidSignatureError(Exception):
    def __init__(self):
        Exception.__init__(self)
    def __str__(self):
        return 'Invalid ciphertext signature'


class BadPaddingError(Exception):
    def __init__(self):
        Exception.__init__(self)
    def __str__(self):
        return 'Given final block not properly padded'


class IllegalBlockSizeError(Exception):
    def __init__(self, blocksize=8):
        Exception.__init__(self)
        self.length = blocksize
    def __str__(self):
        return 'Input length must be multiple of %d when decrypting with padded cipher' % self.length


def pkcs7_pad(data, blklen):
    # This is from M2Crypto.util:
    # http://websvn.osafoundation.org/filedetails.php?repname=m2crypto&path=%2Ftrunk%2FM2Crypto%2Futil.py

    if blklen > 255:
        raise ValueError("Illegal block size")

    pad = (blklen - (len(data) % blklen))
    return data + chr(pad) * pad


def sign_then_aes_decrypt(ctext, aes_key, hmac_key, codec='base64'):
    if codec is not None:
        if codec == 'base64':
            ctext = d_b64(ctext, '-', '_')
        else:
            ctext = ctext.decode(codec)

    cipher, mac = ctext[:-20], ctext[-20:]

    if is_equal(hmac.new(hmac_key, cipher, hashlib.sha1).digest(), mac):
        iv, ciphertext = cipher[:16], cipher[16:]
        aes = AES.new(aes_key, AES.MODE_CBC, iv)

        try:
            ptext = aes.decrypt(ciphertext)
            padding_length = struct.unpack("B", ptext[-1])[0]
            ptext = ptext[:-padding_length]
        except ValueError:
            raise IllegalBlockSizeError(16)

        return ptext

    else:
        raise InvalidSignatureError


def aes_encrypt_then_sign(ptext, aes_key, hmac_key, codec='base64'):
    iv = os.urandom(16)
    aes = AES.new(aes_key, AES.MODE_CBC, iv)

    ctext = aes.encrypt(pkcs7_pad(ptext, 16))
    signature = hmac.new(hmac_key, iv + ctext, hashlib.sha1).digest()

    if codec is not None:
        if codec == 'base64':
            token = e_b64(iv + ctext + signature, '-', '_').rstrip('=').rstrip()
        else:
            token = (iv + ctext + signature).encode(codec).rstrip()
    else:
        token = iv + ctext + signature

    return token


def aes_decrypt(ctext, aes_key, iv=None, codec='base64'):
    if codec is not None:
        if codec == 'base64':
            ctext = d_b64(ctext, '-', '_')
        else:
            ctext = ctext.decode(codec)

    if iv is None:
        iv = "\x00" * 16
        cipher = ctext
    else:
        iv, cipher = ctext[:16], ctext[16:]

    aes = AES.new(aes_key, AES.MODE_CBC, iv)

    try:
        ptext = aes.decrypt(cipher)
    except ValueError:
        raise IllegalBlockSizeError(16)

    return ptext


def aes_encrypt(ptext, aes_key, iv=None, codec='base64'):
    if iv is None:
        iv = "\x00" * 16
    else:
        iv = os.urandom(16)

    aes = AES.new(aes_key, AES.MODE_CBC, iv)

    ctext = aes.encrypt(pkcs7_pad(ptext, 16))

    if codec is not None:
        if codec == 'base64':
            token = e_b64(ctext, '-', '_').rstrip('=').rstrip()
        else:
            token = ctext.encode(codec).rstrip()
    else:
        token = ctext

    return token


def des_decrypt(ctext, des_key, codec='base64'):
    if codec is not None:
        if codec == 'base64':
            ctext = d_b64(ctext, '-', '_')
        else:
            ctext = ctext.decode(codec)

    des = DES.new(des_key, DES.MODE_ECB)

    try:
        ptext = des.decrypt(ctext)
    except ValueError:
        raise IllegalBlockSizeError(8)

    return ptext


def des_encrypt(ptext, des_key, codec='base64'):
    des = DES.new(des_key, DES.MODE_ECB)

    ctext = des.encrypt(pkcs7_pad(ptext, 8))

    if codec is not None:
        if codec == 'base64':
            token = e_b64(ctext, '-', '_').rstrip('=').rstrip()
        else:
            token = ctext.encode(codec).rstrip()
    else:
        token = ctext

    return token



def sign(text, hmac_key):
    signature = hmac.new(hmac_key, text, hashlib.md5).digest()
    return signature


def is_equal(x, y):
    result = 0
    if len(x) != len(y):
        return False

    for i, j in zip(map(ord, x), map(ord, y)):
        result |= i ^ j

    return result == 0


def is_equal2(x, y):
    start = time.time()
    result = 0
    if len(x) != len(y):
        return False, (time.time() - start)

    start = time.time()

    for i, j in zip(map(ord, x), map(ord, y)):
        if i ^ j != 0:
            result |= i ^ j
            break
        else:
            result |= i ^ j
            time.sleep(.1)

    elapsed = time.time() - start

    return result == 0, elapsed


def authorize(cookie, aes_key, hmac_key, challenge):
    try:
        token = sign_then_aes_decrypt(cookie.value, aes_key, hmac_key)
    except (AttributeError, TypeError):
        return False
    except (IllegalBlockSizeError, InvalidSignatureError):
        return False

    if token == challenge:
        return True

    return False


def e_html(s, style='hex', encode_all=False):
    """
    Return HTML-entity encoded string.

    @param s: A string.
    @param style: HTML entity encoding style: hexadecimal (default) or decimal.
    @param encode_all: Boolean encode HTML entities (False, default) or all characters.
    @return: An HTML entity encoded string.
    """
    if style == 'hex':
        if encode_all:
            return e_hex(s, '&#x', ';')
        else:
            return ''.join([(ch in ALNUMS) and ch or "&#x%02x;" % ord(ch) for ch in s])

    elif style == 'dec':
        if encode_all:
            return e_dec(s, '&#', ';')
        else:
            return ''.join([(ch in ALNUMS) and ch or "&#%d;" % ord(ch) for ch in s])

    else:
        raise TypeError, 'Invalid HTML Encoding style'


def e_dec(s, delim='', tail=''):
    """
    Return decimal encoded string, with an optional delimiter and trailing tail
    chracter.

    @param s: A string.
    @param delim: A byte string delimiter, i.e., '&#x'.
    @param tail: A byte string trailing char, i.e., ';'.
    @return: A decimal encoded string.
    """
    return "%s%s" % (delim.strip(),
                     delim.join(["%s%s" % (ord(ch), tail) for ch in s]))

def e_hex(s, delim='', tail=''):
    """
    Return hex encoded string, with an optional delimiter and trailing tail
    character.

    @param s: A string.
    @param delim: A byte string delimiter, i.e., '&#x'.
    @param tail: A byte string trailing char, i.e., ';'.
    @return: A hexdecimal encoded string.
    """
    return "%s%s" % (delim.strip(),
                     delim.join(["%02x%s" % (ord(ch), tail) for ch in s]))


def d_b64(s, plus='+', slash='/', url=False):
    """
    Returns a Base64 decoded string with optional character substitutions for
    the '+' and '/' characters often used for URL encoding.  Automatically
    attempts to decode modified Base64 for URL strings where the '=' padding
    was stripped away.

    Common substitutions for URL encoding the '+' and '/':
    + = %2B
    / = %2F

    @param s: A Base64 encoded string.
    @param plus: Character(s) to subsitute for '+'.
    @param slash: Character(s) to subsitute for '/'.
    @param url: Boolean indicating to strip trailing '=' characters.
    @return: A Base64 decoded string.
    """
    if plus is not '+':
        s = s.replace(plus, '+')
    if slash is not '/':
        s = s.replace(slash, '/')
    if url:
        s = s.replace('-', '+').replace('_', '/')

    try:
        return base64.b64decode(s)
    except TypeError:
        try:
            return base64.b64decode(s + '=')
        except TypeError:
            try:
                return base64.b64decode(s + '==')
            except TypeError:
                raise TypeError, "String does not appear to be Base64 encoded."


def e_b64(s, plus='+', slash='/', url=False):
    """
    Returns a Base64 encoded string with optional character substitutions for
    the '+' and '/' characters often used for URL encoding.

    Common substitutions for URL encoding the '+' and '/':
    + = %2B
    / = %2F

    @param s: A string.
    @param plus: Character(s) to subsitute for '+'.
    @param slash: Character(s) to subsitute for '/'.
    @param url: Boolean indicating to strip trailing '=' characters.
    @return: A Base64 encoded string.
    """
    encoded = base64.b64encode(s)

    if plus is not '+':
        encoded = encoded.replace('+', plus)
    if slash is not '/':
        encoded = encoded.replace('/', slash)
    if url:
        encoded = encoded.rstrip('=').replace('+', '-').replace('/', '_')

    return encoded
