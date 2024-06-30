task = input("Enter task description: ")
priority = input("Enter tast priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")
if priority in ["high", "medium", "low"]:
    match priority:
        case "high":
            print(f"task {task} has high priority. ")
        case "medium":
            print(f"Task {task} has medium priority. ")
        case "low":
            print(f"Task is {task} has low priority. ")
else:
    print(f"Error invalid priority. ")
if time_bound == "yes":
    print(f"Task {task} is time_bound and requires attention. ")
elif time_bound == "no":
    print(f"task {task} is not time_bound. ")
else:
    print(f"Invalid input.")        
