import requests
from os import path
from pprint import pprint
from collections import Counter


def getPythonSite():
	r = requests.get('https://www.python.org')
	# print(r.content)

	# Count # of spans in r.content
	s = f'span count: {str(r.content).count("span")}'
	print(s)
	f = open('newFile.txt', 'w')
	f.write(s)
	f.close()

def getMobyDick():
	"""
	Download Moby Dick
	"https://www.gutenberg.org/files/76/76-0.txt"
	len == 691343
	"""
	# Implement file check
	if path.exists("mobyDick.txt"):
		print("Already downloaded!")
		return
		# f = open('mobyDick.txt', 'r')
		# s = f.read()


	r = requests.get('https://www.gutenberg.org/files/76/76-0.txt')
	a = r.text.replace("\n", ' ').replace("\r", ' ')
	# f = open('mobyDick.txt', 'w')
	# f.write(str(r.content))
	# f.close()

	with open('mobyDick.txt', 'w') as f:
		pprint(dir(f))
		f.write(a)

def readBook(s):
	""" count 10 most common words
	Return dictionary
		{
			"word": 102
		}
	"""
	with open(s) as f:
		s = f.read()
		words = s.split()
		# create data structure of 10 
		# most common words with counts
		c = Counter(words)
		pprint(c.most_common(10))
		print(f"Count a: {s.count(' a ')}")



if __name__ == "__main__":
	# getPythonSite()
	getMobyDick()
	readBook('mobyDick.txt')



