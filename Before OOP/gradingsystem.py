def get_grade(score):
    if score>=70 and score<=100:
        print("You get and an A")
        return "A"
    elif score>=60 and score<=69:
        print("You get and an B")
        return "B"
    elif score>=50 and score<=59:
        print("You get and an C")
        return "C"
    elif score>=45 and score<=49:
        print("You get and an D")
        return "D"
    elif score>=40 and score<=44:
        print("You get and an E")
        return "E"
    elif score>=0 and score<=39:
        print("You get and an F")
        return "F"
    else:
        return "Invalid Score"
    
score= int(input("Enter your score: "))
grade= get_grade(score)
print(f"Grade: {grade}")