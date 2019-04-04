# Version Control - Github | Gitlab 
1 . Commands
2.  Resources

*****

# Git Commit 
ou commit only the changed files by:

```
git commit [some files]
```

Or if you are sure that you have a clean staging area you can

```
git add [some files]       # add [some files] to staging area
git add [some more files]  # add [some more files] to staging area
git commit                 # commit [some files] and [some more files]
```

If you want to make that commit available on both branches you do

```
git stash                     # remove all changes from HEAD and save them somewhere else
git checkout <other-project>  # change branches
git cherry-pick <commit-id>   # pick a commit from ANY branch and apply it to the current
git checkout <first-project>  # change to the other branch
git stash pop                 # restore all changes again
```
*****
#### Perfect way to git when doing project with your team.
When you have made some changes and and your friend has already pushed it and want you  to pull it.
so, if you pull it git will display first commit your changes or merge the files,that will cause merge conflict.
You can overcome this by:

Stash your local changes:

```
git stash
```

Update the branch to the latest code

```
git pull origin dev
```

see your commits from stash 
```
git stash show
```

Merge your local changes into the latest code:

```
git stash apply
```

Add, commit and push your changes

```
git add <files>
git commit -m "message"
git push origin dev

```



*****
### You could follow these steps to revert the incorrect commit(s) or to reset your remote branch back to correct HEAD/state.

1. checkout the remote branch to local repo.

 ``` git checkout development_branch
 ```
copy the commit hash (i.e. id of the commit immediately before the wrong commit) from git log git log -n5

output:
```
        commit 7cd42475d6f95f5896b6f02e902efab0b70e8038 "Merge branch 'wrong-commit' into 'development'"
        commit f9a734f8f44b0b37ccea769b9a2fd774c0f0c012 "this is a wrong commit"
        commit 3779ab50e72908da92d2cfcd72256d7a09f446ba "this is the correct commit"
```
2. reset the branch to the commit hash copied in the previous step

   ``` git reset <commit-hash> (i.e. 3779ab50e72908da92d2cfcd72256d7a09f446ba)```
3. run the this command   to show all the changes that were part of the wrong commit.

   ```git status ```
4. then simply run this to revert all those changes.

```git reset --hard ``` 
5. force-push your local branch to remote and notice that your commit history is clean as it was before it got polluted.

 ```git push -f origin development```




#### Remove files from the tree
[Scenarion 1](): make a commit and notice a stray directory or file that shouldn’t be in the repo. First, add the file to .gitignore, and then:

```
$ git rm --cached <file-name>
# Globbing is possible as usual
$ git rm --cached *.log
```

If a directory, use the -r flag:

```
$ git rm -r --cached directory/
```
******
#### Remove files from the staging area

[Scenario 2:]() if unwanted files were added to the staging area, but not yet committed, then a simple reset will do the job:

```
$ git reset HEAD file
# Or everything
$ git reset HEAD .
```

#### Nuke all made changes for good

Scenario 3: changes in the repo are wanted to be decimated from all eternity:

```
$ git reset --hard
```

Careful now, that will remove staged and unstaged changes.

To only remove unstaged changes in the current working directory, use:



#### Rebase master to feature-branch

```
$ git checkout master
# Pull in the new stuff
$ git pull origin master
````

# Checkout your feature and rebase master to it

```
$ git checkout some-feature-branch
$ git rebase master
```

Next, Git will try to move the new commits in master to the tip of your some-feature-branch. Here’s what might happen:

    Hopefully not, but most likely yes, Git will whine about merge conflicts.
    Solve the conflicts by opening the files that have conflict, remove the inserted markers, and make it look like you want it to be.
    $ git add <file-name> or in one clump $ git add -A.
    $ git rebase --continue.
    Rinse and repeat until Git stops whining.

Dealing with merge conflicts in dist files

You might have CSS or JavaScript files in the dist/ directory (or build, or whatever you named it) that are generated automatically by a build task, like Sass or r.js. You can exclude the whole dist dir from the repo, but if you’re like me, and use Git to deploy the project also, that’s not doable.

I haven’t really found a good solution to this, other than just ignoring them by blindly adding all files in dist and continue with the rebase. Then, of course, run the build script after the rebase is done.

    $ git add dist/
    $ git rebase --continue

Now there’s tons of merge conflicts in your dist/*.css and dist/*.js files and that’s why you need to run your build task again.

We’re done with the rebasing, great! Lets look at merging the feature branch to master.
Merge feature branch to master

This should be a cakewalk now, since we just resolved all the merge conflicts, all you need to do is:

$ git checkout master
$ git rebase some-feature-branch






# Branching

Creating a branch

You can create branches on Git and Mercurial repositories. Git branches always have a name, but Mercurial has the concept of a branch and a named branch. For more information, Steve Losh's guide is a good resource explaining branching in the two systems.
Create a Git branch

There are three ways to create a Git branch: In Bitbucket, at your local command line, or in Jira Software.
To create a branch from Bitbucket

    From the repository, click + in the global sidebar and select Create a branch under Get to work.
    From the popup that appears, select a Type (if using the Branching model), enter a Branch name and click Create.

    After you create a branch, you need to check it out from your local system. Use the fetch and checkout commands that Bitbucket provides, similar to the following:
    $ git fetch && git checkout <feature>

    Make your changes locally and then add, commit, and push your changes to the <feature> branch:
    $ git add .
    $ git commit -m "adding a change from the feature branch"
    $ git push origin <feature>

    Click the Source page of your repository. You should see both the master and the <feature> branch in the branches dropdown. When you make commits to the feature branch, you'll see the files specific to that branch.

To create a branch locally

You can create a branch locally as long as you have a cloned version of the repo.

    From your terminal window, list the branches on your repository.
    $ git branch

    * master

    This output indicates there is a single branch, the master and the asterisk indicates it is currently active.

    Create a new feature branch in the repository
    $ git branch <feature_branch>

    Switch to the feature branch to work on it.
    $ git checkout <feature_branch>

    You can list the branches again with the git branch command.

    Commit the change to the feature branch:
    $ git add .
    $ git commit -m "adding a change from the feature branch"

    Switch back to the master branch.
    $ git checkout master

    Push the feature branch to Bitbucket:
    $ git push origin <feature_branch>

    View the Source page of your repository in Bitbucket. You should see both the master and the feature branch. When you select the feature branch, you see the Source page from that perspective. Select the feature branch to view its Recent commits.


