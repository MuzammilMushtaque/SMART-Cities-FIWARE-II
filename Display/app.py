
# Extract the Outcomes of City-Weather from Fiware/Orion and Display in local host


# app.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

context_broker_url = 'http://host.docker.internal:1026'

latest_weather_status = {}

@app.route('/')
def index():
    # Get real-time weather data from Context Broker
    weather_data = get_weather_data()

    # Update global variable with latest weather status
    global latest_weather_status
    latest_weather_status = weather_data
    return render_template('index.html', weather_data=weather_data)

def get_weather_data():
    response = requests.get(f'{context_broker_url}/v2/entities?type=WeatherObserved')
    
    if response.status_code == 200:
        entities = response.json()
        weather_data = []

        for entity in entities:
            data = {
                'id': entity['id'],
                'ObservedTime' : entity.get('dateObserved', {}).get('value', 'Unknown'),
                'city' : entity.get('refDevice', {}).get('value', 'Unknown'),
                'temperature': entity.get('temperature', {}).get('value', 'Unknown'),
                'wind_speed': entity.get('windSpeed', {}).get('value', 'Unknown'),
                'humidity': entity.get('relativeHumidity', {}).get('value', 'Unknown'),
                'illuminance': entity.get('illuminance', {}).get('value', 'Unknown')
            }
            weather_data.append(data)
            
        # Sort the weather data based on observation time (assuming it's a valid ISO format)
        weather_data.sort(key=lambda x: x.get('ObservedTime'), reverse=True)
        print (weather_data)
        return weather_data
    else:
        return {}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')