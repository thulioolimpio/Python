first_question = input("You wake up in a dark room with no memory of how you got there. You see a door in front of you and a window on the side.Do you want to try to open the DOOR or check out the WINDOW? ")

if first_question.lower() == "door" :
    print("You try to open the door, but it's locked. You notice a keyhole and a note on the door that says 'Find the key to escape'. You search the room and find a piece of paper with a riddle that leads to the location of the key. You solve the riddle and find the key. You unlock the door and escape to outside.There are two paths outside: one leading to a RIVER and the other to some TRESS. Which path do you want to take? ")
elif first_question.lower() == "window" :
    print("You look out the window and notice that you are on the second floor of a building. You see a tree outside that you think you could climb down. You jump out the window and start climbing down the tree. You hear a noise and turn around to see a group of people chasing you. You continue to climb down and escape, but you realize that you are in the middle of a forest with no idea where to go.Do you want to RUN, or HIDE behind a tree")
else:
    print("Invalid option. Please choose a valid option.")