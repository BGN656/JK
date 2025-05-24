import requests

API_URL = "https://restcountries.com/v3.1/name"


def get_country_info(country_name):
    """Получает информацию о стране из REST Countries API."""
    try:
        response = requests.get(f"{API_URL}/{country_name}")
        if response.status_code == 200:
            data = response.json()[0]  # Получаем первый результат
            name = data.get("name", {}).get("common", "Неизвестно")
            capital = ", ".join(data.get("capital", ["Нет столицы"]))
            population = data.get("population", "Нет данных")
            area = data.get("area", "Нет данных")
            currencies = ", ".join(data.get("currencies", {}).keys())
            region = data.get("region", "Нет данных")
            print(f"\nИнформация о стране '{name}':")1
            print(f"Столица: {capital}")
            print(f"Население: {population}")
            print(f"Площадь: {area} км²")
            print(f"Регион: {region}")
            print(f"Валюты: {currencies}")
        else:
            print("Страна не найдена. Проверьте правильность ввода.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    print("Программа: Информация о странах")
    while True:
        print("\nМеню:")
        print("1. Получить информацию о стране")
        print("2. Выйти")
        choice = input("Выберите действие (1-2): ").strip()

        if choice == "1":
            country_name = input("Введите название страны (на английском): ").strip().lower()
            get_country_info(country_name)
        elif choice == "2":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")