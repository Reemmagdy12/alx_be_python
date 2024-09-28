from datetime import datetime, timedelta
def display_current_datetime() :
    global current_date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

display_current_datetime()

try:
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    def calculate_future_date():
        future_date = current_date.date() + timedelta(days = number_of_days)
        print(f"Future date: {future_date}")
except ValueError:
    print("Invalid input.")
calculate_future_date()

    
           

   