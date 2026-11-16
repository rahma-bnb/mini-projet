import os

from flask import Flask

app = Flask(__name__)

MESSAGE = os.environ.get("MESSAGE", "Bonjour depuis un conteneur Docker !")


@app.route("/")
def accueil():
    return MESSAGE + "\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
