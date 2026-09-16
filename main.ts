/**
 * Reads light
 */
// Calls the function that Reads light
input.onButtonPressed(Button.A, function () {
    readT()
})
// Reads temperature
function readT () {
    if (input.temperature() < 18) {
        basic.showLeds(`
            . . . . .
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            `)
    } else if (input.temperature() > 18 && input.temperature() < 30) {
        basic.showLeds(`
            # . . . #
            # . . . #
            . . . . .
            # . . . #
            . # # # .
            `)
    } else {
        basic.showLeds(`
            # # . # #
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            `)
    }
    basic.pause(5000)
}
function readL () {
    if (light2 > 0 && light2 < 88) {
        basic.showIcon(IconNames.Skull)
    } else if (light2 > 88 && light2 < 204) {
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
    } else {
        basic.showLeds(`
            # # . # #
            . . . . .
            . # # # .
            # # # # #
            # # # # #
            `)
    }
    basic.pause(5000)
}
input.onButtonPressed(Button.AB, function () {
    readH()
})
input.onButtonPressed(Button.B, function () {
    readL()
})
// Calls the function that Reads light
function readH () {
    if (humidity < 300) {
        for (let index = 0; index < 4; index++) {
            basic.showLeds(`
                # . # . #
                # . # . #
                . # . # .
                . # . # .
                . . . . .
                `)
            basic.showLeds(`
                . # . # .
                . # . # .
                # . # . #
                # . # . #
                . . . . .
                `)
        }
    } else if (humidity >= 300 && humidity <= 700) {
        basic.showLeds(`
            . # . . .
            # # # . .
            # # # . #
            . # . # .
            . . # . .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            . # . . #
            # # # . #
            # # # . .
            # # # . #
            `)
    }
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    music.play(music.stringPlayable("- - A G F E - - ", 140), music.PlaybackMode.UntilDone)
    serial.writeLine("Bye")
    basic.showString("Byeee! ")
})
let temp = 0
let humidity = 0
let light2 = 0
music.play(music.stringPlayable("E E F G G F E D ", 140), music.PlaybackMode.UntilDone)
basic.forever(function () {
    light2 = input.lightLevel()
    temp = input.temperature()
    humidity = pins.analogReadPin(AnalogPin.P0)
})
