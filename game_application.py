# game_application.py

import pygame
from pygame.locals import *


class GameApplication():
	"""
	An instance of your game.
	"""

	_motd = "Greets from the Simple Pygame wrapper (SPy). https://github.com/gregkrsak/SPy"

	def __init__(self):
		pygame.init()
		print(self._motd)
		self.display_info = pygame.display.Info()

	def __del__(self):
		pygame.quit()

	# Wait for the user to press any key on the keyboard
	# Ref: https://stackoverflow.com/questions/20748326/pygame-waiting-the-user-to-keypress-a-key/28931488#28931488
	def wait_for_keypress(self):
		pygame.event.clear()
		while True:
			event = pygame.event.wait()
			if event.type == KEYDOWN:
				return event.key
