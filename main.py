import requests
s_city = "Moscow,RU" 
appid = "bfdc10344674be68fcf7cd914d4a89dc"
endpoint = "http://api.openweathermap.org/data/2.5"
params = {
        'q': s_city,
        'units': 'metric',
        'lang': 'ru',
        'appid': appid
    }

data = requests.get(f"{endpoint}/weather", params = params).json()

print(f"Город: {s_city}")
print(f"Погодные условия: {data['weather'][0]['description']}")
print(f"Температура: {data['main']['temp']}")
print(f"Минимальная температура: {data['main']['temp_min']}")
print(f"Максимальная температура: {data['main']['temp_max']}")
print(f"Видимость: {data['visibility']}")
print(f"Скорость ветра: {data['wind']['speed']}")

data = requests.get(f"{endpoint}/forecast", params = params).json()

print("\nПрогноз погоды на неделю:")
for i in data['list']:
    print(f"Дата: {i['dt_txt']}")
    print(f"Температура: {int(i['main']['temp'])}")
    print(f"Погодные условия: {i['weather'][0]['description']}")
    print(f"Видимость: {i['visibility']}")
    print(f"Скорость ветра: {i['wind']['speed']}")
    print("____________________________")