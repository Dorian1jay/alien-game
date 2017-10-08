
class Settings():
	""" class that stores all alien settings"""
	
	def __init__(self):
		"""initializing the games settings"""
		# screen settings
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		# Bullet settings
		self.bullet_speed_factor = 3
		self.bullet_width = 500
		self.bullet_height = 15
		self.bullet_color = (60, 60 ,60)
		self.bullets_allowed = 4
		
		# Ship settings
		self.ship_speed_factor = 1.5
		self.ship_limit = 5
		
		# Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
