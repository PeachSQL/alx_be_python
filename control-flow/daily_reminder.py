# daily_reminder.py

def main():
    print("---- Daily Task Reminder ----")

    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Determine the priority phrase using Match Case
    match priority:
        case "high":
            priority_phrase = "high priority task"
        case "medium":
            priority_phrase = "medium priority task"
        case "low":
            priority_phrase = "low priority task"
        case _:
            priority_phrase = "task with unspecified priority"

    # Build the reminder message (include the task in single quotes)
    if time_bound == "yes":
        reminder_message = f"'{task}' is a {priority_phrase} that requires immediate attention today!"
    else:
        reminder_message = f"'{task}' is a {priority_phrase}. Consider completing it when you have free time."

    # Print in the exact format the tests expect (starts with "Reminder:")
    print(f"Reminder: {reminder_message}")


if __name__ == "__main__":
    main()
