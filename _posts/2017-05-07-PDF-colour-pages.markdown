---
layout: post
title:  "Counting and reducing colour pages in PDF documents"
date:   2017-05-07
tags: [LaTeX, developer]
excerpt_separator: <!--more-->
---

![Mac OS X Terminal screenshot](/images/blog/2017/05/grayscale-cli.png)

When having documents printed by a professional printer, costs per page tend to be higher for pages including colour than for pages which are grayscale or black-and-white (five times higher in my recent experience). This is fair enough and unavoidable, though if the colour pages are counted and selected automatically, you may pay for more colour pages than you anticipated. The reason for this is that pages which look grayscale or black-and-white, particularly those with figures, may be coded and recognised as colour. 

The following details my approach to counting and finding all 'colour' pages, and ensuring pages which really should be grayscale are detected as such. 
It requires [Ghostscript](https://ghostscript.com) (gs) and should work in the command line interfaces of Mac and *nix systems. 


### Counting and finding colour pages

Some online print services or copy shops require you to specify the number of colour and black-and-white or grayscale pages yourself, so then the following will save you some time or confirm your manual counting. 

{% highlight bash %}
$ gs -o - -sDEVICE=inkcov Thesis.pdf | grep -v "^ 0.00000  0.00000  0.00000" | grep "^ " | wc -l
{% endhighlight %}

To merely find the colour pages, go through the full output (or write a script that tells you the corresponding page numbers):

{% highlight bash %}
$ gs -o - -sDEVICE=inkcov Thesis.pdf
{% endhighlight %}

which gives you an output similar to 

{% highlight bash %}
GPL Ghostscript 9.16 (2015-03-30)
Copyright (C) 2015 Artifex Software, Inc.  All rights reserved.
Processing pages 1 through 211.
Page 1
 0.00000  0.00000  0.00000  0.01082 CMYK OK
Page 2
 0.15453  0.15882  0.34933  0.07392 CMYK OK
Page 3
 0.00000  0.00000  0.00000  0.03928 CMYK OK
...
{% endhighlight %}

in a case where the second page contains colour. It shows the relative 'ink coverage' of all colours, in this case of cyan, magenta, yellow, and black (CMYK).


### Converting to grayscale

When a page in a document, or a figure embedded in this page, looks grayscale but is identified as a colour page, the page or figure should be converted to a different colourmap. 


{% highlight bash %}
$ gs -sDEVICE=pdfwrite -dProcessColorModel=/DeviceGray -dColorConversionStrategy=/Gray -dPDFUseOldCMS=false -o output-grayscale.pdf -f input-colour.pdf 
{% endhighlight %}

Make sure the input and output name aren't the same, or you get a blank document. 

I have also tried to save a PDF in Mac OS X's preview, with a Black & White or Gray Tone Quartz Filter, but this didn't do the trick for me. The above works like a charm though. 

Using [ImageMagick](http://imagemagick.org/script/index.php), the result gets rasterised and of very poor quality if you zoom in a bit. (Almost sent it off like this!) 
However, for changing the colour map of raster images the following works fine:

{% highlight bash %}
$ convert -colorspace gray img/input-colour.jpeg img/output-grayscale.jpeg
{% endhighlight %}

Here, a different output file name is not necessary: the file can be edited in-place. 

* * *
<br>
After successfully converting pages or figures within a document, the aforementioned colour page counting method should return a lower number, saving you some unnecessary colour printing costs. 

### Sources

* [Super User - Count BW / color pages in PDF](https://superuser.com/questions/234408/count-bw-color-pages-in-pdf) 
* [Stack Overflow - How to convert a PDF to grayscale from command line avoiding to be rasterized?](http://stackoverflow.com/questions/20128656/how-to-convert-a-pdf-to-grayscale-from-command-line-avoiding-to-be-rasterized)
