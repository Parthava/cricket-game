import random

wkt=1
run=0
while(wkt<10):
	num=(0,1,2,3,4,6)
	r1=random.choice(num)
	if(r1==1):
		run=run+1
		print('\nPlayer:',wkt)
		print('\nRun:',run)
		input('\nNext ball')
	elif(r1==2):
		run=run+2
		print('\nPlayer:',wkt)
		print('\nRun:',run)
		input('\nNext ball')
	elif(r1==3):
		run=run+3
		print('\nPlayer:',wkt)
		print('\nRun:',run)
		input('\nNext ball')
	elif(r1==4):
		run=run+4
		print('\nPlayer:',wkt)
		print('\nRun:',run)
		input('\nNext ball')
	elif(r1==6):
		run=run+6
		print('\nPlayer:',wkt)
		print('\nRun:',run)
		input('\nNext ball')
	else:
		print('\nPlayer:',wkt)
		wkt=wkt+1
		if(wkt>0):
			print('\n---------- Out ---------')
print('\n****** All Out *******')
print('\nYour score is',run)