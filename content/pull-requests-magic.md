Title: Care and keeping of pull requests, part iv
Date: 2015-07-02 12:00
Category: computing
Tags: git, github, collaboration, version control, pull requests, care and keeping of prs
Slug: pull-requests-magic
Authors: Christina Koch

See [first post disclaimer](http://christinalk.github.io/blog/pull-requests.html)

Scenario: You've submitted your pull requests, but due to various circumstances, 
your pull request can't be automatically merged and you need to update 
it.  (Alternatively: you are the owner of the central repository 
and are trying to merge in some very out-of-date pull requests.)  There 
are lots of ways to do this.  

> In what follows, the name of the repository is `mario-kart`.  
> In our local repository, we have used `origin` to refer to the central repository, 
> and `master` is the main branch of 
> development.  Our fork (and github username) is `peach` and our branch that 
> we submitted for the PR is called `banana-peels`.  

## WAIT!  First update the primary branch

The first step when rehashing an old pull request (so, dealing with an out-of-date 
branch) is to get the freshest copy you can of the main branch `master`.  

~~~
$ git checkout master
$ git pull origin master
~~~

Now you can tackle integrating your changes with the new authoritative copy.  

## Update your development branch

### For minor changes

Merge the changes from the main branch into your development branch.  

~~~
$ git checkout banana-peels
$ git merge master
~~~

This will likely generate a conflict.  Resolve the conflict.  Your 
development branch is now updated.  

### Alternatively (again for smallish changes)
<a name="rebase"></a>
Rebase your old branch onto the tip of the main branch.  This essentially takes 
your branch and "replants" it on the most current version of `master`.  

Caveat: rebasing is not recommended for branches on which other people may be 
doing their own development work.  For example, if your development branch, 
`new-wheelie-feature` is also being contributed to by a few other people, you
you should not be rebasing.  However, in the case of submitting a pull request, 
the only person who has contributed to the branch is probably you.  

Rebasing is done from the development branch.  Check it out: 
~~~
$ git checkout banana-peels
~~~

And then rebase: 

~~~
$ git rebase master
~~~

This may cause a conflict.  Resolve as usual to finish updating your branch.  

(Optional: [squash all your changes into one commit before rebasing](
pull-requests-squash.html) )

### Saving just a few changes from the development branch
<a name="cherry"></a>
I know some people have found cherry-pick hard to use, but I have had amazing 
success with it, so I will include it here.  `git cherry-pick` is great if your development branch (`banana-peels`) is old, wildly different from `master`, and you want just one or two changes from the development branch to merge back into `master`.  

I usually make a new branch when I use cherry-pick.  From the updated 
`master` branch, create a branch. 

~~~
git branch updated-banana-peels
~~~

Then, identify the commits from the old development branch that you want to save.  You can find these by checking out out that branch and running `git log`.  

~~~
$ git checkout banana-peels
$ git log --oneline
009 added other image
008 added image 
007 changed the header
006 FEAR THE BORG
005 TOO MANY TRIBBLES
~~~

Now I know that I just want the changes from commits `007`, `008` and `009`.  I'll 
check out my new branch again: 

~~~
$ git checkout updated-banana-peels
~~~

And then cherry-pick my chosen commits on top.  

~~~
git cherry-pick 007 008 009
~~~

This will take the changes from those three commits, and place them on 
`updated-banana-peels`.   

See [this tutorial](http://think-like-a-git.net/sections/rebase-from-the-ground-up/cherry-picking-explained.html) for more info.  

(Optional: [squash all your changes into one commit before cherry-pick](
pull-requests-squash.html) )

### When in doubt, start over

If none of these seem manageable to you, create a new branch based on the current 
`master` and try to incorporate the changes from your old development branch as 
best you can.  Close the old pull request and submit the new branch as 
a new pull request.  There is no shame in this.  

## Update the pull request

In any of these situations, you should end up with either a new branch with changes 
or an updated branch with changes.  Once everything is squared away, push those 
branches to your fork to update existing pull requests or create a new one.  

~~~
$ git push peach banana-peels
~~~
or
~~~
$ git push peach updated-banana-peels
~~~

## Some links

I find this the hairiest part of dealing with pull requests, so have some links 
where I got some of this information!  

* https://github.com/edx/edx-platform/wiki/How-to-Rebase-a-Pull-Request
* http://git-scm.com/docs/git-rebase
* http://git-scm.com/book/en/v2/Git-Branching-Rebasing
* http://stackoverflow.com/questions/7947322/preferred-github-workflow-for-updating-a-pull-request-after-code-review