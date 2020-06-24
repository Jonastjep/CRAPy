from flask import Flask, render_template
import serial

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600)

@app.route('/')
def index():
	data = ser.readline().decode("utf-8")
	parse = data.split(",")
	templateData = {
		'temperature': parse[0],
		'pressure': parse[1],
		'altitude': parse[2]
	}

	return render_template('index.html', **templateData)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
