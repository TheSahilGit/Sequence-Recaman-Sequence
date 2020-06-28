"""Visualizing the Recaman's Sequence"""
### Sahil Islam ###
### 28/06/2020 ###
import numpy as np
import matplotlib.pyplot as plt
import pygame


def recaman(n):
    series = np.zeros(n)
    series[0] = 0
    for i in range(1, n):
        if series[i - 1] - i > 0 and series[i - 1] - i not in series:
            series[i] = series[i - 1] - i
        else:
            series[i] = series[i - 1] + i
    return series


def scatterPlot(n):
    series = recaman(n)
    x = np.linspace(0, n, n)

    plt.scatter(x, series, marker='.')
    plt.xlabel("n")
    plt.ylabel("$n^{th} term$")
    plt.title("Recaman Serquence")
    plt.show()


def Plot(n):
    series = recaman(n)
    x = np.linspace(0, n, n)

    plt.plot(x, series)
    plt.xlabel("n")
    plt.ylabel("$n^{th} term$")
    plt.title("Recaman Serquence")
    plt.show()


def circularVisual(n):
    pygame.init()
    width = 1000
    height = 600
    screen = pygame.display.set_mode((width, height))
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    clock = pygame.time.Clock()

    def circle(x, y, r):
        pygame.draw.circle(screen, red, (int(x), int(y)), int(r), 2)

    series = recaman(n)

    scale = 5

    screen.fill(black)
    while True:
        for i in range(len(series) - 1):

            yo = height / 2.
            r = abs(series[i + 1] - series[i]) / 2.
            xo = r + series[i]

            circle(scale * xo, yo, scale * r)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
            clock.tick(5)
