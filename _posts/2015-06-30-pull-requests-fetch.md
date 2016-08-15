---
layout: post
title: Care and keeping of pull requests, part ii
date: 2015-06-30 12:00
categories:
   - how-to
tags: 
   - git
   - collaboration
   - care and keeping of prs
slug: pull-requests-fetch
authors: Christina Koch
---

See [first post disclaimer](http://christinalk.github.io/blog/pull-requests.html)

Scenario: You now have a copy of the main repository and your own local changes (which 
are also now on your remote copy).  What if you want to look at someone *else's* 
changes, that they have made in *their* local copy and pushed to *their* remote 
repository?  You could just clone their remote repository, but 
it's nice to be able to have your work and their work within the same local 
repository.  Is it possible?  Yes it is!  

(This is also just a handy technique to know about if you're going to be 
mucking around with multiple remote repositories.)  

> In what follows, our collaborator's username is `mario`, and he has added changes to 
> the `mario-kart` repository under the `mushroom` branch.  

## Fetching someone else's remote repository

Fetching a copy of someone else's remote repository is great, because by itself 
it will never break anything or cause conflicts.  The first thing to do is add
the other remote repository to your list of remotes.  

~~~
$ git remote add mario https://github.com/mario/mario-kart
~~~

You can call the remote whatever you want - I often use the username 
of the owner so I have less to remember.  

Once the remote is added, fetch its contents: 

~~~
$ git fetch mario
~~~

It may seem like nothing has happened, but the fetch command has pulled down 
all the commits from the Mario's repository (including all their branches) and stored them in your repository, but not in a visible way.  To see all these fetched branches, use: 

~~~
$ git branch -a
~~~

Aha!  You should see a list of normally visible (that is, local) branches and then a list of invisible branches (branches that haven't been checked out locally yet).  To 
make a particular branch visible, keep reading.  

## Checking out someone else's development branch

Maybe I want to actually look at Mario's `mushroom` branch (which would be 
signified by `mario/mushroom` in the full list of branches given by 
`git branch -a`).  There are different ways to deal with remote branches, but I think 
the easiest is to check them out locally.  With two commands, it looks like this: 

~~~
$ git branch marios-changes mario/mushroom
$ git checkout marios-changes
~~~

With one command, like this: 

~~~
$ git checkout -b marios-changes mario/mushroom
~~~

Either one of these options will a) create a new local branch called `marios-changes` 
(you can call it whatever you want) b) link that new local branch to Mario's 
patch that you pulled down from his repository (`mario/mushroom`) and c) checkout
that new branch.  You now have a 
branch just like any other, that can be committed to, merged and even updated using: 

~~~
$ git checkout marios-changes
$ git pull mario mushroom
~~~

(This pulls changes from the `mushroom` branch in the `mario` remote 
repository into your local copy of the branch, called 
`marios-changes`).  
