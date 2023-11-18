# game_screen.py

from mvc import View

import pygame


class GameScreen(View):
	"""
	Represents the screen that the game plays on.
	"""

	def __init__(self, width: int, height: int):
		super().__init__()
		self.output = pygame.display.set_mode((width, height))

	# Call this to update the screen with the latest changes
	def tick(self):
		pygame.display.update()
