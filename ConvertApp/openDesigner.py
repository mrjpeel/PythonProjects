import subprocess

p = subprocess.Popen("C:/Program Files/Anaconda3/Library/bin/designer.exe")

stdout,stderr = p.communicate()

print('Finished')

