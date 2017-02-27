---
layout: post
title:  "Paper in the Journal of the Audio Engineering Society"
date:   2017-02-27
tags: [research, mix engineering]
excerpt_separator: <!--more-->
---

[Brecht De Man](/), [Kirk McNally](http://www.stereosonic.org/phd/cv.html) and [Joshua D. Reiss](http://www.eecs.qmul.ac.uk/~josh/), “[Perceptual Evaluation and Analysis of Reverberation in Multitrack Music Production](http://www.aes.org/e-lib/browse.cfm?elib=18548),” Journal of the Audio Engineering Society, Vol. 65 (1/2), pp. 108-116, January/February 2017\. 
[[pdf](/publications/pdf/jaes-DREAMS-hires.pdf) &#124; [BibTeX](/publications/BibTeX-txt/jaes-dreams.txt)]

* * * 

<br>

It is with great pleasure that I present a writeup of my latest research project on the perception of reverb in music production, which appeared in [this month's issue of the Journal of the Audio Engineering Society](http://www.aes.org/journal/online/JAES_V65/1_2/). 
A tip of the veil was lifted at last year's [60th International AES Conference on Dereverberation and Reverberation of Audio, Music, and Speech](http://www.aes.org/conferences/60/) (yes, DREAMS) in Leuven, Belgium, where I presented a poster on preliminary work in this area and was invited to give a [tutorial on artificial reverberation in music production](http://www.brechtdeman.com/blog/aes60-dreams-conference.html). Speakers at this conference were encouraged to submit their extended work to this special issue of the JAES, to which anyone could contribute. 

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Automatic mix diagnostics: a thing of the future? Find out this Thursday &amp; Friday at the <a href="https://twitter.com/AESorg">@AESorg</a> <a href="https://twitter.com/hashtag/AES60?src=hash">#AES60</a> conference! <a href="https://t.co/idXdXr9KiV">pic.twitter.com/idXdXr9KiV</a></p>&mdash; Brecht De Man (@BrechtDeMan) <a href="https://twitter.com/BrechtDeMan/status/694608488576765952">February 2, 2016</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

*Announcement of my 2016 lecture which somehow went viral*

This work, which started mid-2015 and saw its final paper review in October 2016, was also an important component of the PhD dissertation I submitted last month. In a way, the whole thesis came together in this project, which proved the concept of understanding a mix process and its impact on perception based on quantitative analysis and subjective evaluation of a corpus of mixes. 

The article is Open Access, which means anyone can read it, even without membership of the Audio Engineering Society (in my opinion there are many other reasons to become an AES member, one of which is unlimited access to the complete AES library). 
It is also published under a [Creative Commons 'CC BY' license](https://creativecommons.org/licenses/by/4.0/), meaning you can do whatever you want with it such as reusing exact or modified excerpts from the paper, including figures, as long as you credit the authors. 

<!--more-->

### Summary

In this work, which builds on data accumulated in previous studies [<a href="#ref1" target="_self">1</a>–<a href="#ref3" target="_self">3</a>], we explore the possibility of reliably measuring the percept 'total amount of reverberation' using objective metrics. To this end, several mixes produced in [<a href="#ref1" target="_self">1</a>] are analysed by extracting their reverb signal and the remaining, 'dry' signal. Perceptual evaluation data in the form of preference ratings and, in particular, comments describing and comparing different mixes of the same songs are used to determine the proportion of listeners who perceive each mix as 'too reverberant' or 'not reverberant enough'. 
As such, we were able to study the application of reverberation in a realistic music production environment, contrasting with earlier studies on the topic which focussed on a certain aspect of use or perception of reverberation in a laboratory setting. 

From the average preference rating of the predominantly 'too reverberant' and 'not reverberant enough' mixes, and those which weren't classified as either, a lower preference was noted for those which were too reverberant, but such tendency was not apparent for overly 'dry' mixes. This confirmed some earlier studies on this topic. 
The comments themselves illustrated how important reverberation is for the subjective impression of a mix, as over 35% of the comments mention reverberation. Furthermore, agreement with regard to the amount of reverberation is high: only 4 of the 525 comments disagree with another comment about this aspect. 

The first audio feature we assess as a predictor for perceived reverberation amount is 'relative reverb loudness', defined as the loudness of the total reverberation signal relative to the loudness of the complete mix. This correlates quite well with the subjects' perception of which mixes have too much or too little reverb, and –14 LU appears to be a good middle ground, providing an estimate of a generic 'optimal reverb loudness'. 

For some mixes, the subjective impression of reverb amount did not correspond with the reverb loudness measure. Upon closer inspection, 'long' reverbs are also likely to be perceived as an excess of reverberant energy, while loud but 'short' reverbs still sound 'dry'. To quantify this, we developed a measure of reverberation time for a multitrack mix. Reverberation time is quite readily measured from a reverberation impulse response, but in the case of multitrack music production, different reverb effects are applied to various degrees to different sources. To this end, we developed an Equivalent Impulse Response, which captures the temporal characteristics of the combined reverberation, from which the traditional acoustic measures can then be derived. This helped explain some of the remaining variance, further improving the model fit. 

We were also pleasantly surprised to see relatively small variation in the findings overall, compared to previous, more controlled studies. We believe this can be attributed to the high level of expertise of the subjects involved in the study, all of whom were highly trained sound engineers. 
Forthcoming work will look at the level of agreement of less experienced listeners, when comparing differing mixes. 

In the interest of reproduction and extension of the work, raw tracks, mixes, and reverb stems are shared on the [Open Multitrack Testbed](http://multitrack.eecs.qmul.ac.uk). 
An [example test](http://webprojects.eecs.qmul.ac.uk/bdm30/mixevaluation/test.html?url=CC.xml) not unlike the perceptual evaluation experiment in the paper is available too.

<br>

PS: Kudos to the [DREAMS project](http://www.dreams-itn.eu) for using the Oxford comma in 'Dereverberation and Reverberation of Audio, Music, and Speech'. 

* * *

<br>

<span id="ref1">[1]</span> [Brecht De Man](/), [Brett Leonard](http://www.blpaudio.com), [Richard King](http://www.rkrecording.com) and [Joshua D. Reiss](http://www.eecs.qmul.ac.uk/~josh/), “[An analysis and evaluation of audio features for multitrack music mixtures](http://www.terasoft.com.tw/conf/ismir2014/proceedings/T025_293_Paper.pdf),” 15th International Society for Music Information Retrieval Conference (ISMIR 2014), October 2014\. 

[2] [Brecht De Man](/), [Matthew Boerum](http://www.mattboerum.com/), [Brett Leonard](http://www.blpaudio.com/), [Richard King](http://www.rkrecording.com/), [George Massenburg](http://www.massenburg.com/) and [Joshua D. Reiss](http://www.eecs.qmul.ac.uk/~josh/), “[Perceptual evaluation of music mixing practices](http://www.aes.org/e-lib/browse.cfm?elib=17659),” 138th Convention of the Audio Engineering Society, May 2015\. 

<span id="ref3">[3]</span> [Brecht De Man](/) and [Joshua D. Reiss](http://www.eecs.qmul.ac.uk/~josh/), “[Analysis of peer reviews in music production](http://arpjournal.com/analysis-of-peer-reviews-in-music-production/),” Journal on the Art of Record Production, Vol. 10, July 2015\.
