Title: Practice what you preach
Date: 2015-01-29 7:00
Category: computing
Tags: r, programming, data, motivation, swc, true story
Slug: practice-what-you-preach
Authors: Christina Koch

I had a Software Carpentry "moment" at work this week.  I had to sort through an excel spreadsheet of accumulated computing hours ([like this](http://monitor.chtc.wisc.edu/uw_condor_usage/usage365.shtml)), finding all users 
with significant hours in a certain pool.  

I knew that this would be a very simple select, filter and sort with dplyr.  "But I only need the list once" I said, "and when did I last do something in dplyr?"  Was it worth converting the file to .csv or .tsv, figuring out how to load it using read.table() and then revisiting dplyr?  

I thought the answer was 'no' and then I said, "screw it, why not" and that turned out to be a great decision because I then needed to load another spreadsheet, filtered by project, to determine top users within groups.  Four lines of code, used at least 15 times.  MagrittR and dplyr for the win!  

The fact that I was reluctant to invest 5 minutes in coding, that I was surprised at how beneficial it was, that I fell for the "I'll only do this once" despite having taught multiple Software Carpentry workshops saying otherwise - I don't know what that means, except maybe that old habits die hard and believing in initial investment/future payoff really is a step of faith.  Leading by example, if I'm going to teach people about computing practices, I've got to practice what I preach!  

(hat tip to [@STAT545](https://twitter.com/stat545) *cough* Jenny Bryan *cough* for the [online encouragement](https://twitter.com/_christinaLK/status/560494461692956672) to get back on the dplyr bike and just go for it.  :D)