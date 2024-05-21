# student.py
from faker import Faker
import random

fake = Faker()

# Load all names from a file
# with open('all_names.txt') as f:
#     all_names = f.read().splitlines()


def generate_student():

    name = fake.name()
    major = fake.random_element(Student.MAJOR_TUITION.keys())
    return Student(name, major)

    # Select a random name from the list
    # name = random.choice(all_names)
    # major = random.choice(Student.MAJOR_TUITION.keys())
    # return Student(name, major)


class Student:

    MAJOR_TUITION = {
        "Math": 5000,
        "Science": 7500,
        "Engineering": 10000,
        "Humanities": 2500,
    }

    def __init__(self, name, major, tuition=0):
        self.name = name
        self.major = major
        self.tuition = self.calculate_tuition(self.major)

    def calculate_tuition(self, major):
        return self.MAJOR_TUITION[major]
