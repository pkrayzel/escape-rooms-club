from flask import Flask, render_template

app = Flask(__name__)


@app.route("/exitgames.cz")
def home():
    return render_template("exitgamescz.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
