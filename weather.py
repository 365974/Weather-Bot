import requests

def get_weather(city="Москва"):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["current_condition"][0]["temp_C"]
        weather_desc = data["current_condition"][0]["weatherDesc"][0]["value"]
        return f"Погода в {city}: {temp}°C, {weather_desc}"
    else:
        return "Ошибка получения данных"

if __name__ == "__main__":
    city = input("Введите название города: ")
    print(get_weather(city))
