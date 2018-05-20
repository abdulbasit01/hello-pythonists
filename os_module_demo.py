import os#is use to find directories
cur_dir=os.getcwd()
print(cur_dir)

import time
time.sleep(2)
os.rename("mkdir","new_dirf")
time.sleep(2)
os.rmdir("mkdir5")
