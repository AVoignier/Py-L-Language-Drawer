import pygame as pg

class Turtle:
    def __init__(self, position, orientation = 0):
        self.position_init = position
        self.orientation_init = orientation
        self.rotation_angle_init = 20 #deg
        self.speed_init = 50

        self.position = position
        self.orientation = orientation
        self.rotation_angle = self.rotation_angle_init
        self.speed = self.speed_init

        self.rotation_angle = 30 #deg
        self.speed = 30

    def draw(self, screen, sentence):
        print(sentence)

        self.position = self.position_init
        self.orientation = self.orientation_init
        self.rotation_angle = self.rotation_angle_init
        self.speed = self.speed_init

        position_saves = []

        for c in sentence:
            # F -> Forward
            # [ -> Save position
            # ] -> Load last position
            # - -> Turn left
            # - -> Turn Right

            if c == '[':
                position_saves.append( ( pg.Vector2(self.position[0],self.position[1]) , self.orientation) )
            elif c == ']':
                position_reccup = position_saves.pop()
                self.position = position_reccup[0]
                self.orientation = position_reccup[1]
            elif c == '-':
                self.turn_left()
            elif c == '+':
                self.turn_right()
            elif c == 'F':
                old_position = pg.Vector2( self.position[0],self.position[1]  )
                self.forward()
                pg.draw.line(screen, (255,255,255), old_position, self.position )
                print(old_position, self.position)

    def forward(self):
        self.position += pg.Vector2(0,-self.speed).rotate(self.orientation)

    def turn_left(self):
        self.orientation = (self.orientation - self.rotation_angle)%360

    def turn_right(self):
        self.orientation = (self.orientation + self.rotation_angle)%360
    