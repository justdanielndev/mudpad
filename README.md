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

![schem](https://hc-cdn.hel1.your-objectstorage.com/s/v3/05f8c9525a0f34a865e9f09e2c8b13cb693d316e_image.png)

CAD:

![case](https://hc-cdn.hel1.your-objectstorage.com/s/v3/3c665f4070628efd7d3af828a2785aee71abaa40_image.png)

PCB:

![pcb](https://hc-cdn.hel1.your-objectstorage.com/s/v3/220af71976f05f3ff0b9532594660a1949670c24_image.png)

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
