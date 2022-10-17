

def say_hello():
    print("Hello")
def show_help():
    print("yout can add new venture, user and section")
def add_user(name="foo", age=42):
    print("Adding user", name, age)

commands = {
    "hello": say_hello,
    "help": show_help,
    "adduser": add_user,
    #TODO add more commands
}


def check_input():
    command = input("Enter command: ")
    # map to command
    if command in commands:
        if command == "adduser":
            commands[command]("foo", 42) # call with variables
        else:
            commands[command]()
    else:
        print("Invalid command")



