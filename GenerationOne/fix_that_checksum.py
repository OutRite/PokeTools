#!/bin/python3

import sys

if (len(sys.argv) < 2):
	print("Usage:")
	print("./fix_that_checksum.py [broken save]")
	sys.exit()

with open(sys.argv[1], 'rb+') as f:
	print("Reading file {}".format(sys.argv[1]))
	savedata = bytearray(f.read())
	print("Current checksum: 0xff")
	checksum = 0xff
	for c in savedata[0x2598:0x3523]:
		checksum -= c
		print("Current checksum: {}".format(hex(checksum)))
	print("Found checksum: {}".format(checksum&0xff))
	savedata[0x3523] = checksum & 0xff
	print("Writing checksum to file...")
	f.seek(0, 0)
	f.write(savedata)
	print("Complete!")