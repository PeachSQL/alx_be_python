# pattern_drawing.py
# Objective: Draw a square pattern using nested loops

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate positive integer input
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to handle rows
while row < size:
    # For loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    
    # Move to the next line after each row
    print()
    
    # Increment the row counter
    row += 1
