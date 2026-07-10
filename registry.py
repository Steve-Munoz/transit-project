from route import Route

class RouteRegistry:
    def __init__(self):
        self.routes = {}
    def add(self,route):
        if route.name in self.routes:
            raise ValueError(f"{route.name} already. exists in registry")
        self.routes[route.name] = route
        print(f"{self.routes[route.name]} has been updated")
    def get(self,name):
        if name not in self.routes:
            raise KeyError(f"{name} does not exists in registry")
        print(f"Here is {self.routes[name]}")
        return {name}
    def update(self,name,trips,on_time):
        if name not in self.routes:
            raise KeyError(f"{name} does not exists in registry")
        self.routes[name] = Route(name,trips,on_time)
        print(f"{name} has been updated")
    def delete(self,name):
        if name not in self.routes:
            raise KeyError(f"{name} does not exist in registry")
        removed = self.routes.pop(name)
        print(f"Removed: {removed}")
    def display(self):
        for rank,route in enumerate(sorted(self.routes.values(),key = lambda r:r.get_percentage()),start = 1):
            print(f"{rank}) - {route}")