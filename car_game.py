started=False
while True:
    Enter = input('>')
    if Enter.upper() == "HELP":
        print("""
start - to start the car
stop - to stop the car 
quit - to exit
        """)
    elif Enter.upper() == "START":
        if started:
            print('Car already started!')
        else:
            started=True
            print('car is started...ready to go!')
    elif Enter.upper() == "STOP":
        if not started:
            print('car is already stopped!')
        else:
            started=False
            print('car stopped.')

    elif Enter.upper() == "QUIT":
        break
    else:
        print("I don't Understand that...")
