"""A script for playing sound effects at regular time intervals.

The expected file structure consists of:
./
    timer.py
    settings.ini
    sounds/
        (any sound effect files referenced in settings.ini)
"""

import configparser
import os.path
import time

import playsound3

#------------------------------------------------------------------------------

sound_folder = "sounds" # name of folder that contains sounds

def _read_settings(infile="settings.ini"):
    """Reads timer settings from config file.
    
    Returned settings include, respectively:
        sound - Name of chime sound file in sound_folder.
        interval - Number of seconds between chimes.
        cutoff - Maximum number of loops to run.
        interval2 - Alternate time interval. If nonempty, alternates between
            playing chimes at time intervals of "interval" and "interval2".
    """
    
    config = configparser.ConfigParser()
    config.read(infile)
    
    # Read settings file
    sound = os.path.join(sound_folder, config["settings"]["sound"].strip('"\' '))
    interval = int(config["settings"]["interval"])
    cutoff = int(config["settings"]["cutoff"])
    
    # Read interval2 last (for backward compatibility)
    interval2 = interval
    try:
        interval2 = int(config["settings"]["interval2"])
    except (KeyError, ValueError):
        pass
    
    return sound, interval, cutoff, interval2

def main():
    """Runs the main chime-playing script."""
    
    # Read settings
    sound, interval, cutoff, interval2 = _read_settings()
    
    # Run until a stop condition is met
    stopping = False
    alternate = False
    iter = 0
    while stopping == False:
        iter += 1
        
        # Play sound
        playsound3.playsound(sound)
        
        # Determine stopping condition
        if iter >= cutoff:
            stopping = True
        
        # Wait (unless already stopping)
        if stopping == False:
            # Alternate time intervals
            if alternate == False:
                time.sleep(interval)
            else:
                time.sleep(interval2)
            alternate = not alternate

#------------------------------------------------------------------------------

if __name__ == "__main__":
    # Read settings and compute maximum time
    _, interval, cutoff, interval2 = _read_settings()
    maxtime = cutoff*((interval + interval2)/2)
    if maxtime <= 60:
        mtstring = f"{maxtime:g} seconds"
    elif maxtime % 60 == 0:
        m = maxtime // 60
        mtstring = f"{m:g} minutes"
    else:
        m = maxtime // 60
        s = maxtime % 60
        mtstring = f"{m:g} minutes, {s:g} seconds"
    
    # Print instructions
    if interval == interval2:
        print(f"Chimes playing in {interval:g}-second intervals for up to " +
        f"{mtstring}.")
    else:
        print(f"Chimes playing in alternate {interval:g}-second/{interval2:g}" +
        f"-second intervals for up to {mtstring}.")
    print("Press [Ctrl]+[C] (or close window) to quit early.")
    
    # Start main loop
    main()
