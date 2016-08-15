---
layout: post
Title: Your computer as a kitchen
Date: 2015-07-26 18:00
Category: 
   - reflections
Tags: 
   - computing
   - software
   - teaching
Slug: kitchen-computer
Authors: Christina Koch
---

In three days I will be presenting on software portability at the 
[Open Science Grid summer school](https://twiki.opensciencegrid.org/bin/view/Education/OSGUserSchool2015).  I've 
used a metaphor at the start of my talk, to motivate and explain what software 
portability IS and why we care about it, and I've been thinking that it's actually a 
decent way to explain how computers work in general.  

The metaphor?  Your computer is like a kitchen.  

It has some basic tools (an oven, microwave, sink, refrigerator) and storage 
space (cabinets).  There's even some dynamically shareable space for holding 
food as its being prepared (countertops).  Maybe this is a restaurant kitchen, 
with a head chef and many sous-chefs.  Each sous-chef has his or her own task 
and perhaps some specialized cooking gear, in addition to what pieces are in 
common.  The sous-chefs are following a recipe, but ultimately, they are under
the control of the head chef.  

In the same way, your computer comes with some basic tools (processors, drives, 
network card) and storage space (your filesystem on a hard disk).  It also has 
shared memory for running processes.  One master process (the operating 
system) oversees many small processes, serving as the gatekeeper in their 
interactions with the kitchen.  Many of these processes are following instructions 
written in their source code, using tools specifically written for them, but 
also some tools that are native to the computer/OS.  

In my talk about software portability, we are
dealing with the scenario of running distributed high throughput 
work, which runs your task (a software process) on someone else's computer.  In 
this case, you're sending your sous-chef to cook something up in someone 
else's kitchen and so you must make sure the chef has everything they need 
(ingredients, recipe, pots/pans = data, code, libraries) in order to accomplish 
their task succesfully.  

We'll see if this parallel works for other computing scenarios in the future!  