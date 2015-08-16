Title: Preparing to teach Python
Date: 2015-08-16 15:00
Category: teaching
Tags: python, software carpentry, learning, education
Slug: python-prep
Authors: Christina Koch

**Context:** I read a [blog post](http://blog.byronjsmith.com/swc-python-lesson.html) by [Byron Smith](https://twitter.com/ByronJSmith), [tweeted](https://twitter.com/rgaiacs/status/632519587679084544) by [Raniere Silva](https://twitter.com/rgaiacs) about his experience teaching the Software Carpentry novice Python lesson.  As I had just started to prepare to teach the Python lesson myself, I thought I'd write up what I've done so far, and how I plan to 
continue.  

I've been slated to teach Python at a Software Carpentry workshop at the 
end of August, through my job at the University of Wisconsin Madison.  I've 
taught the Python lesson before, but not for several months, and I remembered 
having trouble figuring out the lesson fit together, so I was a bit 
concerned as I opened up tabs with the [lesson pages](http://swcarpentry.github.io/python-novice-inflammation/) and [github repo](https://github.com/swcarpentry/python-novice-inflammation).  

Fortunately, reading through the lesson, I was able to make sense of the content 
and order by the guiding statement/question: 

> We have to accomplish a task (reading in data, analyzing and plotting it)
> by writing a program.  How can we be smart about it?

The answers, as I see them in the lesson are: 
> * Don't write everything from scratch; use libraries (Analyzing Patient Data)
> * Don't copy/paste for repetition; use a loop (Repeating Actions with Loops, Storing Multiple Values in Lists, Analyzing Data from Multiple Files)
> * Don't just run tools as they are; write "intelligent" code that can tell you something (Making Choices)
> * Don't copy/paste identical code; write functions (Creating Functions)
> * Don't just leave chicken scratch; test and document your work (Creating Functions, Defensive Programming)
> * Don't partition workflow of multiple parts by depending on IDE; write command line scripts (Command-Line Programs)

So in terms of teaching, 
I plan to introduce very quickly that python can be run on the command line, 
or in an IDE like the notebook, we will be using the notebook, and a quick tour.  

I will then present the guiding question, as above, and explain that the lesson 
will be talking about big picture answers to that question (that can be applied 
to any language), but that we will be using Python as our implementation method 
and therefore, there will be some sections that are more about Python details.  

Then, I will probably open *two* notebooks, one for the "big picture" stuff as 
it applies to the inflammation data example, and one for more Python-y things, 
like toy functions, playing around with lists...essentially "scratch" space.  For 
each bullet point above, I'll introduce the idea, why we use it, how to 
implement it in Python, and then have some combination of exercises / application 
to the inflammation data example.  For example, I'll introduce the idea of a 
for loop, do a demo from the "Repeating Actions with Loops" lesson, have the 
students do an exercise, repeat these two steps for lists, and then finally have the students 
try applying the idea of a loop to their inflammation analysis, with some help from me 
when it comes to `glob`.  The exercises will be curated from the list 
of possibilities - I'm not planning to show them all to students in the
workshop. 

I will be skipping all the material on errors, testing and debugging, as our 
workshop will cover that separately in a different session. I will possibly 
omit certain sections of lessons (for example, the example of testing a function in 
"Creating Functions").  "Making choices" may get moved to after "Creating Functions" 
(still on the fence for that one.   I hope to make it 
all the way to command-line programs by the end of the morning.  

The one thing that doesn't fit well 
(in my mind) to the 
framework above, is the extensive discussion of indexing in the very first part of 
the lesson.  I may skip it entirely, or move it to the portion of the lesson on 
lists.  And when I talk about lists, I will point out that it is a sidebar to 
our main goal (making smart choices), but we need to know about it in order to 
do other things.  Also, while it's not a focus of the lesson, I will probably 
use the list portion to point out that your language probably has a "native" 
data type for lots of pieces of data and it's important to understand how at 
least the base type works in order to program effectively.  

Having thought this through, I'm planning to do a practice run this week
(testing if it's worth it to juggle 
two notebooks, how long the typing will take if I expect people to follow me, 
where I need to cut and paste).  I've printed out the lessons and will 
annotate them with things like which notebook to be using, when to break for 
exercises, etc.  I also need to create a page with my exercises of choice, and 
(several hours later) I hope to be ready.  

I'll have to report back in early September to see if it went as smoothly 
as I'm hoping!  