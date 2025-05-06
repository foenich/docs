# Opto_16
This is the hardware for a opto board which was designed for the PPUC pinball project, but can be useful in other applications as well.
It is designed for being low cost and functional for experimental use.
Not everything is tested nor does it fulfill EMC or any other specifications.
Use at your own risk!
To make use of anything of this project a basic understanding of electronics and programming is necessary. Nothing of it is "plug and play". I'm surely not liable for any damage to assemblies, pinball machines or even persons.

<!--
## Picture of the Board
![PCB Pic](tbd.jpg)
-->

## Name
[Opto_16](https://github.com/PPUC/Hardware_Opto_16/) as it has 16 inputs and 16 led divers. Additionally it has one special output.

## Application
Please be aware that in pinball many different opto types are used. You have to know which type of opto coupling you need for your purpose. I found the following types:
* Optos with photo transistors as a receiver and common collector (used for example in Dirty Harry with board A-16998.1).
* Optos with photo transistors as a receiver and common emitter (used for example in Rollergames with board C-13205). Commonly used for drop targets and flipper buttons.
* Optos with photo diodes as a receiver (used for example in World Poker Tour with board 520-5239-01).

The transmitter LEDs I've seen so far, are either single (2 pins) or share a common cathode.

This Opto_16 PCB can be used to drive transmitter LEDs from a 5 V power supply and can cope with common collector photo transistors and photo diodes.
There are 2 groups of inputs (2 x 8). One group is for photo transistors. The other group can be configured to be inputs for photo diode or photo transistor. Jumpers are used for configuration. You can only change the whole group (8 inputs), not a single channel. If no jumper is placed (all open) then the configurable group of 8 inputs are good for photo diodes. If you want them to be for photo transistors you have to close jumper JP2 and also put jumpers on the channel-connectors J18 to J25. Actually only the connectors for used channels has to be shorted by a jumper, not used channel can be left open.

If you have an application with common emitters you can use the inputs of the switch-matrix board (IO_16x8_matrix) of the PPUC project. The inputs of the standard IO board (IO_16_8_1) should work as well. In either case you need to drive the transmitter LED with a constant current of about 20 mA. This can be done with a 180 Ohm resistor at a 5 V supply (you have to wire this yourself).

If you have an opto board already (e.g. from an existing pinball machine) you can use this with the inputs of the switch-matrix board (IO_16x8_matrix) or the inputs of the standard IO board (IO_16_8_1). Connect the output transistor of the opto board to the input of the PPUC board in a way that the transistor switches to ground. Be aware that opto boards are powered with either 12 V or 5 V in existing pinball machines. Both can be used with PPUC.

## Power Supply
The IO card must be supplied by 5 V (+-0.5 V). In the circuit this is named 5V_IN.

## Controller
A RP2040 is used for it's cost/performance ratio. It is the same controller that is used in the Raspberry Pi Pico.

## Communication Interfaces
* RS_485: main communication interface for controlling the outputs. Usually connected to a host interface like a PC or Raspberry Pi or similar.
* USB C: for programming, debug and flashing
* Serial Wire: alternative for programming, debug and flashing

## Switches (on board)
* Reset: hardware reset for controller (RP2040)
* Boot: if active, the board connects to a PC like an USB stick. Usually used for programming the code into the flash memory on the board.
* DIP-switches: usually used to select an address for RS485 (16 combinations)

## LED drivers
There are 16 outputs. Each of them drives one LED (usually red or infra red).

## Inputs
There are 2 groups of inputs, each with 8 channels:
* A group of 8 inputs are designed to be used with optos that use a photo transistor as receiver and are connected to have a common collector.
* A group of 8 inputs are designed to be used with optos that use a photo diode as receiver. They are usually single (two pins) or share a common cathode.

## Special Output
One special output is available for high speed signals. The voltage is 5 V, it is a push pull output that can drive a current up to 8 mA. It can be used to e.g. control a WS2812 LED strip.

## Additional analog functions
* There are 2 ADC channels from the RP2040 made accessible through a connector. Filtered by a 1st order low pass (1 kOhm/100 nF, fg = 1.6 kHz).
* 6 GPIOs are also routed to this connector. They are also filtered by a 1st order low pass (1 kOhm/100 nF, fg = 1.6 kHz) and could be used for analog output per PWM.

## Connectors
There are pads for connectors that fit the A-16998.1 board. Additionally for 8 inputs and drivers there are pins for single LEDs (transmitter and receiver) in 2.54 mm pitch.


