Title: 一道网络安全作业题
Date: 2012-12-09 09:45
Author: 糖拌咸鱼
Slug: dao-wang-luo-an-quan-zuo-ye-ti

**PS：这是网络安全的作业题目，要是也有选这课同学看到这篇文章，希望不要直接copy，要不然老师发现会比较不爽哈\~![微笑][]**

</p>

 

</p>

#### <span style="font-weight: bold; font-size: x-large;">题目</span>

</p>

请设计和实现一个算法，把一个文件M由A传输到B，并保证：

</p>

– 文件M的完整性

</p>

– B能够认证M的发送方

</p>

– 文件M的完整性、机密性

</p>

#### <a name="OLE_LINK8"></a><a name="OLE_LINK7"></a><span style="font-weight: bold; color: #333333; font-size: x-large;">算法设计思路</span>

</p>

信息完整性和抗否认性是信息安全保证的两个基本要素，数字签名技术通过对消息摘要技术和公开密钥技术的有机结合，实现了对在不可靠网络中传输的信息的完整性和抗否认性的有效保证。

</p>

使用数字签名的方式，实现对文件M完整性和认证的保证。

</p>

数字签名的大致过程如下：消息发送方首先利用Hash函数对待发消息进行摘要处理，生成一个固定长度的消息摘要H(M)，然后用自己的私钥对该散列值进行加密，形成发送方的一个数字签名，这个数字签名作为消息的附件随消息一起被发送到消息的接受方。接受方利用数字签名中的消息摘要能对消息的完整性进行判断，用发送方的公钥对签名解密则能对发送方进行身份认证和保证抗否认性。

</p>

我们使用MD5函数作为上述方法的Hash函数，使用RSA算法作为非对称加密算法。具体实现流程如下：

</p>

<a name="OLE_LINK6"></a><a name="OLE_LINK5"></a>发送端A的操作流程：

</p>

[![1][]][]

</p>

接收端B的操作流程：

</p>

[![2][]][]

</p>

由上面两图可以清楚知道该算法的工作流程。通过对文件M进行数字签名可以保证文件M传输后的完整性和抗否认性。对文件M使用B的public
key进行加密，使得只有B能够通过自己的private
key进行解密，保证了文件M的机密性。

</p>

#### 文件清单

</p>

[![clip\_image005[4]][]][]

</p>

#### <span style="font-size: x-large;"><span style="font-weight: bold;">运行方法及相关说明:</span></span>

</p>

1、
程序采用c++语言编写，文件清单里的main.cpp是主控程序，其他文件问逻辑处理函数或是工具类。

</p>

**2、文件PrimeGenerator用于生成public key与 private key。**

</p>

3、
程序基于文件驱动运行，即将各种文件作为参数作为程序的入口。在程序的根目录下必须保证收发端的public
key 以及private key，以及待发送处理的文件M。命名规则如下图所示：

</p>

[![clip\_image007[4]][]][]

</p>

4、
运行DigitalSignature.exe可执行程序，运行终端显示如下（下图显示了整个工作流程信息，模拟了send和Receive的过程）：

</p>

[![clip\_image009[4]][]][]

</p>

5、 文件输出为

</p>

[![clip\_image011[4]][]][]

</p>

DigitalSignature.txt
表示发送端生成的数字签名，cypherFile.txt表示使用接受端的publickey
B\_public.key加密message.txt后的密文文件。Newmessage文件表示的是接受端B时候自己的private
key解密后的文件。

</p>

**<span style="font-size: large;">6、 一个具体事例的演示：</span>**

</p>

​a) message.txt文件内容

</p>

[![clip\_image013[4]][]][]

</p>

​b) 发送端使用MD5生成message.txt文件的指纹为

</p>

[![clip\_image014[4]][]][]

</p>

​c) 发送端使用A\_private.key加密该指纹得数字签名DigitalSignature.txt

</p>

[![clip\_image016[4]][]][]

</p>

​d) 发送端使用B\_public.key 加密文件message.txt
，并将密文保存为cypherFile.txt

</p>

[![clip\_image018[4]][]][]

</p>

​e) 发送端操作结束

</p>

​f) 接收端使用A\_publickey解密DigitalSignature.txt，得到解密后指纹1

</p>

[![clip\_image019[4]][]][]

</p>

​g)
接收端使用B\_privatekey解密cypherFile.txt，得到解密后的文件，并写入newmessage.txt。发现与原文件内容相同。

</p>

[![clip\_image021[4]][]][]

</p>

​h) 接收端使用MD5生成文件newmessage.txt的指纹2

</p>

