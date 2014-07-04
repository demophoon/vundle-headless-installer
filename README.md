Headless Vundle Installer
=========================

Install your Vundle plugins without opening Vim.

How to use
----------

It's as easy as running `python install.py`.
The script looks for your vimrc files and installs any bundles within them.

Why not just open Vim and run :BundleInstall?
---------------------------------------------

I had problems where I would try to install my dotfiles in a docker container
build where everything runs headless and vim does not open because there is no
screen. After the build finishes Vim is installed but I have to run
:BundleInstall every time I launch a container. This script fixes that.
