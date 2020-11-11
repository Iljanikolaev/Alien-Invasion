class GameStats():
	"""Отслеживание статистики для игры Alien Invasion."""

	def __init__(self, ai_settings):
		"""Инициализирует статистику."""
		self.ai_settings = ai_settings
		self.reset_stats()
		#Игра Alien Invasion запускается в активном состоянии.
		self.game_active = False
		#Рекорд не должен сбрасываться.
		with open('record.txt') as rec:
			record = int(rec.read().strip())
		self.high_score = record
		

	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся в ходе игры"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1