import os
import time
import subprocess
import random

date2 = 120
date1 = 90

numbers = 3
# while True:
# os.system("start \"\" cmd /k \"cd /D C:\\ & color 04\"")
a = 'git status'
b = 'git add .'
d = 'git push origin main'
for i in range(date1, date2):
	print("*********************************************", i)
	run_or = random.randint(1, 6)
	if run_or != 1:
		numbers = random.randint(2, 8)
		for j in range(1, numbers):

			file_object = open('data.txt', 'a')
			file_object.write(str(i) + str(j))
			file_object.close()

			c = 'git commit --date="' + str(i) + ' day ago" -m "new data added ' + str(j) + '"'
			print(c)
			e= a + ' && ' + b + ' && ' + c + ' && ' + d 
			subprocess.call(e, shell = True)
	else:
		continue

		