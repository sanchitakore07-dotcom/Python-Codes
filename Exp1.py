
# 🏢 EMPLOYEE SALARY MANAGEMENT SYSTEM

print("━━━━━━━━━━━━━━ 🧾 EMPLOYEE DETAILS 🧾 ━━━━━━━━━━━━━━\n")
print("🔴 Please fill in the following details carefully 🔴\n")

# ---------- Employee Input Section ----------
employee_name = input("👤 Enter employee name: ")
employee_age = int(input("🎂 Enter employee age: "))
employee_phonenum = input("📞 Enter employee phone number: ")
employee_address = input("🏠 Enter employee address: ")
employee_email = input("📧 Enter employee email: ")
employee_salary = int(input("💰 Enter employee base salary: "))

# ---------- Salary Calculation Section ----------
interest_rate = 5          # 5% interest
time_period = 1            # 1 year
bonus = 2000               # Fixed bonus amount

interest = (employee_salary * interest_rate * time_period) / 100
total_salary = employee_salary + bonus + interest

# ---------- Output Section ----------
print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print("👩‍💻 YOUR EMPLOYEE PROFILE 👩‍💻\n")

print(f"✅ Employee Name      : {employee_name}")
print(f"✅ Employee Age       : {employee_age}")
print(f"✅ Phone Number       : {employee_phonenum}")
print(f"✅ Address            : {employee_address}")
print(f"✅ Email              : {employee_email}")

print("\n💼 SALARY DETAILS 💼")
print(f"🔹 Base Salary        : ₹{employee_salary}")
print(f"🎁 Bonus Added        : ₹{bonus}")
print(f"📈 Interest (5%)      : ₹{interest}")

print("\n💸 TOTAL SALARY 💸")
print(f"✨ Final Salary Payable: ₹{total_salary}")

print("\n━━━━━━━━━━━━━━ 🎉 THANK YOU 🎉 ━━━━━━━━━━━━━━")

