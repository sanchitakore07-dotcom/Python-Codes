
# calculates income tax based on the user's annual income
print("--------------------------< 💰 Income Tax Calculation based on your details >-----------------------------")

name_of_people = input(" Enter your name: ")
age_of_people = int(input(" Enter your age: "))
address_of_people = input("Enter your address: ")
email_of_people = input("Enter your email: ")
current_location = input(" Enter your location: ")
annual_income = int(input("💵 Enter your annual income: "))

# Deducted according to your annual income
if annual_income > 250000:
    if annual_income < 1000000:
        print("₹50,000 standard deduction applied")
        deducted_income = annual_income - 50000

# tax variable to store calculated tax amount
tax_amount = 0

# Applying tax conditions based on
if annual_income <= 1000000:
    if annual_income <= 250000:
        tax_amount = 0
        print(f"Your annual income is ₹{annual_income}.")
        print("🎉 Income is below ₹2.5 LPA So NO TAX FOR YOU!")

    elif annual_income <= 500000:
        tax_amount = 0.05 * annual_income
        print(f" Your annual income is ₹{annual_income}.")
        print("📊 For you Applicable Tax is 5%")

    else:
        tax_amount = 0.20 * annual_income
        print(f"Your annual income is ₹{annual_income}.")
        print("📊 For you Applicable Tax is 20%")
else:
    tax_amount = 0.30 * annual_income
    print(f"Your annual income is ₹{annual_income}.")
    print("📊 For you Applicable Tax is 30%")


if age_of_people > 60 :
    if annual_income > 1500000:
        print("Senior citizen membership applied 3% tax reduction)")
        tax_deducted = tax_amount - (0.03 * annual_income)
        print(f"After senior citizen benefit tax: ₹{tax_amount}")
    else:
        print(" High income surcharge: 70% extra tax added")
        tax_deducted = tax_amount + (0.70 * tax_amount)


# Displaying the final calculated tax amount

print("\n-----------------------------< 🧾 TAX SUMMARY >-----------------------------")
print(f"Your Name :{name_of_people}")
print(f"Your Age : {age_of_people}")
print(f"Your Location  : {current_location}")
print(f"Your Annual Income 💰: ₹{annual_income}")
print(f"Your Tax Payable🧾 : ₹{tax_amount}")
print(f"Deducted income: {deducted_income}")
print(f"Tax: {tax_deducted}")









#if annual_income > 1000000:
'''if annual_income > 1500000:
    print(" High income surcharge: 70% extra tax added")
    tax_amount = tax_amount + (0.70 * tax_amount)
else:
    print("Income above 10 LPA but no surcharge")

print(f"\n Final Tax Payable : ₹{tax_amount}")'''


























'''if age_of_people > 60:
    print("You got senior citizen membership!! Your tax reduced by 3%!!! ")
    print(f"Before tax {tax_amount}")
    tax_deducted=-tax_amount-(0.03*annual_income)
    print(f"After tax {tax_deducted}")
else:
    if annual_income > 1000000:
        if annual_income > 1500000:
            print("⚠ High income surcharge: 70% extra tax added")
            tax_amount = tax_amount + (0.70 * tax_amount)
        else:
            print("ℹ️ Income above 10 LPA but no surcharge")
    else:
        print("ℹ️ Income below surcharge limit")'''







