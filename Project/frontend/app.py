from flask import Flask, request, render_template
from flask import Flask
# from Project.frontend.backend import generate_daily_agenda
from backend import generate_daily_agenda, extract_course_data, organize_classes, convert_times_and_sort_days, convert_to_datetime


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
    course_data = extract_course_data(crns)
    days = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
    classes = generate_daily_agenda(days, course_data)
    sorted_day = {}
    classes_datetime = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
    test = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
    convert_times_and_sort_days(days, sorted_day)
    convert_to_datetime(classes_datetime)
    organize_classes(test, classes_datetime)

    return render_template('enterCRN.html', test = test, crns = crns)
  else: 
    return render_template('enterCRN.html')