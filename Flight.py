class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passenger(self, name):
        if len(self.passangers) < self.capacity:
            self.passangers.append(name)
        else:
            print("ups, you don't have more capacity")


f = Flight(3)

f.add_passenger('Jaime')
f.add_passenger('Bernardo')
f.add_passenger('Richard')
f.add_passenger('Regis')

print(f.passangers)
