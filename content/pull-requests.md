Status: draft
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

Forthcoming posts on what to do when there's a conflict between your PR and the `master`.  Git-fu abounds!