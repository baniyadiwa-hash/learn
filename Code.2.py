n1 = int(input("Enter youe code passwords: "))
Name = input("Enter your name: ")

def deaf(name, n1):
    if  n1 == 123456:
        print("Welcome", Name)
    
    else:
        print("Wrong password")

deaf(Name, n1)