import hashlib,binascii
s=input()
s=s.encode('utf8')
s=hashlib.new('ripemd160',s).digest()
print(str(binascii.hexlify(s))[2:-1])