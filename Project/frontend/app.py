from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def main():
  return render_template('enterCRN.html', test = "")
@app.route("/", methods=['post'])
def firstPagePost():
    
  crns = []
  crns.append(request.form['crn1'])
  crns.append(request.form['crn2'])
  crns.append(request.form['crn3'])
  crns.append(request.form['crn4'])
  crns.append(request.form['crn5'])
  days = {'M': [['09:00AM - 09:50AM', '149 National Soybean Res Ctr'],
  ['12:00PM - 12:50PM', '112 Gregory Hall'],
  ['10:00AM - 10:50AM', '4029 Campus Instructional Facility'],
  ['13:00PM - 14:50PM', '325 David Kinley Hall']],
 'T': [['14:00PM - 15:20PM', '8 ACES Lib, Info & Alum Ctr']],
 'W': [['12:00PM - 12:50PM', '112 Gregory Hall'],
  ['10:00AM - 10:50AM', '4029 Campus Instructional Facility'],
  ['13:00PM - 14:50PM', '325 David Kinley Hall']],
 'R': [['14:00PM - 15:20PM', '8 ACES Lib, Info & Alum Ctr']],
 'F': [['10:00AM - 10:50AM', '4029 Campus Instructional Facility'],
  ['13:00PM - 14:50PM', '325 David Kinley Hall']]}
  test = str(days)
  return render_template('enterCRN.html', test=test, crns = crns)