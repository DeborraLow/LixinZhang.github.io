Title: 基于pexpect实现的远程多主机多脚本执行
Date: 2012-07-14 10:26
Author: 糖拌咸鱼
Slug: ji-yu-pexpectshi-xian-de-yuan-cheng-duo-zhu-ji-duo-jiao-ben-zhi-xing

**<span style="font-size: 14pt;">什么是Pexpect?</span>**

</p>

      Pexpect 是一个用来启动子程序并对其进行自动控制的 Python 模块。
Pexpect 可以用来和像 ssh、ftp、passwd、telnet
等命令行程序进行自动交互。  
      关于pexpect的具体介绍可以参考以下几条链接：  
1、Pexpect 官网  
http://www.noah.org/wiki/pexpect  
2、探索 Pexpect，第 1 部分：剖析 Pexpect  
http://www.ibm.com/developerworks/cn/linux/l-cn-pexpect1/

</p>

3、探索 Pexpect，第 2 部分：Pexpect 的实例分析  
<http://www.ibm.com/developerworks/cn/linux/l-cn-pexpect2/>

</p>

**<span style="font-size: 14pt;">需求分析</span>**

</p>

   
 最近在“创新工场-行云”下的“云计算”组实习，主要使用的开发语言是python。目前遇到一个功能需求，就是客户端需要对远程的多台主机进行多脚本执行。具体来讲，就是需要将一台主机上的多个脚本文件分发拷贝到远程的多台主机上，然后在远程主机上按序执行这一系列脚本，并能够获取这些脚本的执行结果。在对远程主机进行操作时，会存在密码授权等交互问题，而利用pexpect模块可以方便的进行命令行程序的自动交互。

</p>

1、如何将脚本文件拷贝到远程主机上；  
   
 本文使用scp命令，进行脚本文件的远程拷贝，因为scp是成熟的命令，可以确保文件的完整性与安全性。

</p>

2、如何触发远程主机上脚本的执行；  
   
 触发脚本执行功能使用的pexpect提供的pxssh模块，该模块式是对pexpect核心模块的进一步封装，并用于实现基于ssh方式通信的交互模块。由于，脚本的执行效果与耗时都是无法预知的，客户端触发脚本执行命令后不可能一直等待这些脚本进程结束。因此，在下达执行命令后，客户端应该立即结束自身，而执行脚本应该把运行过程中产生的输出内容重定向写入到某个日志文件中，客户端获取该文件得到输出结果。

</p>

3、如何获取脚本的运行状态与执行结果。  
   
 有一些重要的问题需要考虑：客户端如何获知这些脚本的执行是否已经结束了？它们是正常结束的，还是出错挂掉的？以及当前正在运行的是哪个脚本文件？
因此，我们需要获取这些脚本执行进程的状态。在linux上，一般用ps命令进行进程状态的查看，使用grep可以进行内容的筛选。在这里，我们利用某种标识串对每个脚本进行标识，这样使用“ps
-aux | grep
标识串”命令就可以查看该执行脚本的进程状态了。为了判断脚本文件执行是否是正常退出的，我们在按序执行这些脚本后在日志文件结尾插入一个标识串。如果日志文件中，存有该标志串则证明是正常结束的，否则可能仍在执行或是发生了某些错误。

</p>

**<span
style="font-size: 14pt;">程序源代码（水平有限，仅供参考）</span>**

</p>

看程序代码，可能会更方便理解。程序里，也使用了一些小技巧。

</p>

<div class="cnblogs_code">

