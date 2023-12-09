# game_queue.py

from mvc import Model, Controller

from collections.abc import Callable

import queue
import threading


class GameQueue(Model, queue.SimpleQueue):
	"""
	Wraps queue.SimpleQueue in an effort to implement multithreaded queues.
	"""

	def __init__(self, controller: Controller, callback: Callable[..., None]):
		super().__init__(view = None)
		self._worker_callback = callback
		self.controller = controller
		# FIXME: Uncomment this
		#self.controller.model = self

		def worker():
			while True:
				next_item = self.get()
				## Do work here ##
				self._worker_callback(next_item)
				##################

		threading.Thread(target = worker, daemon = True).start()
