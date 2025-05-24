import requests

def get_weather(city):
    """Получает текущую погоду для заданного города."""
    try:
        # Получение координат города
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url).json()
        if "results" not in geo_response:
            return f"Город '{city}' не найден."

        location = geo_response["results"][0]
        lat, lon = location["latitude"], location["longitude"]

        # Получение данных о погоде
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url).json()

        current_weather = weather_response["current_weather"]
        temperature = current_weather["temperature"]
        windspeed = current_weather["windspeed"]

        return (f"Погода в {city}:\n"
                f"- Температура: {temperature}°C\n"
                f"- Скорость ветра: {windspeed} м/с")
    except Exception as e:
        return f"Ошибка при получении данных: {e}"

if __name__ == "__main__":
    print("Программа для получения текущей погоды")
    while True:
        city = input("\nВведите название города (или 'выход' для завершения): ").strip()
        if city.lower() == "выход":
            print("До свидания!")
            break
        print(get_weather(city))