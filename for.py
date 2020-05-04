vowels = 0
consonants = 0

txt = input("Please enter any text: ").strip()

for  letter in txt:
    if letter.lower() in "aeiou":
        vowels = vowels +1
    elif letter == "":
        pass
    else:
        consonants = consonants +1

print("There are {} vowels ".format(vowels))

print("There are {} consonants ".format(consonants))

