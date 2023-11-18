# game_object.py

from mvc import Model, View

from game_position import GamePosition


class GameObject(Model):
	"""
	The parent class of any object within the gameplay.
	"""

	def __init__(self, view: View, location: GamePosition):
		super().__init__(view = view)
		self.location = location
