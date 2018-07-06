from .Agent import *
import random


class AgentDemo(Agent):
    def __init__(self, maze_env):
        super(AgentDemo, self).__init__(maze_env)
        self.virtual = True  # we are working with a virtual maze
        self.maze_env = maze_env
        self.counter = 0

    def move(self):
        for i in range(0,4):
            self.step(0)

    def Find_Direction(self):
        self.look(0)
        while (self.look(1)[0] != 3 and self.look(0)[0] != 3 and self.look(2)[0] != 3 and self.look(3)[0] != 3):
            x = random.randint(0,3)

            if not self.look(x)[0] == -1:
                self.step(x)


























