#### BMP Heads

##### Head
```java
0x00 0x01
42 4D
BM
const
```
Only `BMP` file head.

##### FileSize
```java
0x02   0x05
XX XX XX XX
int
```
文件大小.

此处及之后 `int` 型数据均以此方式存储(小端方式):

```py
b=int(i).to_bytes(4,'little')
```

##### bfReserved
```java
0x06   0x09
00 00 00 00
const
```

##### bfOffBits
$\rm11\sim14,4B$
```java
0x0a   0x0d
XX XX XX XX
int
```
偏移量,即文件头总长度.
`24位位图` 为 `54` 即 `0x36` 即
```java
0x0a   0x0d
36 00 00 00
const int
```


#### `24位位图` Heads
After BMP Heads.

##### biSize
```java
0x0e   0x11
28 00 00 00
const int
```
`24位位图` Heads 长度,为 `40` 即 `0x28`.

##### biWidth,biHeight
```java
0x12   0x15  0x16   0x19
XX XX XX XX  XX XX XX XX
int          int
```
宽和高.

##### biPlanes
```java
0x1a 0x1b
01 00
const
```

##### biBitCount
```java
0x1c 0x1d
18 00
const short
```
像素 `bit` 数,为 `24` 即 `0x18`.

##### biCompression
$\rm31\sim34,4B$
```java
0x1e   0x21
00 00 00 00
const int
```
压缩等级,为 `0`.

##### ImageSize
```java
0x22   0x25
XX XX XX XX
int
```
图片内容大小(像素数 `*3B`).

##### Others
```java
0x26                                          0x36
00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
const
```

#### `24位位图` 模板
```java
42 4D XX XX XX XX 00 00  00 00 36 00 00 00 28 00 
      [FileSize ]
00 00 XX XX XX XX XX XX  XX XX 01 00 18 00 00 00 
      [  Width  ] [  Height  ]
00 00 XX XX XX XX 00 00  00 00 00 00 00 00 00 00 
      [ImageSize]
00 00 00 00 00 00       
```
Total: $\rm54B$


#### e.g. $1280*720$
$\rm Width=1280=0x0500,Height=720=0x02D0,$
$\rm ImageSize=1280*720*3=2764800B=0x002A3000,$
$\rm FileSize=ImageSize+54=2764854B=2.64MB=0x002A3036.$
```java
42 4D 36 30 2A 00 00 00  00 00 36 00 00 00 28 00 
      [FileSize ]
00 00 00 05 00 00 D0 02  00 00 01 00 18 00 00 00 
      [  Width  ] [  Height  ]
00 00 00 30 2A 00 00 00  00 00 00 00 00 00 00 00 
      [ImageSize]
00 00 00 00 00 00       
```

#### e.g. $1920*1080$
$\rm Width=1920=0x0780,Height=1080=0x0438,$
$\rm ImageSize=1920*1080*3=6220800B=0x005EEC00,$
$\rm FileSize=ImageSize+54=6220854B=5.93MB=0x005EEC36.$
```java
42 4D 36 EC 5E 00 00 00  00 00 36 00 00 00 28 00 
      [FileSize ]
00 00 80 07 00 00 38 04  00 00 01 00 18 00 00 00 
      [  Width  ] [  Height  ]
00 00 00 EC 5E 00 00 00  00 00 00 00 00 00 00 00 
      [ImageSize]
00 00 00 00 00 00       
```

#### e.g. $2560*1080$ (choose this)
$\rm Width=2560=0x0A00,Height=1080=0x0438,$
$\rm ImageSize=2560*1080*3=8294400B=0x007E9000,$
$\rm FileSize=ImageSize+54=8294454B=7.91MB=0x007E9036.$
```java
42 4D 36 90 7E 00 00 00  00 00 36 00 00 00 28 00 
      [FileSize ]
00 00 00 0A 00 00 38 04  00 00 01 00 18 00 00 00 
      [  Width  ] [  Height  ]
00 00 00 90 7E 00 00 00  00 00 00 00 00 00 00 00 
      [ImageSize]
00 00 00 00 00 00       
```

```py
b'BM6\x90~\x00\x00\x00\x00\x006\x00\x00\x00(\x00'
b'\x00\x00\x00\n\x00\x008\x04\x00\x00\x01\x00\x18\x00\x00\x00'
b'\x00\x00\x00\x90~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
b'\x00\x00\x00\x00\x00\x00'
```


#### e.g. $7680*4320$
$\rm Width=7680=0x1E00,Height=1080=0x10E0,$
$\rm ImageSize=7680*4320*3=99532800B=0x05EEC000,$
$\rm FileSize=ImageSize+54=99532854B=94.9MB=0x05EEC036.$
```java
42 4D 36 C0 EE 05 00 00  00 00 36 00 00 00 28 00 
      [FileSize ]
00 00 00 1E 00 00 E0 10  00 00 01 00 18 00 00 00 
      [  Width  ] [  Height  ]
00 00 00 C0 EE 05 00 00  00 00 00 00 00 00 00 00 
      [ImageSize]
00 00 00 00 00 00       
```

```py
head_8k=b'BM6\xc0\xee\x05\x00\x00\x00\x006\x00\x00\x00(\x00'
b'\x00\x00\x00\x1e\x00\x00\xe0\x10\x00\x00\x01\x00\x18\x00\x00\x00'
b'\x00\x00\x00\xc0\xee\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
b'\x00\x00\x00\x00\x00\x00'
```
