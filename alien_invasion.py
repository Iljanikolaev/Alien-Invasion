import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():

	#Инициализирует игру и создает объект экрана
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#Создание кнопки Play. 
	play_button = Button(ai_settings, screen, "Play")
	#Создание эксземпляров GameStats и Skoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	#Создание корабля, группы пуль и группы пришельцев.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	#Назначение фона
	ai_settings.bg_color = pygame.image.load('images/bg.jpg').convert()
	#Фиксируем fps
	clock = pygame.time.Clock()
	FPS = 60

	#Запуск основного цикла игры
	while True:
		clock.tick(FPS)
		#Отслеживание событий клавиатуры и мыши.
		gf.check_events(ai_settings, screen, stats, sb,  play_button, ship, aliens, bullets)
		#Если игра активна, обновление корабля, пуль, пришельцев
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		#Обновленние пришельцев
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()

