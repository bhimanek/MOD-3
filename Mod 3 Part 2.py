# Part 2: 24-Hour Clock Alarm Time Calculation

# Ask the user to enter the current time in hours (0-23)
current_time = int(input("Enter the current time (0-23): "))

# Ask the user to enter the number of hours to wait for the alarm
waiting_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the future time
future_time = (current_time + waiting_hours) % 24

# Display the future time
print(f"The time when the alarm will go off is: {future_time:02d}:00")
