import time

name = input("So, chap... What's your name? ")
confirm = input("So your name is " + name + "? Type yes or no to confirm. ")
if confirm == "yes":
    print("Oh, nice! Good to meet you, " + name + ".")
    time.sleep(2)
elif confirm == "no":
    print("Oops! Sorry about that.")
    time.sleep(2)
else:
    print("When I ask you to type yes or no, please type yes or no.")
    time.sleep(2)


