# game_state.py


class GameState:
	"""
	A state for Finite State Machines.
	"""

	def __init__(self, name: str):
		super().__init__()
		self.name = name
