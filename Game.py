# An adventure game

import time

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
        part2_room1()
    if direction.lower() == "2":
        print("""
        You ignore her and walk up to the huge door. You give a
        quick glance behind you to see that she is not very
        happy with you ignoring her, she drives off with the
        same expression.""")
        part2_room1()

def part2_room1():
    global time
    
    print("""
    You feel a bit intimidated by the huge door and have to stand there
    for a second""")
    print(" 1: Knock on the door")
    print(" 2: Wait")
    direction = input("option:  ")
    if direction.lower() == "1":
        print("""
        You are greeted by your friend John""")
        part3_room1()
    if direction.lower() == "2":
        print("""
        You wait outside the whole night in the cold and dark. You get
        picked up the next day. You didnt progress the story at all.
        GAME OVER!""")
        time.sleep(2)
        quit()

def part3_room1():

    print("""
    John has been your best friend for as long as you can remember. You had done everything together
    from playing video games to going to school together.""")
    print(" 'Hay. You tuck sometime to get here, you ok?' John said in unusual happy manner")
    print(" 1: Yeah it was just the traffic. You know this city")
    print(" 2: You seem happy today do you.")
    direction = input("option:  ")
    if direction.lower() == "1":
        print("""
        'Yeah, I guess your right. Come in' You step into the house and look around. The
        rooms of the house are huge, with enough space to fit a truck in.""")
    if direction.lower() == "2"
        print("""
        He looked at you, now with a surprised look on his face. 'What a guy can't be happy
        when his friend comes to sleep over? Never mind just come inside' You step into the house and look around. The
        rooms of the house are huge, with enough space to fit a truck in.""")

    def part4_room1():

        print("""
        You sat down in the living room while John goes upstairs to get his nintendo console
    







# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()

