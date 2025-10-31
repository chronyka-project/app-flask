from flask import Flask, render_template
import os

app = Flask(__name__)
app.debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"

@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/contato.html")
def contato():
    return render_template('contato.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
