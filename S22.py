import requests

def get_ip_info(ip_addresses, save_to_file=False, filename="ip_info.txt"):
    results = []

    for ip in ip_addresses:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip.strip()}")
            data = response.json()

            if data['status'] == 'success':
                info = (
                    f"🌍 IP: {ip}\n"
                    f"🗺️ Страна: {data['country']}\n"
                    f"🏙️ Город: {data['city']}\n"
                    f"🛰️ Провайдер: {data['isp']}\n"
                    f"🧭 Координаты: {data['lat']}, {data['lon']}\n"
                    "------------------------------"
                )
            else:
                info = f"❌ Не удалось определить данные для IP: {ip}\n------------------------------"
        except Exception as e:
            info = f"⚠️ Ошибка для IP {ip}: {e}\n------------------------------"

        print(info)
        results.append(info)

    if save_to_file:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(results))
        print(f"\n📁 Результаты сохранены в файл: {filename}")

# 🔹 Запрос IP-адресов у пользователя
user_input = input("Введите один или несколько IP-адресов через запятую: ")
ip_list = user_input.split(',')

# 🔹 Вызываем функцию
get_ip_info(ip_list, save_to_file=True)