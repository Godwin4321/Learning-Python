# start --> Car started...Ready to go!
# stop --> Car stopped.
# quit --> program finished
# help --> will show all the commands
# other commands --> I don't understand that...

command = ""
started = False

while True:
        command = input("> ").lower()
        if command == "start":
            if started:
                print("Car already started")
            else:
                print("Car started...Ready to go!")
                started = True
        elif command == "stop":
            if not started:
                print("Start the car first, once the car is started then you can stop")
            else:
                print("Car stopped.")
                started = False
        elif command == "help":
            print("start - to start the car")
            print("stop - to stop the car")
            print("quit - to quit")
        elif command == "quit":
            break
        else:
            print("I don't understand that...")