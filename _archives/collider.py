# collider.py

from dataclasses import dataclass

from design_patterns import Observer, Observable

from pygame.mask import Mask

from rectangle import Rectangle


@dataclass
class Collider(GameObject, Observer, Observable):
	"""
	DATA CLASS: Collider
	"""

	area: Rectangle
	mask: Mask
