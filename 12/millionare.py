questions = [
    ["Who is Virat Kohli?" ,"Actor","Cricketer","Fighter","Delhi",2],
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Who invented the light bulb?", "Newton", "Edison", "Einstein", "Tesla", 2],
    ["What is H2O commonly known as?", "Oxygen", "Hydrogen", "Water", "Acid", 3],
    ["What is the national animal of India?", "Tiger", "Lion", "Elephant", "Peacock", 1],
    ["Which gas do humans need to breathe?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Helium", 1],
    ["How many days are there in a leap year?", "365", "366", "364", "367", 2],
    ["Which is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
    ["Who is known as the Father of the Nation in India?", "Bhagat Singh", "Mahatma Gandhi", "Jawaharlal Nehru", "Subhash Chandra Bose", 2]
]

prizes=[10000,1000000,10000000,10000000,100000,10000000,10000]
sum=0
i = 0
for q in questions:
    
    print(q[0])
    print(f"1. {q[1]}")
    print(f"2. {q[2]}")
    print(f"3. {q[3]}")
    print(f"4. {q[4]}")

    ans = int(input("Enter your answer (1-4): "))

    if q[5] == ans:
        print("✅ Correct answer!\n")
    else:
        print(f"❌ Incorrect answer! The correct answer is option {q[5]}: {q[q[5]]}\n")
        break
    sum+=prizes[i]
    print("You won{i}")
    i+=1
