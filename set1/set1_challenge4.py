#!/usr/bin/env python2
import encoding
import set1_challenge3

asc = lambda c : ord(c)

file = open('4.txt', 'r')

n = 0
for line in file.readlines():
	print "Line #%d: %s" %(n, line.rstrip())
	c = set1_challenge3.findXord(line.rstrip())
	if (c > -1):
		print "Encoded (%d): %s" %(c, set1_challenge3.unxor(encoding.hexDecode(line.rstrip()), c))
	n += 1
		
#7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f
#nOWTHATHEPARTYISJUMPING* (Xor'd with 21)
