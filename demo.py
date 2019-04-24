from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()


green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

def message():
   sense.show_message("Hvad siger det? Alexander!", text_colour = pick_random_colour(), back_colour = pink, scroll_speed = 0.05)
   
def letter():
  sense.show_letter("a",text_colour = pick_random_colour(), back_colour = white)
  sleep(1)
  sense.show_letter("l",text_colour = pick_random_colour(), back_colour = white)
  sleep(1)
  sense.show_letter("e",text_colour = pick_random_colour(), back_colour = white)
  sleep(1)
  sense.show_letter("x",text_colour = pick_random_colour(), back_colour = white)
  sleep(1)
  sense.show_letter("a",text_colour = pick_random_colour(), back_colour = white)
  sleep(1)
  sense.show_letter("n",text_colour = pick_random_colour(), back_colour = white)
  sleep(1)
  sense.show_letter("d",text_colour = pick_random_colour(), back_colour = white)
  sleep(1)
  sense.show_letter("e",text_colour = pick_random_colour(), back_colour = white)
  sleep(1)
  sense.show_letter("r",text_colour = pick_random_colour(), back_colour = white)
  sleep(1)
  
def trinket_logo():
  G = green
  Y = yellow
  B = blue
  O = nothing
  logo = [
  O, O, O, O, O, O, O, O,
  O, B, B, O, O, B, B, O,
  O, B, B, O, O, B, B, O,
  O, O, O, O, O, O, O, O,
  G, O, O, Y, Y, O, O, G,
  O, G, O, O, O, O, G, O,
  O, O, G, G, G, G, O, O,
  O, O, O, O, O, O, O, O,
  ]
  return logo
while True:
  letter()
  message()
  sense.set_pixels(trinket_logo())
  sleep(4)
