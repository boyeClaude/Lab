def checkUsernameLength(username): # type: ignore
    if len (username) <= 3: # type: ignore
        print("Username must more than three characters")
    else:
        print("sucess")


output =  checkUsernameLength("Claude")

##elif statements
def checkAge(age):# type: ignore
    if age <= 5 :
        print("child")
    elif age >=6 and age < 18:
        print("Hum tu deviens l'homme")
    else:
        print("amonann hein")


checkAge(18)