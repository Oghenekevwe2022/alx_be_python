def safe_dvide(numerator, denominator):
    try:
        numberator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."