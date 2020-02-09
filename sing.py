import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time

SONG = [
    "We could leave the Christmas lights up 'til January",
    "This is our place, we make the rules",
    "And there's a dazzling haze, a mysterious way about you, dear",
    "Have I known you twenty seconds or twenty years?",
    "Can I go where you go?",
    "Can we always be this close forever and ever?",
    "And ah, take me out, and take me home",
    "You're my, my, my, my lover",
    "We could let our friends crash in the living room",
    "This is our place, we make the call",
    "And I'm highly suspicious that everyone who sees you wants you",
    "I've loved you three summers now, honey, but I want 'em all",
    "Can I go where you go?",
    "Can we always be this close forever and ever?",
    "And ah, take me out, and take me home (forever and ever)",
    "You're my, my, my, my lover",
    "Ladies and gentlemen, will you please stand?",
    "With every guitar string…"
]

def say(robot, thing):
    robot.say_text(thing).wait_for_completed()

def turtle(robot: cozmo.robot.Robot):
    line = 0
    while True:
        say(robot, SONG[line])
        line += 1
        robot.drive_straight(distance_mm(100), speed_mmps(300)).wait_for_completed()
        robot.turn_in_place(degrees(45)).wait_for_completed()
    
cozmo.run_program(turtle, use_viewer=True, force_viewer_on_top=True)