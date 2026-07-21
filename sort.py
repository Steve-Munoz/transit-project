routes = [
    {"name": "Route 101", "trips": 60, "on_time": 50},
    {"name": "Route 202", "trips": 80, "on_time": 60},
    {"name": "Route 302", "trips": 70, "on_time": 30},
    {"name": "Route 402", "trips": 60, "on_time": 40},
]


def get_percentage(route):
    return round(route["on_time"] / route["trips"] * 100, 1)


def bubble_sort(routes):
    n = len(routes)
    for i in range(n):
        for j in range(n - 1 - i):
            if get_percentage(routes[j]) > get_percentage(routes[j + 1]):
                routes[j], routes[j + 1] = routes[j + 1], routes[j]
    return routes


def binary_search(sorted_routes, target):
    left  = 0
    right = len(sorted_routes) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_percentage = get_percentage(sorted_routes[mid])

        if mid_percentage == target:
            return mid
        elif mid_percentage < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Part 1 and 2 — Sort then Search
sorted_routes = bubble_sort(routes)

print("Sorted routes (lowest to highest %):")
for route in sorted_routes:
    print(f"{route['name']} — {get_percentage(route)}%")

# Part 3 — Binary search
target_1 = 83.3
target_2 = 99.9

result_1 = binary_search(sorted_routes, target_1)
result_2 = binary_search(sorted_routes, target_2)

if result_1 != -1:
    print(f"\nBinary search for {target_1}%: found at index {result_1}")
else:
    print(f"\nBinary search for {target_1}%: not found")

if result_2 != -1:
    print(f"Binary search for {target_2}%: found at index {result_2}")
else:
    print(f"Binary search for {target_2}%: not found")



##sorted_routes = [Route302(42.9), Route402(66.7), Route202(75.0), Route101(83.3)]
                 ## index 0         index 1          index 2         index 3

### Starting: [Route101(83.3), Route202(75.0), Route302(42.9), Route402(66.7)]