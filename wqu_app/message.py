import requests
def get_ip_address():
    '''Return IP address of our computer'''
    response = requests.get('https://api.ipify.org')
    
    return response.text
    
def get_geo_location(ip_address):
    '''Return geolocation of given IP address'''
    response = requests.get(f'http://ipinfo.io/{ip_address}')
    data = response.json()
    return [float(coord) for coord in data['loc'].split(',')]

def get_weather_data(coords):
    '''Return weather data for given geolocation'''
    url = (f'http://www.7timer.info/bin/api.pl?lon={coords[0]}&lat={coords[1]}&product=astro&output=json')
    response = requests.get(url)
    data = response.json()
    return data['dataseries'][0]['temp2m']

def greet():
    ip_address = get_ip_address()
    coords = get_geo_location(ip_address)
    temp = get_weather_data(coords)
    
    return f'Hello, tempeature is {temp} deg C'

if __name__=='__main__':
    print(greet())