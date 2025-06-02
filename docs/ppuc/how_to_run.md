# Run PPUC

Open a Terminal and enter the following command for a list of options:
```shell
ppuc-pinmame -h
```

- To get started you can do a dry run as described [here](build_from_source.md#test).
- Clearly you need the appropiate pinmame rom for your pinball machine.
- Also a .yml file is required which defines the IO for your hardware as explaned [here](config_tool.md).

## USB connections

PPUC uses USB to access your hardware:

1. USB - RS485: This is required to communicate with the PPUC IO boards.
Note that the comandline for the dry run uses the -n option to disable this.
2. Optionally connect a ZeDMD display. This is also possible without the IO boards.

## Linux

You can use any Linux distribution you like. We tested with both Debian and Ubuntu. 
For Raspberry Pi use: Raspberry Pi OS Lite (no need for a desktop or other software).

### USB access

USB access is only possible when your username is in the 'dialout' group.

To see in which groups you are:
```shell
groups
```

To get USB access:
```shell
sudo usermod -a -G tty $USER
sudo usermod -a -G dialout $USER
```
When using Raspberry Pi OS you also need to be in the plugdev group:
```
sudo usermod -a -G plugdev $USER
```

### USB ports

To check if your USB device is recognized by Linux, use:
```shell
lsusb
```
The following command lists the USB to serial interfaces (USB-RS485 for PPUC IO).
```shell
ls -l /dev/ttyUSB*
```

### Run

Run from the ppcu directory:
```
ppuc/ppuc-pinmame -c <your>.yml
```
This should run PPUC with RS484 communication to control the IO boards. It will also use a ZeDMD when available. Exit with CTRL-C.

### VirtualBox

Oracle [VirtualBox](https://www.virtualbox.org/) is a very nice tool to experiment with the software. Especially when you are not familiar with the Linux OS:

- Run any Linux distro in a separate virtual machine (a fresh start is easy). Easy to remove / delete when done.
- Use snapshots to save a specific machine state. That allows you to go back to a known good situation.
- Have a secure environment which is isolated from your OS, disks and network. You control what is shared / connected.

After creating a virtual computer it is best to install the VirtualBox Guest Additions: 

- Allows you to copy-paste from your computer (host) to the virtual machine.
- Provides functionallity to share folders.

When you want to use ppuc on the the virtual Linux machine with hardware (IO boards / ZeDMD) install the VirtualBox Extension Pack.
Then you can use the Virtual Machine Status Bar to connect with the appropiate USB port(s).
 