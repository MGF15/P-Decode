import itertools,sys,time
from hashlib import sha1

'''

android pattern cracker 

Coded by MGF15

file in android ->  /data/system/gesture.key
'''

pattern = "012345678"

p_ = '''
 +---+---+---+
 | 0 | 1 | 2 |
 +---+---+---+
 | 3 | 4 | 5 |
 +---+---+---+
 | 6 | 7 | 8 |
 +---+---+---+
'''
now=time.time()

def crack(hash):
	
	for i in range(4,10):

		for p in itertools.permutations(pattern, i):
			# pattern -> 1234 -> 01020304 -> \x01\x02\x03\x04 then sha1 hash
			x = ''.join(['0' + i for i in p]).decode('hex')

			sha1_hash = sha1(x).hexdigest()

			if hash == sha1_hash:

				print '[+] pattern -> ' , ''.join(p) 
				print p_
				print '[*] Time : ', round(time.time() - now, 2)
if __name__ == "__main__":

	if len(sys.argv) < 3:
		print 'p-decode.py [-p hash ] or [-f gesture.key]'

	elif sys.argv[1] == '-f':
		file = open(sys.argv[2],'rb').read()
		hash = file.encode('hex')
		crack(hash)

	elif sys.argv[1] == '-p':
		hash = sys.argv[2]		
		crack(hash)
	else:
		exit()
