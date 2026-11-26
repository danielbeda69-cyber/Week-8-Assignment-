# toolkit.py
# Personal Mini-Toolkit - a menu-driven program with four tools:
#   1. To-Do List            (uses a list that changes while the program runs)
#   2. Simple Calculator     (uses conditionals)
#   3. Temperature Converter (uses conditionals)
#   4. Multiplication Table  (uses a loop)
# The menu keeps running until the user chooses to quit.

print("=" * 40)
print("   Welcome to your Personal Mini-Toolkit!")
print("=" * 40)

# The to-do list is stored in a list so it can grow and shrink while the program runs.
todo_items = []

running = True

while running:
    # ---------- MAIN MENU ----------
    print("\n----------- MAIN MENU -----------")
    print("1. To-Do List")
    print("2. Simple Calculator")
    print("3. Temperature Converter")
    print("4. Multiplication Table")
    print("5. Quit")
    choice = input("Choose a tool (1-5): ").strip()

    # ---------- ROUTE THE CHOICE ----------
    if choice == "1":
        # ===== TOOL 1: TO-DO LIST =====
        # Lets the user add, view and remove tasks stored in the todo_items list.
        print("\n--- To-Do List ---")
        in_todo = True
        while in_todo:
            print("\n a) Add a task")
            print(" b) View tasks")
            print(" c) Remove a task")
            print(" d) Back to main menu")
            action = input("What would you like to do? ").strip().lower()

            if action == "a":
                task = input("Enter the new task: ").strip()
                if task == "":
                    print("A task can't be empty. Nothing was added.")
                else:
                    todo_items.append(task)
                    print(f"Added: '{task}' (you now have {len(todo_items)} task(s))")
            elif action == "b":
                if len(todo_items) == 0:
                    print("Your to-do list is empty. Nice and clear!")
                else:
                    print("\nYour tasks:")
                    number = 1
                    for item in todo_items:
                        print(f" {number}. {item}")
                        number = number + 1
            elif action == "c":
                if len(todo_items) == 0:
                    print("There is nothing to remove - your list is empty.")
                else:
                    number = 1
                    for item in todo_items:
                        print(f" {number}. {item}")
                        number = number + 1
                    position = input("Enter the number of the task to remove: ").strip()
                    if position.isdigit() and 1 <= int(position) <= len(todo_items):
                        removed = todo_items.pop(int(position) - 1)
                        print(f"Removed: '{removed}'")
                    else:
                        print("That is not a valid task number.")
            elif action == "d":
                in_todo = False
            else:
                print("Please type a, b, c or d.")

    elif choice == "2":
        # ===== TOOL 2: SIMPLE CALCULATOR =====
        # Takes two numbers and an operation, then uses conditionals to pick the maths.
        print("\n--- Simple Calculator ---")
        first_text = input("Enter the first number: ").strip()
        second_text = input("Enter the second number: ").strip()
        operation = input("Choose an operation (+, -, *, /): ").strip()

        # Check that both entries are numbers (digits with an optional minus sign and one dot).
        first_ok = first_text.replace("-", "", 1).replace(".", "", 1).isdigit()
        second_ok = second_text.replace("-", "", 1).replace(".", "", 1).isdigit()

        if not (first_ok and second_ok):
            print("Please enter valid numbers next time.")
        else:
            num1 = float(first_text)
            num2 = float(second_text)
            if operation == "+":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operation == "-":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operation == "*":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operation == "/":
                if num2 == 0:
                    print("You can't divide by zero!")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Unknown operation. Use +, -, * or /.")

    elif choice == "3":
        # ===== TOOL 3: TEMPERATURE CONVERTER =====
        # Converts between Celsius and Fahrenheit, using conditionals to pick the formula.
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        direction = input("Choose 1 or 2: ").strip()

        if direction == "1" or direction == "2":
            value_text = input("Enter the temperature: ").strip()
            if value_text.replace("-", "", 1).replace(".", "", 1).isdigit():
                value = float(value_text)
                if direction == "1":
                    result = value * 9 / 5 + 32
                    print(f"{value} C = {round(result, 2)} F")
                else:
                    result = (value - 32) * 5 / 9
                    print(f"{value} F = {round(result, 2)} C")
            else:
                print("Please enter a valid number.")
        else:
            print("Invalid choice. Please pick 1 or 2.")

    elif choice == "4":
        # ===== TOOL 4: MULTIPLICATION TABLE =====
        # Uses a for loop to print the 1 to 12 times table of a number.
        print("\n--- Multiplication Table ---")
        number_text = input("Which number's table do you want? ").strip()
        if number_text.isdigit():
            number = int(number_text)
            print(f"\nMultiplication table for {number}:")
            for i in range(1, 13):
                print(f"{number} x {i} = {number * i}")
        else:
            print("Please enter a whole number (0 or higher).")

    elif choice == "5":
        # ===== QUIT =====
        running = False

    else:
        # Anything not on the menu gets a polite message instead of a crash.
        print(f"Oops! '{choice}' isn't on the menu. Please enter a number from 1 to 5.")

print("\nThanks for using the Mini-Toolkit. Goodbye!")
