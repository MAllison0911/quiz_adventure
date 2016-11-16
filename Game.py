# An adventure game

def room1():
    global health

    print(" You arrive at your friends house after a long trip.")
    print("""
    'I'll pick you up at 8 tommorow morning' your mother shouted as she
    watched you head up the drive""")
    print(" 1: Wave goodbye")
    print(" 2: Ignore")
    direction = input("option:  ")

    if direction.lower() == "1":
        print("""
        You wave back and watch her drive off down the street then you
        walk up to huge door of your friends house""")
    if direction.lower() == "2":
        print("""
        You ignore her and walk up to the huge door. You give a
        quick glance behind you to see that she is not very
        happy with you ignoring her, she drives off with the
        same expression.""")








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()

