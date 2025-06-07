import pygame
import random
from dataclasses import dataclass

@dataclass
class Config:
    width: int = 400
    height: int = 400
    block_size: int = 20
    fps: int = 10

class SnakeGame:
    def __init__(self, config: Config = Config()):
        self.config = config
        pygame.init()
        self.screen = pygame.display.set_mode((config.width, config.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.snake = [(self.config.width // 2, self.config.height // 2)]
        self.direction = (self.config.block_size, 0)
        self.spawn_food()
        self.alive = True

    def spawn_food(self):
        grid_x = self.config.width // self.config.block_size
        grid_y = self.config.height // self.config.block_size
        while True:
            pos = (
                random.randrange(grid_x) * self.config.block_size,
                random.randrange(grid_y) * self.config.block_size,
            )
            if pos not in self.snake:
                self.food = pos
                return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.alive = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, self.config.block_size):
                    self.direction = (0, -self.config.block_size)
                elif event.key == pygame.K_DOWN and self.direction != (0, -self.config.block_size):
                    self.direction = (0, self.config.block_size)
                elif event.key == pygame.K_LEFT and self.direction != (self.config.block_size, 0):
                    self.direction = (-self.config.block_size, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-self.config.block_size, 0):
                    self.direction = (self.config.block_size, 0)

    def move(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        # Check wall collision
        if (
            new_head[0] < 0
            or new_head[0] >= self.config.width
            or new_head[1] < 0
            or new_head[1] >= self.config.height
            or new_head in self.snake
        ):
            self.alive = False
            return
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for x, y in self.snake:
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                pygame.Rect(x, y, self.config.block_size, self.config.block_size),
            )
        fx, fy = self.food
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            pygame.Rect(fx, fy, self.config.block_size, self.config.block_size),
        )
        pygame.display.flip()

    def run(self):
        while self.alive:
            self.clock.tick(self.config.fps)
            self.handle_events()
            self.move()
            self.draw()
        pygame.quit()

