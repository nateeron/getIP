import socket
import os
import platform

def get_ip_addresses():
    ip_list = []
    if platform.system() == "Windows":
        # Windows implementation
        hostname = socket.gethostname()
        ip_list.append(socket.gethostbyname(hostname))
        ip_list.append(socket.gethostbyname_ex(hostname))
    else:
        # Unix/Linux implementation
        for interface in os.listdir('/sys/class/net/'):
            try:
                ipv4 = socket.gethostbyname(interface)
                ip_list.append(ipv4)
            except socket.gaierror:
                pass
            
            try:
                ipv6 = socket.getaddrinfo(interface, None, socket.AF_INET6)
                for addr in ipv6:
                    ip_list.append(addr[4][0])
            except socket.gaierror:
                pass

    return ip_list


    
    

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
  
ip_addresses = get_ip_addresses()
for ip in ip_addresses:
    print(ip)

d = get_location_from_ip('172.23.128.1')
print(d)