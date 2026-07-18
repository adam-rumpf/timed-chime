# Timed Chime

<a href="https://github.com/adam-rumpf/timed-chime/search?l=python"><img src="https://img.shields.io/badge/language-python-blue?logo=python&logoColor=white"/></a> <a href="https://github.com/adam-rumpf/timed-chime/releases"><img src="https://img.shields.io/github/v/release/adam-rumpf/timed-chime"/></a> <a href="https://github.com/adam-rumpf/timed-chime/blob/main/LICENSE"><img src="https://img.shields.io/github/license/adam-rumpf/timed-chime"/></a> <a href="https://github.com/adam-rumpf/timed-chime/commits/main"><img src="https://img.shields.io/maintenance/no/2026"/></a>

A small utility for playing chimes at timed intervals. Running the main script plays a chime sound effect at regular intervals (or alternating between two different intervals).

## Usage

This utility is meant to be run by executing the main `timer.py` script, while changing settings in the `settings.ini` file. Available settings include:

* `sound`: Name of the chime sound effect file in the `sounds/` folder.
* `sound2`: If nonempty, causes chimes to alternate between the sound effects "sound" and "sound2".
* `interval`: Number of seconds between chimes.
* `interval2`: If nonempty, causes chimes to alternate between `interval` seconds and `interval2` seconds.
* `cutoff`: Maximum number of chimes to play before automatically stopping.
* `delay`: If nonempty, specifies an initial delay before the first chime (in seconds).

## Credits

This software is released under an [MIT license](https://img.shields.io/github/license/adam-rumpf/timed-chime), Adam Rumpf, 2026.

The included sound effect `chime.wav` was generated using [Bfxr](https://www.bfxr.net/). Its pitch was lowered to create `chime2.wav` using [Audacity](https://www.audacityteam.org/).
