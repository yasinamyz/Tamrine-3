Name = input("Enter your First name:")
Family = input("Enter your Family name:")
A = int(input("Enter A lesson:"))
B = int(input("Enter B lesson:"))
C = int(input("Enter C lesson:"))
Average = (A + B + C)/3

if Average == 17 and Average > 17:
    print(Name , Family , "Great")
    if Average == 12 and Average > 12 and Average < 17:
        print(Name , Family , "Normal")
    if Average < 12:
         print(Name , Family , "Fail")