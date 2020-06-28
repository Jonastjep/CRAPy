from flask import Flask, render_template
app = Flask(__name__)
import sqlite3

def getData():
  latitudes = list()
  longitudes = list()
  altitudes =list()
  conn=sqlite3.connect('C:/webenvironment/gpsdata.db')
  curs=conn.cursor()
  for row in curs.execute('SELECT * FROM GPSDATA'):
    latitudes.append(row[0])
    longitudes.append(row[1])
    altitudes.append(row[2])
    
    
  conn.close()
  return latitudes, longitudes, altitudes
  
  
@app.route("/")
def index():
  latitudes, longitudes, altitudes = getData()
  templateData = {'latitudes': latitudes, 'longitudes': longitudes,'altitudes': altitudes}
  return render_template('index.html', templateData=templateData)    
		
if __name__ == "__main__":
  app.run(debug=True)