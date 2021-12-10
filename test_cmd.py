import os
import time
import subprocess

# while True:
# os.system("start \"\" cmd /k \"cd /D C:\\ & color 04\"")
a = 'git status'
b = 'git add .'
c = 'git commit -m "fixed"'
d = 'git push origin main'
e= a + ' && ' + b + ' && ' + c + ' && ' + d 
print(e)
subprocess.call(e, shell = True)
# subprocess.call(p, shell = True)