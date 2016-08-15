---
layout: post
title: Git Models
date: 2015-11-24 23:00
categories: 
   - reflections
tags: 
   - programming
   - computing
   - git
   - shell
   - teaching
slug: git-models
authors: Christina Koch
---

There are several motivations to this post: 

* I'm always seeking ways to explain git more clearly (one example given 
in my [previous post](activities.html)).
* I've been thinking about the idea of [threshold concepts](http://www.ee.ucl.ac.uk/~mflanaga/thresholds.html) (which, as it 
sounds, are concepts necessary to achieve a new level of understanding)...in 
particular, considering what threshold concepts are important for novice 
learners in Software Carpentry workshops.  
* [This recent XKCD](http://xkcd.com/1597/)

Git is challenging.  There's no getting around it.  But I've found some 
coherence in the complexity by taking a key concept from the unix shell
 and applying it to git.  In some ways, this approach just shuffles the 
learning challenge to a different place (learn this arcane command line technology 
and then you'll understand git!) but I'm writing this up in the hopes that 
it will be helpful for people who *have* done a lot with the shell, but 
are still uncomfortable with git.  

So let's start with
interacting with a Unix system via the shell.  For me, one threshold concept in 
understanding the shell is "location is everything."  Everything you do 
in the shell is done in the context of the filesystem.  From within 
a shell, you can move yourself from one arbitrary point in 
the filesystem to another.  You can 
run a program from anywhere, using files from anywhere, sending output to 
anywhere.  When you install software, that software goes into a location, using 
tools installed in another location, and libraries in another location.  While 
the filesystem is normally represented as a tree, I like to think of it more 
as a map.  

Location is everything.  

A pivotal moment in my understanding of git was applying this threshold concept 
to git.  Location is still everything, but now, instead of location in your computer 
(on disk, essentially), with git, we are navigating **location in time**.  The 
`HEAD` pointer 
is the equivalent of `whoami`.  We can move ourselves to any place in our timeline 
in the same way that we can use `cd` (and with the same variety of options: absolute 
and relative paths become commit hashes and `HEAD~1`).  When we move around in 
our timeline, we see different files, same as moving around the 
filesystem.  We can pull copies of files 
from the past using `checkout` in the same way that we normally use `cp` and 
`mv`.  A rebase moves a set of commits in the same way that `mv` could move a 
set of nested directories.  We can see where we are in time by running `git branch`
or `git log`, just like we use `pwd` when running around the filesystem.  And the 
list of files in this time, the `ls` of git, is `git status`.  

And, of course, both the filesystem + and a git commit history are 
represented as trees.  

This relationship isn't going to help answer all the git 
questions.  It
doesn't really address remotes, nor does it provide a good equivalent for the names 
of git branches (what would the equivalent of `master` be in the 
filesystem?  Home `~`?)  And the particular names/syntax for git commands is 
never going to be intuitive.  But hopefully it's another helpful way 
to build understanding around another piece of useful-but-hard-to-understand 
software.  
