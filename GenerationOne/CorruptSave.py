print("POKEMON SAVE CORRUPTOR")
print("THIS WILL DESTROY YOUR SAVE DATA")
print("DO NOT USE WITHOUT A BACKUP NO MATTER WHAT")
confirmation_data = input("IF YOU ARE ABSOLUTELY SURE, TYPE OkAyTheNCorrUpTIt: ")

if confirmation_data != "OkAyTheNCorrUpTIt":
	import sys
	print("Okay, quitting...")
	sys.exit()

print("Fine. I take no responsibility.")

print("Importing libraries...")

import sys
import random
import os

filename = input("Enter filename: ")

with open(filename, 'rb+') as f:
	print("Reading file {}...".format(filename))
	savedata = bytearray(f.read())
	print("Beginning corruption...")
	for corrupted_mem_place in range(0, 0x3523-0x2597):
		corrupted_byte = random.randrange(255)
		savedata[corrupted_mem_place+0x2597] = corrupted_byte
		# print("Byte: {}".format(corrupted_byte))
		# print("Address: {}".format(hex(corrupted_mem_place)))
		print("Corrupted {}%".format(round((corrupted_mem_place/0xF8B)*100, 2)))
	print("Corrupted!")
	print("Saving...")
	f.seek(0, 0)
	f.write(savedata)
	print("Complete. Fixing checksum...")

os.system('python3 fix_that_checksum.py {}'.format(filename))
print("gg rip your save")