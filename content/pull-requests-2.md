Status: draft
Title: Care and keeping of pull requests, part 2
Date: 2015-02-29 7:00
Category: computing
Tags: git, github, collaboration, version control, pull requests
Slug: pull-requests-2
Authors: Christina Koch

> In what follows, `origin` is the central repository, `master` is the main branch of 
> development, `my-fork` is your fork of the central repository and `my-patch` is the
> branch where you made your changes.  

##Updating someone else's pull request

A useful preliminary skill for updating someone else's pull request is being able to "download" and edit the branch that they submitted as a pull request.  

~~~
git remote add user <address of repository>
git fetch user
~~~

The fetch command will pull down all the commits from the other user's repository (including all their branches) and store them in your repository, but not in a visible way.  To see all these fetched branches, use: 

~~~
git branch -a
~~~

Aha!  You should see a list of normally visible (that is, local) branches and then a list of invisible branches (branches that haven't been checked out locally yet).  We want to check out `user/user-branch` in our local repository.  That's actually pretty easy.  Using the `git checkout` command with the `-b` flag (which creates a new branch), the syntax:

~~~
git checkout -b branch-name user/user-branch
~~~

Will create a new local branch (`branch-name`), that matches `user`'s branch `user-branch`, and then switch to `branch-name`.  

### Merging pull requests locally.  

This strategy is best if you have push rights to the central repository and can simply merge the changes without submitting another PR.  

Fetch the user's branch as described above.  Then, making sure you're on the locally checked out branch, make any changes you like and commit them.  Then, switching back to `master`, run a merge.  

~~~
git checkout master
git merge user-branch
~~~

If you then push `master` to the central repository: 

~~~
git push central master
~~~

The original pull request with `user`'s branch will be closed, as it has been merged locally.  


###PR to their fork

Say you don't have access to the central repository.  You can submit a pull-request on top of that user's branch on *their* repository.  Fetch the user's branch, as above and check it out.  

THEN, undergo the normal pull request process.  Create another branch

Change the base fork to the other user's repository (if it isn't already) and the base branch to the original PR branch.  Then submit a PR as usual.  