import pygame
pygame.mixer.init()
pygame.mixer.music.load('D:\Programming\Python\Desafios\music01.mp3')
pygame.mixer.music.play()
while pygame.mixer_music.get_busy():
    continue
