# KMK firmware for a 3x3 Hackpad (Seeed XIAO RP2040)
# Wiring: columns on D0, D1, D2 - rows on D8, D9, D10 - diodes point column -> row
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Layout matches the board, top row first:  S1 S2 S3 / S4 S5 S6 / S7 S8 S9
# Mac shortcuts (LGUI = Command)
keyboard.keymap = [
    [
        KC.LGUI(KC.C),  KC.LGUI(KC.V),   KC.LGUI(KC.Z),             # copy, paste, undo
        KC.LGUI(KC.S),  KC.LGUI(KC.TAB), KC.LGUI(KC.LSFT(KC.Z)),    # save, app switch, redo
        KC.VOLD,        KC.MUTE,         KC.VOLU,                   # volume down, mute, volume up
    ]
]

if __name__ == "__main__":
    keyboard.go()
