import datetime 
def display_current_datetime() :
    global current_date
    current_date = datetime.datetime.now().replace(microsecond=0)
    print(f"Current date and time: {current_date}")

display_current_datetime()

try:
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    def calculate_future_date():
        future_date = current_date.date() + datetime.timedelta(days = number_of_days)
        print(f"Future date: {future_date}")
except ValueError:
    print("Invalid input.")
calculate_future_date()

    
           

   