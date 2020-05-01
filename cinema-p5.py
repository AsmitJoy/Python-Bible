films = {
        "Finding Dory": [3,5],
        "Inception":[55,3],
        "Tarzan":[18,6],
        "Evil Dead":[12,5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()
    
    if choice in films:
        age = int(input("How old are you?: ").strip())

        #check user age
        if age>=films[choice][0]:

            #check enough seats
            num_seats = films[choice][1]

            if num_seats >0:
            
               print("Enjoy the flim!")
               films[choice][1] = num_seats -1
            else:
                print("Sorry!! The room is full....")
            
        else:
            print("You are too young to watch the flim!")
    else:
        print("We don't have that film....")
