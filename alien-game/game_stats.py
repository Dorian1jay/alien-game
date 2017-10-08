class GameStats():
	"""Track statistics for alien invasion."""
	
	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
		
		# Start alien invasion in an inactive state.
		self.game_active = False
		
	def reset_stats(self):
		"""initialize stats that can change during the games."""
		self.ships_left = self.ai_settings.ship_limit
