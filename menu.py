def prompt_quiz_options() -> dict:
    """Prompt user to select quiz options and return selections"""
    options = {
        "type": "",
        "amount": 0
    }
    menu = """
🧠 Welcome to the quiz app! 🧠
What type of questions?
-----------------------------
1) Terms
2) Acronyms"""
    print(menu)
    while True:
        type_selection = input("Select a quiz type by number: ")
        if type_selection == "1":
            options["type"] = "terms"
            print("Terms quiz selected")
            break
        elif type_selection == "2":
            options["type"] = "acronyms"
            print("Acronyms quiz selected")
            break
        else:
            print("🚫 Invalid selection - Try again.")
            continue

    print("""
How many questions?
-----------------------------
1) 10
2) 20
3) All
""")
    while True:
        amount_selection = input("Select an amount by number: ")
        if amount_selection == "1":
            options["amount"] = 10
            break
        elif amount_selection == "2":
            options["amount"] = 20
            break
        elif amount_selection == "3":
            options["amount"] = 0
            break
        else:
            print("🚫 Invalid selection - Try again.")
            continue

    return options
