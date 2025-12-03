# Müdpad

Müdpad is an (almost) 4×4, 15-key macropad with a single rotary encoder, that I'll probably use for random shenanigans and to control my Mac :D

## Overview

It has one clickable rotary encoder (used to control music or other media) and (of course, lol) buttons, in this case 15, in a 4x4 grid

## Stuff it has

- **15 mechanical switches** arranged in an almost 4×4 grid
- **1 rotary encoder** (with push)
- **No OLED or screen**; sadly couldn't fit those with the Xiao

- ## Bill of Materials (BOM)

| Component | Quantity |
|-----------|----------|
| Cherry MX Switches | 15 |
| Rotary encoder (EC11) | 1 |
| XIAO RP2040 | 1 |
| PCB | 1 |
| Diodes (1N4148) | 15 |
| USB-C Cable | 1 |
| 3D Printed Case | 1 |
| 3D Printed Knob for the encoder | 1 |
| Keycaps | 15 |

## Screenshots

Schematic (extra button just in case and to not break 4x4 structure):

![schem](https://i.ibb.co/Fqf5jZwC/image.png)

CAD:

![case](https://i.ibb.co/TDFn8xvw/image.png)

PCB:

![pcb](https://i.ibb.co/b5fqH8sq/image.png)

### Tools Required

- Soldering iron (temperature controlled recommended)
- Solder (leaded or lead-free)
- Flush cutters
- Multimeter (for testing)
- Firmware flashing tool (depends on microcontroller)

## Layout

It's composed of a 4x4 grid with the exception of the bottom right key being actually a rotary encoder.

## Set up

You basically have to:

1. **Flash the chosen firmware** to your microcontroller (following that firmware's documentation)
2. **Solder the switches**, diodes, and encoder
3. **Configure your keymap**
4. **Use it** :3
