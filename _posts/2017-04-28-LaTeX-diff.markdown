---
layout: post
title:  "Show changes in modular LaTeX document"
date:   2017-04-28
tags: [LaTeX, developer]
excerpt_separator: <!--more-->
---

This is my process to highlight changes in a document written in LaTeX, for instance for the minor thesis corrections recommended by my examiners, or any edits you wish to show to a supervisor or collaborator. 
It's somewhat similar to 'track changes' functionality in Microsoft Word or Google Docs, and can be done after the fact, between any two versions of a document. 

<!--more-->

### Flatten documents

If the document's structure is modular (which I highly recommend), including or inputting parts, chapters, or sections, you will need to 'flatten' the document, i.e. merge all parts into one big .tex file. 

First, go to the old version of the document on source control (you do use source control, right?). There, run [this Perl script](http://ctan.triasinformatica.nl/support/latexpand/latexpand) ([other, similar tools exist](https://tex.stackexchange.com/questions/21838/replace-inputfilex-by-the-content-of-filex-automatically)) on the root document as follows:

{% highlight bash %}
perl latexpand.pl Thesis.tex > Thesis-old-flat.tex
{% endhighlight %}

To be sure, compile the newly created document to see if it is identical to the original. 

Store this document in a place where it will not be affected by going 'back to the future' of your revision history. 

Then, do the exact same thing with the new version of the document you wish to compare with the old one:

{% highlight shell %}
perl latexpand.pl Thesis.tex > Thesis-new-flat.tex
{% endhighlight %}

### Diff

Now, put the two flattened documents in the same folder – probably the main folder your document lives in, so that figures and bibliography can be found. 

Then, [get latexdiff](https://www.sharelatex.com/blog/2013/02/16/using-latexdiff-for-marking-changes-to-tex-documents.html) and run it on both documents: 

{% highlight shell %}
latexdiff Thesis-old-flat.tex Thesis-new-flat.tex > Thesis-diff.tex
{% endhighlight %}

The resulting file can be compiled like you would compile any LaTeX file, and will show deleted bits in red and struck through, and additions in blue with a squiggly line underneath – see below. 

![latexdiff output](/images/blog/2017/04/latexdiff.png)

Note that if you are including external .bib, .pdf, .jpeg, ... files, changes to these will not be highlighted! Only when including different figures with different names, or in different places, they will be highlighted as a change. 

Another caveat is that the deleted portions will take up space so that the layout and number of pages may well be different from the updated document. 

That's it! 
