task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound_str = input("Is it time-bound? (yes/no): ") #Respond with yes or no

match priority:
    case "high":
    print("Finish this task first")
    case "medium":
    print("Finish task soon")
    case "low":
    print ("Schedule task for completion")
if priority == "high":
    print("Finish project report' is a high priority task that requires immediate attention today!")
if time_bound == "yes":
    print ("Reminder: This task requires immediate attention today!")
    case_:
    print ("No attention required")


