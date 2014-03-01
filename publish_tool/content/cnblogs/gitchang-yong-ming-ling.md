Title: Git常用命令
Date: 2014-01-04 14:30
Author: 糖拌咸鱼
Slug: gitchang-yong-ming-ling

Create remote repo
------------------

</p>

<p>
    pwd:/Users/zhanglx/workspace/gittest/git init --bare

</p>

Clone repo from remote repo
---------------------------

</p>

<p>
    git clone /Users/zhanglx/workspace/gittest/

</p>

Init a local git repo and add a remote
--------------------------------------

</p>

This is equal to "Clone"

</p>

<p>
    mkdir myrepocd myrepo/git initgit remote add origin /Users/zhanglx/workspace/gittest/

</p>

New branch and switch to this branch
------------------------------------

</p>

<p>
    git branch testgit checkout test

</p>

Type `git branch` to check which branch you are working on.

</p>

Add, modify, commit, reset and checkout history
-----------------------------------------------

</p>

### Git文件状态

</p>

Git文件的状态分为untracked和tracked,
untracked文件是指新建的文件，尚未被git管理起来。

</p>

tracked又分为三种状态:

</p>

已提交（committed），已修改（modified）和已暂存（staged）。已提交表示文件已被安全地保存在本地数据库中了；已修改表示修改了某个文件，但没有提交保存；已暂存表示把已修改的文件放在下次提交时要保存的清单中。

</p>

### Github

</p>

`git remote show origin` 查看相关信息

`git push origin master` 将commit的代码，push到github上。

`git pull origin master` 将github上的代码，update到本地。

</p>

### Delete

</p>

`git delete file` 然后commit的，将无法恢复。

`rm file`, 可以通过`git checkout -- file`进行恢复。

`git rm --cached file`，只是在缓存中删除，

</p>

恢复更改的文件

git checkout — //未git add的文件

</p>

git reset HEAD //已经git
add的文件，可以用这个取消add，然后用上一条命令恢复

</p>

### Push master branch of locale repo to remote origin

</p>

`git push origin master`

</p>

### Pull (if there are some conflicts, git will call git merge automatically)

</p>

`git pull origin master`

</p>

创建SSH key
-----------

</p>

<p>
    ssh-keygen生成的SSH key文件保存在中～/.ssh/id_rsa.pub

</p>

添加SSH key到github
-------------------

</p>

<p>
    接着拷贝.ssh/id_rsa.pub文件内的所以内容打开github帐号管理中的添加SSH key界面的步骤如下：1. 登录github2. 点击右上方的Accounting settings图标3. 选择 SSH key4. 点击 Add SSH key

</p>

