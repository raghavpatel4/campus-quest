# building.py
class Building:
    BUILDING_TYPES = {
        "Classroom": 5000,
        "Housing": 10000,
        "Library": 15000,
        "Gym": 7000,
        "Dining Hall": 8000,
    }

    CLASSROOM_SUBTYPES = ["Math", "Science", "Engineering", "Humanities"]

    HOUSING_SUBTYPES = {"Dormitory": {"cost_multiplier": 1.5, "capacity": 500, "level": 1},
                        "Apartment": {"cost_multiplier": 1.75, "capacity": 750, "level": 1}}

    def __init__(self, name, building_type, sub_type=None):
        self.name = name
        self.type = building_type
        self.sub_type = sub_type
        self.level = 1  # Default level for all buildings

        # Set the cost and capacity based on the building type and subtype
        if building_type == "Housing" and sub_type in self.HOUSING_SUBTYPES:
            self.cost = self.BUILDING_TYPES[building_type] * self.HOUSING_SUBTYPES[sub_type]["cost_multiplier"]
            self.capacity = self.HOUSING_SUBTYPES[sub_type]["capacity"]
            self.level = self.HOUSING_SUBTYPES[sub_type]["level"]
        else:
            self.cost = self.BUILDING_TYPES[building_type]
            self.capacity = 0  # Default capacity for non-housing buildings
