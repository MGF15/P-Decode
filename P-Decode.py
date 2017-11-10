import itertools
import sys
import time
import svg
from hashlib import sha1
from binascii import unhexlify
from binascii import hexlify

if sys.version_info >= (3, 0):
    sha = sha1
else:
    import _sha
    sha = _sha.new
'''

android pattern cracker v0.4

Coded by MGF15

file in android ->  /data/system/gesture.key

'''
logo = '''
        |~)  |~\ _ _ _  _| _
        |~ ~~|_/}_(_(_)(_|}_ v0.4\n
             [ {41}ndr0id Pa77ern Cr4ck t00l. ]
       '''
now = time.time()

x_list = ["\x00", "\x01", "\x02", "\x03", "\x04",
          "\x05", "\x06", "\x07", "\x08"]


def crack(hash):

    print (logo)
    print ('[*] Pattern SHA1 Hash   : %s\n' % hash.upper())
    # make it as fast as possible
    # pattern -> 1234 -> 01020304 -> \x01\x02\x03\x04 then sha1 hash

    for i in range(4, 10):

        permutations = itertools.permutations(x_list, i)

        perm_list = map(''.join, permutations)

        for j in perm_list:

            sha_hash = sha(j.encode('utf-8')).hexdigest()

            if hash == sha_hash:

                p = hexlify(j.encode('utf-8')).decode('utf-8')

                pt = ''.join([p[o] for o in range(1, len(p), 2)])

                print ('[+] Pattern Length \t: %s\n' % len(pt))

                print ('[+] Pattern \t\t: %s\n' % pt)

                patt = svg.draw(pt)

                sv = open('%s.svg' % pt, 'wb')

                sv.write(patt.encode('utf-8'))

                sv.close()

                print ('[+] Pattern SVG\t\t: %s.svg\n' % pt)

                print ('[*] Time \t\t: %s sec' % round(time.time() - now, 2))

                exit()

    print ('[-] Pattern not found !')

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print ('p-decode.py [-p hash ] or [-f gesture.key ] or [-g pattern ]')

    elif sys.argv[1] == '-f':
        file = open(sys.argv[2], 'rb').read()
        hash = hexlify(file)    # file.encode('hex')
        crack(hash.decode('utf-8'))

    elif sys.argv[1] == '-p':
        hash = sys.argv[2]
        hash = hash.lower() if hash.isupper() else hash
        crack(hash)

    elif sys.argv[1] == '-g':
        print (logo)
        pat = sys.argv[2]
        gt = unhexlify('0' + '0'.join(pat))
        output = open('gesture.key', 'wb')
        output.write(sha1(gt).digest())
        output.close()
        print ('[+] Pattern file : gesture.key')
    else:
        exit()
