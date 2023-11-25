# game_screen.py

from mvc import View

import pygame


class GameScreen(View):
	"""
	Represents the screen that the game plays on.
	"""

	# Default background color is black
	background_color = (0, 0, 0)

	def __init__(self, width: int, height: int):
		super().__init__()
		self.output = pygame.display.set_mode((width, height))

	# Clears the screen to black
	def clear(self):
		self.output.fill(self.background_color)

	# Call this to update the screen with the latest changes
	def tick(self):
		pygame.display.update()
