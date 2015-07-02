Title: Care and keeping of pull requests, part v
Date: 2015-07-03 12:00
Category: computing
Tags: git, github, collaboration, version control, pull requests, care and keeping of prs
Slug: pull-requests-squash
Authors: Christina Koch

See [first post disclaimer](http://christinalk.github.io/blog/pull-requests.html)  

Scenario:  You have a series of commits on a development 
branch that you would like to include in a PR.  Maybe you want to 
[cherry-pick](pull-requests-magic.html#cherry) them 
onto a new branch, maybe you want to [rebase](pull-requests-magic.html#rebase), 
maybe you want to [just submit](pull-requests-push.html).  In 
any case, you'd rather have one big commit to _____ (cherry-pick, rebase, push) 
instead of the many small commits.  It's squash time!  [[1](#commentary)]

> In what follows, we have a development branch `blue-lightning` with a series of 
> small commits that we would like to squash together.  

## Squashing commits

### Step 1: identify your end points

To squash commits together, you need to establish a range of commits that 
may be squashed.  Just because a commit is the end point of this range doesn't 
mean it will be squashed - this step is more about setting the outer bounds of 
what you'll be able to squash together. [[2](#clopen)]

One endpoint of the range (the newest commit) will always be 
the tip of your current development 
branch, which you indicate by checking out the branch.  

~~~
$ git checkout blue-lightning
~~~

The other endpoint (the oldest commit), needs to be the commit *preceding* 
the oldest commit you want to *squash*.  Suppose my commit history on `blue-lightning` 
looks like this: 

~~~
$ git log --oneline
zzz Zap!
sss Zing! 
ooo Zoom! 
nnn Zounds!
bbb Yikes!
~~~

If I want to squash `nnn` with the commits following it, then 
my "oldest commit" endpoint
should be `bbb`, as it precedes `nnn`.  

### Step 2: start the squashing process

To actually squash commits, you'll be doing an interactive 
rebase[[3](#sigh)], using the 
endpoint you chose above.  From `blue-lightning`, run: 

~~~
$ git rebase -i bbb
~~~

This should throw you into your text editor.  

> #### Aside
> 
> There are multiple ways of indicating your chosen endpoint in this command: 
> * Use the actual commit value (shown above)
> * Use `HEAD~1` notation (in the example above, `bbb` would be equivalent to `HEAD~4`
> * If your endpoint commit is the tip of another branch (like `master`), you can use 
> the name of the branch. 


### Step 3: indicate which commits you want to squash together

In the text editor, there will be a list of the commits between your 
two endpoints.  They should all be prefaced by the word "pick."  As the 
text in the editor should helpfully indicate, if you change the "pick" prefix 
to the word "squash", git will try to squash those commits together.  You 
should leave the most recent commit of the squash as "pick", as that will be 
the commit that the others are squashed into.  Save 
and close the file.  Moments later, your text editor will open again, with 
a second file allowing you to modify the 
commit message that will be attached to the new aggregate commit (the default 
is the message for the most recent commit of the aggregate).  Save and close.  

### The end!  

Links I consulted re: squashing: 
* https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
* http://davidwalsh.name/squash-commits-git

<a name="commentary">[1]</a>  I consider this a "bonus points" git 
practice.  It's usually too fussy for me, 
but has its moments of utility.  So here we are.  

<a name="clopen">[2]</a> For the mathematically minded among you, this 
range of squashable commits will be 
a half-open interval of the form: (oldest commit, newest commit].  

<a name="sigh">[3]</a> From my limited reading, it sounds like interactive 
rebasing is the power-drill of git features, as opposed to poking around 
with the hammers and screwdrivers of `git commit` and `git push` (etc).  I cannot, 
in any way, reverse-engineer my 
intuition to make `git rebase` the obvious choice for git-feature-
that-does-everything.   