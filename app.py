
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Docker Demo", message="Hello from Python!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
