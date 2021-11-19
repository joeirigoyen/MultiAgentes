from mesa import Agent, Model
from mesa.space import MultiGrid
from robot_agents import *
from random import randint


class RobotModel(Model):
    def __init__(self, agents: int, width: int, height: int, boxes: int) -> None:
        # Initialize attributes
        self.grid = MultiGrid(width, height, False)
        self.depots = dict()
        self.agents = agents
        self.width = width
        self.height = height
        self.boxes = boxes
        self.running = True
        # Create depot area (2x2)
        for i in range(2):
            for j in range(2):
                # Initialize depot
                depot = Depot(i, self)
                self.schedule.add(depot)
                # Add depot to grid
                self.grid.place_agent(depot, (i, j))
                self.depots[i * j + i] = (i, j)
        # Create boxes
        for i in range(boxes):
            # Initialize box
            box = Box(i, self)
            self.schedule.add(box)
            # Add box to grid
            while True:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
                if len(self.grid.get_cell_list_contents([(x, y)])) == 0:
                    self.grid.place_agent(box, (x, y))
                    break
        # Create robots
        for i in range(self.agents):
            # Initialize robot
            robot = Robot(i, self)
            self.schedule.add(robot)
            # Add robot to grid
            while True:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
                if len(self.grid.get_cell_list_contents([(x, y)])) == 0:
                    self.grid.place_agent(robot, (x, y))
                    break
    
    def step(self):
        self.schedule.step()
