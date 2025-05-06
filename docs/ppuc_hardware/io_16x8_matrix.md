# IO_16x8_matrix
This is the hardware for a 16x8 switch matrix card which was designed for the PPUC pinball project, but can be useful in other applications as well. The intentionally usecase is to connect an original equipped pinball playfield (including cable harness and diodes). Normally I'd prefer direct switches but if all the switches and cables and diodes are in place already, it is useful to connect the switch matrix directly. The board can also be used for 16 direct inputs and 8 low power signal-outputs (no matrix).
It is designed for being low cost and functional for experimental use.
Not everything is tested nor does it fulfill EMC or any other specifications.
Use at your own risk!
To make use of anything of this project a basic understanding of electronics and programming is necessary. Nothing of it is "plug and play". I'm surely not liable for any damage to assemblies, pinball machines or even persons.

## Picture of the Board
![PCB Pic](https://github.com/PPUC/Hardware_IO_16x8_matrix/raw/main/IO_16x8_matrix/PCB_IO_16x8_matrix.jpg)

## Name
[IO_16x8_matrix](https://github.com/PPUC/Hardware_IO_16x8_matrix/) as it has 16 inputs and 8 signal-outputs to form a 16x8 switch matrix but could also be used as direct inputs and low power outputs. Actually it has an additional high speed output (see "Special Output" below).

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

## Signal Outputs
There are 8 outputs that can be set to 5 V or GND. They are intended to drive the switch matrix (column at WPC, row at S.A.M.). The 5 V signal is derived from the 5 V supply by a 1 kOhm pull up resistor. Therefore it is only good for signaling, not for power load. If used as a matrix please be aware that every switch must have a diode in series.

## Inputs
There are 16 inputs intended to receive the switch status of the matrix (row at WPC, column at S.A.M.). They are pulled up to 5 V and switch at a voltage of about 1.9 V. The inputs are made for low active signals (switched to GND). If used as a matrix please be aware that every switch must have a diode in series.

## Special Output
One special output is available for high speed signals. The voltage is 5 V, it is a push pull output that can drive a current up to 8 mA. It can be used to e.g. control a WS2812 LED strip.

## Connectors
There are pads for connectors that fit S.A.M. systems and also WPC systems. The pinning of the returns (rows at WPC) is unfortunately vice versa to S.A.M. so the connector of the original WPC cable harness has to be rotated by 180° (cables go to the inner side of PCB).
