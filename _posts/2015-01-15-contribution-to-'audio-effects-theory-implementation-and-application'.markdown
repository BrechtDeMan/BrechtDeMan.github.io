---
layout: post
title: 'Contribution to ''Audio Effects: Theory, Implementation and Application'''
date:   2015-01-15 13:57:01 +0200
tags: [research, developer]
excerpt_separator: <!--more-->
---

I'm very excited to report that I have had the opportunity to contribute to a great and comprehensive book on audio effects, '[Audio Effects: Theory, Implementation and Application](http://www.amazon.co.uk/Audio-Effects-Theory-Implementation-Application/dp/1466560282/ref=sr_1_1?s=books&ie=UTF8&qid=1421343120&sr=1-1)' by Joshua D. Reiss and Andrew P. McPherson. I have contributed to the code that goes with it (some revisions, some implementations from scratch) which are AU/[VST](http://www.steinberg.net/en/company/developers.html) plugins created with the [JUCE](http://www.juce.com) framework, and was cited for my work on an [adaptive amplitude distortion effect](http://brechtdeman.com/downloads/aes53.pdf).   

![Book cover](/images/blog/2015/01/book-cover.jpg)

[Josh](http://www.eecs.qmul.ac.uk/~josh/) is my PhD supervisor and, among many other things, an expert on audio engineering and musical signal processing.   
As a Reader at [Queen Mary University of London'](http://www.qmul.ac.uk)s [Centre for Digital Music](http://c4dm.eecs.qmul.ac.uk), he teaches the course Digital Audio Effects (or in short DAFx), of which I will be teaching assistant (TA) for the second year in a row this spring semester. This new book is partly based on the syllabus of this course, and will now replace it. The labs - which I will run - involve analysing and designing digital audio effects, again as VST plugins using [JUCE](http://www.juce.com). 

<!--more-->

[Andrew](http://www.eecs.qmul.ac.uk/~andrewm/) is a senior lecturer, also at [C4DM](http://c4dm.eecs.qmul.ac.uk), where he leads the [Augmented Instruments group](http://www.eecs.qmul.ac.uk/~andrewm/). Known for projects such as the [Magnetic Resonator Piano](http://www.eecs.qmul.ac.uk/~andrewm/research.html#mrp) (MRP), [TouchKeys](http://www.eecs.qmul.ac.uk/~andrewm/research.html#touchkeys) and [Hackable Instruments](http://www.eecs.qmul.ac.uk/~andrewm/research.html#hackable), he also consulted on hardware design for [ROLI](https://www.roli.com)'s [Seaboard](https://www.roli.com/seaboard/) (not surprising if you look at the MRP and TouchKeys). Evidently he is also a DSP wizard, having taught Real-Time DSP and Digital Audio Effects at our university, among others. A slightly more comprehensive list of the many hats Andrew wears can be found on his group's [website](http://www.eecs.qmul.ac.uk/~andrewm/). 

Having spent a considerable part of my PhD, my internship at [Mixgenius](http://mixgenius.com) in Montréal, and many weekends developing audio plugins, I have often used and modified some of the simple audio plugins at a local repository that eventually became the set of plugins that come with this book. For this reason I was asked to update the plugins, for example to work with a more recent version of the continually updated [JUCE](http://www.juce.com) (now owned by [ROLI](https://www.roli.com), showing how small the world of audio and music technology is) and will probably continue to do so, being one of the developers of the repository from which an up-to-date version of the code can be downloaded.   

I created the distortion plugin, a very simple and generic amplitude distortion implementation, which allows switching between a number of 'input-output curves', thus creating more distortion as the input gain (its only knob) is increased. A variation of my code can be found in the book on page 183 as well.   

The characteristic curves correspond largely with those in the book, and are based on a previous project where I also implemented various amplitude distortion curves, but where rather than manipulating the gain, I 'shrunk' or 'expanded' the characteristic input-output curve to avoid overly large level differences (another weekend project that got out of hand). More importantly, the point of this particular implementation was to guarantee a consistent amount of distortion for any level of the incoming signal (e.g. a drop in guitar level would not result in any change in distortion level, whereas with conventional distortion implementations, a hotter input level means more distortion). In order for the output level to be proportional in level to the input level, there could be no variable gain stage to change the distortion, but rather the distortion curve had to be scaled.   
The independence of distortion amount from input level was confirmed in a listening test.   
The paper associated with this implementation can be found here:  

[Brecht De Man](/) and [Joshua D. Reiss](http://www.eecs.qmul.ac.uk/~josh/), “[Adaptive control of amplitude distortion effects](http://www.aes.org/e-lib/browse.cfm?elib=17118),” 53rd Conference of the Audio Engineering Society, January 2014\. [[pdf](http://www.eecs.qmul.ac.uk/~josh/documents/DeMan%20Reiss%20-%20AES53.pdf) &#124; [BibTeX](/publications/BibTeX-txt/aes53.txt) &#124; [poster](/publications/posters/aes53poster.pdf)]	

or in the [Publications](/publications.html) section on this website.   


![Citation](/images/blog/2015/01/citation.jpg)


The video below shows a VST plugin implementation in action (the plugin was designed with help from the team at Mixgenius, in particular Stuart Mansbridge who comes from C4DM as well).   

<iframe src="http://www.youtube.com/embed/BK-Cd_cNc0E?wmode=opaque" frameborder="0" allowfullscreen=""></iframe>


I have also created my own C++ class which takes care of anti-aliasing, as I have found the built-in JUCE/VST class as well as other implementations a bit awkward to use and needlessly complicated (in this case I'm quite happy with upsampling by an integer factor, which is easier in concept than with arbitrary upsampling ratios).   

![Acknowledgement](/images/blog/2015/01/acknowledgement.jpg)


Congratulations Andrew and Josh on a great book, and thanks for your acknowledgement and letting me be a part of it!


> Honoured to be acknowledged and cited in 'Audio Effects' by [@c4dm](https://twitter.com/c4dm)'s [@InstrumentsLab](https://twitter.com/InstrumentsLab) and Josh Reiss! [@QMUL](https://twitter.com/QMUL) [@QMEECS](https://twitter.com/QMEECS) [pic.twitter.com/Da6s7TiumY](http://t.co/Da6s7TiumY)
> 
> — Brecht De Man ([@BrechtDeMan](https://twitter.com/BrechtDeMan)) [January 15, 2015](https://twitter.com/BrechtDeMan/status/555780077645201409)


I'd also like to thank [ROLI](https://www.roli.com)/[JUCE](http://www.juce.com) for creating such great tools (at no cost for academic and GNU licensed use by the way), and [praising](https://twitter.com/WeAreROLI/status/544132601800564736) my work with [Simon-Claudius Wystrach](http://simonclaudius.com) at the last [Music Hack Day in London](https://www.hackerleague.org/hackathons/music-hack-day-london-2014).   
We have used JUCE for our latest two hacks, which you can read about [here](https://www.hackerleague.org/hackathons/music-hack-day-london-2014/hacks/passivist) and [here](http://labrosa.ee.columbia.edu/hamr_ismir2014/proceedings/doku.php?id=intelligent_audio_switch_box). For the latter, we received the 'Best Code' award. 

