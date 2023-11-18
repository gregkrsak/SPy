# mvc.py

from abc import ABC, abstractmethod

import uuid


class View(ABC):
	"""
	MVC Abstract view.
	"""

	@abstractmethod
	def __init__(self, output = None):
		super().__init__()
		self.output = output


class Model(ABC):
	"""
	MVC Abstract model.
	"""

	@abstractmethod
	def __init__(self, view: View):
		super().__init__()
		self.unique_id = uuid.uuid4().hex


class Controller(ABC):
	"""
	MVC Abstract controller.
	"""

	@abstractmethod
	def __init__(self, model: Model):
		super().__init__()
