import requests
import os
api_key = '18616573f23bd8bf0bec23c5f68e32a3'
def get_current_weather(city='enugu'):
    

    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={api_key}&q={city}&units=metric'
# print(request_url)

    weather_data = requests.get(request_url).json()
    return weather_data
# if city not in weather_data:
    

    # pprint(weather_data)
    
    # pprint(weather_data)


        # print(f'The weather focus of {city}\n')
        # print(f'The Temp is: {weather_data["main"]["temp"]}¤c')
        # print(f'Feels like: {weather_data["main"]["feels_like"]}')
        # print(f"Country: {weather_data['sys']['country']}")
    # data = weather_data['weather']
        # print(f"Description: {weather_data['weather'][0]['description']}")

if __name__ == '__main__':

    print('\n ***get current weather data***' )
    city = input('input your city: ').strip()
    if not bool(city.strip()):
        city = 'enugu'
    
    weather_data = get_current_weather(city)
    print()
    print(weather_data)