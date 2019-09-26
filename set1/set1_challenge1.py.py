#!/usr/bin/env python2

import base64

hexchars='0123456789abcdef'
asc = lambda x : ord(x)

def hexDecode(hexStr):
	str = ''
	for i in range(0, len(hexStr), 2):
		str += chr(hexchars.index(hexStr[i]) * 16 + hexchars.index(hexStr[i+1]))
	return str

def base64Encode(str):
	return base64.encodestring(str)

def base64Decode(str):
	return base64.decodestring(str)

def hexEncode(str):
	hexStr = ''
	for i in range(len(str)):
		hexStr += hex(asc[str[i]])[2:]
	return hexStr

def hexToBase64(hexStr):
	return base64Encode(hexDecode(hexStr))

if (__name__=='__main__') :
	print hexToBase64('49276d206b696c6c696e6720796f757220627261696e206'
	+ 'c696b65206120706f69736f6e6f7573206d757368726f6f6d')

