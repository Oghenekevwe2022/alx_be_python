def perform_operation(num1: float, num2: float, operation: str):
    
    if operation == "add":
        return num1 + num2
    elif operation == "substract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "division":
        if num2 == 0:
           return "Division by zero error"
        else:
            return num1 / num2
    else:
        return "Invalid operation"