import requests
from rich.table import Table
from rich.console import Console
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

city = input("Enter a City: ")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial")
data = response.json()  # converts JSON response to a Python dictionary


# print(temperature)
# print(data['weather'][0]['description'])
# print(data['main']['feels_like'])
# print(data['main']['humidity'])


if response.status_code == 200:
    data = response.json()
    temperature = f"{round(data['main']['temp'],1)}°F"
    condition = data['weather'][0]['description']
    feels_like = f"{round(data['main']['feels_like'],1)}°F"
    humidity = f"{round(data['main']['humidity'],1)}%"
    console = Console()
    table = Table(title="Weather")

    table.add_column("City")
    table.add_column("Description")
    table.add_column("Temperature")
    table.add_column("Feels Like")
    table.add_column("Humidity")
    table.add_row(str(city),
                  str(condition),
                  str(temperature),
                  str(feels_like),
                  str(humidity)
                  )
    
    console.print(table)

# City        │ Austin, US          │
 #   │ Condition   │ Clear Sky           │
  #  │ Temperature │ 95.2°F              │
  #  │ Feels Like  │ 102.1°F             │
  #  │ Humidity    │ 45%  
#