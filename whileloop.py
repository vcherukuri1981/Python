name = input("Enter your name: ")
while name == "":
    print("Name cannot be empty")
    
    #name = input("Enter your name: ")
print("Hello", name.lower())


food = input("Enter your favorite food: q to quit: ")
while food.lower() != "q":
    print("Your favorite food is", food)
    food = input("Enter your favorite food: q to quit: ")
print("Bye")