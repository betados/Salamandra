import pygame
from tools import distance, modulo, unit_v


class Salamandra(object):
    def __init__(self, screen):
        self.screen = screen
        self.head = [100, 100]
        # self.verts = [[100, 100], [60, 100], [20, 100]]
        quant = 10
        self.verts = [[200-i*20, 100] for i in range(quant)]
        self.accels = [[0, 0] for _ in range(quant)]
        self.v_max = 0.05
        self.v = [0, 0]
        self.a = [0, 0]

        self.mouse = None

        # pid
        self.kp = 0.000001
        self.ki = 0
        self.kd = 0.0000006
        self._error = [0, 0]
        self.error_ant = None
        self._d_error = [0, 0]
        self.i_error = [0, 0]

    def draw(self, mouse, t):

        self.mouse = mouse
        # print(self.d_error, self.error_ant)

        for i in range(2):
            self.a[i] = self.error[i] * self.kp - self.d_error[i] * self.kd
            self.v[i] += self.a[i] * t
        self.error_ant = self.error

        # self.trim_vel()



        v = modulo(self.v)
        for i, vert in enumerate(self.verts[1:]):
            u = unit_v(self.verts[i-1], vert)
            for i in range(2):
                vert[i] += u[i] * v * t

        for i in range(2):
            self.verts[0][i] += self.v[i] * t


        # print(self.head, '\t', self.d_error)
        # pygame.draw.circle(self.screen, (0, 255, 0), (int(self.head[0]), int(self.head[1])), 1)
        for vert in self.verts:
            pygame.draw.circle(self.screen, (0, 255, 0), (int(vert[0]), int(vert[1])), 1)
            # pygame.draw.circle(self.screen, (0, 255, 0), mouse, 2)

    def trim_vel(self):
        m = modulo(self.v)
        if m > self.v_max:
            for i in [0, 1]:
                self.v[i] *= self.v_max / m

    @property
    def error(self):
        e = []
        for i in [0, 1]:
            e.append(self.mouse[i] - self.verts[0][i])
        return e

    @property
    def d_error(self):
        if self.error_ant:
            e = []
            for i in [0, 1]:
                e.append(self.error_ant[i] - self.error[i])
            return e
        return self.error
