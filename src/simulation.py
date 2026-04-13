import pygame
import numpy as np

class Simulation:
    def __init__(self):
        pygame.init()
        self.grid_size = 20
        self.cell_size = 30
        self.width = self.grid_size * self.cell_size
        self.height = self.grid_size * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("AI Autonomous Navigation Simulation")
        self.clock = pygame.time.Clock()
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        # Add obstacles
        self.grid[5:10, 5:10] = 1
        self.grid[12:15, 12:15] = 1
        self.grid[2, 10:15] = 1
        self.robot_pos = (0, 0)
        self.goal = (19, 19)

    def draw(self):
        self.screen.fill((255, 255, 255))
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                rect = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                if self.grid[i, j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)
                elif (i, j) == self.goal:
                    pygame.draw.rect(self.screen, (0, 255, 0), rect)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)  # Grid lines
        # Robot
        center = (self.robot_pos[1] * self.cell_size + self.cell_size // 2, self.robot_pos[0] * self.cell_size + self.cell_size // 2)
        pygame.draw.circle(self.screen, (255, 0, 0), center, self.cell_size // 2 - 5)
        pygame.display.flip()

    def update_robot(self, pos):
        if 0 <= pos[0] < self.grid_size and 0 <= pos[1] < self.grid_size and self.grid[pos] == 0:
            self.robot_pos = pos

    def is_goal_reached(self):
        return self.robot_pos == self.goal

    def close(self):
        pygame.quit()