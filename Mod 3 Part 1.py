# Part 1: Meal Total Calculation

# Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: "))

# Calculate the tip and tax amounts
tip_amount = food_charge * 0.18
tax_amount = food_charge * 0.07

# Calculate the total amount
total_amount = food_charge + tip_amount + tax_amount

# Display the amounts
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip Amount (18%): ${tip_amount:.2f}")
print(f"Tax Amount (7%): ${tax_amount:.2f}")
print(f"Total Amount: ${total_amount:.2f}")
