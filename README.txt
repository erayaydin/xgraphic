========
XGraphic
========

XGraphic provides Xorg graphic card switching between nvidia and bumblebee. Also, its do it automatically with
enabling/disabling services.

Actions
=======

* Creating Xorg configuration for nvidia

* Creating modprobe configuration for nvidia and bumblebee

* Creating/Removing service of bumblebee

* Creating xinit configuration for nvidia and bumblebee

Installing
==========

Start ``/etc/xgraphic/xgraphic`` before execution DM/WM.

For example, add below line before **exec ...** to `~/.xinitrc` file

```
/etc/xgraphic/xgraphic
```

Usage
=====

Switching to nvidia

``xgraphic -s nvidia``

Switching to bumblebee

``xgraphic -s bumblebee`

**Don't forget to restart xorg**
