# commands = help / start / stop / quit
# print("start - to start a car")
# print("stop - to stop a car")
# print("quit - to exit")

command = ""
input_help = "help"
input_start = "start"
input_stop = "stop"
input_quit = "quit"
last_command = ""
started = False

while True:
    command = input("> ")

    if command.lower() == input_help:
        print('''
start - to start a car
stop - to stop a car
quit - to exit
            ''')
    elif command.lower() == input_start:
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started .... ready to go")
    elif command.lower() == input_stop:
        if not started:
            print("Car is stopped")
        else:
            started = False
            print("Car stopped")
    elif command.lower() == input_quit:
        print("Exiting.....")
        break
    else:
        print("Incorrect of wrong command")
        print("... type help to know options")
print("Exiting...")
