from flask import Flask, request, jsonify, render_template
import geoip2.database

app = Flask(__name__)
reader = geoip2.database.Reader('path/to/GeoLite2-City.mmdb')  # Replace with your database path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_ip_location():
    # Get the client IP address
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr
    
    # Get location from IP using GeoIP2 database
    try:
        response = reader.city(client_ip)
        city = response.city.name
        country = response.country.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        location = f'{city}, {country} ({latitude}, {longitude})'
    except geoip2.errors.AddressNotFoundError:
        location = 'Location not found'

    # Construct Google Maps URL
    google_maps_url = f'https://www.google.com/maps/search/?api=1&query={latitude},{longitude}'

    return jsonify({'location': location, 'google_maps_url': google_maps_url})

if __name__ == '__main__':
    app.run(debug=True)
