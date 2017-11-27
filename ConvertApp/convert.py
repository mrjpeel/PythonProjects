import subprocess

uiFile = input("PLease enter the name of the UI file you want to convert\n")

def convert():
    p = subprocess.Popen("pyuic5.bat -x uiFile -o mainDesign.py")
    stdout,stderr = p.communicate()



if __name__ == '__main__':
    print('Running')
    convert()
    print('Finished')