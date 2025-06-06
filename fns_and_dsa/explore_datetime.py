from datetime import datetime

def display_current_datetime():
    """
    Obtains the current date and time, saves it, and prints it in "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.datetime.now()
    print(f"Current Date and Time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates the future date based on the current date,
    and prints it in "YYYY-MM-DD" format. Handles invalid input for the number of days.
    """
    try:
        num_days_str = input("Enter the number of days to add to the current date: ")
        num_days = int(num_days_str)
    except ValueError:
        print("Invalid input. Please enter a whole number (integer) for the number of days.")
        return

    current_date = datetime.datetime.now()
    # Calculate the future date by adding a timedelta object
    future_date = current_date + datetime.timedelta(days=num_days)
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    print("--- Part 1: Displaying Current Date and Time ---")
    display_current_datetime()

    print("\n--- Part 2: Calculating a Future Date ---")
    calculate_future_date()
