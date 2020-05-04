students = {
        "male":["Tom","Bob","Frank","Harry","Frank"],
        "female":["Sarah","Emma","Emily","Elizabeth","Huda"]
    }
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
