def safe_divide(numerator, denominator):
    """
    Perform division safely, handling division by zero and non-numeric inputs.
    
    Args:
        numerator (str or float): The numerator value
        denominator (str or float): The denominator value
        
    Returns:
        str: The result of division or an error message
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Attempt division
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
