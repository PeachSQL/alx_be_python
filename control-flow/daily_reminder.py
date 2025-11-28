# daily_reminder.py

def main():
    print("---- Daily Task Reminder ----")

    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Start building the reminder message
    reminder_message = f"'{task}' is a "

    # Match Case for priority handling
    match priority:
        case "high":
            reminder_message += "high priority task"
        case "medium":
            reminder_message += "medium priority task"
        case "low":
            reminder_message += "low priority task"
        case _:
            reminder_message += "task with unspecified priority"

    # Check if the task is time-sensitive
    if time_bound == "yes":
        reminder_message += " that requires immediate attention today!"
    else:
        reminder_message += ". Consider completing it when you have free time."

    # Display final reminder
    print("\nReminder:", reminder_message)


# Run the program
if __name__ == "__main__":
    main()
