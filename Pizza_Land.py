print("---------------------------*******************************---------------------------")
print("WELCOME TO THE PIZZA LAND ;)   ")
print("---------------------------*******************************---------------------------")

while(1):
    print("What would you like to have \n1. Tandoori paneer pizza\n2. Paneer makhani pizza\n")
    ch=int(input("Enter your choice :-"))
    if(ch==1):
        print("Sizes Available for Tandoori paneer pizza---->\n1. small\n2. large ")
        n=int(input("Enter the size(1-2):- "))
        if(n==1):
            a=input("Would you like to add extra toppings for your small size Tandoori paneer pizza(y/n) :- ")
            if(a=='y'):
                b=int(input("which toppings you would like to add \n1.Extra cheese\n2. Extra paneer\n enter:-"))
                print("Your small size Tandoori paneer pizza with ",b,"is on your way......")
                print("...........loading.............")
            
            else:
                print("Your small size Tandoori paneer pizza is on your way......")
                print("...........loading.............")
            
            x=input("Would you like to order anything more...(y/n):-")
            if(x=='n'):
                print("Thanking for purchasing from Pizza Land :)  ")
                break
            
        if(n==2):
            a=input("Would you like to add extra toppings for your Large size Tandoori paneer pizza(y/n) :- ")
            if(a=='y'):
                b=int(input("which toppings you would like to add \n1.Extra cheese\n2. Extra paneer\n enter:-"))
                print("Your Large size Tandoori paneer pizza with ",b,"is on your way......")
                print("...........loading.............")
            
            else:
                print("Your Large size Tandoori paneer pizza is on your way......")
                print("...........loading.............")
            
            x=input("Would you like to order anything more...(y/n):-")
            if(x=='n'):
                print("Thanking for purchasing from Pizza Land :)  ")
                break
            
    
    else:
        print("Invalid")
