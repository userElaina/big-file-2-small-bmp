import os
import hashlib

head_25k=b'BM6\x90~\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x00\n\x00\x008\x04\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x90~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
blk_25k=8096*1024

head_480p=b'BM6\x10\x0e\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x80\x02\x00\x00\xe0\x01\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x10\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
blk_480p=896*1024

head_8k=b'BM6\xc0\xee\x05\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x00\x1e\x00\x00\xe0\x10\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\xc0\xee\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
blk_8k=97196*1024

hsh_name=['md5','sha1','sha224','sha256','sha384','sha512',]
hsh_len=[16,20,28,32,48,64,]
hsh_head=[256*1024,]