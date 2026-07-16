 ###Version 1
routes = [
    {"name": "Route 101", "trips": 60, "on_time": 50},
    {"name": "Route 202", "trips": 80, "on_time": 60},
    {"name": "Route 302", "trips": 90, "on_time": 50},
    {"name": "Route 402", "trips": 60, "on_time": 30},
]
def trips_greater_than_50(routes):
    seen_on_time = set()
    for route in routes: ## O(n)

        if route["trips"] > 50:
            if route["on_time"] in seen_on_time: ##O(1) lookup
                print(f"duplicate found {route["on_time"]}")
            seen_on_time.add(route["on_time"])##O(1) add
    print(seen_on_time)
                    
trips_greater_than_50(routes)
        
    
    ###Version 2

def trips_greater_than_50_slow(routes):
    for route in routes:
        if route["trips"] > 50:
            for other in routes:
                if route != other:
                    if route["on_time"] == other["on_time"]:
                        print(f"duplicate: {route["on_time"]}")
trips_greater_than_50_slow(routes)

