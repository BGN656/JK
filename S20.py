import psutil
import time
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn

console = Console()

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery is None:
        return None
    return {
        "percent": battery.percent,
        "plugged": battery.power_plugged,
        "secsleft": battery.secsleft
    }

def format_time(seconds):
    if seconds == psutil.POWER_TIME_UNLIMITED:
        return "∞"
    elif seconds == psutil.POWER_TIME_UNKNOWN:
        return "??"
    else:
        h = seconds // 3600
        m = (seconds % 3600) // 60
        return f"{h} ч {m} мин"

while True:
    status = get_battery_status()
    if not status:
        console.print("[bold red]Батарея не найдена.[/bold red]")
        break

    percent = status["percent"]
    plugged = status["plugged"]
    time_left = format_time(status["secsleft"])
    state = "🔌 На зарядке" if plugged else "🔋 На батарее"

    console.clear()
    console.rule("[bold green] Монитор батареи [/bold green]")
    with Progress(
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        BarColumn(bar_width=40),
        TextColumn(f"{state} | Осталось: {time_left}"),
    ) as progress:
        task = progress.add_task("Батарея", total=100, completed=percent)
        time.sleep(2)