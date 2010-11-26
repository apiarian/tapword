#! /opt/local/bin/python

#getch code adapted from http://code.activestate.com/recipes/134892/
try:
	import msvcrt
	def getch():
		return msvcrt.getch()
except ImportError:
	import sys, tty, termios
	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
		return ch

import time
timeout = 1 #second
length_threshold = 1
target='sssl'
raw_sequence = []
last_t = time.time()
current_t = time.time()
while True:
	a = getch()
	#quit
	if a=="q":
		sys.exit()
	#process
	elif a==" ":
		last_t = current_t
		current_t = time.time()
		delta_t = current_t - last_t
		if delta_t >= timeout:
			raw_sequence = []
			continue
		else:
			raw_sequence.append(delta_t)
		sequence = ''.join([('l' if round(x/min(raw_sequence))>length_threshold else 's') for x in raw_sequence])
		print sequence
		if sequence.endswith(target):
			print 'match!'

