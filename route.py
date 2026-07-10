class Route:
    def __init__(self,name,trips,on_time):
        if trips <= 0:
            raise ValueError("The number of trips can't be less than 0")
        if on_time <= 0:
            raise ValueError("The number of on time can't be less than 0")
        if trips < on_time:
            raise ValueError("The number of on time can't be more than trip")
        if not isinstance(name,str):
            raise ValueError("The name must be a string")
        self.name = name
        self.trips = trips
        self.on_time = on_time
    def get_percentage(self):
        return round(self.on_time/self.trips*100,1)
    def __str__(self):
        return f"{self.name} {self.get_percentage()}% are on time"