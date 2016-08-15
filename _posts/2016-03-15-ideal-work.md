---
layout: post
Title: When Everything Works
Date: 2016-03-15 14:30
category: 
   - stories
tags: 
   - true story
   - computing
   - work
   - SCF 
   - problem-solving
Slug: ideal-work
Authors: Christina Koch
---

Storytime!  Last week, I experienced a great moment at work, 
one of those "lightbulb" moments which exemplified the best of 
what my work can and should be.  

Our story begins with a support email. I've been emailing with her 
since the previous day, having diagnosed + solved a bug that she 
had found in one of our Matlab tools.  Then she emailed 
again in the morning, saying that she had done what I said, but her 
jobs weren't starting.  

"That's funny," I thought. "The Matlab issue should have no impact 
on jobs starting. Must be something else."  

So I looked at the queue and saw that the two jobs she'd submitted 
were idle - and most definitely shouldn't have been!  Working outward, 
I looked at the whole queue - and in fact, there were at least 20-30 
of these job types that were idle when they should have been running.  

I messaged our sys admin, and mentioned this to my co-worker Lauren, who was
sitting next to me.  We both looked at the queue in more detail.  We had
encountered this issue before, where the queue was overloaded, but that wasn't
the case here.  It looked like there was a specific time when these 
jobs didn't start running, so Lauren asked if we had recently upgraded the 
machines, or made some other distinct change that would have caused the issue.  Then 
she remembered that, wait, we'd recently made some changes related to 
the eventual rollout of a new operating system version.  

I had been chatting our sys admin, but it was time to pick up the 
phone.  We called, asking if Lauren's 
hunch was correct.  It was.  Lauren discussed
a plan of attack - our sys admin would modify the recent changes, so that 
new jobs would be able to start again; Lauren would modify the jobs already in the queue 
so that they would be able to start.  

One command later, the requirements were changed, the idle jobs had started, 
and I was able to email the original user to say "Thanks for telling us about this - 
your message helped us find the issue!"  

This is the stuff!  Being available to hear about problems, 
having the tools to figure out what's happening, using each other's expertise, 
deciding on a course of action, and then implementing a solution together.  It's not always 
such a tidy process as today, but it sure is great when it is!  
