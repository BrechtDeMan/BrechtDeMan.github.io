---
layout: post
title:  "Clickable URLs as footnotes in LaTeX"
date:   2017-02-19 17:37:24 +0200
tags: [developer, LaTeX]
excerpt_separator: <!--more-->
---

I often like to link to software packages or websites in scientific papers, and prefer URLs in PDFs to be clickable. You can do this quite easily in LaTeX: 

{% highlight latex %}
Check out my website\footnote{\url{http://www.brechtdeman.com}}. 
{% endhighlight %}

(This requires the [hyperref](https://www.ctan.org/pkg/hyperref?lang=en) package.)

However, this has the ugly 'http://' or 'https://' prefix everywhere in the URLs which is decidedly less neat. You could drop it but come on, that's just bad practice. 

I also thought it would be nice if the relevant part of the text would already be clickable (e.g. 'We published a [browser-based listening test framework](https://github.com/BrechtDeMan/WebAudioEvaluationTool)<sup>1</sup>.')

Sure enough, you can do this too:

{% highlight latex %}
Check out \href{http://www.brechtdeman.com}{my website}
\footnote{\href {http://www.brechtdeman.com}{www.brechtdeman.com}}. 
{% endhighlight %}

Of course, this becomes very long, so I made the following macro and have been using it everywhere since a year or so. 

<!--more-->

{% highlight latex %}
% Make clickable footnote
\newcommand{\hyperfootnote}[1][]{\def\ArgI{{#1}}\hyperfootnoteRelay}
% relay to new command to make extra optional command possible
\newcommand\hyperfootnoteRelay[2][]{\href{#1#2}{\ArgI}\footnote{\href{#1#2}{#2}}}
% the first optional argument is now in \ArgI, the second is in #1
{% endhighlight %}

Then use as follows (still requiring the [hyperref](https://www.ctan.org/pkg/hyperref?lang=en) package):

### 1. Simple (no arguments)

{% highlight latex %}
\hyperfootnote{http://www.mywebsite.com}
{% endhighlight %}

This creates a footnote consisting of a clickable URL. 

### 2. Link text (1 argument)
{% highlight latex %}
\hyperfootnote[My website]{http://www.mywebsite.com}
{% endhighlight %}

This creates a clickable piece of text in the text ('My website') plus a footnote consisting of a clickable URL. 

### 3. Link text and invisible prefix (2 arguments)
{% highlight latex %}
\hyperfootnote[My website][http://]{www.mywebsite.com}
{% endhighlight %}

This creates a clickable piece of text in the text ('My website') plus a footnote consisting of a clickable URL without the prefix (in this case 'http://'). Upon clicking it, however, you are directed to the full link, i.e. 'http://www.mywebsite.com'. 

<br>

This 'minimal working example' consisting of a [LaTeX](/images/blog/2017/02/hyperfootnoteMWE.tex) and a [PDF](/images/blog/2017/02/hyperfootnoteMWE.pdf) file further illustrates the concept. 

You can use the [xspace](https://www.ctan.org/pkg/xspace?lang=en) package to add/absorb spaces when necessary, e.g. to avoid a space between the footnote number and a punctuation mark.
