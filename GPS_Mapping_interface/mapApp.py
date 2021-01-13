from flask import Flask
from flask import render_template, request
app = Flask(__name__)

import os
from dataProcessing import sqliteToJson

@app.route('/')
def map():
    #This creates the json file that the script will use when rendered
    sqliteToJson("static/", "GPS_data.db")
    return render_template('index.html')

@app.route('/', methods=['POST'])
def map_form():
    numSamples = int (request.form['numSamples'])
    #This creates the json file that the script will use when rendered
    sqliteToJson("static/", "GPS_data.db",numSamples)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
