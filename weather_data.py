import requests
from datetime import datetime
import json
import random
import time

def collect_current_weather(api_key, city):
    base_url_current = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }
    response_current = requests.get(base_url_current, params=params)
    response_current.raise_for_status()
    data_current = response_current.json()
    
    entity_type = 'WeatherObserved'
    entity_id = f'WeatherObserved_{city}_{datetime.utcnow().isoformat()}'
   # print (entity_id)
    data = {
        'entity_type' : entity_type,
        'entity_id' : entity_id,
        'temperature': data_current['main']['temp'],
        'description': data_current['weather'][0]['description'],
        'humidity' : data_current['main']['humidity'],
        'wind_speed' : data_current['wind']['speed'],
        'visibility' : data_current['visibility'],
        'City' : city,
        'timestamp': datetime.utcfromtimestamp(data_current['dt']).isoformat() + 'Z'
    }
    return data

def send_to_context_broker(data):
    context_broker_url = "http://host.docker.internal:1026/v2/entities"
    headers = {'Content-Type': 'application/json'}
    
   # print (data)
   # print (data['entity_type'], data['temperature'], data['humidity'])

    payload = {
        'id': data['entity_id'],
        'type': data['entity_type'],
        'dateObserved': {
            'type':'DateTime',
            'value': data['timestamp']
        },
        'temperature': {
            'type': 'Number',
            'value': data['temperature']
        },
        'illuminance' : {
            'type':'Number',
            'value':data['visibility']
        },
        'windSpeed': {
            'type': 'Number',
            'value': data['wind_speed'] 
        },
        'relativeHumidity':{
            'type':'Number',
            'value':data['humidity']
        },
        'refDevice': {
            'type':'Text',
            'value': data['City']
        }
    }

    response = requests.post(context_broker_url, headers=headers, json=payload)
    response.raise_for_status()

    print(f"Data successfully sent to Context Broker. Status Code: {response.status_code}")
    
if __name__ == "__main__":
    repeat = True
    while repeat == True:
        city = random.choice(['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt', 'Stuttgart', 'Dusseldorf', 'Dortmund', 'Essen', 'Leipzig', 'Bremen', 'Dresden', 'Hanover', 'Nuremberg', 'Duisburg', 'Bochum', 'Wuppertal', 'Bielefeld', 'Bonn', 'Mannheim'])
        api_key = '85022880d97158c9a587d3d0e509ff82'
       # city = input('Write the name of City (default: Berlin): ') or 'Berlin'
        send_to_context_broker(collect_current_weather(api_key, city))
        repeat = True
        time.sleep(5)