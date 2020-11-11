import sys
import pygame 
import random

from star import Star
def check_events(ai_settings, screen, stars):
	"""Обрабатывает нажатия клавиш и события мыши."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, stars)
def check_keydown_events(event, ai_settings, screen,  stars):
	"""Реагирует на нажатие клавиш."""
	if event.key == pygame.K_SPACE:
		ai_settings.star_fall = True

	
def star_update(ai_settings, screen, stars):		
	for star in stars:
		star.rect.y += random.randint(0, 1)
		star.rect.x += random.randint(0, 1)
		if (star.rect.y >= ai_settings.screen_height) or (star.rect.x >= ai_settings.screen_width):
			stars.remove(star)


def update_screen(ai_settings, screen, stars):
	"""Обновляет изображения на экране и отображает новый экран"""
	#При каждом проходе цикла перерисовывается экран
	screen.fill(ai_settings.bg_color)
	stars.draw(screen)
	#Отображение последнего прорисованного экрана.
	pygame.display.flip()

def create_stars(ai_settings, screen, stars):
	star = Star(ai_settings, screen)
	star_width = star.rect.width
	star_height = star.rect.height
	avaliable_space_star_x = ai_settings.screen_width / star_width
	avaliable_space_star_y = ai_settings.screen_height / star_height
	number_star_x = int(avaliable_space_star_x / 60 * star_width)
	number_rows = int(avaliable_space_star_y / 60 * star_height)
	for number_row in range(number_rows):
		for number_star in range(number_star_x):
			star = Star(ai_settings, screen)
			stars.add(star)
'''b = list(range(100, 256, 1))
a = iter(b)
def f():
	global a
	global b
	try:
		return next(a)
	except:
		b.reverse()
		a = iter(b)
		return next(a)'''