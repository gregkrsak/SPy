# game_group.py

import pygame


class GameGroup(pygame.sprite.Group):
	"""
	A logical organization container for game sprites, wrapping Pygame's sprite.Group via inheritance.
	"""

	def __init__(self, name: str):
		super().__init__()
		self.name = name
