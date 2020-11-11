import pygame
from pygame.sprite import Sprite
import random

class Star(Sprite):
	"""Класс, представляющий одну звезду"""
	
	def __init__(self, ai_settings, screen):
		"""Инициализирует звезду и задает её начальую позицию."""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#Загрузка изображения звезды и назначение атрибута rect.
		self.image = pygame.image.load('images/star.png')
		self.rect = self.image.get_rect()

		#Каждая новая звезда появляется в левом верхнем углу экрана.
		self.rect.x = random.randint(0, ai_settings.screen_width)
		self.rect.y = random.randint(0, ai_settings.screen_height)
	

	def blitme(self):
		"""Выводит звезду в текущем положении"""
		self.screen.blit(self.image, self.rect)