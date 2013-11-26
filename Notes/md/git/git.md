#git useful commands
##Create remote repo
<pre>
pwd:/Users/zhanglx/workspace/gittest/
git init --bare
</pre>

##Clone repo from remote repo
<pre>
git clone /Users/zhanglx/workspace/gittest/
</pre>

##Init a local git repo and add a remote
This is equal to "Clone"
<pre>
mkdir myrepo
cd myrepo/
git init
git remote add origin /Users/zhanglx/workspace/gittest/
</pre>

##New branch and switch to this branch

<pre>
git branch test
git checkout test
</pre>
Type <code>git branch</code> to check which branch you are working on.

##Add, modify, commit, reset and checkout history

###Git文件状态
Git文件的状态分为untracked和tracked, untracked文件是指新建的文件，尚未被git管理起来。

tracked又分为三种状态:

已提交（committed），已修改（modified）和已暂存（staged）。已提交表示文件已被安全地保存在本地数据库中了；已修改表示修改了某个文件，但没有提交保存；已暂存表示把已修改的文件放在下次提交时要保存的清单中。

###Github

<code>git remote show origin</code> 查看相关信息
<code>git push origin master</code> 将commit的代码，push到github上。
<code>git pull origin master</code> 将github上的代码，update到本地。

###Delete
<code>git delete file</code> 然后commit的，将无法恢复。
<code>rm file</code>, 可以通过<code>git checkout -- file</code>进行恢复。
<code>git rm --cached file</code>，只是在缓存中删除，

恢复更改的文件
git checkout — //未git add的文件

git reset HEAD //已经git add的文件，可以用这个取消add，然后用上一条命令恢复

###Push master branch of locale repo to remote origin

<code>git push origin master</code>

###Pull (if there are some conflicts, git will call git merge automatically)
<code>git pull origin master</code>