[![clip\_image022[4]][]][]

</p>

​i) 比较指纹1和指纹2 , 判断是否可以相同

</p>

[![clip\_image023[4]][]][]

</p>

#### <span style="font-size: x-large;">程序关键代码</span>

</p>

本实验采用了网络上开源的MD5算法以及RSA算法，并对其算法中的一些函数进行了改写与扩充。先将本实验的核心主程序代码给出，代码附有比较详细的注释信息，这里便不再赘述。

</p>

<div class="cnblogs_code"
style="background-color: #f5f5f5; border: #cccccc 1px solid; padding: 5px;">

</p>
<p>
    #include <cstdlib>    //srand()#include <iostream>    //cout#include <ctime>    //time()#include <cstring>    //strcmp()#include "test.h"    //testing functions#include "RSA.h"    //GenerateKeyPair()#include "PrimeGenerator.h"    //Generate()#include "CMd5.h"using std::cout;using std::endl;using std::cin;using namespace std;/*read a key from a key file*/Key ReadKey(const char * keyfile){    std::ifstream source(keyfile, std::ios::in | std::ios::binary);    if (!source){        cout<< "Error : Opening file \"KeyFile\" failed."<<endl;    }    string str_modulus , str_exponent;    source >> str_modulus >> str_exponent;    BigInt modulus(str_modulus);    BigInt exponent(str_exponent);    Key key(modulus , exponent);    return key;}/*read whole text from a file*/std::string GetWholeTextFromFile(const char * filename){    std::ifstream source(filename , std::ios::in | std::ios::binary);    if(!source){        cout<< "Error : Opening file \"File\" failed."<<endl;    }    source.seekg(0, std::ios::end);    const unsigned long int fileSize = source.tellg();    source.seekg(0, std::ios::beg);    char buff[10240];    source.read(buff , fileSize);    buff[fileSize] = '\0';    std::string wholetext = std::string(buff);    source.close();    return wholetext;}/*generate a fingerprint using MD5 algorithm*/std::string GenerateFingerPrintFromFile(const char * filename){    std::ifstream source(filename , std::ios::in | std::ios::binary);    if(!source){        cout<< "Error : Opening file \"File\" failed."<<endl;    }    source.seekg(0, std::ios::end);    const unsigned long int fileSize = source.tellg();    source.seekg(0, std::ios::beg);    char buff[10240];    source.read(buff , fileSize);    buff[fileSize] = '\0';    unsigned char digest[16];    //调用MD5相关函数，生成buff的MD5码，存入digest    md5_state_t md5state;    md5_init(&md5state);    md5_append(&md5state, (const unsigned char *)buff, strlen(buff));    md5_finish(&md5state, digest);    char presentation[33];    md5_presentation(digest , presentation);    presentation[32] = '\0';    std::string fingerPrint = std::string(presentation);    source.close();    return fingerPrint;}/*    Send a messageFile M to a receiver.    Pass messageFile'path , sender's private key path , receiver's public key path to the function.    This function will write M's digitalSignature to a file called 'DigitalSignature.txt';    Also write encrypted M a file called 'cypherFile.txt' using receiver's public key.*/void send(char * messageFile , char * sender_private_key , char * receiver_public_key){    char cypherFile [] = "cypherFile.txt";//output file name    char digitalSignatureFile [] = "DigitalSignature.txt";    std:string fingerPrint = GenerateFingerPrintFromFile(messageFile);    cout<<"1) File M 's fingerPrint is"<<endl<<fingerPrint<<endl;    Key B_publickey = ReadKey(receiver_public_key);    Key A_privatekey = ReadKey(sender_private_key);    std::string cypherText = RSA::Encrypt(fingerPrint, A_privatekey);    cout<<"2) FingerPrint has been encrypted using sender's private key"<<endl        <<"3) DigitalSignatureFile generated , save as a file called 'DigitalSignature.txt'"<<endl;    RSA::Encrypt(messageFile, cypherFile, B_publickey);    cout<<"4) File M has been encrypted using receiver's public key."<<endl          <<"5) Save as a file called 'cypherFile.txt'"<<endl;    std::ofstream dest(digitalSignatureFile, std::ios::out | std::ios::binary);    dest<<cypherText;    dest.flush();    dest.close();}/*    Receive a encrypted file cypherFile and a digitalSignature file From sender ,     check whether M is completed or not , decrypt from cypherFile using receiver's private key.    Pass paths of cypherFile , digitalSignatureFile ,sender_public_key ,receiver_private_key to this function.    This function will print some checking results.*/void receive(char * cypherFile , char * digitalSignatureFile , char * sender_public_key , char * receiver_private_key){    char newmessage [] = "newmessage.txt"; // output file name    Key A_publickey = ReadKey(sender_public_key);    Key B_privatekey = ReadKey(receiver_private_key);    std::string cypherText = GetWholeTextFromFile(digitalSignatureFile);    cout<<"1) DigitalSignatureFile has been decrypted using sender's public key."<<endl        <<"2) Get FingerPrint："<<endl;    std::string newFingerPrint = RSA::Decrypt(cypherText, A_publickey);    cout<<newFingerPrint<<endl;    RSA::Decrypt(cypherFile, newmessage, B_privatekey);    cout<<"3) CypherFile has been decrypted using B's private key."<<endl        <<"4) Get another printfinger:"<<endl;    std::string anotherFingerPrint = GenerateFingerPrintFromFile(newmessage);    cout<<anotherFingerPrint<<endl;    cout<<"5) Now check two printfingers"<<endl;    bool check = (newFingerPrint==anotherFingerPrint);    if (check == true)    {        cout<<"Result : File is completed!"<<endl;    }    else    {        cout<<"Result : File is not completed,Please check!"<<endl;    }}int main(int argc, char *argv[]){    char messageFile [] = "message.txt";    char sender_private_key [] = "A_private.key";    char receiver_public_key [] = "B_public.key";    char sender_public_key [] = "A_public.key";    char receiver_private_key [] = "B_private.key";    char digitalSignature [] = "DigitalSignature.txt";    char cypherFile [] = "cypherFile.txt";    cout<<"***************Read Me***************"<<endl;    cout<<"Please read this algotirhm's document first!"<<endl;    cout<<"This program uses MD5 as hash function and RSA as Asymmetric Encryption Algorithm."<<endl;    cout<<"Please check that you must have both sender and receiver's public key and private key"<<endl;    cout<<"Please check that you must have a message file to be test."<<endl;    cout<<"File structure must look like as following:"<<endl;    cout<<"message.txt,A_private.key,A_public.key,B_private.key,B_public.key"<<endl;    cout<<"*************************************"<<endl;    std::string input;    while(1)    {        cout<<"If you are sure , please input 'yes' to start this program!"<<endl;        cin >> input;        if (input != "yes")            continue;        cout<<"*****************Send****************"<<endl;        send(messageFile , sender_private_key , receiver_public_key);        cout<<"***************Receive***************"<<endl;        receive(cypherFile ,digitalSignature , sender_public_key , receiver_private_key);        break;    }    cout<<"Please press any key to exit!"<<endl;    cin >> input;    return 0;}

