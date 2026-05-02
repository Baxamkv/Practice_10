import pygame
from settings import *
from sprites2 import *
from random import randint

class Game:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(size=70)
        self.font_pause = pygame.font.Font(size=120)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.orientation = 0
        self.pause = False
        self.restart_text = self.font_pause.render("RESTART", True, (255, 255, 200))
        self.restart_text_rect = self.restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))

    def new(self):
        self.orientation = 0
        self.all_sprites = pygame.sprite.Group()
        self.head = Snake(self, 5, 5)
        self.snake_parts = []
        self.snake_parts.append(Snake(self, 4, 5))
        self.snake_parts.append(Snake(self, 3, 5))

        self.food = Food(self, randint(0, WIDTH//TILE_SIZE - 1), randint(0, HEIGHT//TILE_SIZE - 1))
        self.food.is_golden(randint(0, 1))



    def run(self):
        self.playing = True
        while True:
            while self.playing:
                self.clock.tick(SPEED)
                self.events()
                self.update()
                self.draw()
            game_over_text = self.font_pause.render("GAME OVER", True, (255, 255, 255))
            while not self.playing:
                self.screen.fill(RED)
                self.screen.blit(game_over_text, game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
                self.screen.blit(self.restart_text, self.restart_text_rect)
                self.events()
                pygame.display.update()
            self.new()




    def quit(self):
        pygame.quit()
        quit(0)

    def is_body_part(self):
        while True:
            x = randint(0, WIDTH // TILE_SIZE - 1)
            y = randint(0, HEIGHT // TILE_SIZE - 1)
            for body in self.snake_parts:
                if body.x != x and body.y != y:
                    return (x, y)
    def update(self):
        if not self.pause:
            if (self.head.x >= GRIDWIDTH - 1) or self.head.x < 0 or (self.head.y > GRIDHEIGHT - 1) or self.head.y < 0:
                self.playing = False

            if self.food.food_collision():
                x, y = self.is_body_part()
                if self.food.color == GOLD:
                    self.snake_parts.append(Snake(self, self.snake_parts[-1].x, self.snake_parts[-1].y))
                if randint(1, 5) % 5 == 0:
                    self.food.is_golden(True)
                else:
                    self.food.is_golden(False)
                self.food.x, self.food.y = x, y

                self.snake_parts.append(Snake(self, self.snake_parts[-1].x, self.snake_parts[-1].y))
            self.all_sprites.update()

            x, y = self.head.x, self.head.y
            for body in self.snake_parts:
                temp_x, temp_y = body.x, body.y
                body.x, body.y = x, y
                x, y = temp_x, temp_y


            if self.orientation == 0:
                self.head.x += 1
            elif self.orientation == 1:
                self.head.y -= 1
            elif self.orientation == 2:
                self.head.x -= 1
            elif self.orientation == 3:
                self.head.y += 1

            #checking whether it is body collision
            for body in self.snake_parts:
                if body.body_collision():
                    self.playing = False

    def draw_grid(self):
        for row in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, DARKGRAY, (0, row), (WIDTH, row))
        for col in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, DARKGRAY, (col, 0), (col, HEIGHT))

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.all_sprites.draw(self.screen)
        self.food.update()
        self.screen.blit(self.food.image, self.food.image_rect)
        self.draw_grid()
        self.screen.blit(self.font.render(f"SCORE: {len(self.snake_parts) + 1}", True, (255, 255, 255)),(0, 0))
        if self.pause:
            pause_text = self.font_pause.render("Paused", True, (255, 255, 255))
            self.screen.blit(pause_text, pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if not self.orientation == 3:
                        self.orientation = 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if not self.orientation == 1:
                        self.orientation = 3
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if not self.orientation == 2:
                        self.orientation = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if not self.orientation == 0:
                        self.orientation = 2
                elif event.key == pygame.K_SPACE and self.playingw:
                    self.pause = not self.pause
            if not self.playing:
                x, y = pygame.mouse.get_pos()
                if self.restart_text_rect.collidepoint(x, y):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.playing = True




game = Game()
game.new()
game.run()