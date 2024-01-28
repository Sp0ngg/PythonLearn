command = ""
started = False


while True:
    command = input("> ").lower()
    if command == "start":
        if started == False:
            print("Car started...")
            started = True
        else:
            print("The car is already started...")

    elif command == "stop":
        if not started:
            print("Car is already stopped...")
        else:
            print("Stopped the car...")
            started = False

    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit''')

    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")
        