from rich.table import Table
from rich.console import Console
from route import Route

console = Console()
table = Table(title="Route Performance")
table.add_column("Route")
table.add_column("Trips")
table.add_column("On Time")
table.add_column("Percentage")


routes = [
    Route("Route 101", 60, 50),
    Route("Route 202", 80, 60),
    Route("Route 302", 70, 30),
    Route("Route 402", 60, 40),
]

for route in routes:
    table.add_row(
        route.name,
        str(route.trips),
        str(route.on_time),
        f"{route.get_percentage()}%"
    )


console.print(table)