known_users = ["Messi","Ronaldo","Marcelo","Ozil","Kaka","Ronaldinho"]

while True:
    print("Hi, My name is Joy")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello!, {} ".format(name))
        remove = input("Would you like to be removed from the systen(y/n)?: ").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I did'nt want you to leave anyway!")

    else:
        print("Hmmm I don't think i have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system(y/n):").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries. see you around!")   
    
