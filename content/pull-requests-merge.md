Title: Care and keeping of pull requests, part iii
Date: 2015-07-01 12:00
Category: computing
Tags: git, github, collaboration, version control, pull requests, care and keeping of prs
Slug: pull-requests-merge
Authors: Christina Koch

See [first post disclaimer](http://christinalk.github.io/blog/pull-requests.html)

Scenario: The time has come to merge pull requests.  Either you are one of the owners 
of a central repository and are responsible for reviewing and merging pull requests, 
or someone has submitted a pull request to one of your personal repositories.  

To start, I'm going to assume that the pull request can be merged with no conflicts 
(indicated on the page with the request) or very minimal conflict.  For 
details on more complicated merges, see 
the next post on [magic](pull-requests-magic.html).  

> In what follows, the name of the repository is `mario-kart`.  
> In our local repository, we have used `origin` to refer to the central repository, 
> and `master` is the main branch of 
> development.  The owner/maintainer (`nintendo`) is merging a
> pull request made by someone
> with the github username `luigi`, whose pull request branch is named `turtle-shell`.  

## Merging pull requests online.  

Go to the pull requests page on the github page of the 
central repository `github.com/nintendo/mario-kart`.  [[1](#prs)]

Click on the big green button (two times: "Merge Pull Request" and "Confirm Merge").  

The end.  

## Merging pull requests locally.  

On Github, find the pull requestor's copy of the repository.  Fetch that 
repository, and check out the branch that they're comparing (as [previously described](http://christinalk.github.io/blog/pull-requests-fetch.html) on this blog).  If 
 the requestor is Luigi and his development branch to be merged is called 
`turtle-shell`, that process would look something like: 

~~~
$ git remote add luigi https://github.com/luigi/mario-kart
$ git fetch luigi
$ git checkout -b luigis-changes luigi/turtle-shell
~~~

Now, you want to merge `luigis-changes` into the `master` branch.  Make sure 
to checkout `master` first, as that is the branch you ultimately want to 
update.  

~~~
$ git checkout master
$ git merge luigis-changes
~~~

In theory, this method can be used even if there are conflicts at this 
stage; whether or not you merge conflicting pull requests into `master` 
yourself (as opposed to making the original requestor modify their requests) 
is up to you and the group you're working with.

The merge is now complete; you just need to push the newly merged-in 
changes to the central repository: 

~~~
git push origin master
~~~

Through some magic, Github will recognize that the changes from that pull 
request have been merged, and the Github page with that pull request will 
indicate that the branch has been merged and the PR is closed.  


<a name="prs">[1]</a>  Open pull requests can be found on the right 
hand menu of any repository page.  