#### BMP Heads

##### Head
$\rm1\sim2,2B$
```java
42 4D
BM
const
```
Only `BMP` file head.

##### FileSize
$\rm3\sim6,4B$
```java
XX XX XX XX
int
```
文件大小.

此处及之后 `int` 型数据均以此方式存储:

$x_1,x_2,x_3,x_4,:x_i{\rm=hex(size)}[-2i:-2i+2].$



##### bfReserved
$\rm7\sim8,9\sim10,2*2=4B$
```java
00 00 00 00
const
```

##### bfOffBits
$\rm11\sim14,4B$
```java
XX XX XX XX
int
```
偏移量,即文件头总长度.
`24位位图` 为 $54$ 即 `36 00 00 00`.


#### `24位位图` Heads
After BMP Heads.

##### biSize
$\rm15\sim18,4B$
```java
28 00 00 00
const int
```
`24位位图` Heads 长度,为 $40$ 即 `28 00 00 00`.

##### biWidth,biHeight
$\rm19\sim22,23\sim26,2*4=8B$
```java
XX XX XX XX  XX XX XX XX
int
```
宽和高.

##### biPlanes
$\rm27\sim28,2B$
```java
01 00
const
```

##### biBitCount
$\rm29\sim30,2B$
```java
18 00
const short
```
像素 `bit` 数,为 $24$ 即 `18 00`.

##### biCompression
$\rm31\sim34,4B$
```java
00 00 00 00
const int
```
压缩等级,为 $0$ 即 `00 00 00 00`.

##### ImageSize
$\rm35\sim38,4B$
```java
XX XX XX XX
int
```
图片内容大小(像素数$\rm*3B$).

##### Others
$\rm39\sim54,16B$
```java
00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
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
