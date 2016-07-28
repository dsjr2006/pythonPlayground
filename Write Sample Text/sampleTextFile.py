# Use the hashlib Python library to create a 'sample.txt' file in the current directory with the text "My first output file!" save the file, 
# then reopens the file to print to console the files SHA-1, SHA-256, and MD-5 hashes. 

import hashlib

outFile = open('sample.txt', 'w')
outFile.write('My first output file!')
outFile.close()





inFile = open('sample.txt', 'r')
hash_object = hashlib.sha1(inFile.read())
hex_dig = hash_object.hexdigest()
print("SHA-1: "+ hex_dig)
inFile = open('sample.txt', 'r')
hash_object = hashlib.sha256(inFile.read())
hex_dig = hash_object.hexdigest()
print("SHA-256: "+ hex_dig)
inFile = open('sample.txt', 'r')
hash_object = hashlib.md5(inFile.read())
hex_dig = hash_object.hexdigest()
print("MD-5: "+ hex_dig)