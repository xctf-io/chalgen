from flask import Flask, render_template, request
import hashlib
import urllib
import os


secret = b"supersecretkeyyoucantguess"
files = os.popen('ls files').read().split('\n')[:-1]
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/',  methods=["POST"])
def get_file():
    raw_data = request.get_data().decode()
    if len(raw_data) > 200:
        return "Sent too much data!"
    files_raw, sig_raw = raw_data.split('&')
    files_params = files_raw.split('=')
    sig_params = sig_raw.split('=')
    if files_params[0] != 'files':
        return "Missing files parameter!"
    if sig_params[0] != 'sig':
        return "Missing sig parameter!"
    files_bytes = urllib.parse.unquote_to_bytes(files_params[1])
    sig = sig_params[1]
    file_hash = hashlib.sha1(secret + files_bytes).hexdigest()
    if file_hash == sig:
        result = ""
        requested_files = []
        last = 0
        for i,val in enumerate(files_bytes):
            if val == ord('|'):
                requested_files.append(files_bytes[last:i])
                last = i + 1
        requested_files.append(files_bytes[last:])
        for file in requested_files:
            for f in files:
                if f.encode() == file:
                    result += open("files/" + f).read() + '\n\n'
                    break
            else:
                result += "Invalid file\n\n"
        return render_template('index.html', result=result)
    else:
        return "Invalid signature!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
