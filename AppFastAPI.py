from fastapi import FastAPI, Request
import requests

app = FastAPI()

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

@app.get("/get-ip-location")
async def get_ip_location(request: Request):
    client_ip = request.client.host
    location = get_location_from_ip(client_ip)
    return location

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,  port=5356)
