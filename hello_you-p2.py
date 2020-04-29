#Ask user for name

name = input("What is your name ? : ")

#Ask the user for age

age = input("How old are you ? : ")

#Ask user for city
city = input("What city do you live in ? : ")

#Ask user what they enjoy

love = input("What do you love doing ? : ")

#Ask user for city
player = input("Who is your favourite player ? : ")

#Create output text

string  = "Your name is {} and you are {} years old. You live in {} and you love {}. Your favourite player is {}"
output =  string.format(name,age,city,love, player)
 
#Print output to screen

print(output)
