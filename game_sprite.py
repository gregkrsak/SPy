# game_sprite.py

from game_position import GamePosition
from game_state import GameState
from game_object import GameObject
from game_image import GameImage
from game_screen import GameScreen

import pygame


class GameSprite(GameObject, pygame.sprite.Sprite):
	"""
	MVC Model to wrap the Pygame Sprite class via inheritance, additionally implementing states and animation.
	The render_target (MVC View) should be set to a GameScreen instance.
	"""

	def __init__(self,
				 render_target: GameScreen,
				 location: GamePosition,
				 available_states: list[GameState],
				 initial_state: GameState):
		
		super().__init__(view = render_target, location = location)
		
		self.view = render_target
		self.location = location
		self.available_states = available_states
		self.initial_state = initial_state
		self._animation = {}
		self._state = 0
		self._animation_frame = 0

		# Set the current state to the initial state
		self.state = self.initial_state

		# Initialize all animations
		for each_state in available_states:
			self.set_animation_for_state(None, each_state)


	# Current FSM (finite state machine) state, used to show the appropriate animation
	@property
	def state(self):
		return self._state
	@state.setter
	def state(self, value):
		self._state = value
		self._animation_frame = 0


	# Associates a list of images with a state
	def set_animation_for_state(self, animation: list[GameImage], state: GameState):
		self._animation[state.name] = animation

	# Determines the number of images (frames) in an animation
	def _animation_frames_in(self, an_animation: list[GameImage]):
		result = 0
		for each_image in an_animation:
			result += 1
		return result

	# Call this every game tick to make the animations play
	def tick(self):
		current_animation = self._animation[self.state.name]
		current_animation_image = current_animation[self._animation_frame].render_source
		current_screen_position = self.location.xy # FIXME: Expand this (layers, view frustum, etc.)
		### Draw to the screen ################################################
		self.view.output.blit(current_animation_image, current_screen_position)
		#######################################################################
		self._animation_frame += 1
		if self._animation_frame >= self._animation_frames_in(current_animation):
			self._animation_frame = 0
