---
layout: post
title:  "Double last names in BibTeX"
date:   2016-08-04 17:46:01 +0200
tags: developer
excerpt_separator: <!--more-->
---

Being cited is great. 

Being cited with your name spelled wrong is... still great (especially when Google Scholar still recognises you), but also kind of annoying as readers may not recognise you or not find your work when searching online. Instead of singling out some of the excellent researchers who have been polite enough to acknowledge my work, here's a quick tip of how to avoid a common citation gaffe. 

<!--more-->

![Picture](/images/blog/2016/08/citation-blurred.png)

I have a double last name - or rather, my name is in two parts: 'De' ('The') and 'Man' ('Man'). 
True double last names are quite common in Spanish-speaking countries, e.g. 'Sánchez Álvarez'. 
When you are using BibTeX to manage your references, you may be tempted to write something like this: 

{% highlight bibtex %}
@conference{deman2014a,
	Author = {Brecht De Man and Joshua D. Reiss},
	Booktitle = {53rd Conference of the Audio Engineering Society},
	Month = {January},
	Title = {Adaptive Control of Amplitude Distortion Effects},
	Year = {2014}}
{% endhighlight %}

What happens then is that BibTeX, or rather the typical citation styles in LateX, assume that only the last part of the name is a surname, and everything else is first names. As a consequence, I become 'B. D. Man', and the fictional Dr Elena Sánchez Álvarez becomes 'E. S. Álvarez'. (Surnames of the 'de ...' variety are apparently recognised properly.)

However, if you write the names as `surnames, first names`, e.g. 

{% highlight bibtex %}
	Author = {De Man, Brecht and Reiss, Joshua D.},
{% endhighlight %}

there is never this ambiguity. You can also mix and match, e.g. 

{% highlight bibtex %}
	Author = {De Man, Brecht and Joshua D. Reiss},
{% endhighlight %}

whenever there is a potentially problematic name, and it will work fine. 

That is all - please carry on citing my work. 

