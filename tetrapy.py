###############################################################################
# tetrapy.py
# Tetrapy
#
# Copyright (C) 2013 Kesara Rathnayake
#
# Tetrapy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tetrapy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Tetrapy.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import pygame
import random
import sys

# Screen Size
X = 240
Y = 400

# Colours
BLACK   = (000,000,000)
WHITE   = (255,255,255)
RED     = (255,000,000)
GREEN   = (000,255,000)
BLUE    = (000,000,255)


class Tetromino(object):
    def __init__(self, colour):
        self.colour = colour
        self.locked = False

    def draw(self, screen):
        pass

    def move(self, matrix, direction, rotaion):
        pass

    def isLocked(self, matrix):
        pass

    def getMatrix(self):
        pass

    def collied(self, matrix):
        pass


class TetrominoI(Tetromino):
    def __init__(self, colour):
        super(TetrominoI, self).__init__(colour)
        self.W = 20
        self.H = 80
        self.x = 0
        self.y = 0

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.W, self.H)
        pygame.draw.rect(screen, self.colour, rect) 

    def move(self, matrix, direction, rotaion=None):
        if not self.isLocked(matrix):
            if self.x + direction <= X-20 and self.x + direction >= 0:
                self.x += direction
            if self.y <= Y-80:
                self.y += 20

    def isLocked(self, matrix):
        if self.y + 80 == Y:
            self.locked = True
            return True
        elif (self.collied(matrix)):
            return True
        return False

    def getMatrix(self):
        matrix = []
        for i in range(0, 4):
            matrix.append((self.x, self.y+20*i))
        return matrix

    def collied(self, matrix):
        for i in range(0, 4):
            if (self.x, self.y+20*i) in matrix:
                return True
        return False


screen = pygame.display.set_mode((X, Y))
colours = [WHITE, RED, GREEN, BLUE]
active = None
tetrominos = []
matrix = []

while True:
    print matrix

    screen.fill(BLACK)
    if not active:
        active = TetrominoI(random.choice(colours))
    elif active.isLocked(matrix):
        matrix.extend(active.getMatrix())
        tetrominos.append(active)
        active = TetrominoI(random.choice(colours))

    active.draw(screen)
    pygame.display.flip()

    k_left = k_right = 0
    direction = 0
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == pygame.K_RIGHT: k_right += 10
        elif event.key == pygame.K_LEFT: k_left += -10
        elif event.key == pygame.K_ESCAPE: sys.exit(0)
    direction += (k_right + k_left)

    screen.fill(BLACK)
    for tetromino in tetrominos:
        tetromino.draw(screen)
    active.move(matrix, direction)
    active.draw(screen)
    pygame.display.flip()
    pygame.time.wait(100)
