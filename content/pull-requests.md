Title: Care and keeping of pull requests
Date: 2015-02-29 7:00
Category: computing
Tags: git, github, collaboration, version control, pull requests
Slug: pull-requests
Authors: Christina Koch

This is more of a reference to myself than anything else.  I know the basic steps of 
creating a pull request (clone, branch locally, commit changes, push branch to fork, submit PR), but what happens next?  

In what follows, `origin` is the central repository, `master` is the main branch of 
development, `my-fork` is your fork of the central repository and `my-patch` is the branch where you made your changes.  

##Updating a pull request with more changes

If the PR is recent and won't generate any conflicts, this is super easy.  Go back to your local copy (or if on a different computer, clone your fork).  Make sure you're in the correct branch and make/commit changes.  Push the branch to your fork and the PR on the main reposititory will automatically update.  Ta-da!  In code: 

~~~
git checkout my-patch
~~~
Make changes, then: 
~~~
git commit -m "making changes based on suggestions"
git push my-fork my-patch
~~~

##Conflicted PRs, submitter version

You've submitted your PR, but due to various circumstances, your PR can't be automatically merged and you need to make some changes.  In general, the workflow should be: 

### Update primary branch

Update your local copy of the primary branch of the central repository - the easiest thing should be to checkout that branch and pull.  

~~~
git checkout master
git pull origin master
~~~

###Integrate your changes

Integrate your changes with the updated copy.  This can take various forms. 
 
	* Rebase your old branch onto the tip of the main branch.  Get yourself onto your 
	branch, with your changes.  Then use this command: 
	~~~
	git rebase master
	~~~
	(Optional: squash all your changes into one commit before rebasing)
	
	https://github.com/edx/edx-platform/wiki/How-to-Rebase-a-Pull-Request
	http://git-scm.com/docs/git-rebase
	http://git-scm.com/book/en/v2/Git-Branching-Rebasing	http://stackoverflow.com/questions/7947322/preferred-github-workflow-for-updating-a-pull-request-after-code-review
	
	* Merge the tip of the main branch into your patch branch.  
	~~~
	git checkout my-patch
	git merge master
	~~~
	
	* Make a new branch from the tip of the main branch and `cherry-pick` the changes
	from your old branch to the new one.  To do this, you need to know all the commits
	with changes you want to include, say `007`, `008` and `009`
	~~~
	git checkout master
	git checkout -b new-patch
	git cherry-pick 007 008 009
	~~~
	See (http://think-like-a-git.net/sections/rebase-from-the-ground-up/cherry-picking-explained.html) for more info.  
	(Optional: squash all your changes into one commit before rebasing)
	
###Update the PR

	* If you've created a new branch (or done significant monkeying around with the 
	commit history), just submit a new PR.  
	~~~
	git push my-fork new-patch
	~~~
	* If you have the same branch name and you know that no one else is doing work 
	based on your previous commits, force push your updated branch to your fork.  
	~~~
	git push -f my-fork my-branch
	~~~
	The PR will automatically update.  

##"Conflicted" PRs, merger version

Essentially the same scenario as above, but instead of being the person who submitted the 
PR, you're the person who would like to merge it in.  Your options are: 

* Pull down their fork, merge changes, push directly

* Patch their patch

##Creating a pull request on someone else's pull request



##Squashing commits

Bonus points!  This is usually too fussy for me, but can be really useful if you made a 
lot of little commits.  Squashing many commits into one means that if you cherry-pick or rebase, there will only be one commit to incorporate into the master branch instead of a string of small commits.  

