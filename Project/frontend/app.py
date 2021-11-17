from flask import Flask, request, render_template

from backend import getSchedule


app = Flask(__name__)

@app.route("/")
def main():
  return render_template('enterCRN.html', test = "")
@app.route("/", methods=['post'])
def firstPagePost():
    
  crns = []
  if (len(request.form['crn1']) == 5):
    crns.append(request.form['crn1'])
  if (len(request.form['crn2']) == 5):
    crns.append(request.form['crn2'])
  if (len(request.form['crn3']) == 5):
    crns.append(request.form['crn3'])
  if (len(request.form['crn4']) == 5):
    crns.append(request.form['crn4'])
  if (len(request.form['crn5']) == 5):
    crns.append(request.form['crn5'])
  
  
  if len(crns) > 0:
    test = getSchedule(crns)
    return render_template('enterCRN.html', test=test, crns = crns)
  else: 
    return render_template('enterCRN.html')