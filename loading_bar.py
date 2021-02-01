import time
import sys
import os
import keyboard
toolbar_width = 50

# setup toolbar
#sys.stdout.write("%s" % (" " * toolbar_width))
#sys.stdout.flush()
#sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
print("Press DEL to enter Setup..........")
print("")
for i in range(toolbar_width):
    if keyboard.is_pressed("del"):
        os.system("module1.py")
        break
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("█")
    sys.stdout.flush()
#sys.stdout.write("]\n") # this ends the progress bar