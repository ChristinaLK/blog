Status: draft
Title: Care and keeping of pull requests, part v
Date: 2015-07-03 7:00
Category: computing
Tags: git, github, collaboration, version control, pull requests, care and keeping of prs
Slug: pull-requests-squash
Authors: Christina Koch

See [first post disclaimer](http://christinalk.github.io/blog/pull-requests.html)  

## Squashing commits

Bonus points!  This is usually too fussy for me, but can be really useful if you made a 
lot of little commits.  Squashing many commits into one means that if you `cherry-pick` or `rebase` (see [last post](pull-requests-magic.html), 
there will only be one commit to incorporate into the master branch instead of a string of small commits.  Also, it can just look nicer, if you're into style.  
