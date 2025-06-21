from datetime import datetime, timedelta

def generate_schedule(tasks, start_time, duration_per_task):
    """Создает расписание задач."""
    schedule = []
    current_time = start_time


    for task in tasks:
        end_time = current_time + timedelta(minutes=duration_per_task)
        schedule.append({"task": task, "start": current_time, "end": end_time})
        current_time = end_time

    return schedule

def display_schedule(schedule):
    """Выводит расписание."""
    print("\nВаше расписание:")
    for item in schedule:
        print(f"{item['start'].strftime('%H:%M')} - {item['end'].strftime('%H:%M')} | {item['task']}")

if __name__ == "__main__":
    print("Генератор расписания задач")

    tasks = []
    print("Введите задачи (введите 'готово', чтобы завершить):")
    while True:
        task = input("Задача: ").strip()
        if task.lower() == "готово":
            break
        tasks.append(task)



    if not tasks:
        print("Нет задач для составления расписания.")
    else:
        start_time_input = input("Введите время начала (в формате ЧЧ:ММ): ").strip()
        duration_per_task = int(input("Введите длительность одной задачи (в минутах): "))

        start_time = datetime.strptime(start_time_input, "%H:%M")
        schedule = generate_schedule(tasks, start_time, duration_per_task)

        display_schedule(schedule)