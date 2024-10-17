import arithmodule as ar
a=int(input("enter the first number:"))
b=int(input("enter the sec number:"))
while True:
    print("MENU")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.modulus")
    print("6.exponention")
    print("7.floor")
    print("8.exit")
    choice=int(input("enter your choice(1-7)"))
    if choice==1:
        print("addition:",ar.add(a,b))
    elif choice==2:
        print("subtraction:",ar.sub(a,b))
    elif choice==3:
        print("multiplication:",ar.mul(a,b))
    elif(choice==4):
        div=ar.div(a,b)
        print("division:",div)
    elif(choice==5):
           mod=ar.mod(a,b)
           print("modulus:",mod)
    elif(choice==6):
            ex=ar.exp(a,b)
            print("exponntion:",ex) 
    elif(choice==7):
            flo=ar.floor(a,b)
            print("floor:",flo) 
    elif choice==8:
            print("exiting")
            break

