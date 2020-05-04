from random import choice

questions = ["What is you favourite doll?: ","Why the sky is blue?: ",
             "Where are all the dinosaurs?:"]

question = choice(questions)

answer = input(question).lower().strip()

while answer !="just because":
    answer = input("why?: ").strip().lower()

print("Oh....Okay")
 
