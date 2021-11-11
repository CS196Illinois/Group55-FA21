from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def main():
  return render_template('enterCRN.html')
@app.route("/", methods=['post'])
def firstPagePost():
    crn1=request.form['crn1'] 
    crn2=request.form['crn2']
    crn3=request.form['crn3']
    crn4=request.form['crn4']
    crn5=request.form['crn5']
    return render_template('enterCRN.html', crn1=crn1, crn2=crn2, crn3=crn3,
        crn4=crn4, crn5=crn5, product=int(crn1)*int(crn2)*int(crn3)*int(crn4)*int(crn5))