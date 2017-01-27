---
layout: post
title: Secret Santa revisited - Python pairing and emailing script
date:   2015-12-08 13:57:01 +0200
tags: [developer, Python]
excerpt_separator: <!--more-->
---

This is a sequel to my earlier blog post [Getting started with Python / The Secret Santa problem](http://brechtdeman.com/1/post/2015/02/getting-started-with-pythonthe-secret-santa-problem.html), which I wrote as a 'Valentine special' (it was written for a Secret Valentine event with upwards of 50 attendees).   

These two Python scripts take care of the sometimes tedious task of pairing up participants, and emailing each of them to tell them whom to buy/make a present, and sometimes further instructions. For smaller events, where the pairing isn't usually that tedious, there's still the additional advantage that it is purely objective (nobody is to blame when someone is annoyed with who they have to buy a present for or a receive a present from), and you can send out the emails without having a clue who gets whom, if you don't peek. 

Following a few other Secret Santas, I realised that for smaller groups with many 'forbidden pairs', e.g. a number of couples or families, it would also be nice for a 'team' not to have to buy presents for all members of another 'team'. In other words, if A1 and A2 are a couple, and B1 and B2 are a couple, A1 should not have to buy a present for A1 (himself) or A2 (his partner) - but also, if A2 is already the Secret Santa for B2, then A1 shouldn't have to give a present to B1.   
I therefore introduced rule number 4.   

From the README:

1.  _a person doesn't have to give a gift to himself;_
2.  _a person doesn't receive a gift from the person he's given a gift to; _
3.  _a person shouldn't get a gift for a room mate (partner, child, parent); _
4.  **_a person shouldn't give a gift to someone from the same 'room', household or team as his own room mate/team member/partner; and_**
5.  _everyone gets exactly one gift._

As before, the algorithm spits out a permutation of an ordered vector of increasing integers (from 0 to N), and then performs the above 'checks' on this directed graph. Rule 5 is automatically taken care of as the original vector ([0, 1, 2, ..., N]) is permuted without repetition.   
This approach is still less than elegant or computationally efficient, but it is easy to use and doesn't require a whole list of 'forbidden pairs' - a list with names, email addresses and 'team' identifiers suffices.   

I also updated the email script so it now works with Hotmail/Outlook as well as Gmail. I don't think other types of email accounts will be much of a challenge now. 

**Download or pull the source from [this git repository](https://github.com/BrechtDeMan/secretsanta) on [my Github page](https://github.com/BrechtDeMan/). **

<div>
	<div class="github-card" data-user="BrechtDeMan"></div>
	<script src="http://lab.lepture.com/github-cards/widget.js"> </script>
</div>

