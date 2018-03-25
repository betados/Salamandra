import pygame
from tools import distance, modulo, unit_v, forty_fivers


class Salamandra(object):
    def __init__(self, screen):
        self.screen = screen
        self.head = [100, 100]
        # self.verts = [[100, 100], [60, 100], [20, 100]]

        quant = 19
        self.space = 20
        self.verts = [{'pos': [300 - (i * self.space), 100],
                       'feet': [[0, 0], [0, 0]] if i == 2 or i == 7 else None} for i in range(quant)]
        self.v_max = 0.08
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

        for v in enumerate(self.verts):
            print(v)
        print('\n')

        self.mouse = mouse

        for i in range(2):
            # FIXME the derivative part doesn't seem to work well
            self.a[i] = self.error[i] * self.kp - self.d_error[i] * self.kd
            self.v[i] += self.a[i] * t
        self.error_ant = self.error

        self.trim_vel()

        for i in range(2):
            self.verts[0]['pos'][i] += self.v[i] * t

        # Calculate positions of the rest ones
        for i, vert in enumerate(self.verts[1:]):
            k = i+1
            u = unit_v(vert['pos'], self.verts[k - 1]['pos'])

            if vert['feet'] and distance(vert['feet'][1], vert['pos']) > self.space:
                fs = forty_fivers(u)
                for feetIndex, f in enumerate(fs):
                    for l in range(2):
                        vert['feet'][feetIndex][l] = vert['pos'][l] + f[l]

            for j in range(2):
                vert['pos'][j] = self.verts[k - 1]['pos'][j] + u[j] * self.space

        # actual drawing
        for vert in self.verts:
            pygame.draw.circle(self.screen, (0, 255, 0), (int(vert['pos'][0]), int(vert['pos'][1])), 1)
            if vert['feet']:
                for i in range(2):
                    pygame.draw.line(self.screen, (255, 0, 0),
                                     (int(vert['pos'][0]), int(vert['pos'][1])),
                                     (int(vert['feet'][i][0]), int(vert['feet'][i][1])),
                                     1)
                    pygame.draw.circle(self.screen, (255, 0, 0),
                                       (int(vert['feet'][i][0]), int(vert['feet'][i][1])),
                                       2)

    def trim_vel(self):
        m = modulo(self.v)
        if m > self.v_max:
            for i in [0, 1]:
                self.v[i] *= self.v_max / m

    @property
    def error(self):
        e = []
        for i in [0, 1]:
            e.append(self.mouse[i] - self.verts[0]['pos'][i])
        return e

    @property
    def d_error(self):
        if self.error_ant:
            e = []
            for i in [0, 1]:
                e.append(self.error_ant[i] - self.error[i])
            return e
        return self.error
