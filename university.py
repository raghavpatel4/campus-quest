# university.py
from building import Building
from student import Student

import console_ui

class University:
    def __init__(self, name):
        self.name = name
        self.buildings = []
        self.students = []
        self.funds = 50000  # Initial funds
        self.student_population = len(self.students)  # Initial student population
        self.student_capacity = 0  # Initial student capacity

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
            if self.check_funds(Building.BUILDING_TYPES[building_type]):
                if building_type == "Classroom":
                    self.add_classroom()
                elif building_type == "Housing":
                    self.add_housing()
                elif building_type == "Library":
                    self.add_library()
                elif building_type == "Gym":
                    self.add_gym()
                elif building_type == "Dining Hall":
                    self.add_dining_hall()
        else:
            print("Invalid building type. Please try again.")

    def add_classroom(self, building_type="Classroom"):
        pass
        print("Choose a sub-type for the classroom:")
        for sub_type in Building.CLASSROOM_SUBTYPES:
            print(f"- {sub_type}")
        sub_type = input("Enter the sub-type: ")
        if sub_type not in Building.CLASSROOM_SUBTYPES:
            print("Invalid sub-type. Please try again.")
            return
        cost = Building.BUILDING_TYPES[building_type]
        if self.check_funds(cost):
            self.funds -= cost
        else:
            print("Insufficient funds to add this building.")

    def add_housing(self, building_type="Housing"):
        print("\nHousing types available:")
        # Display the available housing subtypes and their costs
        for housing_type in Building.HOUSING_SUBTYPES:
            print(f"- {housing_type} (${Building.BUILDING_TYPES['Housing'] * Building.HOUSING_SUBTYPES[housing_type]['cost_multiplier']})")
            print(f"  Capacity: {Building.HOUSING_SUBTYPES[housing_type]['capacity']} students")

        # Ask the user to choose a housing subtype
        sub_type = input("\nChoose a sub-type for the housing: ")
        if sub_type not in Building.HOUSING_SUBTYPES:
            print("Invalid sub-type. Please try again.")
            return None

        # Calculate the cost of the housing building using the cost multiplier
        cost = Building.BUILDING_TYPES["Housing"] * Building.HOUSING_SUBTYPES[sub_type]["cost_multiplier"]

        # If there are enough funds, add the housing building and increase student capacity
        if self.check_funds(cost):
            # Ask the user to enter the name of the building
            name = input("Enter the name of the building: ")
            new_building = Building(name, building_type)
            self.buildings.append(new_building)

            print(f"Adding {sub_type} housing building...")
            console_ui.loading_text()

            self.funds -= cost
            self.student_capacity += Building.HOUSING_SUBTYPES[sub_type]["capacity"]
            self.student_population += Building.HOUSING_SUBTYPES[sub_type]["capacity"]

            print(f"{sub_type} housing building added successfully! Student population increased to {self.student_population}/{self.student_capacity}.")
        return sub_type

    def add_library(self, building_type="Library"):
        pass
        cost = Building.BUILDING_TYPES[building_type]
        if self.check_funds(cost):
            self.funds -= cost
        else:
            print("Insufficient funds to add this building.")

    def add_gym(self, building_type="Gym"):
        pass
        cost = Building.BUILDING_TYPES[building_type]
        if self.check_funds(cost):
            self.funds -= cost
        else:
            print("Insufficient funds to add this building.")

    def add_dining_hall(self, building_type="Dining Hall"):
        pass
        cost = Building.BUILDING_TYPES[building_type]
        if self.check_funds(cost):
            self.funds -= cost
        else:
            print("Insufficient funds to add this building.")

    def check_funds(self, cost):
        if self.funds >= cost:
            return True
        else:
            return False

