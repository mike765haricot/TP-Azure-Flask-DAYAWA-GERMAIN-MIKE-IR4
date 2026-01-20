from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "C'est incroyable ! La mise à jour est automatique !"