from flask import Flask
from flask import render_template, request
app = Flask(__name__)

import os
from convert_sqlite_into_json import sqliteToJson

@app.route('/')
def Sensors():
#This creates a json file where to store the data from the sqlite database
    sqliteToJson("templates/", "ArduinoData.db")
    return render_template('index.html')

# @app.route('/', methods=['POST'])
# def Sensors_form():
#     numSamples = int(request.form['numSamples'])
# #This creates a json file where to store the data from the sqlite database
#     sqliteToJson("templates/", "ArduinoData.db", numSamples)
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
