import pygame as pg
import sys

class display:
    def __init__(self, size):
        pg.init()

        self.fps = 1
        self.clock = pg.time.Clock()

        self.size = width, height = 800,800

        self.screen = pg.display.set_mode(size)

        self.background = pg.Surface(size)
        self.background = self.background.convert()
        self.background.fill( (0,0,0) )

    def draw_turtle(self, turtle, sentence):

        self.screen.blit(self.background, (0,0))
        turtle.draw(self.screen, sentence)

        pg.display.flip()

    def loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()

            self.clock.tick(self.fps)