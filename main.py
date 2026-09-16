"""

Calls the function that Reads light

"""

def on_button_pressed_a():
    for index in range(4):
        readT()
input.on_button_pressed(Button.A, on_button_pressed_a)

"""

Reads temperature

"""
def readT():
    if input.temperature() < 18:
        basic.show_leds("""
            . . . . .
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            """)
    elif input.temperature() > 18 and input.temperature() < 30:
        basic.show_leds("""
            # . . . #
            # . . . #
            . . . . .
            # . . . #
            . # # # .
            """)
    else:
        basic.show_leds("""
            # # . # #
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            """)
    basic.pause(5000)
    basic.show_string("Check Temp! ")
    basic.pause(5000)
"""

Reads light

"""
def readL():
    if light2 > 0 and light2 < 88:
        basic.show_icon(IconNames.SKULL)
    elif light2 > 88 and light2 < 204:
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
    else:
        basic.show_leds("""
            # # . # #
            . . . . .
            . # # # .
            # # # # #
            # # # # #
            """)
    basic.pause(5000)
"""

Calls the function that Reads light

"""

def on_button_pressed_b():
    for index2 in range(4):
        readL()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global light2
    music.play(music.string_playable("- - A G F E - - ", 140),
        music.PlaybackMode.UNTIL_DONE)
    serial.write_line("Bye")
    basic.show_string("Byeee! ")
    light2 = input.light_level()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

light2 = 0
music.play(music.string_playable("- - E F G A - - ", 140),
    music.PlaybackMode.UNTIL_DONE)