import os
import time
import subprocess
import random

date2 = 100
date1 = 30

numbers = 3
while True:
	a = 'git status'
	b = 'git add .'
	d = 'git push origin main'
	numbers = random.randint(2, 8)
	for j in range(1, numbers):

		file_object = open('data.txt', 'a')
		file_object.write(str(i) + str(j))
		file_object.close()

		c = 'git commit --date="' + str(i) + ' day ago" -m "new data added ' + str(j) + '"'
		print(c)
		e= a + ' && ' + b + ' && ' + c + ' && ' + d 
		subprocess.call(e, shell = True)
	

		