# Build from Source

To build the PPUC executable you need to compile the source files:

1. Install the compiler and some helper tools for automation of the build process.
2. Get the target dependent header files for the system libraries used by PPUC.
3. Run the appropiate build.sh (located in the platforms dir).

## Linux

You can build for an ARM CPU (aarch64) or AMD/Intel CPU (x64) depending on the CPU of the target computer you want to use for PPUC. It does not really matter which Linux distro is used.

The easiest way to compile is on a Linux computer. This guide is tested with Ubuntu and Debian. Both use the Advanced Package Tool (APT). On a Windows PC, you can use VirtualBox.

It is advised to update the list of packages, upgrade installed packages and cleanup first:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
```

### Compiler

Install the compiler :
```shell
sudo apt-get install build-essential
```

Install the tools used by build.sh:
```shell
sudo apt install cmake curl autoconf libtool pkg-config zlib1g zlib1g-dev
```

### Header files

Install the header files to be used by the compiler:
```shell
sudo apt install libudev-dev libasound2-dev libpulse-dev libaudio-dev libjack-dev 
sudo apt install libsndio-dev libx11-dev libxext-dev libxrandr-dev libxcursor-dev
sudo apt install libxfixes-dev libxi-dev libxss-dev libxtst-dev libxkbcommon-dev
sudo apt install libdrm-dev libgbm-dev libgl1-mesa-dev libgles2-mesa-dev
sudo apt install libegl1-mesa-dev libdbus-1-dev libibus-1.0-dev libudev-dev
sudo apt install libpipewire-0.3-dev libwayland-dev libdecor-0-dev liburing-dev
```

### Build

Get the source files:
```
mkdir $HOME/projects
cd $HOME/projects
git clone https://github.com/PPUC/ppuc.git
```

#### Compile (PC):
```
cd ppuc
platforms/linux/x64/build.sh
```
#### Compile (Raspberry Pi):
```
cd ppuc
platforms/linux/aarch64/build.sh
```

### Test

Use the example/t2.yml to try:

- Download the ROM for Terminator 2 Judgement Day (L-8): t2_l8.zip
- Create a directory for pinmame: $HOME/.pinmame
- Create a subdirectory: $HOME/.pinmame/roms
- Copy t2_l8.zip to roms

Run from the ppcu directory (where you called build.sh):
```
ppuc/ppuc-pinmame -c examples/t2.yml -n -i
```
This should run PPUC without RS484 communication. Exit with CTRL-C.

To see all commandline options:
```
ppuc/ppuc_pinmame --help
```
