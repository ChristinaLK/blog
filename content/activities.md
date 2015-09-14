Title: Not Quite Lesson Material
Date: 2015-09-013 18:00
Category: teaching
Tags: programming, computing, motivation, swc, teaching, education, pedagogy
Slug: activities
Authors: Christina Koch

Lesson plans are a funny thing.  The [Software Carpentry lessons](http://www.software-carpentry.org/lessons.html)
are an odd balance of a lesson to be read (like a textbook) and a lesson plan for 
instructors, where they bring the text to life via speaking, live coding, and 
doing exercises.  

This format doesn't lend itself well to a few activities I've used in Software 
Carpentry workshops.  So I'm going to throw them up here until further notice.  

## Git demo

Before teaching the [Git novice](http://swcarpentry.github.io/git-novice) lesson, I 
have done the following live demo.  All that's needed is a picture taking device, 
preferably a smartphone or tablet.  I've never timed it, but I don't think it 
takes very long - probably around 5 minutes.  

I do this *after* configuring git, but before 
the first `git init`.  

* The scenario: the workshop room is directory, each student is a file
* Have all students write down some datum on their green sticky note (I've used 
number of years in higher ed, could be anything).  
* Explain that you want to track this data.  To do so, you'll be creating a 
recording device (hold up the smartphone or tablet) and taking a picture. Before 
you can take a picture, you'll need everybody to stand up so they can 
be in the picture
* Have everyone stand (holding up their sticky with a piece of data), and take a picture
with your device.  Have everyone sit down.  
* Now the data is going to change.  Have everyone write down another datum (you choose), 
on their other sticky note.  
* Explain that this time, you want to save the changes in two batches.  Have half 
the room rise, with both stickies, take a photo.  Do the other half of the room.  
* Optional: point out that you didn't want that last piece of data after all.  So 
hold up the device with the first photo and say "return to this".  Everyone should 
leave their second sticky on the table.  Have everyone rise with just the first 
sticky (again) and take another photo.  

To wrap up, explain that everyone has just experienced a typical git workflow...
* create a recording device, also known as a repository (the smartphone/tablet)
* stage data files (standing up)
* commit those changes (take a picture)
* repeat the process, with the ability to stage and commit groups of files (half and half)
...and that you'll now be covering the commands used in the shell to achieve
the same thing.  

Later in the lesson, when talking about commit hashes, I use this example again 
to explain that Git auto-generates a hash, just like your camera-device gives 
an automatic name to photos, but you can refer to commits in an ordered way 
as well, just as you scroll through photos on your device in chronological order.  

If you want to go really crazy, the contrast of sticky notes in the photo can be 
a parallel to using `git diff` and the return to an original state as an example of 
`git checkout ####`.  

Pedagogical disclaimer: the motivation for this demo is purely to get people standing up, 
moving, and physically interacting with these ideas, which are otherwise very 
abstract.  Personally, I have always found that I remember exactly the bits of 
lessons where I had to stand up and *do* something.  So I have no research-based 
reason to use this demo except my own experience.  That and students seem to like 
it.  If anyone can provide evidence to support me, that'd be great!  

## Shell group activity

There's a fine line in the shell lesson between "teaching shell commands", 
"teaching shell concepts", and "teaching the general concepts behind shell."  Life 
is challenging.  

One thing I do to address this balance is break up the shell lesson into two 
pieces.  The first piece is "shell concepts" (the idea of the filesystem, and being 
able to run any command from anywhere) and the second piece is "general concepts 
behind shell" (scripts, loops, pipes and filters).  To bridge the two, I take a little 
break and have people investigate shell commands themselves.  The logical link for me 
is: we've learned about some very basic shell commands + how the shell works generally; 
now let's do a (brief!) overview of some of the variety of shell commands; then we 
can talk about how good practices like loops, scripts, pipes will allow us to use 
this variety of commands in *even more* ways.  

The activity is very simple - I divide the room into groups and give each of them 
a shell command to research.  A sample list might be: 

* less vs cat
* head
* grep
* wc
* sort
* uniq
* find
* cut

Each group needs to use the `man` pages (or internet) to find out what the command 
does, think of an example for the instructor (me) to demonstrate, and describe a 
scenario where that command might be useful.  After a few minutes working together, 
each group "presents" to the large group, facilitated by the instructor.  I'm 
always careful to point out that this is purely a *brief* summary, and that I'm trying 
to expose them to the range of shell commands and to give them the skills to pursue 
whatever they might need later on their own.  

* Things I like 
about this activity: it provides a natural break from the instructor talking, 
works well for both novice and advanced 
learners (advanced learners can move onto other commands if they finish theirs, or help
their group members), and helps illustrate what the shell can do without explicitly 
covering any one thing in detail.  Also, not much prep!  :)
* Things I don't like about this activity: It could be information overload?  I could see 
it being overwhelming for a true novice.  Or that people would check out if they are 
very noivce or very advanced.  

## Shell demo

I haven't done this yet, because I haven't taught the shell lesson since I thought 
of it.  But I'd like to try to the following to really drive home 
the idea of relative and absolute paths and that 
shell commands are run *relative to the working directory*: 

* Use the same idea as the git demo, that rooms are directories and people are files.  In
that context, `ls` is like saying "tell me the name of everyone in the room.  
* Step outside the room briefly.  Come back in and ask, what response would I get 
if I asked that question outside (running `ls` in a different directory)?  What 
if I asked that question outside, but I specified the workshop room (using `ls` 
with a relatively path)?   
* Back in the workshop room, how would I ask the names of people in a different 
room in the building?  Would need either a relative path (go out the door, down 
the stairs, turn left, etc.) or an absolute path ( Milky Way -> Solar System -> 
Earth -> Continent -> etc.) to know where to go to ask the question.  
* Reiterate the ideas above on the command line, drawing clear parallels between 
the rooms/directories and how to use `ls`.  

It makes sense to me, but I'm not sure if it would clarify ideas or confuse the 
listeners.  
