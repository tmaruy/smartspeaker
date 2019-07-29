# Reference: https://qiita.com/na59ri/items/aea452f2487a393537dd

import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i",dest="input",action="store",default="",help="Path of input directory")
parser.add_argument("-o",dest="output",action="store",default="",help="Path of output file")
args = parser.parse_args()

header = """
begin remote

  name  {}
  flags RAW_CODES
  eps            30
  aeps          100

  gap          200000
  toggle_bit_mask 0x0

      begin raw_codes
"""

footer = """
      end raw_codes

end remote
"""

fo = open(args.output, "w")
groups = os.listdir(args.input)

# convert 
def convert_signal(file):
	count = 0; values = []; lines = []
	fi = open(file)
	for ii, jj in enumerate(fi):
		if ii == 0: continue
		value = jj.strip("\n").split(" ")[1]
		count += len(value) + 1
		if count < 80:
			values.append(value)
		else:
			lines.append(" ".join(values))
			values = [value]
			count = len(value) + 1
	if count < 80:
		lines.append(" ".join(values))
	fi.close()
	return lines

for g in groups:
	# Header
	fo.write(header.format(g))

	# Read & Write
	files = os.listdir(args.input + "/" + g)
	for f in files:
		fo.write("    name " + f + "\n")
		lines = convert_signal(args.input + "/" + g + "/" + f)
		fo.write("\n".join(lines) + "\n")

	# Footer
	fo.write(footer)

fo.close()
