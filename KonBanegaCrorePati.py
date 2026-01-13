# KBC Game (Options 1-4)

questions = [
    ["What is the capital of India ?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    ["Which language is used for web development ?", "Python", "HTML", "Java", "All of these", 2],
    ["Who is known as the father of computers ?", "Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs", 1],
    ["Which data type is immutable in Python ?", "List", "Set", "Dictionary", "Tuple", 4],
    ["What is the capital of India ?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2]
]

levels = [1000, 2000, 3000, 5000, 10000]
money = 0

for i in range(len(questions)):
    q = questions[i]

    print(f"\nQuestion for Rs.{levels[i]}")
    print(q[0])
    print("1.", q[1], "   2.", q[2])
    print("3.", q[3], "   4.", q[4])

    reply = int(input("Enter your option (1-4): "))

    if reply == q[5]:
        print(f"Correct! You won Rs.{levels[i]}")
        money = levels[i]
    else:
        print("Wrong Answer!")
        break

print(f"\nYou take home Rs.{money}")