</p>
<p>
      1 import pexpect  2 from LogUtil import Logging  3 import pxssh  4 import hashlib  5 import datetime  6 import time  7 import threading  8 import Queue  9  10 timeout_ = 100 11 def upload_file(file_path_list , remote_user , remote_host ,remote_path , password , remote_port = 22) : 12     ''' 13     Copy a file to remote machine. return 0 if success 14     ''' 15     logger = Logging.getLogger(log_file='upload_remotefile.log') 16     try : 17         file_path = ' '# multi files 18         for path_item in file_path_list : 19             file_path += path_item 20             file_path += ' ' 21         if not file_path or not remote_user or not remote_host or not remote_path : 22             logger.error('Empty parameter given') 23             raise Excpetion , 'Empty parameter given' 24         cmd_text = 'scp -P %d %s %s@%s:%s' % \ 25             (remote_port , file_path, remote_user, remote_host, remote_path) 26         print cmd_text 27         logger.info(cmd_text) 28         global timeout_ 29         cmd = pexpect.spawn(cmd_text,timeout=timeout_) 30         expect_res = cmd.expect(['(yes/no)','password',pexpect.EOF,pexpect.TIMEOUT]) 31         if expect_res == 0 : 32             logger.info('pexpect expects (yes/no)') 33             cmd.sendline('yes') 34             cmd.expect('password') 35             cmd.sendline(password) 36         elif expect_res == 1 : 37             logger.info('pexpect expects (password)') 38             cmd.sendline(password) 39         elif expect_res == 2 : 40             logger.info('pexpect expects (EOF)') 41         else: 42             logger.info('pexpect expects (TIMEOUT)') 43             raise Exception , 'TIMEOUT' 44         expect_res = cmd.expect(['Permission denied',pexpect.EOF]) 45         if expect_res == 0 : 46             logger.info('Permission denied') 47             cmd.close() 48             cmd.kill(0) 49         else : 50             cmd.close() 51         return cmd.exitstatus 52     except Exception ,e : 53         cmd.close() 54         logger.error(e) 55         return 1 56  57 def do_remotecommand(file_path_list, server_array) : 58     ''' 59     copy a script file list to server_array and execute the script files at remote machines 60     Each file has a unique key_code. 61     The standard output and standard error output of all files are written to a log file named 'log_code.log' 62     return a Queue object which contains [exitstatus, key_code_list, log_code, machine] 63     '''    64     ''' 65     if not file_path_list or type(file_path_list) is not list \ 66             or not server_array or type(server_array) is not list : 67                 return None 68     ''' 69     file_list = [] 70     key_code_list = [] 71     log_code = hashlib.md5(str(datetime.datetime.now())).hexdigest() 72     log_code = log_code[len(log_code)/2:] 73     log_name = log_code + '.log' 74  75     for file_path in file_path_list : 76         if file_path.rfind('/') != 0: 77             file_name = file_path[file_path.rfind('/')+1:] 78         else :  79             file_name = file_path 80         file_code = hashlib.md5(str(datetime.datetime.now())).hexdigest() 81         file_code = file_code[len(file_code)/2:] 82         newfile_name = log_code + file_code + file_name 83         file_list.append((file_name , newfile_name)) 84         key_code_list.append(log_code + file_code) 85     print key_code_list 86     result = Queue.Queue() 87     def work(machine): 88         upload_res =  upload_file(file_path_list,machine['remote_user'], machine['remote_host'], machine['remote_path'],\ 89                 machine['password'], machine.get('remote_port',22)) 90         print upload_res 91         if upload_res == 0 : 92             try: 93                 s = pxssh.pxssh() 94                 is_login = s.login(machine['remote_host'], machine['remote_user'], machine['password']) 95                 if is_login == False : 96                     raise Exception , 'Permission denied' 97                 if machine['remote_path'].endswith('/') == False: 98                     machine['remote_path'] += '/' 99                 s.sendline('cd '+ machine['remote_path'])100                 s.prompt()101                 for file_name , newfile_name in file_list :102                     s.sendline('mv '+ file_name  + ' ' + newfile_name)103                     s.prompt()104                     s.sendline('chmod u+x ' + newfile_name)105                     s.prompt()106                 s.sendline('cd ~')107                 s.prompt()108                 cmd_text = ''109                 for file_name , newfile_name in file_list :110                     newfile_name_ = machine['remote_path'] + newfile_name111                     log_name_ = machine['remote_path'] + log_name112                     cmd_text += newfile_name_ + ' >> ' + log_name_ + ' 2>&1 && '113                 cmd_text += 'echo ' + log_code + '#' +' >> ' + log_name_ + ' &'114                 s.sendline(cmd_text)115                 s.prompt()116                 s.logout()117                 result.put([s.exitstatus,key_code_list,log_code,machine])#success118             except Exception, e: 119                 print e120                 result.put([-1,[],'',machine])#fail121     work_threads = []122     for machine in server_array :123         work_thread = threading.Thread(target = work , args = (machine,))124         work_threads.append(work_thread)125         work_thread.start()126     '''just wait until all work_threads finish'''127     for t in work_threads :128         t.join()129     return result130 131 def do_multi_query(key_code_list , server_array) : 132     '''133     Query for running status of script files.134     return a Queue object which contains [PID,executing_id,exitstatus,content,machine]135     PID : process number of a still running script file136     exectuing_id : which file is running137     exitstatus : ssh exit status , 0 if success138     content : the last 10 lines of the log file 139     machine : for which machine140     '''141     print key_code_list142     log_code = key_code_list[0][:len(key_code_list[0])/2]143     result = Queue.Queue()144     def do_query(key_code_list,machine) :145         try:146             s = pxssh.pxssh()147             is_login = s.login(machine['remote_host'], machine['remote_user'], machine['password'])148             if is_login == False:149                 raise Exception , 'Permission denied'150             s.sendline('ps -aux | grep --color=never ' + log_code)151             s.prompt()152             words = s.before.split()153             index = 0154             PID = -1155             executing_id = 0156             FIND = False157             if machine['remote_path'].endswith('/') == False :158                 machine['remote_path'] += '/'159             for item in words :160                 if item.find(machine['remote_path'] + log_code) >= 0 :161                     PID = int(words[index-10])162                     for code in key_code_list :163                         if item.find(code) >= 0 :164                             FIND = True165                             break166                         executing_id += 1167                     break168                 index+=1169             if FIND == False :170                 executing_id = -1171             s.sendline('cd ' + machine['remote_path'])172             s.prompt()173             s.sendline('tail -10 ' + log_code + '.log')174             s.prompt()175             content = s.before176             end_index = content.find(log_code+'#')177             exitstatus = -1178             if end_index >= 0 :179                 exitstatus = 0180             content = content[content.find('\r\n')+2:end_index]181             result.put([PID , executing_id , exitstatus , content , machine])182         except Exception , e :183             print e184             result.put([-1,-1,-1,'',machine])185     work_threads = [] 186     for machine in server_array :187         work_thread = threading.Thread(target = do_query ,args = (key_code_list,machine,))188         work_threads.append(work_thread)189         work_thread.start()190     for t in work_threads :191         t.join()192     return result193 194 if __name__ == '__main__':195     server_array = []196     file_path_list = []197     machine1 = {'remote_user':'root','remote_host':'192.168.52.131',\198             'remote_path':'/filedir/','password':'123123', 'remote_port':22} 199     machine2 = {'remote_user':'root','remote_host':'192.168.52.131',\200             'remote_path':'/filedir2/','password':'123123'}201     server_array.append(machine1)202     server_array.append(machine2)203     file_path_list.append('/home/zhanglixin/pyworkspace/a.py')204     file_path_list.append('/home/zhanglixin/pyworkspace/b.py')205     file_path_list.append('/home/zhanglixin/pyworkspace/c.py')206     file_path_list.append('/home/zhanglixin/pyworkspace/d.py')207     command_result = do_remotecommand(file_path_list,server_array)208     success_array = []209     key_code_list = []210     while command_result.empty() == False :211         res = command_result.get()212         print res213         do_res = res[0]214         key_code_list = res[1]215         log_code = res[2]216         machine = res[3]217         if do_res == 0 :218             success_array.append(machine)219     while 1:         220         query_result = do_multi_query(key_code_list ,success_array)221         while query_result.empty() == False :222             PID , executing_id , exitstatus , content ,machine = query_result.get()223             print '#'*10 , machine['remote_host'] , '#'*10224             if PID > 0 :225                 print 'Remote process is alive ! , PID : ' , PID 226                 print 'script file ' + file_path_list[executing_id] + ' is running!'227             else :228                 print 'Remote process is dead !'229             if exitstatus == 0 :230                 print 'Done!'231             else :232                 if PID < 0 :233                     print 'Something wrong happened!'234             print content

</p>
<p>

</div>

</p>

 

</p>

