#!/usr/bin/env python

from setuptools import setup
exec(open("xkeysnail_plus/info.py").read())

setup(name="xkeysnail-plus",
      version=__version__,
      author="hikosato",
      url="https://github.com/hikosato/xkeysnail-plus",
      description=__description__,
      long_description=__doc__,
      packages=["xkeysnail_plus"],
      scripts=["bin/xkeysnail-plus"],
      license="GPL",
      install_requires=["evdev", "python-xlib", "inotify_simple"]
      )
