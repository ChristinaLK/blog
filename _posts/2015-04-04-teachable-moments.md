---
layout: post
title: Teachable moments
date: 2015-04-04 14:00
categories: 
   - stories
tags:
   - git 
   - version control
   - collaboration
   - true story
   - empowerment
slug: teachable-moments
authors: Christina Koch
---

Welcome to the "teachable moments" hour, also known as "highlights of Christina's twitter this week" or "I git it!"  

* When teaching git for Software Carpentry, students inevitably ask why we care about `git add` versus `git commit`.  It's a reasonable question, especially for a novice user who just wants to have periodic checkpoints of their work.  

This week, I spent a lot of time getting ready to overhaul our website.  Thankfully, the website directory is already a git repository, so it's straightforward to commit all the current files and then safely make the changes we want.  The thing is, no one has made any large commits in this repository for several months, at least.  When I ran `git status`, there were at least 20 modified and 40 never committed files.  I didn't want to commit everything at once because if I need to check out a previous version of something, smaller commits will make it easier for me to pinpoint what I need.  

![git_add](images/git_add.jpg)

"This, this is why git add is useful".  

* Having committed all outstanding files (or added them to the .gitignore), I then started toying around with a test css file.  Editing on the server is a pain, so I copied the file locally and pushed it to the server using `scp`.  "But I'd really like to have all the files" I thought to myself.  "Isn't there an easier way to do this?"  

![git_clone](images/git_clone.jpg)

Yes.  Yes there is.  

* Not git-related, but in the same vein of tools matching use cases, my co-worker and I have been part of the development process for a new [HTCondor](http://research.cs.wisc.edu/htcondor/) feature which is currently in beta-testing.  We had a researcher come into office hours on Wednesday who wanted to submit a sequence of high-throughput jobs with essentially one command - looping through lists of names, locations, and years to generate a batch of jobs.  And this new feature does exactly that!  

![condor_foreach](images/condor_foreach.jpg)

Good week all around!  