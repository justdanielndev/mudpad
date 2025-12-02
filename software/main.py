import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.extensions.append(MediaKeys())

keyboard.row_pins = (board.D4, board.D3, board.D2, board.D1)
keyboard.col_pins = (board.D8, board.D9, board.D10, board.D11)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.encoder_pins = ((board.D6, board.D5, board.D7),)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MPLY),)
]

keyboard.keymap = [
    [
        KC.F13,   KC.F14,   KC.F15,   KC.F16,
        KC.F17,   KC.F18,   KC.F19,   KC.F20,
        KC.F21,   KC.F22,   KC.F23,   KC.F24,
        KC.F13,   KC.F14,   KC.F15,   KC.F16,
    ]
]

if __name__ == '__main__':
    keyboard.go()
