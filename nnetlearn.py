import os
import pickle
import sys

if len(sys.argv) != 2:
	print("Usage: nnetlearn.py data_file")
	sys.exit(1)

class Net:
	def __init__(self, name):
		self.name = name
	def run(self):
		print "My name is ", self.name


data = Net("Tom")
if os.path.exists(sys.argv[1]):
	with open(sys.argv[1], "rb") as file:
		data = pickle.load(file)
		print(data.run())
else:
	print("starting new")
	with open(sys.argv[1], "w") as file:
		pickle.dump(data, file)
