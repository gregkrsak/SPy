# game_image.py

from game_asset import GameAsset

import pygame


class GameImage(GameAsset):
	"""
	An image asset used by the game code.
	"""

	def __init__(self, asset_filename: str):
		super().__init__(asset_filename = asset_filename)
		self.render_source = pygame.image.load(asset_filename)