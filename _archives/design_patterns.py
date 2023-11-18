# design_patterns.py

from abc import ABC, abstractmethod


class Observer(ABC):
	"""
	ABSTRACT CLASS: Observer
	Fundamental part of the "Observer" design pattern
	"""
	@abstractmethod
	def something(self): # TODO: Add stuff here
		pass


class Observable(ABC):
	"""
	ABSTRACT CLASS: Observable
	Fundamental part of the "Observer" design pattern
	"""
	@abstractmethod
	def something(self): # TODO: Add stuff here
		pass
