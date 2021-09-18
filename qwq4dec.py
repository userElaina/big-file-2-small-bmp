from qwq4 import *
from qwq4 import blk_25k as _blk
from qwq4 import head_25k as _head

def qwq4dec(pth:str,check:bool=True)->None:
	if check:
		print('Goo Goo Goo')
	
	l=pth.rsplit('.',2)
	if len(l)!=3 or l[-1]!='bmp':
		return 'bad file name'
	opth=l[0]
	_o=len(l[1])
	_s=l[0]
	p=lambda x:_s+'.'+str(x).zfill(_o)+'.bmp'
	try:
		if int(l[1])!=1:
			pth=p(1)
	except:
		return 'bad file name'

	if not os.path.exists(pth):
		return 'no such file'

	f=open(pth,'rb')
	readlen=0
	f.read(54)
	
	
	hsh_of_this_blk=f.read(64)
	readlen+=64
	hsh_lst=list()
	nx=int.from_bytes(f.read(1),'little')
	readlen+=1
	if nx:
		hsh_of_next_blk=f.read(64)
		readlen+=64
		hsh_of_next_blk=f.read(1024-readlen)
		readlen=1024
		for h in enumerate(hsh_name):
			hsh_lst.append(f.read(hsh_len[h[0]]))
			readlen+=hsh_len[h[0]]
		for h in enumerate(hsh_head):
			hsh_lst.append(f.read(hsh_len[h[0]]))
			readlen+=hsh_len[h[0]]
	f.read(1024*2-readlen)
	readlen=1024*2

	len_of_blk_1=int.from_bytes(f.read(4),'little')
	readlen+=4
	f.read(1024*3-readlen)
	readlen=1024*3
	file_hsh_lst=list()
	for h in enumerate(hsh_name):
		file_hsh_lst.append(f.read(hsh_len[h[0]]))
		readlen+=hsh_len[h[0]]
	for h in enumerate(hsh_head):
		file_hsh_lst.append(f.read(hsh_len[h[0]]))
		readlen+=hsh_len[h[0]]
	f.read(1024*4-readlen)
	readlen=1024*4

	data=f.read(len_of_blk_1)
	open(opth,'wb').write(data)

	nw=2
	while nx:
		f=open(p(nw),'rb')
		readlen=0
		f.read(54)
		
		hsh_of_this_blk=f.read(64)
		readlen+=64
		hsh_lst=list()
		nx=int.from_bytes(f.read(1),'little')
		readlen+=1
		if nx:
			hsh_of_next_blk=f.read(64)
			readlen+=64
			hsh_of_next_blk=f.read(1024-readlen)
			readlen=1024
			for h in enumerate(hsh_name):
				hsh_lst.append(f.read(hsh_len[h[0]]))
				readlen+=hsh_len[h[0]]
			for h in enumerate(hsh_head):
				hsh_lst.append(f.read(hsh_len[h[0]]))
				readlen+=hsh_len[h[0]]
		f.read(1024*2-readlen)
		readlen=1024*2

		f.read(1024*4-readlen)
		readlen=1024*4

		data=f.read(_blk)
		open(opth,'ab').write(data)
		nw+=1

qwq4dec(r'C:\All\Sakura\Mili\PY\qwq\qwq4\221.iso.001.bmp')