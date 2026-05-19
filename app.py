from flask import Flask, render_template_string, request, redirect, url_for
import Jetson.GPIO as GPIO
import time

app = Flask (__name__)

# --- Hardware Configurastion ---
RPWM_PIN = 11 # Physical Board Pin 32 (Controls the fan speed via the HW-039
DHT_PIN = 12 # Physical Board Pin 12 (Data pin for DHT11)

# --- Initialize GPIO settings ---
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RPWM_PIN, GPIO.OUT)

# --- Initialize PWM on Pin 32 at 490Hz (Standard frequency for motor drivers)
GPIO.setup(RPWM_PIN, GPIO.OUT, initial=GPIO.LOW)

# --- Global Variables ---
target_temp = 24.0 # Defailt threshold temperature temperature in Celcius
current_temp = 22.0 # Default starting room temp placeholder\
fan_status = "OFF"

def read_dht11_basic():
	# For initial testing, this returns a stable baseline reading.
	# To implement raw reading: replace with a dedicated library like Adafruit_DHT
	return 23.5

def update_thermostat():
    global current_temp, target_temp, fan_status
    current_temp = read_dht11_basic()

    if current_temp > target_temp:
        #  Use GPIO.output instead of fan_pwm
        GPIO.output(RPWM_PIN, GPIO.HIGH)
        fan_status = "ON (Cooling)"
    else:
        #  Use GPIO.output instead of fan_pwm
        GPIO.output(RPWM_PIN, GPIO.LOW)
        fan_status = "OFF"

# --- HTML INTERFACE FOR YOUR PHONE ---
HTML_UI = """
<!DOCTYPE html>
<html>
<head>
	<title> Jetson Smart Thermostat</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
		body { font-family: 'Seoge UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background-color:#eef2f3; color:#333; margin: 0; padding: 20px;}
		.container {background: white; max-inline-size: 400px; margin:40px auto; padding: 30px; border-radius:15px; box-shadow:0 8px 16px rgba(0,0,0,0.1;}
		h1 { color:#007bff; margin-bottom:20px;}
		.metric { font-size: 1.2rem; margin:15px 0; }
		.highlight {font-weight:bold; font-size: 1.5rem; color:#2c3e50; }
		.status-on {color:#d9534f; font-weight: bold; }
		.status-off { color:#5cb85c; font-weight: bold; }
		input[type=number] {padding:10px; font-size: 1.2rem; incline-size: 10px; text-align: center; border: 2px solid #ccc border-radius: 5px; margin-bottom 20px; }
		button { padding: 12px 24px; font-size: 1.1rem; background-color:#007bff; color: white; border: none; border-radius: 5px; pointer; transition: 0.2s; }
		button:hover {background-color:#0056b3;}
	</style>
</head>
<body>
	<div class="container">
		<h1> Jetson Thermostat </h1>
		<div class = "metric"> Current Room: <span class="highlight">{{ current_temp }}C</span></div>
		<div class = "metric"> Target Limit: <span class="highlight">{{ target_temp }}C</span></div>
		<div class = "metric">Fan State:
			<span class="{{ 'status-on' if 'ON' in fan_status else 'status-off' }}">{{ fan_status }}</span>
		</div>
		<hr style="border: 0; border-top: 1px solid#eee; margin: 20px 0;">
		<form action="/update" method="POST">
			<label style="font-size: 1rem; display: block; margin-bottom: 10px;"> Set New Target Temp (C):</label>
			<input type="number" step="0.5" name="new_target" value="{{ target_temp}}"><br>
			<button type="submit">Update Thermostat</button>
		</form>
	</div>
</body>
</html>
"""

@app.route('/')
def home():
	update_thermostat()
	return render_template_string(HTML_UI, current_temp=current_temp,target_temp=target_temp, fan_status=fan_status)

@app.route('/update', methods=['POST'])
def update_settings():
	global target_temp
	try:
		target_temp = float(request.form['new_target'])
	except ValueError:
		pass
	return redirect(url_for('home'))

if __name__ == '__main__':
	try:
		# Run the server on port 5000 and allow connections from any local IP (0.0.0.0)
		app.run(host='0.0.0.0', port=5000, debug=False)
	finally:
		# Safely reset to turn off the fan if the script gets terminated
		GPIO.cleanup()
