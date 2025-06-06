import datetime

def display_current_datetime():
    """
    Displays the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.datetime.now()
    print(f"Current Date and Time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    Prints the future date in "YYYY-MM-DD" format.
    """
    try:
        num_days_str = input("Enter the number of days to add to the current date: ")
        num_days = int(num_days_str)
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
        return

    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=num_days)
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    print("--- Part 1: Display Current Date and Time ---")
    display_current_datetime()
    print("\n--- Part 2: Calculate a Future Date ---")
    calculate_future_date()
