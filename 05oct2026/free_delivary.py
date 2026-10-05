amount = int(input("Enter the amount:"))
is_premium = True

free_delivary=amount>=1000 or is_premium

print(free_delivary)