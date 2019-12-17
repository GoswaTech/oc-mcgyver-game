import os
import sys
import pygame

from .constants import STOP, LOOP, WIN, LOSE, PAUSE
from .gyver import Gyver
from .labyrinth import Labyrinth

from .drivers import Driver


class GameLoop:
    """
        GameLoop is the loop of the laby game.
    """

    def __init__(self, **kwargs):
        self.loop = STOP
        self.driver = kwargs.pop('driver', Driver)

    def perform_move(self, move):
        """
            Take a String and move MacGyver.
            The move value :
            - R : Right
            - L : Left
            - U : Up
            - D : Down
            - QUIT : Quit
        """

        if(move in ['R', 'L', 'U', 'D']):

            square = self.driver.labyrinth.get_square(self.driver.gyver.coords)

            if(move == 'R'):
                square = self.driver.gyver.move(self.driver.labyrinth, x=1)
            elif(move == 'L'):
                square = self.driver.gyver.move(self.driver.labyrinth, x=-1)
            elif(move == 'U'):
                square = self.driver.gyver.move(self.driver.labyrinth, y=-1)
            elif(move == 'D'):
                square = self.driver.gyver.move(self.driver.labyrinth, y=1)

            square.after_move(gyver=self.driver.gyver)

        # end conditions
        if(move == 'QUIT'):
            self.loop = STOP
        if(self.driver.gyver.win):
            self.loop = WIN
        elif(self.driver.gyver.lose):
            self.loop = LOSE

    def start_loop(self):
        """
            The loop call only the driver and perform the move.
        """

        self.loop = LOOP

        while self.loop == LOOP:
            self.driver.draw_labyrinth()
            move = self.driver.wait_for_move()

            self.perform_move(move)

        if(self.loop == WIN):
            self.driver.win_scenario()

        elif(self.loop == LOSE):
            self.driver.lose_scenario()
