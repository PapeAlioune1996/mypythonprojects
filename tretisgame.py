import pygame
import random

# Initialisation de Pygame
pygame.init()


# Paramètres du jeu
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 500
GRID_SIZE = 25
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SHAPE_COLORS = [(0, 0, 0), (0, 255, 255), (255, 165, 0), (0, 0, 255), (255, 0, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0)]

# Formes des blocs
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
]

# Classe représentant le jeu Tetris
class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_shape = None
        self.current_shape_pos = (0, 0)
        self.current_shape_type = None
        self.score = 0

    def new_shape(self):
        self.current_shape_type = random.randint(0, len(SHAPES) - 1)
        self.current_shape = SHAPES[self.current_shape_type]
        self.current_shape_pos = (GRID_WIDTH // 2 - len(self.current_shape[0]) // 2, 0)

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(self.screen, SHAPE_COLORS[self.grid[y][x]], pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                pygame.draw.rect(self.screen, BLACK, pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    def draw_shape(self):
        for y in range(len(self.current_shape)):
            for x in range(len(self.current_shape[y])):
                if self.current_shape[y][x] == 1:
                    pygame.draw.rect(self.screen, SHAPE_COLORS[self.current_shape_type + 1],
                                     pygame.Rect((self.current_shape_pos[0] + x) * GRID_SIZE, (self.current_shape_pos[1] + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                    pygame.draw.rect(self.screen, BLACK,
                                     pygame.Rect((self.current_shape_pos[0] + x) * GRID_SIZE, (self.current_shape_pos[1] + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    def check_collision(self):
        for y in range(len(self.current_shape)):
            for x in range(len(self.current_shape[y])):
                if self.current_shape[y][x] == 1:
                    if self.current_shape_pos[0] + x < 0 or self.current_shape_pos[0] + x >= GRID_WIDTH or \
                       self.current_shape_pos[1] + y >= GRID_HEIGHT or self.grid[self.current_shape_pos[1] + y][self.current_shape_pos[0] + x] != 0:
                        return True
        return False

    def merge_shape(self):
        for y in range(len(self.current_shape)):
            for x in range(len(self.current_shape[y])):
                if self.current_shape[y][x] == 1:
                    self.grid[self.current_shape_pos[1] + y][self.current_shape_pos[0] + x] = self.current_shape_type + 1

    def check_lines(self):
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_to_clear.append(y)

        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
            self.score += 10

    def run(self):
        game_over = False
        self.new_shape()

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.current_shape_pos = (self.current_shape_pos[0] - 1, self.current_shape_pos[1])
                if self.check_collision():
                    self.current_shape_pos = (self.current_shape_pos[0] + 1, self.current_shape_pos[1])
            if keys[pygame.K_RIGHT]:
                self.current_shape_pos = (self.current_shape_pos[0] + 1, self.current_shape_pos[1])
                if self.check_collision():
                    self.current_shape_pos = (self.current_shape_pos[0] - 1, self.current_shape_pos[1])
            if keys[pygame.K_DOWN]:
                self.current_shape_pos = (self.current_shape_pos[0], self.current_shape_pos[1] + 1)
                if self.check_collision():
                    self.current_shape_pos = (self.current_shape_pos[0], self.current_shape_pos[1] - 1)
            if keys[pygame.K_UP]:
                new_shape = list(zip(*self.current_shape[::-1]))
                if self.current_shape_pos[0] + len(new_shape[0]) <= GRID_WIDTH and not self.check_collision():
                    self.current_shape = new_shape

            self.current_shape_pos = (self.current_shape_pos[0], self.current_shape_pos[1] + 1)
            if self.check_collision():
                self.current_shape_pos = (self.current_shape_pos[0], self.current_shape_pos[1] - 1)
                self.merge_shape()
                self.check_lines()
                self.new_shape()
                if self.check_collision():
                    game_over = True

            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_shape()
            pygame.display.set_caption(f"Tetris - Score: {self.score}")
            pygame.display.flip()
            self.clock.tick(5)

        pygame.quit()


if __name__ == "__main__":
    tetris = Tetris()
    tetris.run()
