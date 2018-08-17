# -*- coding: utf-8 -*-

import math

import pygame

from tools import angle, cosTh, forty_fivers
from vector import Vector, VectorPolar


class Salamandra(object):
    def __init__(self, screen):
        self.screen = screen
        self.head = Vector(100, 100)

        quant = 19
        self.space = 20
        self.verts = [{'pos': Vector(300 - (i * self.space), 100),
                       'feet': [Vector(0 - (i * self.space), 80),
                                Vector(300 - (i * self.space), 120)] if i == 2 or i == 7 else None,
                       'elbow': [Vector(0, 0), Vector(0, 0)] if i == 2 or i == 7 else None,
                       'shoulder angle': math.pi / 6.0,
                       'elbow angle': math.pi / 6.0,
                       } for i in range(quant)]
        self.ulna_radius = self.space * 0.5
        self.humerus = self.space * 0.99
        self.v_max = 0.05
        self.v = Vector(0, 0)
        self.a = Vector(0, 0)

        self.mouse = None

        # pid
        self.kp = 0.000001
        self.ki = 0
        self.kd = 0.0000006
        self._error = [0, 0]
        self.error_ant = None
        self._d_error = [0, 0]
        self.i_error = [0, 0]

        self.status = self.moving_feet

    def draw(self, mouse, t):

        self.actualize(mouse, t)

        # self.debugDraw()

        # actual drawing
        for vert in self.verts:
            pygame.draw.circle(self.screen, (0, 255, 0), vert['pos'].get_comps(False), 1)
            if vert['feet']:
                for i in range(2):
                    pygame.draw.line(self.screen, (255, 0, 0),
                                     vert['pos'].get_comps(),
                                     vert['elbow'][i].get_comps(False),
                                     1)
                    pygame.draw.line(self.screen, (255, 0, 0),
                                     vert['elbow'][i].get_comps(False),
                                     vert['feet'][i].get_comps(False),
                                     1)
                    pygame.draw.circle(self.screen, (255, 0, 0),
                                       vert['feet'][i].get_comps(False),
                                       2)

    def debugDraw(self):
        for vert in self.verts:
            if vert['feet']:
                pygame.draw.line(self.screen, (0, 0, 255),
                                 vert['pos'].get_comps(),
                                 vert['feet'][0].get_comps(),
                                 1)

    def actualize(self, mouse, t):

        self.mouse = Vector(*mouse)

        # FIXME the derivative part doesn't seem to work well
        self.a = self.error * self.kp - self.d_error * self.kd
        self.v += self.a * t
        self.error_ant = self.error

        self.trim_vel()

        self.verts[0]['pos'] += self.v * t

        # Calculate positions of the rest ones
        for i, vert in enumerate(self.verts[1:]):
            u = (vert['pos'] - self.verts[i]['pos']).get_unit()
            u_angle = angle(Vector(1, 0), u)
            # print u_angle
            pygame.draw.line(self.screen, (200, 0, 255),
                             vert['pos'].get_comps(False),
                             (vert['pos'] - u * self.space).get_comps(False),
                             1)

            vert['pos'] = self.verts[i]['pos'] + u * self.space

            if vert['feet']:
                if vert['shoulder angle'] + u_angle < math.pi / 6.0:
                    self.status = self.moving_feet
                if vert['shoulder angle'] + u_angle > 1 * math.pi / 2.0:
                    self.status = self.static_feet

                # print self.status.__name__

                self.status(vert)
                for e, mult in enumerate([-1, 1]):
                    vert['elbow'][e] = VectorPolar(self.humerus,
                                                   mult * vert['shoulder angle'] + u_angle).to_cartesian() + vert['pos']
                    vert['feet'][e] = VectorPolar(self.ulna_radius,
                                                  mult * (-vert['shoulder angle']) + u_angle).to_cartesian() + vert['elbow'][e]

    def moving_feet(self, vert):
        vert['shoulder angle'] += math.pi / 160.0

    def pass_func(self, *args):
        pass

    def static_feet(self, vert):
        vert['shoulder angle'] -= math.pi / 160.0

    def trim_vel(self):
        if abs(self.v) > self.v_max:
            self.v *= self.v_max / abs(self.v)

    @property
    def error(self):
        e = self.mouse - self.verts[0]['pos']
        return e

    @property
    def d_error(self):
        if self.error_ant:
            return self.error_ant - self.error
        return self.error
