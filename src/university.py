# university.py
from src.building import Building

from src import console_ui
from src.student import Student, generate_student


def money_to_string(money):
    return "{:.2f}".format(money)


class University:
    def __init__(self, name):
        self.name = name
        self.buildings = []
        self.students = []
        self.funds = 50000  # Initial funds
        self.income = 0  # Initial income
        self.student_population = len(self.students)  # Initial student population
        self.student_capacity = len(self.students)  # Initial student capacity

    def current_funds(self):
        return self.funds

    def view_campus(self):
        print(f"\n{self.name} Campus:")
        if not self.buildings:
            print("No buildings yet.")
        for building in self.buildings:
            print(f"- {building.name} ({building.type})")
        print(f"\nFunds: ${money_to_string(self.current_funds())}")

        print(f"Student population: {self.student_population}/{self.student_capacity}")

        print("\nWhat would you like to do on campus?")
        print("\n1. View students")
        print("2. Back to main menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            self.view_students()
        elif choice == "2":
            return

    def view_students(self):
        print(f"\nThere are {len(self.students)} students in the university...")
        # Print the first 10 names of the students, then give the user option to view 10 more students
        if len(self.students) > 0:
            while True:
                for student in self.students[:10]:
                    print(f"- {student.name} ({student.major})")
                more = input("View 10 more students? (y/n): ")
                if more.lower() != "y":
                    break


    def add_building(self):
        print("\nChoose a building type to add: ")
        for building_type, cost in Building.BUILDING_TYPES.items():
            print(f"{building_type} (${cost})")

        building_type = input("Enter the building type: ")

        if building_type in Building.BUILDING_TYPES:
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
        print("Choose a sub-type for the classroom:")
        for sub_type in Building.CLASSROOM_SUBTYPES:
            print(f"- {sub_type}")
        sub_type = input("Enter the sub-type: ")
        if sub_type not in Building.CLASSROOM_SUBTYPES:
            print("Invalid sub-type. Please try again.")
            return
        cost = Building.BUILDING_TYPES[building_type]
        if self.buy(cost):
            # Ask the user to enter the name of the building
            name = input("Enter the name of the building: ")
            new_building = Building(name, building_type)
            self.buildings.append(new_building)

            print(f"Adding {sub_type} classroom building...")
            console_ui.loading_text()

            print(f"{sub_type} classroom building added successfully!")

    def add_housing(self, building_type="Housing"):
        print("\nHousing types available:")
        # Display the available housing subtypes and their costs
        for housing_type in Building.HOUSING_SUBTYPES:
            print(
                f"- {housing_type} (${Building.BUILDING_TYPES['Housing'] * Building.HOUSING_SUBTYPES[housing_type]['cost_multiplier']})")
            print(f"  Capacity: {Building.HOUSING_SUBTYPES[housing_type]['capacity']} students")

        # Ask the user to choose a housing subtype
        sub_type = input("\nChoose a sub-type for the housing: ")
        if sub_type not in Building.HOUSING_SUBTYPES:
            print("Invalid sub-type. Please try again.")
            return None

        # Calculate the cost of the housing building using the cost multiplier
        cost = Building.BUILDING_TYPES["Housing"] * Building.HOUSING_SUBTYPES[sub_type]["cost_multiplier"]

        if self.buy(cost):
            # Ask the user to enter the name of the building
            name = input("Enter the name of the building: ")
            new_building = Building(name, building_type)
            self.buildings.append(new_building)

            print(f"Adding {sub_type} housing building...")
            console_ui.loading_text()

            self.add_students(Building.HOUSING_SUBTYPES[sub_type]["capacity"])
            self.set_student_capacity()
            self.set_student_population()

            print(
                f"{sub_type} housing building added successfully! Student population increased to {self.student_population}/{self.student_capacity}.")
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
        if self.current_funds() >= cost:
            return True
        else:
            return False

    def buy(self, cost):
        if self.check_funds(cost):
            self.funds -= cost
            return True
        else:
            print(f"\nInsufficient funds to add this building.\nYou need ${cost - self.current_funds()} more.")
            return False

    def add_students(self, num_students):
        for _ in range(num_students):
            self.students.append(generate_student())

    def set_income(self):
        self.income = self.student_population * (len(self.buildings) + 0.14)
        return self.income

    def set_student_population(self):
        self.student_population = len(self.students)

    def set_student_capacity(self):
        self.student_capacity = len(self.students)
