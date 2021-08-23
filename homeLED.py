import RPi.GPIO as GPIO
from flask import Flask, render_template
app=Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pins={
	23 : {'name':'Red LED', 'state':GPIO.LOW},
	24 : {'name':'Yellow LED', 'state':GPIO.LOW},
	25 : {'name':'Green LED', 'state':GPIO.LOW}
	}
	
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
	for pin in pins:
		pins[pin]['state']=GPIO.input(pin)
		
	templateData{ 'pins' : pins}
	return render_template('homeLED.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
	changePin = int(changePin)
	deviceName=pins[changePin]['name']
	
	if action=='on':
		GPIO.output(changePin, GPIO.HIGH)
	if action=='off':
		GPIO.output(changePin, GPIO.LOW)
	
	pins[changePin]['state'] = GPIO.input(changePin)
	
	templateData = {'pins' : pins}
	return render_template('homeLED.html', **templateData)
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=False)
