inputCommand = ""
while inputCommand != "quit" :
    inputCommand = input(" > ").lower()
    if inputCommand == "start":
        print("Car Started .... Ready To Go !!")
    elif inputCommand == "stop":
        print("Car Stopped .... What's Next !!")
    elif inputCommand == "exit":
        print("Exited!")
    elif inputCommand == "help" :
        print('''Start - Started Ready to Go 
        Stop - Car stopped .....
        Exit - Exited the car
        ''')
    else:
        print("Sorry I Don't Understand That")
