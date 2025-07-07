a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a car!")
    case 3:
        print("You won a bike!")
    case 6:
        print("You won a scooter!") 
    case _:
        print("better luck next time!")                 