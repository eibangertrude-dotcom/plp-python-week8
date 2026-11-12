
# ==========================================
# PERSONAL MINI-TOOLKIT
# PLP WEEK 8 FINAL PROJECT
# ==========================================

# Store all tasks in a list
tasks = []


# Tool 1: To-Do List Manager
# Allows users to add, view and remove tasks.
def todo_manager():

    while True:
        print("\n========== TO-DO LIST MANAGER ==========")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Return to main menu")
        print("========================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your new task: ")

            if task.strip():
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is currently empty.")
            else:
                print("\nYOUR TASKS:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                print("\nYOUR TASKS:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                task_number = input("Enter the task number to remove: ")

                if task_number.isdigit():
                    task_number = int(task_number)

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("That task number does not exist.")
                else:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")


# Tool 2: Even or Odd Checker
# Determines whether a number is even or odd.
def even_odd_checker():

    print("\n========== EVEN OR ODD CHECKER ==========")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an EVEN number.")
        else:
            print(f"{number} is an ODD number.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


# Tool 3: Multiplication Table Generator
# Generates a multiplication table from 1 to 10.
def multiplication_table():

    print("\n========== MULTIPLICATION TABLE ==========")

    try:
        number = int(input("Enter a number: "))

        print(f"\nMultiplication table for {number}:")

        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


# Personal Mini-Toolkit welcome message
print("====================================")
print("       WELCOME TO MY MINI-TOOLKIT")
print("====================================")


# Main menu loop
while True:
    print("\n========== MAIN MENU ==========")
    print("1. To-Do List Manager")
    print("2. Even or Odd Checker")
    print("3. Multiplication Table Generator")
    print("4. Quit")
    print("===============================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        todo_manager()

    elif choice == "2":
        even_odd_checker()

    elif choice == "3":
        multiplication_table()

    elif choice == "4":
        print("Thank you for using my Personal Mini-Toolkit!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
