import matplotlib
matplotlib.use('TkAgg')  # avoid non-GUI warning for matplotlib
import matplotlib.pyplot as plt
plt.rcParams['animation.writer'] = 'avconv'
from gym_maze.envs.maze import MazeEnv
from gym_maze.envs.generators import RandomMazeGenerator
from agents import *


width = height = 20
complexity = density = 1


if __name__ == '__main__':
    maze = RandomMazeGenerator(width, height, complexity, density)



    env = MazeEnv(maze, action_type='Moore', render_trace=False)
    env.reset()
    agent = AgentDemo(env)
    AgentDemo.Find_Direction(agent)





