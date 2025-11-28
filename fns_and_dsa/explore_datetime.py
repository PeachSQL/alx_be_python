from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Save current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date


# Part 2: Calculate a Future Date
def calculate_future_date(current_date, number_of_days):
    future_date = current_date + timedelta(days=number_of_days)  # Save future date
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return future_date


# Main program flow
def main():
    # Display current datetime
    current_date = display_current_datetime()

    # Ask user for number of days
    days_input = int(input("Enter the number of days to add to the current date: "))

    # Calculate and display future date
    calculate_future_date(current_date, days_input)


if __name__ == "__main__":
    main()
