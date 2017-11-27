import subprocess

print('Running')

p = subprocess.Popen("C:/Program Files/Anaconda3/Library/bin/pyuic5.bat -x design.ui -o mainDesign.py")

stdout,stderr = p.communicate()

print('Finished')