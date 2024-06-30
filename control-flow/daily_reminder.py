Task = input("Enter your task: ")
Priority = input("Enter your task priority (high, medium, low ): ")
Time_bound = input("Is task time bound? (yes, no): ")
if Priority in ["high", "medium", "low"]:
    match Priority:
        case "high":
            print(f"Task: {Task} - Priority: high" )
            if Time_bound == "yes":
                print("reminder:This task requires immediate attention today!")
        case "medium":
            print(f"Task: {Task} - Preority: medium" )
            if Time_bound == "yes":
                print("reminder:This task requires immediate attention today!")
        case "low":
            print(f"Task: {Task} - Preority low")
            if Time_bound == "yes":
                print("reminder:This task requires immediate attention today!")
else:
    print("Invalid priority entered.")
if time_bound == "no":
    priority_level = ""
    if priority == "high":
        priority_level = "High"
    elif priority == "medium":
        priority_level = "Medium"
    elif priority == "low":
        priority_level = "Low"
        
    print(f"Task: {Task} - Priority: {priority_level}")
    print("Reminder: This task does not have an immediate deadline.")

        
