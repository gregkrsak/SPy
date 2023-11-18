# rectangle.py

from pygame import Rect

from game_object import GameObject
from position import Position


class Rectangle(GameObject):
	"""
	CLASS: Rectangle
	Wraps a 2D Pygame rectangle, with layers implemented (via inheritance) as the location's Z dimention.
	"""

	def __init__(self, location: Position, width: int = 0, height: int = 0):
		self.location = location
		self.width = width
		self.height = height
		self.__rect = Rect(self.top_left.x, self.top_left.y, self.width, self.height)

	@property
	def top_left(self):
		return Position(__sub_halfwidth(self.location.x), __sub_halfwidth(self.location.y), self.location.layer)

	@property
	def bottom_right(self):
		return Position(__add_halfwidth(self.location.x), __add_halfwidth(self.location.y), self.location.layer)

	def __sub_halfwidth(self, value):
		return value - (self.width / 2)

	def __add_halfwidth(self, value):
		return value + (self.width / 2)
