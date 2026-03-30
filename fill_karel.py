from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    # First check if the left is clear,then make the moves
   while left_is_clear():
        finish_one_row()
        move_to_next_row()
   laying_tiles()


         

def finish_one_row():
    laying_tiles()
    turn_around()
    move_to_wall()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def laying_tiles():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def turn_around():
    turn_left()
    turn_left()


def move_to_wall():
    while front_is_clear():
        move()

def move_to_next_row():
    turn_right()
    move()
    turn_right()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
