import requests



def getCityWeather(city:str):
    url = "https://api.openweathermap.org/data/2.5/weather"

    response = requests.get(url, params=dict(q=city, appId="f3c9d54664509651fe2371e7bfe9b3f8"))
    if response.status_code == 200:
        return response.json()
    print(response.text)
    return 
while True:
    city = str(input("Enter city name: "))
    print(getCityWeather(city).get("weather")[0])