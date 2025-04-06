def return_firstname():
    firstname = input("Please enter your first name: ")
    return firstname

def return_lastname():
    lastname = input("Please enter your last name: ")
    return lastname

def return_fullname():
    fullname = return_firstname() + " " + return_lastname()
    print (f"My full name is {fullname}")
    
return_fullname()