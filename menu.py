def prompt_quiz_options() -> dict:
    """Prompt user to select quiz options and return selections"""
    options = {
        "type": "",
        "amount": 0
    }
    menu = """
🧠 Welcome to the quiz app! 🧠
-----------------------------
1) Terms Quiz
2) Acronyms Quiz"""
    print(menu)
    while True:
        type_selection = input("Select a quiz type by number: ")
        if type_selection == "1":
            options["type"] = "terms"
            print("Terms quiz selected")
        elif type_selection == "2":
            options["type"] = "acronyms"
            print("Acronyms quiz selected")
        else:
            print("🚫 Invalid selection - Try again.")
            continue
        # Todo: present / prompt for amount
