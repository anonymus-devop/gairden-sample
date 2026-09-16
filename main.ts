/**
 * Calls the function that Reads light
 */
input.onButtonPressed(Button.A, function () {
    readT()
})
/**
 * Reads temperature
 */
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
/**
 * Reads light
 */
/**
 * Calls the function that Reads light
 */
input.onButtonPressed(Button.B, function () {
    readL()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    music.play(music.stringPlayable("- - A G F E - - ", 140), music.PlaybackMode.UntilDone)
    serial.writeLine("Bye")
    basic.showString("Byeee! ")
})
let temp = 0
let light2 = 0
music.play(music.stringPlayable("- - E F G A - - ", 140), music.PlaybackMode.UntilDone)
basic.forever(function () {
    light2 = input.lightLevel()
    temp = input.temperature()
})
