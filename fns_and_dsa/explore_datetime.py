from datetime import datetime, timedelta

# Display the current Date and Time
def display_current_datetime():
    current_date = datetime.now()
     # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    
# Calculate a Future Datw
def calculate_future_date():
    try:
        
     # Prompt the user to enter the number of days
        days = int(input("Enter the number of days to add to the current date: "))
        # Get the current date
        current_date = datetime.now()
        # Calculate the future date by adding the specified number of days
        future_date = current_date + timedelta(days=days)
        # Format and print the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date: {formatted_future_date}" )
        
    except ValueError:
        print("Please enter a valid integer for the number of days.")