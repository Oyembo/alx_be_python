Task = input("Enter your task: ")
Priority = input("Priority (high, medium, low): ")
Time Bound = input("Is it time-bound (Yes/No): ") #Respond with Yes or No

match priority:
    case "high":
    print("Finish this task first")
    case "medium":
    print("Finish task soon")
    case "low":
    print ("Schedule task for completion")
if priority is "high":
    print("Reminder, task require immediate attention today")

