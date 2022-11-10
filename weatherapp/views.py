from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&d').read()
        json_data = json.loads(res)
        data = {
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+', '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+' K (Kelvin)',
            "pressure":str(json_data['main']['pressure'])+' hPa',
            "clouds":str(json_data['weather'][0]['description']),
            "wind":str(json_data['wind']['speed'])+' M/H',
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data':data})

