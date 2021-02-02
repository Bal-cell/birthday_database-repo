birthday = {"anna":"1st april","harry":"2nd april","ron":"3rd april"}
while True:
    name = input("enter your name to check: ")
    if name in birthday:
        print(name +"'s birthday is " + birthday[name])
    else:
        print("not in the data base but can be added: ")
        check = input("do you want to add 'y' for yes and 'n' for no: ")
        if check.lower() == "y":
            name1 = input("enter name to add: ")
            date = input("enter his/her date of birth: ")
            birthday[name1] = date
        else:
            break
  
