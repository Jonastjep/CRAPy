from flask import Flask, render_template, send_file, make_response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io, sqlite3

app = Flask(__name__)

conn = sqlite3.connect('../sensorData.db', check_same_thread=False)
curs = conn.cursor()

print("\n\nHOW TO START THE SENSOR WEB SERVER\n\n")

def queryLastData():
	conn = sqlite3.connect('../sensorData.db')
	curs = conn.cursor()
	for row in curs.execute("SELECT * FROM BMP280_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		temp = row[1]
		pres = row[2]
		alt = row[3]
	conn.close()
	return time, temp, pres, alt

def queryHistData(nbSamples):
	conn = sqlite3.connect('../sensorData.db')
	curs = conn.cursor()
	curs.execute("SELECT * FROM BMP280_data ORDER BY timestamp DESC LIMIT " + str(nbSamples))
	data = curs.fetchall()

	dates = []
	temps = []
	press = []
	alts = []

	for row in reversed(data):
		dates.append(row[0])
		temps.append(row[1])
		press.append(row[2])
		alts.append(row[3])
	conn.close()
	return dates, temps, press, alts

def maxRowsTable():
	conn = sqlite3.connect('../sensorData.db')
	curs = conn.cursor()
	for row in curs.execute("select COUNT(temp) from  BMP280_data"):
		maxNumberRows=row[0]
	conn.close()
	return maxNumberRows

global numSamples

numSamples = maxRowsTable()
if (numSamples > 101):
	numSamples = 100

@app.route('/')
def index():

	time, temp, pres, alt = queryLastData()
	templateData = {
		'time': time,
		'temperature': temp,
		'pressure': pres,
		'altitude': alt,
		'numSamples' : numSamples
	}

	return render_template('index.html', **templateData)

@app.route('/', methods=['POST'])
def my_form_post():
    global numSamples
    numSamples = int (request.form['numSamples'])
    numMaxSamples = maxRowsTable()
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples-1)
    time, temp, pres, alt = queryLastData()
    templateData = {
	  	'time'	: time,
      	'temperature'	: temp,
      	'pressure'	: pres,
		'altitude': alt,
      	'numSamples'	: numSamples
	}
    return render_template('index.html', **templateData)

@app.route('/plot/temp')
def plot_temp():
	times, temps, press, alts = queryHistData(numSamples)
	ys = temps
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.set_title("Temperature [C]")
	axis.set_xlabel("Samples")
	axis.grid(True)
	xs = range(numSamples)
	axis.plot(xs, ys)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	return response

@app.route('/plot/pres')
def plot_pres():
	times, temps, press, alts = queryHistData(numSamples)
	ys = press
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.set_title("Pressure [Pa]")
	axis.set_xlabel("Samples")
	axis.grid(True)
	xs = range(numSamples)
	axis.plot(xs, ys)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	return response

@app.route('/plot/alt')
def plot_alt():
	times, temps, press, alts = queryHistData(numSamples)
	ys = alts
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.set_title("Altitude [m]")
	axis.set_xlabel("Samples")
	axis.grid(True)
	xs = range(numSamples)
	axis.plot(xs, ys)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	return response

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
