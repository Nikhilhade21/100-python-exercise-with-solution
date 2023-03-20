'''Please write a program to compress and decompress the string ”hello world!hello
world!hello world!hello world!”.'''

import zlib

t = zlib.compress(b'hello world!helloworld!hello world!hello world!')
print(t)
print(zlib.decompress(t))