# game_asset.py

from mvc import Model


class GameAsset(Model):
	"""
	The parent class of any asset (image, sound, etc.) used by the game code.
	"""

	def __init__(self, asset_filename: str):
		super().__init__(view = None)
		self.asset_filename = asset_filename
