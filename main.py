import pygame
from enum import Enum

pygame.mixer.init(44100, -16, 2, 2048)

pygame.init()

class State(Enum):
    EMPTY = 0
    CROSS = 1
    CIRCLE = 2

class Element:
    def __init__(self, screen: pygame.Surface,blockSize: int, blockNumber: int) -> None:
        self.blockSize = blockSize
        self.blockNumber = blockNumber
        self.screen: pygame.Surface = screen
        self.rectangle: pygame.Rect = pygame.Rect((0, 0, self.blockNumber*2, self.blockSize*2))
        self.rectangle.center = (self.blockSize*2, self.blockSize*2)
        return
    def draw(self) :
        pygame.draw.rect(self.screen, "white", self.rectangle)
        return


class Board:
    def __init__(self, screen: pygame.Surface, blockSize: int, blockNumber: int) -> None:
        self.screen: pygame.Surface = screen 
        self.blockSize: int = blockSize
        self.blockNumber: int = blockNumber
        self.font: pygame.font.Font = pygame.font.Font('freesansbold.ttf', 38)
        self.matrix = [['X','O','O'], ['O','X','O'], ['O','O','X']]
        self.element: Element = Element(self.screen, self.blockSize, self.blockNumber) 
        return
    def turns(self):
        for i in range(3):
            for j in range(3):
                text = self.font.render(str(self.matrix[i][j]), True, "white")
                textRect = text.get_rect()
                textRect.center = (250 + (j*100), 250 + (i*100))
                self.screen.blit(text, textRect)
        return
    def table(self):
        # lines
        pygame.draw.line(self.screen, "white", (self.blockSize*3, self.blockSize*2), (self.blockSize*3, self.blockSize*5))
        pygame.draw.line(self.screen, "white", (self.blockSize*4, self.blockSize*2), (self.blockSize*4, self.blockSize*5))
        pygame.draw.line(self.screen, "white", (self.blockSize*2, self.blockSize*4), (self.blockSize*5, self.blockSize*4))
        pygame.draw.line(self.screen, "white", (self.blockSize*2, self.blockSize*3), (self.blockSize*5, self.blockSize*3))
        return
    def draw(self):
        self.table()
        self.turns()
        self.element.draw()
        return


def main() -> None:
    blockSize: int = 100 
    blockNumber: int = 8
    running:bool = True
    screen: pygame.Surface = pygame.display.set_mode((blockSize * blockNumber, blockSize * blockNumber))
    board: Board = Board(screen, blockSize, blockNumber)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
        screen.fill("black")
        board.draw()
        pygame.display.update()
    return

if __name__ == "__main__":
    main()
