import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""Класс, представляющий одного пришельца."""

	def __init__(self, ai_settings, screen):
		"""Инициализирует пришельца и задает его начальую позицию."""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		#Загрузка изображения пришельца и назначение атрибута rect.
		self.image = pygame.image.load('images/a1.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, ai_settings.size)
		self.rect = self.image.get_rect()
		#Каждый новый прищелец появляется в левом верхнем углу экрана.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#Сохранение точной позиции прищельца.
		self.x = float(self.rect.x)

	def update(self):
		"""Перемещает пришелца вправо или влево."""
		self.x += (self.ai_settings.alien_speed_factor * 
						self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		"""Возвращает True, если пришелец находится у края экрана."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			
	def blitme(self):
		"""Выводит пришельца в текущем положении"""
		self.screen.blit(self.image, self.rect)
