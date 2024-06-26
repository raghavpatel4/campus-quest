# main.py
from university import University

def main():
    print("Welcome to Tiny University!")
    university_name = input("Enter the name of your university: ")
    university = University(university_name)

    while True:
        print(f"\nWelcome, President of {university.name}!")
        print(f"Current Funds: ${university.current_funds()}")

        print("What would you like to do?")
        print("\n1. View Campus")
        print("2. Add Building")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            university.view_campus()
        elif choice == "2":
            university.add_building()
        elif choice == "3":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()