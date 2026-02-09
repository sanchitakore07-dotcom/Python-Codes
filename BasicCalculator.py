from unittest import case

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter a choice: "))

match choice:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
         print(num1/num2)
    case _:
        print("invalid choice")


