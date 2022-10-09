import sys
from turtle import Screen
from settings import Settings
import pygame
from ship import Ship

class AlienInvasion:
    #Класс для управления ресурсами и поведением игры

    def __init__(self):
        #Инициализирует игру и создает игровые ресурсы
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode ((1200, 800))
        pygame.display.set_caption ("Alien Invansion")
        self.ship = Ship (Screen)
        #Назначение цвета фона
        self.bg_color = (230, 230, 230)

    def run_game(self):
        #Запуск основного цикла
        while True:
            #Отслеживание событий клавиатуры и мышки
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #При каждом проходе цикла перерисовывается экран
            self.screen.fill (self.settings.bg_color)
            self.ship.blitme()

            #Отображение последнего прорисованного экрана
            pygame.display.flip()

if __name__ == 'main':
    #Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()