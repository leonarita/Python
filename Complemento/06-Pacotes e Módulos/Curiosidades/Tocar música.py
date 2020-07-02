#precisa copiar alguma música e colar no package desse programa

import pygame
pygame.init()
pygame.mixer.music.load('ex.mp3')
pygame.mixer.music.play()
pygame.event.wait()