from Crypto.Cipher import AES
import struct, hashlib
from encrypt_utils import *

challenge1_flag = "this_isnt_the_flag"
challenge1_key = hashlib.md5('xxxxxxxxxxxxxxxxxxx').hexdigest()

def challenge1(sent_matrix_id):
        sid = sent_matrix_id

        challenge = "THE MATRIX IS REAL GUYS|user=neo|password=neo_is_cool_yo|authlevel=5|CHALLENGE1"
        matrix_id = aes_encrypt(challenge, challenge1_key, codec='base64')

        if sid:
            try:
                ptext = aes_decrypt(sid, challenge1_key, codec='base64')
            except TypeError:
                error = "Caught exception during AES decryption..."
                return error

            # This is where we introduce a CBC padding oracle vulnerability
            padding_length = struct.unpack("B", ptext[-1])[0]
            good = (ptext[-padding_length:] == struct.pack("B", padding_length) * padding_length)

            if good is False:
                error = "Looks like you gave the wrong padding for your encrypted stuff"
                return error
            else:
                ptext = ptext[:-padding_length]
                print ptext

            try:
                role = ptext.split('|')[3][-1]
                print ptext.split('|')[3][-1]
            except IndexError:
                error = "Was not able to compute your authlevel. Please submit a valid matrix id."
                return error

            try:
                username, password = ptext.split('|')[1:3]
            except ValueError:
                error = "Was not able to locate username and password in given matrix id."
                return error

            if role == '0':
                return challenge1_flag
            else:
                error = "Your authlevel is not 0. You will never be able to get access to the Matrix, Neo."
                return error

        else:
            return matrix_id

challenge1("BYeqEBmJ2Ms1o6-RnybtWRSLTHMDErux99hYoNCtjkDD_nrgiZ6cg59bzwBtBpa1YKTxqKq2xuZLC4t94UQiiSsa-QO6CUiYze71M6eYCJ8")
