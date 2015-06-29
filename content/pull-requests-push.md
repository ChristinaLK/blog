Status: draft
Title: Care and keeping of pull requests, part ii
Date: 2015-02-29 7:00
Category: computing
Tags: git, github, collaboration, version control, pull requests
Slug: pull-requests-push
Authors: Christina Koch

See [first post disclaimer](http://christinalk.github.io/blog/pull-requests.html)

Scenario: I want to submit some changes to the master repository, 
owned by someone else.  I can't submit them directly, so I'm going to create a pull 
request.  

> In what follows, `master` is the main branch of 
> development.  In our local repository, we have used `origin` 
> to refer to the central repository,  and `my-fork` refers to my fork of the central 
> repository.  

## Submitting a pull request

First I'll create a new branch for my changes and check it out.  This can be done 
with two commands: 

~~~
$ git branch my-patch
$ git checkout my-patch
~~~

or with one: 

~~~
$ git checkout -b my-patch
~~~

After I make the changes  and commit them with the usual `git add` + `git commit` combination, I'll push the branch with my changes to *my* remote (`my-fork`):

~~~
$ git push my-fork my-patch
~~~

This puts my changes online in *my* copy of the repository.  Now I just need 
to notify the central repository (`origin`) by actually submitting the pull request
(literally - "I'm requesting that you pull the changes from my copy").  [[1](#changes)]

You can always submit a pull request by 
1) going to your online remote (so `github.com/my-fork/our-repository`) 
2) clicking on "pull requests" in the right hand menu
3) clicking on the "New Pull Request" button
4) This should land you on a screen that says "Comparing Changes" at the top.  

There are other ways to get to this screen (I never submit a pull request the same way 
on the Github website), but the above will always work. [[2](#buttons)]
Anyhow, once you've clicked some combination of the right buttons, 
and see "Comparing Changes", make sure you have the following: 

* "base-fork": the main repository
* "base" branch: main development branch (`master`)
* "head-fork": your repository 
* branch to "compare": whatever you just pushed to your own repository 
(`my-patch`)

Click on the big green button (two times) to finally 
submit the pull request.  [[3](#all-the-buttons)]

##Updating a pull request with more changes

This is super easy. I'll go back to the local repository I have on my 
computer.  Make sure you're in the correct branch (the one we
were making changes in before)...

~~~
$ git checkout my-patch
~~~

...and make edits/commit changes as before.  I push the branch to my fork.  

~~~
$ git commit -m "making changes based on suggestions"
$ git push my-fork my-patch
~~~

Ta-da!  That's it.  I
don't need to "resubmit" the pull request, as the pull request on the main 
repository will automatically update (Github magic!) based on the changes 
that I've pushed to your copy of the repository.  

<a name="changes">[1]</a> One thing I found confusing when I started making pull requests was that 
the changes were in *my* remote repository, but the pull request appeared on 
the site for the main repository.  Just a heads up.  

<a name="buttons">[2]</a> When in doubt, look for green buttons - they usually 
signify some way to submit a pull request.  

<a name="all-the-buttons">[3]</a>Green buttons everywhere.  