import requests

def getLatLon(location):
    """
    Uses the "Google-style geocoder" API at datasciencetoolkit.org to return the latitude and longitude for a location
    """
    url = 'http://www.datasciencetoolkit.org/maps/api/geocode/json?sensor=false&address='
    response = requests.get(url+location)
    location = response.json()['results'][0]['geometry']['location']
    return (location['lat'], location['lng'])

def getWeather(date, latlon):
    """
    Use the Historical API at worldweatheronline.com to return weather conditions for a latlon and date.
    """
    url = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=e13196bad2ce4aec9f2213413162603&q={latlon}&format=json&date={date}&tp=24'
    response = requests.get(url.format(latlon=str(latlon)[1:-1], date=date.strftime('%Y-%m-%d')))
    return response.json()