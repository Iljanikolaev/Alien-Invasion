class Settings():
	'''Класс для хранения всех настроек игры Alien Invasion'''

	def __init__(self):
		'''Инициализирует настройк игры'''
		#Параметры экрана
		self.screen_width = 1300
		self.screen_height = 600
		self.bg_color = (0, 0, 0)
		self.star_fall = False
