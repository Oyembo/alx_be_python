task = input("Enter task description: ")
priority = input("Choose task priority (high, medium, low): ")
time_bound = input("Is the task time-bound: ") #Respond with Yes or No

match priority:
    case "high":
    print("Finish this task first")
    case "medium":
    print("Finish task soon")
    case "low":
    print ("Schedule task for completion")
if priority is "high":
    print("Reminder, task require immediate attention today")

