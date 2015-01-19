global loginname
import os.path

def login():
    global loginname
    import os.path
    print("CodeXOS - It's cool or something.")
    print("")
    print("")
    if os.path.isfile("users"):
        fo = open('users', 'r')
        loginname = fo.read()
        print("Welcome back to CodeXOS, " + loginname + "! What would you like to do?")
        print("")
        mainstuff()
    else:
        loginname = input("Please enter your username. ")
        fo = open('users', 'w')
        fo.write(loginname)
        fo.close()
        print("Welcome to CodeXOS, " + loginname + "! From here, you can do some things. What would you like to do?")
        print("")
        mainstuff()

def mainstuff():
    global loginname
    print("Type \"Hey there\" to do something. Or type \"Log out\" to log out of CodeXOS.")
    action = input("")
    if action == "Hey there":
        print("Boom!")
        mainstuff()
    elif action == "Log out":
        print("Are you sure you want to log out? Type yes or no to confirm. ")
        logout = input("")
        if logout == "yes":
            print("Bye, " + loginname + "! See you soon!")
        elif logout == "no":
            print("Sorry about that, " + loginname + ".")
            mainstuff()
        else:
            print("I'm sorry, " + loginname + ", but I don't understand that.")
            mainstuff()
    elif action == "Major Adventure" or action == "Major adventure" or action == "major adventure":
        import game
    else:
        print("I'm sorry, " + loginname + ", but I don't understand that.")
        mainstuff()

if __name__ == '__main__': login()