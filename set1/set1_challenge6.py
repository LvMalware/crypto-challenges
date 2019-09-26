#!/usr/bin/env python2

import encoding
import set1_challenge5
import math

asc = lambda c : ord(c)

def hamDist(c1, c2):
	dist, val = 0, asc(c1).__xor__(asc(c2))
	while (val != 0):
		dist +=1
		val &= val-1
	return dist
	
def getEditDistance(str1, str2):
	dist = int(((len(str1) - len(str2))**2)**0.5)
	for i in range(min(len(str1), len(str2))):
		dist += hamDist(str1[i], str2[i])
	return dist

def guessKeySize(text, minLen, maxLen):
	blockSizes = {}
	#print 'SIZE\tDISTANCE\tRELATION'
	for size in range(minLen, maxLen):
		dist = 0
		for k in range(size):
			if ((k + 1 * size) < len(text)):
				dist += hamDist(text[k + 0 * size], text[k + 1 * size])
			if ((k + 2 * size) < len(text)):
				dist += hamDist(text[k + 1 * size], text[k + 2 * size])
			if ((k + 3 * size) < len(text)):
				dist += hamDist(text[k + 2 * size], text[k + 3 * size])
			if ((k + 4 * size) < len(text)):
				dist += hamDist(text[k + 3 * size], text[k + 4 * size])
		#print '  %d\t    %d\t        %f' %(size, dist, float(dist)/size)
		blockSizes[dist / float(size)] = size
	blockDists = blockSizes.keys()
	blockDists.sort()
	best = math.ceil(sum(blockDists[:4]) / 4.0)
	#print best
	index = 0
	cmpr = abs(blockDists[0] - best)
	for i in range(len(blockDists)):
		tmp = abs(blockDists[i] - best)
		if (tmp < cmpr):
			cmpr = tmp
			index = i
	return blockSizes[blockDists[index]]
	
def sliceText(text, size):
	slices = []
	for i in range(0, len(text), size):
		slices.append(text[i : i+size])
	return slices

def transposeBlocks(slices, size):
	transposed = []
	for i in range(size):
		block = ''
		for j in range(len(slices)):
			if len(slices[j]) > i:
				block += slices[j][i]
			else:
				break
		transposed.append(block)
	return transposed

invalidChars = [chr(x) for x in range(8)] + [chr(x) for x in range(14, 25)] + [
                chr(x) for x in range(129, 256)] + ['\xc3', '~', '^', '/', '|',
                '`', '%', '#', '&', '?', '[','<', '>', '\\', ']', '{','}', '$',
                '=', '+'] #+ ['!']

def betterHistogram(block):
	count = []
	for k in range(256):
		tmp = ''
		for c in block:
			tmp += chr(asc(c).__xor__(k))

		val = len(tmp)
		for c in invalidChars:
			if (tmp.count(c) > 0):
				val = 0
				break
		count.append(val)
	m = 0
	for i in range(256):
		if count[i] > count[m]:
			m = i
	return m

def main():
	text = open('6.txt', 'r').read()
	text = encoding.base64Decode(text)
	print 'Text size:', len(text)
	print
	size = guessKeySize(text, 2, 40)
	print 'Provably key size:', size
	print
	part = sliceText(text, size)
	print 'Text splitted into %d blocks of %d bytes' %(len(part), len(part[0]))
	print
	tran = transposeBlocks(part, size)
	print 'Transposed blocks.'
	print 'Now we have %d blocks of %d bytes' %(len(tran), len(tran[0]))
	print
	key = ''
	for block in tran:
		key += chr(betterHistogram(block))
	print 'The key appears to be:', key
	print
	print 'The original text would be:'
	print
	print encoding.hexDecode(set1_challenge5.xorCrypt(text, key))
if __name__ == '__main__':
	main()
	

