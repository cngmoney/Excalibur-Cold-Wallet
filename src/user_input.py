class UserInput:
    @staticmethod
    def prompt_string(prompt_text, allow_empty=False):
        while True:
            val = input(f"{prompt_text}: ").strip()
            if val or allow_empty:
                return val
            print("❗ Input cannot be empty.")

    @staticmethod
    def prompt_float(prompt_text, min_val=None, max_val=None):
        while True:
            try:
                val = float(input(f"{prompt_text}: "))
                if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                    print(f"❗ Value must be between {min_val} and {max_val}.")
                else:
                    return val
            except ValueError:
                print("❗ Invalid number. Please try again.")

    @staticmethod
    def prompt_choice(prompt_text, choices):
        print(f"{prompt_text}:")
        for i, choice in enumerate(choices, start=1):
            print(f"  {i}. {choice}")
        while True:
            try:
                selection = int(input("Select an option: "))
                if 1 <= selection <= len(choices):
                    return choices[selection - 1]
                print("❗ Invalid choice. Try again.")
            except ValueError:
                print("❗ Invalid input. Enter a number.")

# Example usage:
if __name__ == "__main__":
    ui = UserInput()
    name = ui.prompt_string("Enter your name")
    amount = ui.prompt_float("Enter amount", min_val=0.01)
    currency = ui.prompt_choice("Select currency", ["BTC", "ETH", "RLUSD"])
    print(f"You entered: {name}, {amount} {currency}")
