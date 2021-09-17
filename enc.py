
import os
import hashlib

_head=b'BM6\x90~\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x00\n\x00\x008\x04\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x90~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

_hsh=['sha3_512','md5','sha1']
# _head3=4*1024
_block=8096*1024

def qwq4(pth:str)->None:
	sz=os.path.getsize(pth)
	n=(sz-1)//_block
	mo=sz-n*_block

	if n<100:
		p=lambda x:pth+'.'+str(x).zfill(2)+'.bmp'
	elif n<1000:
		p=lambda x:pth+'.'+str(x).zfill(3)+'.bmp'
	elif n<1000:
		p=lambda x:pth+'.'+str(x).zfill(4)+'.bmp'
	elif n<1000:
		p=lambda x:pth+'.'+str(x).zfill(5)+'.bmp'
	else:
		p=lambda x:pth+'.'+str(x).zfill(10)+'.bmp'

	print('Cut the file...')

	hsh_lst=list()
	with open(pth,'rb') as f:
		data=f.read(mo)

		for h in _hsh:
			hsh_lst.append(hashlib.new(h,data))

		blk_lst=[0,hsh_lst[0].digest(),]

		open(p(1)+'.block','wb').write(data+b'\x00'*(_block-mo))

		for i in range(n):
			data=f.read(_block)
			
			for h in hsh_lst:
				h.update(data)

			blk_lst.append(hashlib.new(_hsh[0],data).digest())
			open(p(i+2)+'.block','wb').write(data)

	print('Make heads...')

	oldata=None
	for ii in range(n+1):
		i=n-ii+1

		data=blk_lst[i]
		if i!=n+1:
			data+=b'\x01'+blk_lst[i+1]
			data+=b'\x00'*(1024-len(data))
			for h in _hsh:
				data+=hashlib.new(h,oldata).digest()
			data+=hashlib.new('md5',oldata[:256*1024]).digest()
		data+=b'\x00'*(1024*2-len(data))

		if i==1:
			data+=mo.to_bytes(4,'little')
			data+=b'\x00'*(1024*3-len(data))
			for h in hsh_lst:
				data+=h.digest()
			data+=hashlib.new('md5',open(pth,'rb').read(256*1024)).digest()
		data+=b'\x00'*(1024*4-len(data))

		data+=open(p(i)+'.block','rb').read()
		os.remove(p(i)+'.block')

		open(p(i),'wb').write(_head+data)
		oldata=data
