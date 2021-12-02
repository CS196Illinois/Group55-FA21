from flask import Flask, request, render_template
from flask import Flask

# from Project.frontend.backend import generate_daily_agenda
from backend import generate_daily_agenda, extract_course_data, organize_classes, convert_times_and_sort_days, convert_to_datetime, finalClasses
import folium
app = Flask(__name__)

from geopy.geocoders import Nominatim
geocoder = Nominatim(user_agent = app)
# @app.route("/")
# def base():
#   map = folium.Map(
#     width=500,height=500, location=[45, -122]
#   )
#   return map._repr_html_()

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
  if (len(request.form['crn6']) == 5):
    crns.append(request.form['crn6'])
  if (len(request.form['crn7']) == 5):
    crns.append(request.form['crn7'])
  if (len(request.form['crn8']) == 5):
    crns.append(request.form['crn8'])
  
  if len(crns) > 0:
    test = finalClasses(crns)
    # '59821', '75111', '73308', '75272', '48924', '70667', '62829', '57971'
    print(test)
    # location = geocode("Bevier Hall UIUC")
    # print(location)
    map = folium.Map(
    width=1000,height=1000, location=[45, -122]
    )
    loc = [(40.720, -73.993),
       (27.205, 77.498)]
    folium.PolyLine(loc,
                color='red',
                weight=15,
                opacity=0.8).add_to(map)
    return map._repr_html_()
    # return render_template('enterCRN.html', test = test, crns = crns) #, map._repr_html_()
    
  else: 
    return render_template('enterCRN.html')