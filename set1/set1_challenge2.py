#!/usr/bin/env python2
import encoding

asc = lambda c : ord(c)


def xorStr(str1, str2):
	str1 = encoding.hexDecode(str1)
	str2 = encoding.hexDecode(str2)
	str3 = ''
	for i in range(len(str1)):
		str3 += chr(asc(str1[i]).__xor__(asc(str2[i])))
	return encoding.hexEncode(str3)
	
print xorStr('1c0111001f010100061a024b53535009181c',
             '686974207468652062756c6c277320657965')
