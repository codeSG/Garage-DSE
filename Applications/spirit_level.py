"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""
import board
import displayio

from adafruit_clue import clue
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon
from adafruit_display_shapes.roundrect import RoundRect

# Make component groups
design = displayio.Group(max_size=20)
bubble_groupx = displayio.Group(max_size=2)
bubble_groupy = displayio.Group(max_size=2)

# Make a background color fill
def draw_background():
    color_bitmap = displayio.Bitmap(320, 240, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF
    bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
    return bg_sprite

#Make outer boundary of the spirit level
def draw_poly():
    polygon = Polygon(
        [
        (80, 10),
        (160,10),
        (220,220),
        (20,220)
        ],
        outline=0x0,)
    return polygon

#Make spirit rectangle(yellow coloured)
def draw_sprit_rect(centerx, centery, xlength, ylength):
    rect = RoundRect(centerx-(xlength//2), centery-(ylength//2), xlength, ylength,20, fill=0xFFFF44, outline=0x0)
    return rect

#Make spirit bubbles(green circle)
def draw_bubbles():
    x, y, _ = clue.acceleration   
    level_bubble1 = Circle(int(x + 120), int(180), 15, fill=clue.GREEN, outline=clue.BLUE)
    level_bubble2 = Circle(int(120), int(90+y), 15, fill=clue.GREEN, outline=clue.BLUE)
    bubble_groupx.append(level_bubble1)
    bubble_groupy.append(level_bubble2)

#Main func. to construct all components of sprit level
def draw_spirit():
    design.append(draw_background())

    design.append(draw_sprit_rect(120,90, 40, 120))
    design.append(Line(100, 110, 140, 110, 0x0))
    design.append(Line(100, 70, 140, 70, 0x0))

    design.append(draw_sprit_rect(120,180, 120, 40))
    design.append(Line(100, 160, 100, 200, 0x0))
    design.append(Line(140, 160, 140, 200, 0x0))
    design.append(draw_poly())

    draw_bubbles()
    design.append(bubble_groupx)
    design.append(bubble_groupy)

#Check whether it is levelled upto given accuracy level
def Islevelled(accu_level):
    if accu_level >-3 and accu_level <3:
        return True
    return False

#indicate neopixel if levelled->green else red light
def IndicateNeoPixel(x,y):
    if Islevelled(x) and Islevelled(y):
        clue.pixel.fill(clue.GREEN)
    else:
        clue.pixel.fill(clue.RED)

draw_spirit()

#continuous loop for monitoring
while True:
    x, y, _ = clue.acceleration
    bubble_groupx.x = int(x)
    bubble_groupy.y = int(y)
    IndicateNeoPixel(x,y)
    board.DISPLAY.show(design)
