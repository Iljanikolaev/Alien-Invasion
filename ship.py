import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		'''Инициализирует корабль и задает его начальную позицию.'''
		super().__init__()
		self.screen = screen 
		self.ai_settings = ai_settings

		#Загрузка изображения корабля и получение прямоуголника.
		self.image = pygame.image.load('images/1.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, ai_settings.size)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Каждый новый корабль появляется у нижнего края экрана
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#Сохранение вещественной координаты корабля.
		self.center = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		#Флаг перемещения
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		#Обновлячется атрибут center, не rect
		"""Обновляет позицию корабля с учетом флага."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.centery -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.ship_speed_factor
		#Обновление атрибута rect на основании self.center
		self.rect.centerx = self.center
		self.rect.centery = self.centery
	
	def center_ship(self):
		"""Размещает корабль в центре нижней стороны."""
		self.center = self.screen_rect.centerx


	def blitme(self):
		'''Рисует корабль в текущей позиции'''
		self.screen.blit(self.image, self.rect)
		