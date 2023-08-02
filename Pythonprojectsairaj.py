import string
def passwordstrength():
    print("Password Strength Checker:-" )
    password = input("Enter Password =")
    password1 = password2 = password3 = password 
    strength = 0
    loweralp=capalp=special=numc=0
    for char in password:
        if char in string.ascii_lowercase:
            loweralp = +1
        elif char in string.ascii_uppercase:
            capalp = +1
        elif char in string.digits:
            numc = +1
        else:
            special = +1
    if len(password)>8:
        strength = strength +1  
    if loweralp>=1:
        strength = strength +1
    if capalp>=1:
        strength = strength +1
    if numc>=1:
        strength = strength +1
    if special>=1:
        strength = strength +1
    
    if strength ==1:
        print("\nVERY WEAK PASSWORD!")
    if strength == 2:
        print("\nWEAK PASSWORD")
    if strength ==3:
        print("\nDECENT PASSWORD")
    if strength == 4:
        print("\nGOOD PASSWORD")
    if strength == 5:
        print("\nEXCELLENT PASSWORD!")
        exit()
    
    q = input("\nSuggest a stronger password?\n1 for yes\n2 for No=\n")
    if q == "1":
        for char in password:
            if char in string.ascii_lowercase:
                password = password.capitalize()
                password1 = password2 = password3 = password 
        password1 = "@" + password1 +"126"
        password2 = "#" + password2 +"072"
        password3 = password3 + "@" + "3423"        
        print("Following are Stronger Password related to your passwords=\n")
        print("1)",password1 +"\n")
        print("2)",password2,"\n")
        print("3)",password3,"\n")

    if q =="2":
        print("Thank You!")
        exit()

passwordstrength()