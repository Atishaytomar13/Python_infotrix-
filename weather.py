import json,sys,requests
if len(sys.argv)<2:
    print("Usage : weather.py location")
    sys.exit()
location = ' '.join(sys.argv[1:])
url = "https://www.weatherapi.com/my/"%location 
response=requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)

data = weatherData['weather']
print('Current weather in %s:' % (location))
print(data[0]['main'], "-", data[0]['description'])

temp = weatherData['main']
print('Temperaure is: ', temp['temp']-273.15,"Celcius")
print()



