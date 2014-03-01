Title: 某公司校园招聘在线测试题
Date: 2011-09-08 06:41
Author: 糖拌咸鱼
Slug: mou-gong-si-xiao-yuan-zhao-pin-zai-xian-ce-shi-ti

<div>

**题目：**

</div>

</p>

<div>

以下程序是一个信息编码的程序，阅读其encode部分，并补全其decode部分 

</div>

</p>

<div>

最后运行程序，会打印出的一句话。这句话就是我们要求的答案。 

</div>

</p>

<div>

</div>

</p>

<div>

**注意！这句话是用GBK编码的！ **

</div>

</p>

<div>

**  
**

</div>

</p>

<div>

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:cpp;gutter:false;}
#include  <stdio.h> #include  <stdlib.h> #include  <stdint.h> #include  <assert.h> #include  <string.h> int  encode(const  void*  raw_in,  void*  raw_out,  uint32_t  password,  size_t  len) { const  uint8_t*  in  =  (const  uint8_t*)raw_in; uint8_t*  out  =  (uint8_t*)raw_out; uint32_t  seed  =  password  ^  0x283265afu; for  (size_t  i  =  0  ;  i  <  len;  ++i)  {     uint8_t  a  =  (  in[i]  ^  seed  )  >>  3;    uint8_t  b  =  (  (  ((uint32_t)in[i])  <<  20  )  ^  seed  )  >>  (20-5);   a  &=  31;   b  &=  224;  a  =  31  &  (  a  ^  (b  <<  3));     out[i]  =  a  |  b;  seed  =  (seed  *  129491  ^  seed  ^  in[i]); } } int  decode(const  void*  raw_in,  void*  raw_out,  uint32_t  password,  size_t  len) {     const  uint8_t*  in  =  (const  uint8_t*)raw_in;     uint8_t*  out  =  (uint8_t*)raw_out;  uint32_t  seed  =  password  ^  0x283265afu;     for  (size_t  i  =  0  ;  i  <  len;  ++i)  { 
```

</p>
<p>
``` {.brush:cpp;gutter:false;}
　　　　　　//以下为要求编写的decode代码     uint8_t a = (in[i]&31);      uint8_t b = (in[i]&224);     uint8_t c =(b^(seed>>15))>>5;        c &= 7;      uint8_t d = ((a<<3)^seed);     d-=(d&7);        out[i] = c+d;        seed  =  (seed  *  129491  ^  seed  ^  out[i]);  } } int  main() {  const  uint8_t  buf1[]  =  {0x77,  0xc8,  0x43,  0x35,  0x56,  0xc2,  0x51,  0x43,  0x63,  0xff,  0xb1,  0x26,  0x00,  0xc4,  0x86,  0xf9,  0xe6,  0x4c,  0xe9,  0x48,  0x83,  0xa9,  0x27,  0x6a,  0xa5,  0xb2,  0x27,  0x2b,  0x98,  0x5f,  0xc0,  0x3f,  0xe0,  0xdf,  };     uint8_t  buf2[100]  =  {};   const  uint32_t  password  =  0xfbf2eeabu;   const  size_t  len  =  sizeof(buf1);     decode(buf1,buf2,password,len);　　　printf("%s\d",buf1);    } 
```

</p>
<p>

</div>

</p>

　　

</p>
<p>

</div>

</p>

<div>

</p>

　　有点悲剧的。点开题目，发现答题时间是30分钟，那时候我没准备c++编译工具，后来又答了一次，发现vc6.0无法编译。好吧，我换了linux，发现用g++可以通过，大喜，但是输出的格式却不是要求的GBK，调了很久，也没输出成GBK。
最后一次，果断在linux上把输出结果输出到文件，然后再邮件到windows，再用windows打开，发现终于出现预期结果了，但是结果是一则广告。。。 

</p>

　　最后写以下思路：

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:cpp;gutter:false;}
uint8_t  a  =  (  in[i]  ^  seed  )  >>  3; 
```

</p>
<p>

</div>

</p>

　　这个仔细分析下，发现可以逆解析出原数据的一部分，后3bit丢失。

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:cpp;gutter:false;}
uint8_t  b  =  (  (  ((uint32_t)in[i])  <<  20  )  ^  seed  )  >>  (20-5); 
```

</p>
<p>

</div>

</p>

　　这个呢，分析可以发现后5bit是没有丢失的，可以decode出来，和前面的一款
，可以拼接出原来的内容，接下来，只要知道a和b的值就ok了。

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:cpp;gutter:false;}
a  &=  31; b  &=  224; a  =  31  &  (  a  ^  (b  <<  3)); out[i]  =  a  |  b; 
```

</p>
<p>

</div>

</p>

　　这几句话，仔细分析一下，可以发现 out =
a+b;(a和b分别保留了后面几位)，但是通过out用&=可以很容易反解出a和b。最后按上面的思路，逆过来就ok了。

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:cpp;gutter:false;}
uint8_t a = (in[i]&31);uint8_t b = (in[i]&224);uint8_t c =(b^(seed>>15))>>5;c &= 7;uint8_t d = ((a<<3)^seed);d-=(d&7);out[i] = c+d;seed  =  (seed  *  129491  ^  seed  ^  out[i]); 
```

</p>
<p>

</div>

</p>

　　题目，就是各种移位，但是GBK格式这个问题，纠结了我很长时间，悲嘞个剧。

</p>

</p>
<p>

</div>

</p>

