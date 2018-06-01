def go_direction(self, direction):
    # follow the right side of the wall
    # returns which direction to go
    # north = 0 ; east = 1 ; south = 2 ; # west = 3

    if self.look(self.re_direct(direction))[0] == -1:  # if we can't go forward

        if self.look(self.re_direct(direction + 1))[0] == 0:  # If we can go right
            direction = self.re_direct(direction + 1)  # We go right
            print('we turn right')
        elif self.look(self.re_direct(direction + 3))[0] == 0:  # If we can go left
            direction = self.re_direct(direction + 3)  # We go left
            print('we turn left')
        else:
            direction = self.re_direct(direction + 2)  # We go back
            print('we turn back')

    if direction == 0:
        print("we go north")
    elif direction == 1:
        print("we go east")
    elif direction == 2:
        print("we go south")
    else:
        print("we go west")

    return direction