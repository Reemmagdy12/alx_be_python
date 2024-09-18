task = input("Enter your task:")
priority = input ("Priority (high/medium/low):")
time_bound = input ("Is it time-bound? (yes/no):")
match priority:
    case "low":
       reminder = f"{task} is a low priority task"
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "high" :
        reminder = f"{task} is a high priority task"
    case _ :
        print ("invalid input")

if time_bound == "yes" :
    reminder+=" that requires immediate attention today!"
    print(f"Reminder: {reminder}") 


 
