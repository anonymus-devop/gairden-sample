"""

Calls the function that Reads light

"""

def on_button_pressed_a():
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

def on_button_pressed_ab():
    readH()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    readL()
input.on_button_pressed(Button.B, on_button_pressed_b)

"""

Reads light

"""
"""

Calls the function that Reads light

"""
def readH():
    if humidity < 300:
         for index in range(4):
            basic.show_leds("""
                # . # . #
                # . # . #
                . # . # .
                . # . # .
                . . . . .
                """)
            basic.show_leds("""
                . # . # .
                . # . # .
                # . # . #
                # . # . #
                . . . . .
                """)
    elif humidity >= 300 and humidity <= 700:
        basic.show_leds("""
            . # . . .
            # # # . .
            # # # . #
            . # . # .
            . . # . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . # . . #
            # # # . #
            # # # . .
            # # # . #
            """)

def on_logo_pressed():
    music.play(music.string_playable("- - A G F E - - ", 140),
        music.PlaybackMode.UNTIL_DONE)
    serial.write_line("Bye")
    basic.show_string("Byeee! ")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

temp = 0
humidity = 0
light2 = 0
music.play(music.string_playable("E E F G G F E D ", 140),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    global light2, temp, humidity
    light2 = input.light_level()
    temp = input.temperature()
    humidity = pins.analog_read_pin(AnalogPin.P0)
basic.forever(on_forever)
