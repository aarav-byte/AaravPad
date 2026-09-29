# AaravPad

AaravPad is a 3×3 macropad built for Hack Club's Hackpad program. It has nine MX-style keys, a Seeed XIAO RP2040, and runs KMK firmware. By default it handles copy, paste, undo, redo, save, app switching and volume control on macOS.

![AaravPad](assets/hackpad.png)

## Why I made it

I wanted a small pad for the shortcuts I use constantly while working on school projects and code, and I wanted to learn the full hardware pipeline: schematic, PCB layout, case CAD and firmware.

## Challenges

- I first designed the board around an Arduino Pro Micro, then found it isn't an approved Hackpad part and switched the design to the XIAO RP2040, rewiring the matrix and rerouting the tracks.
- The microcontroller's USB port originally sat well inside the board edge, so a cable couldn't reach it through the case. I moved it to the edge and trimmed the board outline so the margins are even on all sides.
- I generated the case with a Fusion 360 Python script, so the switch cutouts, USB slot and screw holes are placed directly from the PCB coordinates.

## Schematic

![Schematic](assets/schematic.png)

A 3×3 key matrix with one 1N4148 diode per switch (column to row). Columns go to D0–D2 and rows to D8–D10 on the XIAO, leaving the I2C pins free for future additions.

## PCB

![PCB](assets/pcb.png)

Two-layer board, about 89 × 63 mm, with 0 DRC errors.

## Case

![Case](assets/case.png)

A two-part 3D-printed sandwich case (about 108 × 82 × 21 mm):

- **Top:** 1.5 mm switch plate with 14 mm cutouts, an opening over the XIAO (so the BOOT button stays reachable), a USB-C slot and four counterbored M3 holes.
- **Bottom:** tray with four 4.7 mm holes for M3 heat-set inserts.

The switches clip into the plate and the PCB is soldered to them, so the PCB hangs from the top. Four M3×16 screws go through the top into the heat-set inserts. Neither part needs supports: print the top plate-side down and the bottom floor-side down.

## Firmware

KMK (CircuitPython). The keymap is in `firmware/main.py`:

| | | |
|---|---|---|
| Copy (⌘C) | Paste (⌘V) | Undo (⌘Z) |
| Save (⌘S) | App switch (⌘Tab) | Redo (⌘⇧Z) |
| Volume − | Mute | Volume + |

## BOM

| Part | Qty |
|---|---|
| Seeed XIAO RP2040 (through-hole) | 1 |
| MX-style switches | 9 |
| 1N4148 through-hole diodes | 9 |
| White blank DSA keycaps | 9 |
| M3×16 mm screws | 4 |
| M3×5×4 mm heat-set inserts | 4 |
| Custom PCB (production/gerbers.zip) | 1 |
| 3D-printed case: Top + Bottom | 1 set |

## Files

- `cad/`: full assembly (case + PCB) as STEP
- `pcb/`: KiCad project, schematic and PCB
- `firmware/`: KMK source
- `production/`: gerbers.zip, Top.STEP, Bottom.STEP, main.py
