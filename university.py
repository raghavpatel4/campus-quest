# university.py
from building import Building
from student import Student

class University:
    def __init__(self, name):
        self.name = name
        self.buildings = []
        self.students = []
        self.funds = 50000 # Initial funds
        self.student_population = len(self.students) # Initial student population
        self.student_capacity = 0 # Initial student capacity

    def current_funds(self):
        return self.funds

    def view_campus(self):
        print(f"\n{self.name} Campus:")
        if not self.buildings:
            print("No buildings yet.")
        for building in self.buildings:
            print(f"- {building.name} ({building.type})")
        print(f"\nFunds: ${self.funds}")

        print(f"Student population: {self.student_population}/{self.student_capacity}")

    def add_building(self):
        print("\nChoose a building type to add: ")
        for building_type, cost in Building.BUILDING_TYPES.items():
            print(f"{building_type} (${cost})")

        building_type = input("Enter the building type: ")

        if building_type in Building.BUILDING_TYPES:
            if self.funds >= Building.BUILDING_TYPES[building_type]:
                name = input("Enter the name of the building: ")
                new_building = Building(name, building_type)
                self.buildings.append(new_building)
                self.funds -= new_building.cost
                print(f"{building_type} '{name}' added to the campus.")
                print(f"\nRemaining funds: ${self.funds}")
            else:
                print("Insufficient funds to add this building.")
        else:
            print("Invalid building type. Please try again.")
