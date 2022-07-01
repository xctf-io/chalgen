from flask import render_template, request
import hashlib, struct

from encrypt_utils import *

challenge1_flag = "flag{what_if_i_told_you_you_solved_the_challenge}"
challenge1_key  = hashlib.md5('polyctf_super_key_1').hexdigest()

challenge2_flag = "flag{}"
challenge2_key  = hashlib.md5('polyctf_super_key_2').hexdigest()

challenge3_flag = "flag{}"
challenge3_key  = hashlib.md5('polyctf_super_key_3').hexdigest()

def init_views(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/challenge1/source')
    def challenge1_source():
        return app.send_static_file('challenge1_source.py')

    @app.route('/challenge1')
    def challenge1():
        sid = request.args.get('matrix-id')

        challenge = "THE MATRIX IS REAL GUYS|user=neo|password=neo_is_cool_yo|authlevel=5|CHALLENGE1"
        matrix_id = aes_encrypt(challenge, challenge1_key, codec='base64')

        if sid:
            try:
                ptext = aes_decrypt(sid, challenge1_key, codec='base64')
            except TypeError:
                error = "Caught exception during AES decryption..."
                return render_template('challenge1.html', matrix_id=matrix_id, error=error)

            # This is where we introduce a CBC padding oracle vulnerability
            padding_length = struct.unpack("B", ptext[-1])[0]
            good = (ptext[-padding_length:] == struct.pack("B", padding_length) * padding_length)

            if good is False:
                error = "Looks like you gave the wrong padding for your encrypted stuff"
                return render_template('challenge1.html', matrix_id=matrix_id, error=error)
            else:
                ptext = ptext[:-padding_length]
                print ptext

            try:
                role = ptext.split('|')[3][-1]
                print ptext.split('|')[3][-1]
            except IndexError:
                error = "Was not able to compute your authlevel. Please submit a valid matrix id."
                return render_template('challenge1.html', matrix_id=matrix_id, error=error)

            try:
                username, password = ptext.split('|')[1:3]
            except ValueError:
                error = "Was not able to locate username and password in given matrix id."
                return render_template('challenge1.html', matrix_id=matrix_id, error=error)

            if role == '0':
                return render_template('challenge1.html', flag=challenge1_flag)
            else:
                error = "Your authlevel is not 0. You will never be able to get access to the Matrix, Neo."
                return render_template('challenge1.html', matrix_id=matrix_id, error=error)

        else:
            return render_template('challenge1.html', matrix_id=matrix_id)

    @app.route('/challenge2')
    def challenge2():
        if AUTHENTICATE is True:
            c2 = cherrypy.request.cookie.get('c2')
            if not authorize(c2, CSAW_CRYPTO_2_KEY, CSAW_SIGNING_KEY, CSAW_CRYPTO_2_CHALLENGE_TOKEN):
                return self.index()

        if role is None:
            c2 = cherrypy.request.cookie.get('c2')
            if c2:
                role = c2.value
            else:
                token = aes_encrypt("CSAW 2010 CRYPTO #02|%s|%s|BLAHCHALLENGEAAAAA|role=5" % ('guest', 'guest'), CSAW_CRYPTO_2_KEY)
                cherrypy.response.cookie['c2'] = token
                return WELCOME_CHALLENGE_2

        # OK, we got this far..  they've passed the correct challenge token
        # this is a bit flipping challenge, so flip 1 bit to get role=0
        token = aes_decrypt(role, CSAW_CRYPTO_2_KEY)
        username, teamname, = token.split('|')[1:3]

        padding_length = struct.unpack("B", token[-1])[0]
        roleid = token[:-padding_length].rsplit('|', 1)[-1]


        if roleid[-1] == '0':
            if AUTHENTICATE is True:
                token = aes_encrypt_then_sign(CSAW_CRYPTO_3_CHALLENGE_TOKEN, CSAW_CRYPTO_3_KEY, CSAW_SIGNING_KEY)
                cherrypy.response.cookie['c3'] = token
            signature = e_b64(sign('guest', CSAW_SIGNING_KEY), '-', '_').rstrip('=').rstrip()

            return SUCCESS_CHALLENGE_2 % (e_html(username), e_html(teamname), CSAW_CRYPTO_2_FLAG, "guest", signature)
        else:
            return RETURNING_CHALLENGE_2 % (e_html(username), e_html(teamname), e_html(roleid[-1]))

        return render_template('challenge2.html')

    @app.route('/challenge3')
    def challenge3():
        return render_template('challenge3.html')
