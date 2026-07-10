import requests
from rich.table import Table
from rich.console import Console


console = Console()
table = Table(title="Route Performance")
table.add_column("Name")
table.add_column("Spacecraft")

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()  # converts JSON response to a Python dictionary
people = data["people"]


if response.status_code == 200:
    data = response.json()
    console = Console()
    table = Table(title="🚀 Current ISS Crew")
    table.add_column("Astronaut Name")
    table.add_column("Spacecraft")


    for person in people:
     table.add_row(
        str(person['name']),
        str(person['craft']),
    )
    total_crew = len(people)
        


    console.print(table)
    print(f"Total Crew: {total_crew}")

    
    
else:
    print(f"Error: {response.status_code}")

# for data in people:
#     print(f"{data['name']}")
#     print(f"{data['craft']}")

