from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def firstPage():
  return render_template('enterCRN.html')
@app.route("/login")
def index():
    return render_template('index.html')

