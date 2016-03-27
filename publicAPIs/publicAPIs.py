import requests
import datetime

def getLatLon(location):
    """
    Uses the "Google-style geocoder" API at datasciencetoolkit.org to return the latitude and longitude for a location
    """
    if not isinstance(location, str):
        raise ValueError
    url = 'http://www.datasciencetoolkit.org/maps/api/geocode/json?sensor=false&address='
    response = requests.get(url+location)
    location = response.json()['results'][0]['geometry']['location']
    return (location['lat'], location['lng'])

def getWeather(date, latlon):
    """
    Use the Historical API at worldweatheronline.com to return weather conditions for a latlon and date.
    """
    #todo: Handle case when API call returns an error
    if not isinstance(date, datetime.datetime) or not isinstance(latlon, tuple):
        raise ValueError
    elif not isinstance(latlon[0], float) or not isinstance(latlon[1], float):
        raise ValueError
    url = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=e13196bad2ce4aec9f2213413162603&q={latlon}&format=json&date={date}&tp=24'
    response = requests.get(url.format(latlon=str(latlon)[1:-1], date=date.strftime('%Y-%m-%d')))
    return response.json()
