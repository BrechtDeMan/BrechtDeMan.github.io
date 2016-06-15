---
layout: post
title: Getting started with Python/The Secret Santa problem
date:   2015-02-14 13:57:01 +0200
categories: developer
excerpt_separator: <!--more-->
---

**Valentine's day special!**  

This is my Valentine’s gift to you: I took it upon myself to streamline the organisation of a ‘Secret Valentine’ event in the building where I live, and wrote [this code](https://github.com/BrechtDeMan/secretsanta) to take care of the tedious tasks of pairing the participants in an appropriate way, as well as sending emails to inform them of their assigned platonic partner for the day.   

To make sure I would get something out of it myself as well, I forced myself to write it in [Python](https://www.python.org) and get some experience with this very hip and happening language all the cool kids seem to be using, endorsed by among others Randall Munroe ([xkcd](http://xkcd.com)):   

![Picture](/uploads/3/4/4/2/34427003/385724302.png)

Conversely, if you type  

{% highlight python %}
>>> import antigravity
{% endhighlight %}

into a Python command line, [it opens the above comic in your default browser](http://www.reddit.com/r/ProgrammerHumor/comments/1hvb5n/til_if_you_type_import_antigravity_into_a_python/?sort=new).   

There's also [this](http://xkcd.com/413/) comic (sadly 'import soul' doesn't natively do anything in Python... yet).   

Also related to xkcd, there is a [Python library](https://pypi.python.org/pypi/xkcd/) to access and retrieve links to comics from xkcd.com.  

Back to the Secret Valentine/Secret Santa problem.   
To be precise, I have used Python before but never beyond introductory exercises, [Software Carpentry](http://software-carpentry.org) workshops, maintaining and debugging scripts from [The Open Multitrack Testbed](http://multitrack.eecs.qmul.ac.uk) (an online multitrack audio repository with semantic database that I recently launched), modelling the navigation system for a robot (modded [Roomba](http://www.irobot.com/For-the-Home/Vacuum-Cleaning/Roomba.aspx)) I helped develop as an undergraduate - I’m told one of them is known as ‘BDM’ and still happily driving around in [IBCN](https://www.ibcn.intec.ugent.be)'s wireless lab at [UGent](https://www.ibcn.intec.ugent.be).   

[![Picture](/uploads/3/4/4/2/34427003/4314438_orig.jpg)](/uploads/3/4/4/2/34427003/4314438_orig.jpg)

Preparations for the Secret Valentine event by @YvBellingen


While there is some excellent work on elegant solutions to this problem, many rooted in graph theory, I’ve chosen the lazy route - also known as efficient in terms of coding effort if slightly inefficient from a computation point of view. After all it is a weekend project, a solution for a fairly mundane task, that I already spent way too much time on (mainly Googling Python syntax). But as it hurts the proud coder in me, I may update this at some point.   
For some background reading, see [this](http://www.teamavolition.com/topic/14175-interesting-programming-problem-secret-santa/) and [this](http://stackoverflow.com/questions/273567/secret-santa-algorithm) discussion and [this very mathematical paper](http://www.lix.polytechnique.fr/~liberti/sesan.pdf).   

So what I do here is to generate a random ‘index vector’ of integers, where if the first position’s value is X, person 1 has to find a gift for person X. Then I check for two more or less obvious conditions:  


> 1\. The value at position X cannot be X; otherwise person X would have to find a present for himself.   
> 2\. The value at position X cannot be Y, if the value at position Y is X; otherwise person X receives a present from the person he also has to give a present to, i.e. person Y. 

The latter is purely a matter of preference, and there could be situations where you wouldn’t want this condition implemented.   

A third condition was added due to the nature of the event, where if couples or families would take part, it would be dull if one would have to find a present for a family member - this would likely happen outside of this event already and not really add to the Secret Santa/Valentine experience in this case.   


> 3\. The value at position X cannot be Y, if person X and Y share the same room numbers. 

To accommodate this, the signup sheet (using Google Forms) included a room number field as well.   

If a randomly generated vector did not meet any of these requirements for any element in the vector, a new random vector was generated. This usually only took a couple of attempts (depending on the length of the list and the number of participants sharing a room).  

**Intermezzo:** an [xkcd](http://xkcd.com/1016/) comic about Valentine's day:

![Picture](/uploads/3/4/4/2/34427003/553440289.png)

I created a different Python ‘module’ for pairing and sending out emails, as I wanted to send the organisers of the event a proposal of ‘pairs’ of people, before sending emails to everyone (sending more than one email was not an option).   

That's it!   
See [my GitHub page](https://github.com/BrechtDeMan/) for the [code repository](https://github.com/BrechtDeMan/secretsanta).   

**Overal experience:**  
I like the language, it’s elegant and intuitive, and overall makes a lot of sense. It’s not too stringent on syntax, meaning there are often many different ways of writing something (the strings which can be ‘string’ or “string” is but one example of this).   
It can be a definite drawback that the code is not checked as much as e.g. C++, i.e. debugging only happens at runtime.   
I have found XCode to be a dreadful editor for Python, even if I like it for C++. I will have to look into other editors (I know there are more than enough out there).   


> Going [#Python](https://twitter.com/hashtag/Python?src=hash). Are most on 3.x? How about libraries (especially music&audio related)? [@functiontelechy](https://twitter.com/functiontelechy) [@utstikkar](https://twitter.com/utstikkar) [@chris_cannam](https://twitter.com/chris_cannam) [@RDCLayne](https://twitter.com/RDCLayne)
> 
> — Brecht De Man (@BrechtDeMan) [January 12, 2015](https://twitter.com/BrechtDeMan/status/554616315936530432)


It seems many are still on version 2.7, even if Python 3 is available and many libraries have been ported to this version - see the above [conversation](https://twitter.com/BrechtDeMan/status/554616315936530432) on Twitter.   

On another note, I have found that documenting my work with a blog post such as this one really improves the thinking process, so may do it more often. I doubt it will be of help to someone, but if anything it has been helpful for me.   

Finally, I haven’t been able to find a nice alliterating name for a Valentine’s Secret Santa (Veiled Valentine?). All suggestions are welcome.   

[![Picture](/uploads/3/4/4/2/34427003/8015391_orig.jpg)](/uploads/3/4/4/2/34427003/8015391_orig.jpg)

Secret Valentine event


More xkcd comics on Valentine: [63](http://xkcd.com/63/), [223](http://xkcd.com/223/), [701](http://xkcd.com/701/)  
Python best practice: [PEP 8](https://www.python.org/dev/peps/pep-0008/), [Python docs](http://docs.python-guide.org/en/latest/writing/style/), [How Not To Write Python Code](http://eikke.com/how-not-to-write-python-code/), [Code Like A Pythonista](http://python.net/~goodger/projects/pycon/2007/idiomatic/presentation.html)
