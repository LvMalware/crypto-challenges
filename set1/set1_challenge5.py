#!/usr/bin/env python2

import encoding

asc = lambda c : ord(c)

def xorCrypt(str, key):
	enc = ''
	for i in range(0, len(str), len(key)):
		for j in range(len(key)):
			if (i+j) < len(str):
				enc += chr(asc(str[i+j]).__xor__(asc(key[j])))
			else:
				break
	return encoding.hexEncode(enc)

if __name__ == '__main__':
	enc1 = xorCrypt('Burning \'em, if you ain\'t quick and nimble\n'
                  + 'I go crazy when I hear a cymbal', 'ICE')
	dec1 = encoding.hexDecode(xorCrypt(encoding.hexDecode(enc1), 'ICE'))
	print dec1
