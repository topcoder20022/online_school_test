import os
import time
import subprocess
import random

a = 'git status'
b = 'git add .'
d = 'git push origin main'
c = 'git commit -m "fixed"'

numbers = random.randint(5, 30)
for j in range(1, numbers):

	file_object = open('data.txt', 'a')
	file_object.write(str(j))
	file_object.close()

	e= a + ' && ' + b + ' && ' + c + ' && ' + d 
	subprocess.call(e, shell = True)
	

		