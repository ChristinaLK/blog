---
layout: post
title: Care and keeping of pull requests, part i
date: 2015-06-29 12:00
categories: 
   - how-to
tags: 
   - git
   - collaboration
   - care and keeping of prs
slug: pull-requests-push
authors: Christina Koch
---

See [first post disclaimer](http://christinalk.github.io/blog/pull-requests.html)

Scenario: You want to submit some changes to the master repository, 
owned by someone else.  You can't submit them directly, so you have to 
create a pull request.  

> In what follows, `master` is the main branch of 
> development.  In our local repository, we have used `origin` 
> to refer to the central repository,  and `peach` refers to your fork of the central 
> repository.  

## Submitting a pull request

First, create a new branch for the changes and check it out.  This can be done 
with two commands: 

~~~
$ git branch banana-peels
$ git checkout banana-peels
~~~

or with one: 

~~~
$ git checkout -b banana-peels
~~~

After changes are made and committed (with the usual `git add` + `git commit` combination), you can push the branch with your changes to *your* remote (`peach`):

~~~
$ git push peach banana-peels
~~~

This puts changes online in *your* (`peach`'s) copy of the repository.  Now you just need 
to notify the central repository (`origin`) by actually submitting the pull request
(literally - "I'm requesting that you pull the changes from my copy").  [[1](#changes)]

You can always submit a pull request by 
1) going to your online remote (so `github.com/peach/our-repository`) 
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
(`banana-peels`)

Click on the big green button (two times) to finally 
submit the pull request.  [[3](#all-the-buttons)]

## Updating a pull request with more changes

This is super easy. Go back to the local repository you have on my 
computer.  Make sure you're in the correct branch (the one we
were making changes in before)...

~~~
$ git checkout banana-peels
~~~

...and make edits/commit changes as before.  Push your branch to your fork...

~~~
$ git push peach banana-peels
~~~

Ta-da!  That's it.  You
don't need to "resubmit" the pull request, as the pull request on the main 
repository will automatically update (Github magic!) based on the changes 
that you've pushed to your copy of the repository.  

<a name="changes">[1]</a> One thing I found confusing when I started making pull requests was that 
the changes were in *my* remote repository, but the pull request appeared on 
the site for the main repository.  Just a heads up.  

<a name="buttons">[2]</a> When in doubt, look for green buttons - they usually 
signify some way to submit a pull request.  

<a name="all-the-buttons">[3]</a>Green buttons everywhere.  