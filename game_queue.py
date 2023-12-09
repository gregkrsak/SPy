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
		print(f'GameQueue {self.unique_id} initializing...')
		self._worker_callback = callback
		print(f'GameQueue {self.unique_id} callback = {self._worker_callback}')
		self.controller = controller
		# FIXME: Uncomment this
		#self.controller.model = self

		def worker():
			while True:
				next_item = self.get()
				## Do work here ##
				print(f'GameQueue {self.unique_id} working on {next_item}...')
				self._worker_callback(next_item)
				print(f'GameQueue {self.unique_id} completed {next_item}')
				##################

		threading.Thread(target = worker, daemon = True).start()
