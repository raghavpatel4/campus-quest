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

    def __init__(self, name, building_type, sub_type=None):
        self.name = name
        self.type = building_type
        self.sub_type = sub_type
        self.cost = self.BUILDING_TYPES[building_type]