
while True:
    print("\n====================================")
    print("       PYTHON FUNDAMENTALS")
    print("         INTERACTIVE MENU")
    print("====================================")
    print("[1] Print Statements")
    print("[2] Variables")
    print("[3] Operators")
    print("[4] Conditionals")
    print("[5] Loops")
    print("[6] Lists")
    print("[7] Functions")
    print("[8] User-Defined Programs")
    print("[9] Exit")
    print("====================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nYou selected Print Statements.")

    elif choice == "2":
        print("\nYou selected Variables.")

    elif choice == "3":
        print("\nYou selected Operators.")

    elif choice == "4":
        print("\nYou selected Conditionals.")

    elif choice == "5":
        print("\nYou selected Loops.")

    elif choice == "6":
        print("\nYou selected Lists.")

    elif choice == "7":
        print("\nYou selected Functions.")

    elif choice == "8":
        print("\nYou selected User-Defined Programs.")

    elif choice == "9":
        print("\nThank you for using Python Fundamentals!")
        break

    else:
        print("\nInvalid choice! Please select from 1-9.")
