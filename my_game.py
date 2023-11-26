# my_game.py
#
# Written by Greg M. Krsak (greg.krsak@gmail.com).
# Originally created Novenber 17, 2023.
#
# This is a test of a Pygame wrapper framework that I started writing yesterday.
#

from game_application import GameApplication
from game_screen import GameScreen
from game_sprite import GameSprite
from game_image import GameImage
from game_state import GameState
from game_group import GameGroup
from game_position import GamePosition
from game_queue import GameQueue

# TODO: Wrap this
import threading


# Create the game instance
application = GameApplication()

# Initialize the screen
screen = GameScreen(application.display_info.current_w, application.display_info.current_h)

# Create sprite groups
player_group = GameGroup("player")
photo_group = GameGroup("photo")
art_group = GameGroup("art")

# Create game states
state_walking = GameState("walking")
state_stationary = GameState("stationary")

# Load images
# --- player ---
image_1 = GameImage("dino-1.png")
image_2 = GameImage("dino-2.png")
image_3 = GameImage("dino-3.png")
image_4 = GameImage("dino-4.png")
image_5 = GameImage("dino-5.png")
image_6 = GameImage("dino-6.png")
# --- photo ---
photo_1 = GameImage("20231117_162838.png")
# --- art ---
art_1 = GameImage("test_image_128x128.png")

# Create sprites
# --- player ---
player_location = GamePosition(128, 128, 0)
player = GameSprite(screen, player_location, [state_walking], state_walking)
player.set_animation_for_state([image_1, image_2, image_3, image_4, image_5, image_6], state_walking)
# --- photo ---
photo_location = GamePosition(512, 128, 0)
photo = GameSprite(screen, photo_location, [state_stationary], state_stationary)
photo.set_animation_for_state([photo_1], state_stationary)
# --- art ---
art_location = GamePosition(128, 512, 0)
art = GameSprite(screen, art_location, [state_stationary], state_stationary)
art.set_animation_for_state([art_1], state_stationary)

# Add sprites to groups
player_group.add(player)
photo_group.add(photo)
art_group.add(art)

# Create queues
clear_screen_queue = GameQueue(
	controller = None, # FIXME: testing purposes only
	callback = lambda value: screen.clear_with(value)
)

# Test game loop
i = 0
while i < 6:
	# Animate the sprite
	player.tick()
	photo.tick()
	art.tick()
	screen.tick()

	# Wait for the user to press any key
	application.wait_for_keypress()

	# Clear the screen and update
	clear_screen_queue.put(screen.background_color)
	screen.tick()

	i += 1 
