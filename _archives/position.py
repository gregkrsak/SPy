# position.py

import pygame


class Position:
	"""
	CLASS: Position
	Wraps a Pygame Vector3 into a 2D effective space, with "layers" encoded via the Z coordinate.
	"""
	
	def __init__(self, x: int = 0, y: int = 0, layer: int = 0):
		self.__xyz = pygame.math.Vector3(x, y, layer)

		@property
		def x(self):
			return self.__xyz.x
		@x.setter
		def x(self, value: int):
			self.__xyz.x = value

		@property
		def y(self):
			return self.__xyz.y
		@y.setter
		def y(self, value: int):
			self.__xyz.y = value

		@property
		def xy(self):
			return (self.__xyz.x, self.__xyz.y)
		@xy.setter
		def xy(self, value: Tuple[int, int]):
			self.__xyz.x = value[0]
			self.__xyz.y = value[1]

		@property
		def layer(self):
			return self.__xyz.z
		@layer.setter
		def layer(self, value: int):
			self.__xyz.z = value
		
