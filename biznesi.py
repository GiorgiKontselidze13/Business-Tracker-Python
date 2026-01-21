# Lists to store data
weekly_profit = [] 

print("--- Weekly Financial Summary ---")

# Loop for 3 days
for day in range(1, 4):
    profit = int(input(f"Enter profit for day {day}: "))
    weekly_profit.append(profit)

# Calculations
total_profit = sum(weekly_profit)
best_day_profit = max(weekly_profit)
best_day_number = weekly_profit.index(best_day_profit) + 1

print(f"\n--- Results ---")
print(f"Total profit for 3 days: {total_profit} GEL")
print(f"Your best day was day {best_day_number} with {best_day_profit} GEL")

# Motivation logic
if total_profit > 1500:
    print("Great pace! The Audi RS6 is getting closer.")
else:
    print("Keep working hard, your family is proud of you!")