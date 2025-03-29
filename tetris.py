import pygame
from random import choice, randint
import sys

pygame.init()

class TetrisApp:
    TILE_SIZE = 30
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20

    COLORS = [
        (0, 0, 0),  # 검은색 (빈 공간)
        (255, 255, 255),  # 흰색
        (0, 0, 255),  # 파란색
        (255, 165, 0),  # 주황색
        (0, 255, 255),  # 청록색
        (255, 0, 255),  # 마젠타
        (255, 0, 0),  # 빨간색
        (0, 255, 0),  # 녹색
        (255, 255, 0)  # 노란색
    ]

    SHAPES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1, 1],  # T
         [0, 1, 0]],
        [[0, 1, 1],  # S
         [1, 1, 0]],
        [[1, 1, 0],  # Z
         [0, 1, 1]],
        [[1, 1],  # ㅁ
         [1, 1]],
        [[1, 1, 1],
         [1, 0, 0]],
        [[1, 1, 1],
         [0, 0, 1]]
    ]

    def __init__(self):
        self.width = TetrisApp.TILE_SIZE * TetrisApp.BOARD_WIDTH
        self.height = TetrisApp.TILE_SIZE * TetrisApp.BOARD_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tetris')

        self.clock = pygame.time.Clock()
        self.board = [[0] * TetrisApp.BOARD_WIDTH for _ in range(TetrisApp.BOARD_HEIGHT)]
        self.current_piece = None
        self.current_piece_color = None
        self.current_piece_x = 0
        self.current_piece_y = 0
        self.game_over = False

        self.new_piece()

    def new_piece(self):
        self.current_piece = choice(TetrisApp.SHAPES)
        color_index = randint(1, len(TetrisApp.COLORS) - 1)
        self.current_piece_color = TetrisApp.COLORS[color_index]
        self.current_piece_x = TetrisApp.BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw_tile(self, x, y, color):
        rect = pygame.rect.Rect(
            (x * TetrisApp.TILE_SIZE,
             y * TetrisApp.TILE_SIZE,
             TetrisApp.TILE_SIZE,
             TetrisApp.TILE_SIZE)
        )
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, (128, 128, 128), rect, 1)


    def draw(self):
        self.screen.fill((0,0,0))
        self.draw_tile(0, 0, (255, 255, 255))

        if self.current_piece:
            for

            pygame.display.flip()
        
    def run(self):
        while not self.game_over:
            self.handle_input()
            self.update()
            self.draw()

def main():
    app = TetrisApp()
    app.run()

if __name__ == '__main__':
    main()