</p>
<p>

</div>

</p>

 

</p>

**程序源代码:**

</p>

[Source Code and Document][]

</p>

  [微笑]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744271606.png
  [1]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744285585.png
    "1"
  [![1][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744283982.png
  [2]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744299423.png
    "2"
  [![2][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744291408.png
  [clip\_image005[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744308801.png
    "clip_image005[4]"
  [![clip\_image005[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744291898.png
  [clip\_image007[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744301243.jpg
    "clip_image007[4]"
  [![clip\_image007[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744303228.jpg
  [clip\_image009[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/20121209174431620.jpg
    "clip_image009[4]"
  [![clip\_image009[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744302290.jpg
  [clip\_image011[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744314699.jpg
    "clip_image011[4]"
  [![clip\_image011[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744316684.jpg
  [clip\_image013[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744329060.jpg
    "clip_image013[4]"
  [![clip\_image013[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744329126.jpg
  [clip\_image014[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744332582.png
    "clip_image014[4]"
  [![clip\_image014[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744334010.png
  [clip\_image016[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744335896.jpg
    "clip_image016[4]"
  [![clip\_image016[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744335057.jpg
  [clip\_image018[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744347466.jpg
    "clip_image018[4]"
  [![clip\_image018[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744343911.jpg
  [clip\_image019[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744345797.png
    "clip_image019[4]"
  [![clip\_image019[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744348862.png
  [clip\_image021[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744354336.jpg
    "clip_image021[4]"
  [![clip\_image021[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744355448.jpg
  [clip\_image022[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744357891.png
    "clip_image022[4]"
  [![clip\_image022[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744355731.png
  [clip\_image023[4]]: http://images.cnblogs.com/cnblogs_com/coser/201212/20121209174435681.png
    "clip_image023[4]"
  [![clip\_image023[4]][]]: http://images.cnblogs.com/cnblogs_com/coser/201212/201212091744355698.png
  [Source Code and Document]: http://files.cnblogs.com/coser/homework2.zip
