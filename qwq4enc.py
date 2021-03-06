from qwq4 import *
from qwq4 import blk_25k as _blk
from qwq4 import head_25k as _head

def qwq4enc(pth:str)->None:
	sz=os.path.getsize(pth)
	n=(sz-1)//_blk
	mo=sz-n*_blk

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

		for h in hsh_name:
			hsh_lst.append(hashlib.new(h,data))

		blk_lst=[0,hsh_lst[-1].digest(),]

		open(p(1)+'.blk','wb').write(data+b'\x00'*(_blk-mo))

		for i in range(n):
			data=f.read(_blk)
			
			for h in hsh_lst:
				h.update(data)

			blk_lst.append(hashlib.new(hsh_name[-1],data).digest())
			open(p(i+2)+'.blk','wb').write(data)

	print('Make heads...')

	oldata=None
	for ii in range(n+1):
		i=n-ii+1

		data=blk_lst[i]
		if i!=n+1:
			data+=b'\x01'+blk_lst[i+1]
			data+=b'\x00'*(1024-len(data))
			for h in hsh_name:
				data+=hashlib.new(h,oldata).digest()
			for h in enumerate(hsh_head):
				data+=hashlib.new(hsh_name[h[0]],oldata[:h[1]]).digest()
		data+=b'\x00'*(1024*2-len(data))

		if i==1:
			data+=mo.to_bytes(4,'little')
			data+=b'\x00'*(1024*3-len(data))
			for h in hsh_lst:
				data+=h.digest()
			for h in enumerate(hsh_head):
				data+=hashlib.new(hsh_name[h[0]],open(pth,'rb').read(h[1])).digest()
		data+=b'\x00'*(1024*4-len(data))

		data=_head+data+open(p(i)+'.blk','rb').read()
		os.remove(p(i)+'.blk')

		open(p(i),'wb').write(data)
		oldata=data

qwq4enc(r'C:\All\Sakura\Mili\PY\qwq\qwq4\221.iso')
