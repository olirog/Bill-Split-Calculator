
print("Bill Split Calculator")
print("---------------------")

print("Enter the bill amount ($):")
bill_amount = float(input())

print("Enter the tip percentage (%):")
tip_percentage = float(input())

print("Enter the number of people:")
num_people = int(input())

tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / num_people

print("---------------------")
print(f"Total (including tip): ${total_amount:.2f}")
print(f"Each person pays: ${amount_per_person:.2f}")
print("---------------------")
print("Thank you for using Bill Split Calculator!")
