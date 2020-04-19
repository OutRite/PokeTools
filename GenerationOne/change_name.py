#!/bin/python3

print("Loading...")

import re
import sys
import os

if len(sys.argv) != 3:
	print("Usage: ./change_name [name] [save file]")
	sys.exit()

print("Pokemon Red Trainer name changer")
print("Only letters should be used.")



player_name = sys.argv[1]

# regex: [A-z]

regex_test = re.findall("[A-z]", player_name)

if (len(regex_test) == len(player_name)):
	if (len(player_name) >= 8):
		print("Name too long!")
		sys.exit()
	else:
		print("Valid name")
		print("Name: {}".format(player_name))
		print("Name length: {}".format(len(player_name)))
		print("Converting name to Pokemon encoding...")
		fixed_name = ""
		for i in range(0, len(player_name)):
			# print("i: {}".format(i))
			# print("original character: {}".format(player_name[i]))
			old_name_char = player_name[i]
			fixed_name += chr(ord(player_name[i]) + 0x3F)
			print("Converted {} to {}!".format(hex(ord(old_name_char)), hex(ord(fixed_name[i]))))
		fixed_name += chr(0x50)
		filename = sys.argv[2]
		with open(filename, 'rb+') as f:
			print("Reading file {}...".format(filename))
			savedata = bytearray(f.read())
			print("Writing new name...")
			debug_data = ""
			for j in range(0, len(fixed_name)):
				debug_data += hex(ord(fixed_name[j])) + " "
				print("Current name data written: {}".format(debug_data))
				savedata[0x2598+j] = ord(fixed_name[j])
			print("Saving...")
			f.seek(0, 0)
			f.write(savedata)
		print("Fixing checksum... (Requires fix_that_checksum.py)")
		os.system('python3 fix_that_checksum.py {}'.format(filename))
else:
	print("Name contains invalid (non-alphabetical) characters.")
	sys.exit()



# capital A is 80