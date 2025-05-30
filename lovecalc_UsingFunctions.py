# def calculate_love_score(name1,name2):
#     combined_names = name1+name2.lower()
#     true_count = sum(combined_names.count(letter) for letter in "true")
#     love_count = sum(combined_names.count(letter) for letter in "love")
#     love_score = int(str(true_count)+str(love_count))
#     return f"Your love score is {love_score}"

# if __name__ == "__main__":
#     print("Welcome to the Love Calculator!")
#     name1 = input("What is your name? ")
#     name2 = input("What is their name? ")
#     print(calculate_love_score(name1, name2))


def calculate_love_score(name1, name2):
    combined_names = name1 + name2.lower()
    t = combined_names.count('t')
    r = combined_names.count('r')
    u = combined_names.count('u')
    e = combined_names.count('e')
    first_part = t + r + u + e
    l = combined_names.count('l')
    o = combined_names.count('o')
    v = combined_names.count('v')
    #print(f"v={v}")
    e = combined_names.count('e')
    #print(e)
    second_part = l + o + v + e
    love_score = int(str(first_part) + str(second_part))
    print( {love_score})

if __name__ == "__main__":  
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? ")
    name2 = input("What is their name? ")
    calculate_love_score(name1, name2)