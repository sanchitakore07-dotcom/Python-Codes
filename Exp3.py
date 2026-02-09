
# calculates income tax based on the user's annual income
print("--------------------------< 💰 Income Tax Calculation based on your details >-----------------------------")

name_of_people = input(" Enter your name: ")
age_of_people = int(input(" Enter your age: "))
address_of_people = input("Enter your address: ")
email_of_people = input("Enter your email: ")
current_location = input(" Enter your location: ")
annual_income = int(input("💵 Enter your annual income: "))

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

# Displaying the final calculated tax amount

print("\n-----------------------------< 🧾 TAX SUMMARY >-----------------------------")
print(f"Your Name :{name_of_people}")
print(f"Your Age : {age_of_people}")
print(f"Your Location  : {current_location}")
print(f"Your Annual Income 💰: ₹{annual_income}")
print(f"Your Tax Payable🧾 : ₹{tax_amount}")


print("-----------------------< 😊 Thank you for using the Income Tax Calculator😊 >--------------------------------")

