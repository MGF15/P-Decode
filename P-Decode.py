import itertools,sys,time
from hashlib import sha1
from binascii import unhexlify , hexlify

'''

android pattern cracker v0.2

Coded by MGF15

file in android ->  /data/system/gesture.key

'''

pattern = "012345678"

patt = '''
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
	print '''
	|~)  |~\ _ _ _  _| _
	|~ ~~|_/}_(_(_)(_|}_ v0.2\n
		[ {41}ndr0id Pa77ern Cr4ck t00l. ]
	'''
	print '[*] Pattern Hash   : %s\n' % hash

	for i in range(4,10):

		for p in itertools.permutations(pattern, i):
			# pattern -> 1234 -> 01020304 -> \x01\x02\x03\x04 then sha1 hash
			
			x = unhexlify(''.join(p).replace("","0")[:-1]) # ''.join(['0' + i for i in p])) #.decode('hex')
			
			sha1_hash = sha1(x).hexdigest()
			
			if hash == sha1_hash:
				print '[+] Pattern Length : %s\n' % len(p)
				print '[+] Pattern \t   : %s' % ''.join(p) 
				print patt
				print '[*] Time : %s sec' % round(time.time() - now, 2)  
				exit()
	print "[-] Pattern not found !"
if __name__ == "__main__":

	if len(sys.argv) < 3:
		print 'p-decode.py [-p hash ] or [-f gesture.key]'

	elif sys.argv[1] == '-f':
		file = open(sys.argv[2],'rb').read()
		hash = hexlify(file) #file.encode('hex')
		crack(hash)

	elif sys.argv[1] == '-p':
		hash = sys.argv[2]		
		crack(hash)
	else:
		exit()
