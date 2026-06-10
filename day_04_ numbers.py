# 1. My Current Battery percentage in the laptop while running AI task
current_battery = 23
ai_app_drain = 5.08
hours_coding = 2

# 2. Multiplying line 3 and 4 together
total_drain = ai_app_drain * hours_coding
print(
    f"Total battery drain after {hours_coding} hours of coding: {total_drain}%")

# 3. create a variable for the final battery percentage
final_battery = current_battery - total_drain
print(f"Final battery remaining: {final_battery}%")
print(type(final_battery))
