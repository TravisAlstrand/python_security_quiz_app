def prompt_quiz_type() -> str:
    """Prompt user to select quiz type and return selection"""
    menu = """
🧠 Welcome to the quiz app! 🧠
-----------------------------
1) Terms Quiz
2) Acronyms Quiz"""
    print(menu)
    while True:
        selection = input("Select a quiz type by number: ")
        if selection in ["1", "2"]:
            return "terms" if selection == "1" else "acronyms"
        print("🚫 Invalid selection - Try again.")
