import matplotlib
matplotlib.use('TkAgg')  # avoid non-GUI warning for matplotlib
import matplotlib.pyplot as plt
plt.rcParams['animation.writer'] = 'avconv'
from colorama import Fore
from colorama import Style
import random
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


class Agent(object):

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    WALL = -1
    GOAL = 3

    def __init__(self, maze_env):
        super(Agent, self).__init__()
        self.virtual = True  # we are working with a virtual maze if false we are working with the real robot
        self.maze_env = maze_env
        self.counter = 0
        self.debug = 1
        """ROBOT VARIABLES BELOW :"""
        self.previous_direction = 0
        self.direction = 0

    """
        
    MAZE FUNCTIONS
         
         
    """

    def look(self, direction):  # stays
        # maze look
        # get sensor information
        # return the info to the user or move function
        done = 0
        if direction != -1:
            direction = self.re_direct(direction)
            if direction > 4:
                raise TypeError('direction must be [0, 1, 2, 3]')

            if self.virtual:
                # return maze magic
                reward, done, state = self.maze_env.look(direction)  # returns reward, done and state
                if done == 1:
                    self.counter = 0
                return reward, done, state

            else:
                # return robot magic
                print('robot')

    def print_maze(self, maze):  # TODO : Put somewhere else ?

        for row in maze:

            for number in row:
                if number == 1:
                    # print(str(number) + str(number), end="", flush=True)
                    print('1', end="", flush=True)
                elif number == 2:
                    print(f'{Fore.BLUE}' '2', end="", flush=True)
                    print(f'{Style.RESET_ALL}', end="", flush=True)
                elif number == 3:
                    print(f'{Fore.GREEN}' + '3', end="", flush=True)
                    print(f'{Style.RESET_ALL}', end="", flush=True)
                elif number == 0:
                    print(f' ', end="", flush=True)
            print('')

    def step(self, direction):  # stays
        if direction != -1:
            # call maze actions
            if self.virtual:
                # do maze magic
                obs, _, _, self.location = self.maze_env.step(direction)
                # print(self.location)
                if self.debug:
                    self.print_maze(obs)

                # self.maze_env.render()
            else:
                # do robot magic
                self.Robot.step(direction)
                print()

    def move(self):  # stays but is empty
        # movement logic
        # all your loops
        # throw an error.
        raise NotImplementedError('implement this in your own Agent class')

    """
    
    ROBOT FUNCTIONS
     
    """

    def robot_look(self, direction):
        # uses open CV to recognize shapes in the environment
        return direction

    def robot_step(self, robot: cozmo.robot.Robot):

        if not robot.is_cliff_detected:
            robot.drive_straight(distance_mm(50), speed_mmps(70)).wait_for_completed()
        else:
            print('cliff detected')

    '''                    
     
    
     
     USEFUL FUNCTIONS BELOW FO THE MAZE         
    
    
    
    
    '''
    # TODO : Find a way to put them in an other file

    def number_to_name(self, direction):
        """ converts int into string """
        direction_name = ''
        if direction == 0:
            direction_name = 'north'
        if direction == 1:
            direction_name = 'east'
        if direction == 2:
            direction_name = 'south'
        if direction == 3:
            direction_name = 'west'
        return direction_name

    def re_direct(self, direction):
        """ redirect the direction if > 3 """
        while direction > 3:
            direction = direction - 4
        return direction

    def only_one_possibility(self, direction):

        """ goes to the only possibility, returns which direction to go """

        if self.look(direction + 1)[0] == 0:  # if can go right
            direction = direction + 1  # go right
        elif self.look(direction + 3)[0] == 0:  # if can go left
            direction = direction + 3  # go left
        elif not self.look(direction)[0] == 0:
            direction = direction + 2  # go back

        return self.re_direct(direction)

    def check_possibilities(self, direction):
        """ Checks the number of possible directions and returns it"""

        possibilities = 0

        if self.look(direction)[0] == 0:  # if can go forward
            possibilities += 1
        if self.look(direction + 1)[0] == 0:  # if can go right
            possibilities += 1
        if self.look(direction + 3)[0] == 0:  # if can go left
            possibilities += 1
        if self.look(direction + 2)[0] == 0:  # if can go back
            possibilities += 1

        return possibilities

    def choose_random_direction(self, direction, path, intersection_count):

        """ Goes to 'direction' until an intersection, then chooses a random direction among different possibilities """
        """ Records the path and count the number of intersections """
        possibilities = self.check_possibilities(direction)

        if possibilities == 1:  # if dead end (the only possibility is to go back)
            direction = direction + 2  # go back

        elif possibilities == 2:  # if only one other possibility than going back
            direction = self.only_one_possibility(direction)  # go for it

        else:  # if multiple possibilities
            direction = direction + random.choice(seq=[0, 1, 3])  # pick random forward, right, left
            intersection_count += 1
            path.append('intersection ' + str(intersection_count))
        return self.re_direct(direction), intersection_count

    def follow_right_side(self, direction):

        """ follows the right hand side of the wall, returns the direction """

        if self.look(direction+1)[0] == -1:  # if can't go right

            if self.look(direction + 3)[0] == 0:  # if can go left
                direction = direction + 3  # go left
            elif not self.look(direction)[0] == 0:
                direction = direction + 2  # go back
        else:
            direction = direction + 1  # go right

        return self.re_direct(direction)

    '''                    



     USEFUL FUNCTIONS BELOW FOR THE ROBOT         




    '''

    def robot_move(self, robot: cozmo.robot.Robot, direction=None):
        if direction is None:
            direction = self.direction

        # turns the robot 90 degree left or right or 180 degree (back)
        if direction - self.previous_direction == 1:
            robot.turn_in_place(degrees(-90)).wait_for_completed()  # turn right
        elif direction - self.previous_direction == abs(2):
            robot.turn_in_place(degrees(180)).wait_for_completed()  # turn back
        elif self.previous_direction != direction:
            robot.turn_in_place(degrees(90)).wait_for_completed()  # turn left
        self.robot_step(self.robot)


