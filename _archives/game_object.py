# game_object.py

from dataclasses import dataclass


@dataclass
class GameObject(Model)
	"""
	DATA CLASS: GameObject
	The base class of every "thing" within the game.
	"""

	location: Position = Position()
