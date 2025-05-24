import python_weather

import asyncio
import os

def f_to_celsius(temp):
    return round((temp - 32) * 5/9, 2)
async def getweather(city) -> None:

    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(city)

        print(f"Температура в {city} - {f_to_celsius(weather.temperature)} C")

        for daily in weather:
            print(f"========={daily}==========")

            # hourly forecasts
            for hourly in daily:
                print(f' --> {hourly!r}')


if __name__ == '__main__':
       if os.name == 'nt':
          asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
city = input('Enter city: ')
asyncio.run(getweather(city))
