# mvc_abc.py

from ABC import ABC, abstractmethod

from uuid import uuid


class Model(ABC):
	"""
	ABSTRACT CLASS: Model
	All MVC "model" objects inherit this class.
	"""
	
	def __init__(self):
		self.id: str = uuid4().hex
