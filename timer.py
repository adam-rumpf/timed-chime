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
    """
    
    config = configparser.ConfigParser()
    config.read(infile)
    sound = os.path.join(sound_folder, config["settings"]["sound"].strip('" '))
    interval = int(config["settings"]["interval"])
    cutoff = int(config["settings"]["cutoff"])
    
    return sound, interval, cutoff

def main():
    """Runs the main chime-playing script."""
    
    # Read settings
    sound, interval, cutoff = _read_settings()
    
    # Run until a stop condition is met
    stopping = False
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
            time.sleep(interval)

#------------------------------------------------------------------------------

if __name__ == "__main__":
    # Read settings and compute maximum time
    _, interval, cutoff = _read_settings()
    maxtime = cutoff*interval
    if maxtime <= 60:
        mtstring = f"{maxtime} seconds"
    elif maxtime % 60 == 0:
        m = maxtime // 60
        mtstring = f"{m} minutes"
    else:
        m = maxtime // 60
        s = maxtime % 60
        mtstring = f"{m} minutes, {s} seconds"
    
    # Print instructions
    print(f"Chimes playing in {interval}-second intervals for up to {mtstring}.")
    print("Press [Ctrl]+[C] (or close window) to quit early.")
    
    # Start main loop
    main()
