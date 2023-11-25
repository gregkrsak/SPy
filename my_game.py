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


# Create the game instance
application = GameApplication()

# Initialize the screen
screen = GameScreen(application.display_info.current_w, application.display_info.current_h)

# Create a sprite group
player_group = GameGroup("player")

# Create game states
state_stationary = GameState("stationary")

# Load images
image_1 = GameImage("20231117_162838.png")
image_2 = GameImage("test_image_128x128.png")

# Create sprites
location = GamePosition(128, 128, 0)
player = GameSprite(screen, location, [state_stationary], state_stationary)
player.set_animation_for_state([image_1, image_2], state_stationary)

# Add sprites to group
player_group.add(player)


# Test game loop
i = 0
while i < 5:
	# Animate the sprite and update the screen
	player.tick()
	screen.tick()

	# Wait for the user to press any key
	application.wait_for_keypress()

	# Clear the screen
	screen.clear()

	i += 1
