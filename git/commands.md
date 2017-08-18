1. Git工作流指南：Gitflow工作流 http://blog.jobbole.com/76867/
2. Changing history, or How to Git pretty http://justinhileman.info/article/changing-history/  http://justinhileman.info/article/git-pretty/ 
3. https://www.atlassian.com/git/tutorials/git-merge
4. https://www.atlassian.com/git/tutorials/undoing-changes
5. https://www.atlassian.com/git/tutorials/saving-changes
6. https://wildlyinaccurate.com/a-hackers-guide-to-git/


### get all files from master
```shell
git fetch origin master
git reset --hard FETCH_HEAD
```


```sh
$ git clone git@github.com:user/project_name.git
$ cd project_name
$ git config user.name "yourname"
$ git config user.email "your email"
$ git pull origin <branch-name>

$ git init
Initialized empty Git repository in /home/demo/simple-repository/.git/
$ ls -l .git
$ echo 'This is the readme.' > README
$ git add README
$ git commit -m "First commit"

$ git show --format=raw flag   # flag is something like d409ca7 
$ git status
On branch master
nothing to commit, working directory clean
git status has told us that we are on branch master. As we will learn in a later section, branches
are just references. We can see this by looking in .git/refs/heads.

$ ls -l .git/refs/heads/
total 4
-rw-rw-r-- 1 demo demo 41 May 24 20:02 master
We can easily see which commit master points to by reading the file.
$ cat .git/refs/heads/master
d409ca76bc919d9ca797f39ae724b7c65700fd27
$ git show --oneline master
d409ca7 First commit
$ git rev-parse master
d409ca76bc919d9ca797f39ae724b7c65700fd27
$ cat .git/HEAD
ref: refs/heads/master


$ git commit -am "Fix issue #1: change helo to hello"
$ git push


$ git remote add upstream https://github.com/user/project_name
$ git fetch upstream
$ git checkout master
$ git rebase upstream/master
$ git push -f origin master



$ git branch test-branch
$ cat .git/refs/heads/test-branch
d409ca76bc919d9ca797f39ae724b7c65700fd27


$ cat .git/HEAD
ref: refs/heads/master
$ git checkout test-branch
Switched to branch 'test-branch'
$ cat .git/HEAD
ref: refs/heads/test-branch


$ echo 'Some more information here.' >> README
$ git add README
$ git commit -m "Update README in a new branch"
[test-branch 7604067] Update README in a new branch
1 file changed, 1 insertion(+)
$ cat .git/refs/heads/test-branch
76040677d717fd090e327681064ac6af9f0083fb


$ git tag 1.0-lightweight
$ cat .git/refs/tags/1.0-lightweight
d409ca76bc919d9ca797f39ae724b7c65700fd27

We can verify this by using git cat-file to inspect the tag.
$ git cat-file -p 1.0-lightweight

First commit
$ git cat-file -p d409ca7


$ git tag -a -m "Tagged 1.0" 1.0
$ cat .git/refs/tags/1.0

$ git cat-file -p 1.0
Tagged 1.0

tag objects also store a tag message and information about the tagger.

$ git checkout master
$ git merge hotfix



```


```
$ git checkout -b <new-branch>
$ git add --all
$ git commit -m "start a merge"
$ git push -u origin <branch-name>
```

```
git pull origin develop
git checkout develop
git merge some-feature
git push
git branch -d some-feature
```




List all of the branches in your repository.
```sh
git branch
```


Create a new branch called <branch>. This does not check out the new branch. The repository history remains unchanged. All you get is a new pointer to the current commit. To start adding commits to it, you need to select it with git checkout, and then use the standard git add and git commit commands.
```sh
git branch <branch>
```


Delete the specified branch. This is a “safe” operation in that Git prevents you from deleting the branch if it has unmerged changes.
```sh
git branch -d <branch>
```


Force delete the specified branch, even if it has unmerged changes. This is the command to use if you want to permanently throw away all of the commits associated with a particular line of development.
```sh
git branch -D <branch>
```


Rename the current branch to <branch>
```sh
git branch -m <branch>
```


Check out the specified branch, which should have already been created with git branch. This makes <existing-branch> the current branch, and updates the working directory to match.
```sh
git checkout <existing-branch>
```


Create and check out <new-branch>. The -b option is a convenience flag that tells Git to run git branch <new-branch> before running git checkout <new-branch>. git checkout -b <new-branch> <existing-branch>
```sh
git checkout -b <new-branch>
```


```sh
git branch new-feature
git checkout new-feature

git add <file>
git commit -m "Started work on a new feature"
```


Merge the specified branch into the current branch. Git will determine the merge algorithm automatically.
```sh
git merge <branch>
```


Merge the specified branch into the current branch, but always generate a merge commit (even if it was a fast-forward merge). This is useful for documenting all merges that occur in your repository.
```sh
git merge --no-ff <branch>
```


