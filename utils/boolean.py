class Boolean:
    def yes_no(self, query):
        while True:
            try:
                user_input = input(query).upper()
                if not user_input.isalpha():
                    raise TypeError
                if user_input not in ("Y", "N"):
                    raise ValueError
                if user_input == "Y":
                    return True
                else:
                    return False
            except (TypeError, ValueError):
                print("Oops! Invalid input. Try again.")
