from flask import Flask, render_template, request, render_template_string
import bjoern
import os

app = Flask(__name__)
blacklist = {{blacklist}}

story = {
    "title": "A Spooky Campfire Story",
    "blanks": [
        "adjective",
        "adjective",
        "number",
        "adjective",
        "animal",
        "noun",
        "animal",
        "name",
        "verb",
        "adjective",
        "adjective"
    ],
    "value": [
        "Every summer, I get totally amped and ",
        " to go camping in the deep, ",
        " forests. It's good to get away from it all - but not too far, like getting lost! Last year, my friend and I went hiking and got lost for ",
        " hour(s). We started off on a(n) ",
        " adventure, but we kept losing the trail. Night began to fall, and when we heard the howls of a ",
        ", we began to panic. It was getting darker and our flashlights were running on ",
        ". I'm sure glad my pet ",
        ", ",
        ", was with us. He is one gifted creature, because he was able to guide us back by ",
        " the ",
        " s'mores by the campfire. This year, before setting off on an ",
        " journey, I'll be sure to have working flashlights - and of course, my gifted pet!"
    ]
}


@app.route('/')
def index():
    return render_template("index.html", blanks=story["blanks"])


@app.route('/madlib',  methods=["POST"])
def gen_mad_lib():
    vals = list(request.form.to_dict().values())
    base = story["value"]
    if len(vals) != len(base) - 1:
        return "Too many or not enough blanks!"
    formatted = [base[i] + vals[i] for i in range(len(base) - 1)]
    text = "".join(formatted) + base[-1]
    for block in blacklist:
        if block in text:
            return "<h1>HACKER ATTEMPT DETECTED!!!</h1>"
    with open("/app/templates/mad_lib.html", 'r') as f:
        mad_lib = f.read()
        mad_lib = mad_lib.replace("madlib", text)
    return render_template_string(mad_lib, title=story["title"])

if __name__ == '__main__':
    os.chdir('/app')
    bjoern.run(app, "127.0.0.1", 5000)
