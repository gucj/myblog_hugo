+++
date = "2016-06-15T18:46:48+08:00"
draft = false
title = "git学习笔记"
categories = [
    "linux和shell",
]
tags = [
    "linux和shell",
]

+++
[TOC]
##git学习笔记
### git init ：初始化一个git仓库
即把某个目录创建为git仓库，目录下会多一个.git 文件
### git add ：添加文件到仓库

* git add .    添加当前目录的所有内容
* git add file   添加某个具体的文件

### git rm ：从仓库删除文件
可以添加 -f 强制删除已经改动的文件
### git checkout -- file ：撤销工作区对某个文件的修改
### git commit -m "commitMessage"：将改动提交到仓库，备注提交说明

**备注:**

在git commit前，可以进行多次git add,最终会把多次添加的所有文件都提交到仓库
### git status ： 查看仓库当前状态
展示增加了哪些,删除了哪些,哪些文件修改了，但是还没有提交等信息
### git diff 某个文件 ：查看文件具体改动
距离上次add时做的改动
git diff HEAD -- 具体某文件
查看工作区（即当前操作电脑目录里）和版本库里最新版本的区别
### git log ：查看提交日志
从最近开始倒序排列
#### git log --pretty=oneline:让每条提交记录显示在一行
#### git log --graph :可以看到分支合并图

HEAD 代表当前版本

HEAD^ 代表上一个版本

HEAD^^ 代表上上个版本

HEAD~100 代表往前第100个版本
### git reset --hard commitId ：回退到某个版本
#### git reset --hard HEAD^：回退到上一个提交的版本： 
回退到其他历史提交的版本,把HEAD^ 替换为：

* 具体某个历史提交版本的commitId,可以只写commitId前几位（eg:7位），git 会自动匹配
* 也可以是HEAD~NUM,eg:HEAD~100(往前第100个版本)

#### git reset HEAD file ：撤销缓存区的修改，重新放回工作区


### git reflog ： 展示所有提交的记录

### 暂存区的概念
不同于SVN,git有暂存区的概念

具体细节

**1 当git add 后,先把修改的文件添加到暂存区**

**2 当git commit 后，把暂存区的所有内容提交到当前分支**
### git remote add origin git@server-name:path/repo-name.git ：本地仓库关联远程仓库
### git push branchName：把本地某分支push 到远程仓库
**把本地master分支push 到远程仓库：  git push -u origin master**

把本地的master分支推送到远程的master分支，并和远程的master分支关联起来

**以后就可以直接使用git push origin master**
### git clone 远程仓库地址 ：克隆远程仓库到本地
### git branch ：查看分支，展示当前是哪个分支
执行结果如下所示，展示所有的分支，* 标明当前的分支

	→ git branch
  	dev
	* master

### git branch branchName 创建分支
### git checkout branchName 切换到某个分支
### git checkout -b branchName 创建并切换到某个分支
#### git checkout -b branchName origin/branchName：在本地创建和远程某分支对应的分支
备注：本地和远程分支的名称最好保持一致
### git merge --no-ff -m commitMessage branchName :合并某分支到当前分支，并备注commit信息
#### git merge branchName 快速合并某分支到当前分支
**说明：**

git merge branchName:Fast forword 模式合并，此次合并，没有说明信息

git merge --no-ff -m commitMessage branchName : no-ff 模式，把此次合并当做一次
commit，需要备注此次合并的说明信息，在master上可以看到此次合并的log信息

####git merge --no-ff -m "merge with no-ff" dev
### git branch -d name 删除某分支
#### git branch -D name:在分支还没有被合并时，强制删除分支
### git stash：把工作现场储藏起来，等以后恢复
对于被git管理的文件，在当前工作空间做了修改，但是未add 未commit，在当前工作空间修改后，git stash 后，储藏这些修改，git status 会隐藏这些修改（对于未被git 管理的文件不适用）
#### git stash list ：展示所有stash的记录
	git stash list
	stash@{0}: WIP on dev: 34b4cce branch dev
#### git stash apply stash@{Num}：恢复某个stash，but不删除某个stash
#### git stash drop stash@{Num}：删除某个stash
#### git stash pop stash@{Num}：恢复某个stash并删除stash
### git remote：查看远程仓库的信息
远程仓库的默认名称是origin
#### git remote -v ：显示远程仓库更详细的信息
### git branch --set-upstream 本地branchName origin/branchName：指定本地dev分支与远程分支的链接

git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建
### git tag tagName(eg:V1.0):打标签
默认打标签是在最新提交的commit上
#### git tag tagName commitId:给某次提交打标签
#### git tag -a tagName -m "tagMessage":创建带有说明信息的标签
-a 指定标签名，-m 指定说明文字
#### git tag -s tagName -m "tagMessage":创建使用PGP签名的标签
签名采用PGP签名，必须首先安装gpg，如果没有找到gpg，或者没有gpg秘钥对，会报错
#### git tag ：查看所有tag
#### git show tagName:查看某标签的信息
#### git tag -d tagName:删除本地某标签
#### git push origin :refs/tags/tagName :删除推送到远程库的标签
#### git push origin tagName：推送某个标签到远程
#### git push origin --tags：推送所有本地尚未推送到远程的标签到远程仓库
### 忽略特殊文件
#### 定义自己的.gitignore，忽略某些文件
对于特殊文件，eg:数据库密码，邮箱密码等文件，不想git status 显示 Untracked files 时

可以在git 工作区的根目录创建 .gitignore文件，把要忽略的文件名填进去，git 会自动忽略这些文件

**备注：**

.gitignore 文件也需要提交到git
#### git add -f fileName:强制添加被忽略的文件
#### git check-ignore -v fileName：查看某个文件不能提交是因为哪个规则
### git命令配置别名
[git命令配置别名点击这里查看](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375234012342f90be1fc4d81446c967bbdc19e7c03d3000)















    





