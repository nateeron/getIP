from flask import Flask, request, jsonify, redirect, url_for
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

def get_location_from_ip(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        data = response.json()

        if data['status'] == 'success':
            location_info = {
                'country': data['country'],
                'region': data['regionName'],
                'city': data['city'],
                'zip': data['zip'],
                'lat': data['lat'],
                'lon': data['lon'],
                'timezone': data['timezone'],
                'isp': data['isp'],
                'org': data['org'],
                'as': data['as']
            }
            return location_info
        else:
            return {'error': 'Failed to get location information'}

    except Exception as e:
        return {'error': str(e)}

@app.route('/', methods=['GET'])
def run():
  
    return "OK Run..."


@app.route('/get', methods=['GET'])
def get_ip_location():
        # Get the client IP address
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr
  
    location = get_location_from_ip(client_ip)
    # Construct Google Maps URL
    google_maps_url = f'https://www.google.com/maps/search/?api=1&query={location}'

    return jsonify({'location': location, 'google_maps_url': google_maps_url})

if __name__ == '__main__':
    app.run(debug=True)

