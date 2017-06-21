XGraphic
===

Linux helper for switching between Nvidia and Bumblebee.

# Actions

- Creating Xorg configuration for nvidia
- Creating modprobe configuration for nvidia and bumblebee
- Creating/Removing service of bumblebee
- Creating xinit configuration for nvidia and bumblebee

# Installing

Add below line to `~/.xinitrc` file

```
/etc/xgraphic/xgraphic
```

# Usage

Switching to nvidia
```
xgraphic -s nvidia
```

Switching to bumblebee
```
xgraphic -s bumblebee
```

**Don't forget to restart xorg**

# Changing Stubs

## Switching to Nvidia

- Copy `stubs/xorg.conf` file to `/etc/X11/xorg.conf`
- Copy `stubs/nvidia.conf` file to `/usr/lib/modprobe.d/nvidia.conf`
- Copy `stubs/.xgraphic-nvidia` file to `/etc/xgraphic/.xgraphic`
- Disabling **bumblebeed** service (`systemctl disable bumblebeed`)
- Removing `/usr/lib/modprobe.d/bumblebee.conf` file

## Switching to Bumblebee

- Copy `stubs/bumblebee.conf` file to `/usr/lib/modprobe.d/bumblebee.conf`
- Copy `stubs/.xgraphic-bumblebee` file to `/etc/xgraphic/.xgraphic`
- Enabling **bumblebeed** service (`systemctl enable bumblebeed`)
- Removing `/etc/X11/xorg.conf` file
- Removing `/usr/lib/modprobe.d/nvidia.conf`

## Extra Configuration

When you need add or remove something, you can change stub file. Example, if you want change DPI on bumblebee you can
change `stubs/.xgraphic-bumblebee` file.