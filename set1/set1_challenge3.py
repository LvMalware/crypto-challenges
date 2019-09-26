#!/usr/bin/env python2
import encoding

asc = lambda c : ord(c)

english_commons = ['for', 'with', 'not', 'hard', 'well', 'easy', 'nice',
                   'you', 'never', 'bad', 'good', 'try', 'yes', 'please',
                   'very', 'now', 'never', 'always', 'right', 'crazy', 'the', 
                   'that', 'this']
def unxor(str, c):
	out = ''
	for j in range(len(str)):
		out += chr(asc(str[j]).__xor__(c))
	return out

def findXord(str):
	str = encoding.hexDecode(str)
	pos = []
	for i in range(256):
		pos.append(0)
		tmp = unxor(str, i).lower()
		for wrd in english_commons:
			if wrd in tmp:
				pos[i] = pos[i] + 1
	m = 0
	for y in range(256):
		if pos[y] > pos[m]:
			m = y
	if (pos[m] == 0):
		return -1
	return m
		


xor = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#XOR'd with char 88 (X)
#Original text: "Cooking MC's like a pound of bacon"

if (__name__ == '__main__'):
	c = findXord(xor)
	print c
	print unxor(encoding.hexDecode(xor), c)
