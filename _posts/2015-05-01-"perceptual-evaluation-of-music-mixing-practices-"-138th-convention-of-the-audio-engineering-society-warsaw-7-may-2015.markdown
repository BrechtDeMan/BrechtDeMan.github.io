---
layout: post
title: '"Perceptual evaluation of music mixing practices," 138th Convention of the
  Audio Engineering Society, Warsaw, 7 May 2015'
date:   2015-05-01 13:57:01 +0200
categories: mix engineering, research
excerpt_separator: <!--more-->
---

I will present the following paper

> [Brecht De Man](http://brechtdeman.com/), [Matthew Boerum](http://www.mattboerum.com/), [Brett Leonard](http://www.blpaudio.com/), [Richard King](http://www.rkrecording.com/), [George Massenburg](http://www.massenburg.com/) and [Joshua D. Reiss](http://www.eecs.qmul.ac.uk/~josh/), “[Perceptual evaluation of music mixing practices](http://brechtdeman.com/publications.html),” 138th Convention of the Audio Engineering Society, May 2015. 

on Thursday 7 May at 3pm CET in the session _"[P3 - (Lecture) Recording and Production](http://www.aes.org/events/138/papers/?ID=4358)"_ at the upcoming Convention of the Audio Engineering Society, in Warsaw, Poland.   

Abstract:   


> The relation of music production practices to preference is still poorly understood. Due to the highly complex process of mixing music, few studies have been able to reliably investigate mixing engineering, as investigating one process parameter or feature without considering the correlation with other parameters inevitably oversimplifies the problem. In this paper we present an experiment where different mixes of different songs, obtained with a representative set of audio engineering tools, are rated by experienced subjects. The relation between the perceived mix quality and sonic features extracted from the mixes is investigated, and we find that a number of features correlate with quality. 

The paper will be available from the [AES E-Library](http://www.aes.org/e-lib/) from next week onwards.   

Resources can be found here:   

*   raw tracks, mixes, and DAW files (Avid Pro Tools 10) for 6 out of 10 songs in the test can be found here, and will be searchable on the Open Multitrack Testbed;
*   code for the MATLAB-based listening test interface I designed can be found on SoundSoftware;
*   the impulse responses from the [left](http://brechtdeman.com/downloads/Left-01.wav) and [right](http://brechtdeman.com/downloads/Right-01.wav) speaker in the CIRMMT Critical Listening lab (44.1 kHz/24 bit PCM WAV files), with the power spectral density plotted below. 


[![PSD left](/uploads/3/4/4/2/34427003/2171298.png?557)](/uploads/3/4/4/2/34427003/2171298_orig.png?557)

[![PSD right](/uploads/3/4/4/2/34427003/8906241.png?557)](/uploads/3/4/4/2/34427003/8906241_orig.png?557)


Impulse responses recorded and graphs plotted by Brett Leonard, with the MATLAB script below.

{% highlight matlab linenos %}
clear all; close all;
tic;
% make sure you are in the IR folder:
[irL, fs] = audioread('Left-01.wav');
[irR, fs2] = audioread('Right-01.wav');
assert(fs==fs2);

figure(1);
nfft = 2^nextpow2(length(irL));
Pxx = abs(fft(irL,nfft)).^2/length(irL)/fs;

% Create a single-sided spectrum
Hpsd = dspdata.psd(Pxx(1:length(Pxx)/2),'Fs',fs);  
plot(Hpsd); 
ylim([-220 -80]);

figure(2);
nfft = 2^nextpow2(length(irR));
Pxx = abs(fft(irR,nfft)).^2/length(irR)/fs;

% Create a single-sided spectrum
Hpsd = dspdata.psd(Pxx(1:length(Pxx)/2),'Fs',fs);  
plot(Hpsd); 
ylim([-220 -80]);
toc;
{% endhighlight %}

Furthermore, the resampling of the audio from 96 kHz or 88.2 kHz to 44.1 kHz, for feature extraction from a more perceptually relevant range, was done using [SoX](http://sox.sourceforge.net). The performance of SoX can be compared to other resampling algorithms at [src.infinitewave.ca](http://src.infinitewave.ca). 


> HQ batch [#audio](https://twitter.com/hashtag/audio?src=hash) resampling: for i in *.wav; do sox [$i](https://twitter.com/search?q=%24i&src=ctag) -b 24 temp.wav rate -v 48k; done w/ [@TheBaronHimself](https://twitter.com/TheBaronHimself) [#SoX](https://twitter.com/hashtag/SoX?src=hash) [pic.twitter.com/6KfaHBQ0jP](http://t.co/6KfaHBQ0jP)
> 
> — Brecht De Man ([@BrechtDeMan](https://twitter.com/BrechtDeMan)) [February 12, 2015](https://twitter.com/BrechtDeMan/status/566008411897462784)

