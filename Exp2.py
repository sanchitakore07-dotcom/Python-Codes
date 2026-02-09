
# 💡 ELECTRICITY BILL CALCULATOR

print(">>============== USER DETAILS ==============<<")
print("🔴 Please fill in the following details carefully 🔴\n")

# ---------- User Input Section ----------
user_name = input("👤 Enter your name: ")
user_phonenum = input("📞 Enter your phone number: ")
user_email = input("📧 Enter your email  : ")
user_address = input("🏠 Enter your address : ")
user_electricityunit = float(input("💡 Enter electricity units: "))

# ---------- Electricity Bill Calculation ----------
rate_per_unit = 10  # ₹10 per unit
electric_bill = user_electricityunit * rate_per_unit

# ---------- Output Section ----------
print("\n--== ⚡ ELECTRICITY BILL SUMMARY ⚡ ==--\n")

print("💻 USER INFORMATION")
print(f"✅ Name          : {user_name}")
print(f"✅ Phone Number  : {user_phonenum}")
print(f"✅ Email         : {user_email}")
print(f"✅ Address       : {user_address}")

print("\n💰 BILL DETAILS")
print(f"🔹 Units Consumed : {user_electricityunit}")
print(f"🔹 Rate per Unit  : ₹{rate_per_unit}")
print(f"💡 Total Bill    : ₹{electric_bill} ❗")

print("\n>>>>> ✔ BILL GENERATED SUCCESSFULLY ✔ <<<<<")
print("⚠️ Please pay your electricity bill on time ⚠️")
print("============================================")

