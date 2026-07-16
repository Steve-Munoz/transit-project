# from rich.table import Table
# from rich.console import Console
# from database import create_table, insert_route, get_all_routes, delete_route
# def display_routes(title = "Route Performance"):
#     routes = get_all_routes()
#     console = Console()
#     table = Table(title = title)
#     table.add_column("Routes", style = "cyan" )
#     table.add_column("Trips", style ="white")
#     table.add_column("on_time", style = "white")
#     table.add_column("percentage", style = "magenta")
#     for route in routes:
#         percentage = round(route["on_time"]/route["trips"] *100,1)
#         table.add_row(
#             route["name"],
#             str(route["trips"]),
#             str(route["on_time"]),
#             f"{percentage}%"
#         )
#         console.print(table)

# # Step 1 — Set up the database
# create_table()

# # Step 2 — Insert routes
# insert_route("Route 101", 60, 50)
# insert_route("Route 202", 80, 60)
# insert_route("Route 302", 70, 30)
# insert_route("Route 402", 60, 40)

# # Step 3 — Display all routes
# print("\n--- Initial State ---")
# display_routes()

# # Step 4 — Delete one and show updated state
# delete_route("Route 302")
# print("\n--- After Deleting Route 302 ---")
# display_routes()
from rich.table import Table
from rich.console import Console
from database import get_all_routes,create_table,insert_route,delete_route

def display_routes(title = "Route Performance"):
    routes = get_all_routes()
    console = Console()
    table = Table(title = title)
    table.add_column("Routes", style = "cyan")
    table.add_column("Trips", style = "white")
    table.add_column("On Time", style = "white")
    table.add_column("Percentage", style = "magenta")

    for route in routes:
        percentage = round(route["on_time"]/route["trips"]*100,1)
        table.add_row(
            route["name"],
            str(route["trips"]),
            str(route["on_time"]),
            f"{percentage}%"
        )
    console.print(table)
create_table()

insert_route("Route 101",60,50)
insert_route("Route 202",60,55)
insert_route("Route 302",60,30)
insert_route("Route 402",60,59)
print("------Intial State------------")
display_routes()

delete_route("Route 402")
print("--------Final State-----------")
display_routes()