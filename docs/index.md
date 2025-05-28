# PPUC, PPUC/DMD and ZeDMD
[![Discord](https://img.shields.io/discord/759478464733642814.svg?logo=discord&logoColor=white&color=5865F2&label=Discord)](https://discord.gg/fkkk4MbBn5)

The Pinball Power-Up Controller software and hardware family is designed to enhance the capabilities of classic pinball
machines, mainly of the 80s and 90s, to repair broken machines and to drive the hardware of home brew pinball machines.

[![Watch the video](https://img.youtube.com/vi/-LGO8dxLg2c/hqdefault.jpg)](https://youtu.be/-LGO8dxLg2c)
*Click the image to watch the video on YouTube.*

Meanwhile the PPUC family has grown and the hard and software covers various use-cases, like modding a pinball machine,
repairing a pinball machine or to drive homebrew pinball machines.

The first PPU Controller was designed to enhance existing machines. It is able to monitor all playfield switches, lights,
and solenoids and to trigger and distribute corresponding *events* to attached sub-systems.
It is possible to monitor DMD and sound commands, too.

Sub-system like the built-in EffectController are able to drive additional LEDs, motors, and coils.
Other sub-systems could be video players or audio systems. The additional effects are bundled per pinball machine in
so-called *Pinball Power-Ups* (PPUs).

For homebrew machines there will be additional software to act as "CPU", running the game logic aka rules and
communicating with the controllers. The target is to use the VPX Standalone script engine and the VPX Standalone ecosytem.

A special variation of that "CPU" is suitable as replacement for a broken CPU of an existing machine.
That development started as part of the [PinMAME project](https://github.com/vpinball/pinmame/tree/master/src/ppuc).
Nowadays it is a standalone programm that leverages libpinmame: https://github.com/PPUC/ppuc

As a sub-project ZeDMD has been created to emulate a real DMD for virtual pinball machines and to be used with as
replacement in real machines.

To get involved in the development or to discuss your PPUC project, join us on [Discord](https://discord.gg/fkkk4MbBn5).

## Motivation

We want to enable people to be creative and to modernize old pinball machines using today's technology.
Or to get an old broken machine back to work.
Our goal is to establish an open and affordable platform for that.

Ideally people will publish their game-specific PPUs so others could
leverage and potentially improve them. We want to see a growing library of PPUs and a vital homebrew pinball community.

## Concept

### Enhancing / Modding an existing machine

The Pinball Power-Up Controllers consist of multiple micro controllers to perform several tasks in parallel. The entire
system is modular, so you can choose what you really need. The basic setup consists of a controller to capture a
pinball's events and another independent one to run effects.

We will provide several integrated boards and vendor specific adaptor boards (currently in development: Williams WPC,
Data East, Stern SAM and Whitestar).

The Effect Controller should be able to drive hundreds (or thousands?) of LEDs, PWM devices, ... in parallel in a
non-blocking way.

[![Watch the video](https://img.youtube.com/vi/LCGjzt88AMo/default.jpg)](https://youtu.be/LCGjzt88AMo)
[![Watch the video](https://img.youtube.com/vi/L5reBPVoL4c/default.jpg)](https://youtu.be/L5reBPVoL4c)
[![Watch the video](https://img.youtube.com/vi/4dq9ez786GY/default.jpg)](https://youtu.be/4dq9ez786GY)
[![Watch the video](https://img.youtube.com/vi/aY2foJ0kw9o/default.jpg)](https://youtu.be/aY2foJ0kw9o)
*Click the images to watch the videos on YouTube.*

### Homebrew machines or Replacing a CPU (and drivers)

Still WIP, but the hardware and [io-boards firmware](https://github.com/PPUC/io-boards) gets better and better ;-)

A PPUC board can control solonoids, flashers, motors, etc. They could read dedicated switches or a
switch matrix.
Lamps could als be controlled as dedidicated bulbs or LEDs, as light matrix or as addressable RGB(W) LEDs including
after glow effects.

Multipe boards can be cascaded to to have enough input and output ports. The communication happens via a BUS and the
protocol enhances the DOF protocol which is known from the virtual pinball world.

![PCB Pic](https://github.com/PPUC/Hardware_IO_16_8_1/raw/main/IO_16_8_1/PCB_V010_TH.jpg)
![PCB Pic](https://github.com/PPUC/Hardware_Out_8x10/raw/master/Out_8x10/PCB_Out_8x10.jpg)

In case of replacing a broken CPU and driver boards, the platform independent
[PPUC command line tool](https://github.com/PPUC/ppuc) can run on any old or small computer like a Raspberry Pi
and leverages libpinmame to emulate the ROM.

[![Watch the video](https://img.youtube.com/vi/BKefBGnp9Js/hqdefault.jpg)](https://youtu.be/BKefBGnp9Js)
*Click the image to watch the video on YouTube.*

It you replace the entire electronics and wiring of an existing machine, a
[web-based configuration tool](https://github.com/PPUC/config-tool) could be used to configure your setup.

In case of a homebrew machine, the intention is that you design and devolep your pinball machine using VPX.
Our plan is to create a special version of VPX Standalone (VPX for Linux, macOS, iOS, Android) to operate the machine.
You would have all capabilities like PUP Packs, FlexDMD, etc.

[![Watch the video](https://img.youtube.com/vi/MTMMOd1anZY/hqdefault.jpg)](https://youtu.be/MTMMOd1anZY)
*Click the image to watch the video on YouTube.*

![Overview pic](images/hardware/overview.png)

## Licence

The code is licenced under GPLv3. Be aware of the fact that your own *Pinball Power-Ups* (PPUs) need to be licenced
under a compatible licence.
That doesn't prevent any commercial use, but you need to respect the terms and conditions of GPLv3!

We would appreciate contributions to PPUC itself or as game-specific PPUs.

## ZeDMD

ZeDMD is a "real" DMD for pinball emulations and other use cases, developed as part of the PPUC project.
For more details, visit the [ZeDMD page](https://github.com/PPUC/ZeDMD).

[![Watch the video](https://img.youtube.com/vi/B6D00oB4Co8/hqdefault.jpg)](https://youtu.be/B6D00oB4Co8)
*Click the image to watch the video on YouTube.*

## Other components of the PPUC project

To reach our goals, we contribute to other projects like VPX Standalone, batocera, libdmdutil, libserum etc.
Some libraries and sub-projects that are also leveraged by others are hosted as PPUC projects:

- [libzedmd](https://github.com/PPUC/libzedmd)
- [libpupdmd](https://github.com/PPUC/libpupdmd)
- [libframeutil](https://github.com/PPUC/libframeutil)
- [libserum (concentrate)](https://github.com/PPUC/libserum_concentrate)

