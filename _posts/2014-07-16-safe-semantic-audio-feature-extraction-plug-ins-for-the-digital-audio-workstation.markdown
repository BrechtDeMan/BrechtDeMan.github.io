---
layout: post
title:  'SAFE: Semantic Audio Feature Extraction plug-ins for the digital audio workstation'
date:   2014-07-16 13:57:01 +0200
tags: [mix engineering, research]
excerpt_separator: <!--more-->
---

**EDIT 11 September 2014:** _Our work was featured in [this BBC article](http://www.bbc.co.uk/news/science-environment-29146655), following a press conference at the British Science Festival. _  

For the last 7 months, I have been involved in an exciting, [EPSRC](http://www.epsrc.ac.uk)-funded project, part of the [Semantic Media](http://semanticmedia.org.uk) project. In this project, we aim to overcome the lack of transferable semantic descriptors in music production, and meet the requirement for more intuitive control of audio effects to provide easier access to music technology, by evaluating large amount of labelled data taken from within the digital audio workstation. We will propose a model for the estimation of perceptually accurate descriptors based on a large corpus of annotated music production data.   

One of the main outcomes is a suite of audio effects that you can [download here](http://www.ryanstables.co.uk/SAFE/site/wordpress/?page_id=27). They are normal, powerful music production tools, but they also allow you to describe how you used them to affect the sound (i.e. 'bright' if you used an EQ to brighten up a guitar), along with extracted audio features and information about yourself and the track. All this data is then collected via a server.   
It also works the other way around though: if you want to achieve a certain effect, let's say to make a kick drum 'punchier', you can enter 'punchy', let the effect listen to a short fragment of your kick drum audio, and it will load parameter settings based on what others have called 'punchy' or 'punch' before on similar sounding audio and/or on (kick) drums. This will of course work better and better over time (when more and more accurate descriptor-parameters-audio triplets are added, and when the algorithms to process them become smarter) - which is why we need as many people as possible to download the plug-ins and add labels!   

![Workflow](/images/blog/2014/06/safe-workflow.png)

**FIGURE 1:** Semantic plug-ins workflow


My personal contribution has primarily been writing the audio processing part of the compressor, EQ and overdrive plugins. (The reverb plug-in is based on [MVerb](http://www.kvraudio.com/product/mverb-by-martin-eastwood-audio).) You can see the compressor interface below:  


![SAFE Compressor](/images/blog/2014/06/safe-compressor.png)

**FIGURE 2:** The dynamic range compressor interface. The text box on the right allows you to assign a sonic descriptor ('punchy', 'fuzzy', 'warm') to the effect, or to automatically set the parameter settings based on your desired semantic term.

At the next [International Society for Music Information Retrieval conference](http://ismir2014.ismir.net) in Taipei, Taiwan, I will be presenting a demo of this project (as well as a paper on analysis of eight songs times eight different mixes, and how parameter settings and audio features vary for different songs, mixing engineers, and instruments!).   
ISMIR papers are attributed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), so I should be able to share the work once the conference has taken place (27-31  October).   

For more information, please see the [project website](http://www.semanticaudio.co.uk).   
You can also visit the [Centre for Digital Music](http://c4dm.eecs.qmul.ac.uk) (Queen Mary University of London) and [Digital Media Technology Lab](http://www.bcu.ac.uk/tee/research/digital-technology) (Birmingham City University) pages, for more information on the collaborating research groups. 