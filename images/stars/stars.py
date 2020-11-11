import pygame
from pygame.sprite import Group

from settings_star import Settings
import game_functions_star as gf
def run_game():
	#Инициализирует игру и создает объект экрана
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Stars")

	#Создание здвездного неба.
	stars = Group()
	gf.create_stars(ai_settings, screen, stars)
	#Назначение цвета фона
	bg_color = (0, 0, 0)
	#Запуск основного цикла игры
	#i = 0 
	while True:
		#Отслеживание событий клавиатуры и мыши.

		gf.check_events(ai_settings, screen, stars)
		#i += 1
		#if i%2 == 0:
		#	ai_settings.bg_color = (gf.f(), 0, 150)
		if ai_settings.star_fall:
			gf.star_update(ai_settings, screen, stars)
		gf.update_screen(ai_settings, screen, stars)
		print(len(stars))
run_game()

