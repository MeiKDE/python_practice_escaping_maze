#Reeborg's World
#Escape the maze!
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal(): 
    if (right_is_clear()==True) and front_is_clear()==True:
        move()
    elif front_is_clear()==True:
        move()
        if right_is_clear()==True:
            turn_right()
    elif wall_in_front()==True:
        turn_left()
    else:
        done()