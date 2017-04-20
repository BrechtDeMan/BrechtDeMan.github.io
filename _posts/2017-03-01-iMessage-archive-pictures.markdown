---
layout: post
title:  "How to archive pictures and videos from iMessage"
date:   2017-03-01
tags: [developer]
excerpt_separator: <!--more-->
---

*This describes a method for backing up all files from iMessage from a Mac computer with OS X.10.*

As our devices grow ever faster and larger, so do – apparently – our system requirements. This seems to be exceedingly true for my phone and its storage capacity, which fills up incredibly quickly with pictures, videos (!), and podcasts. With my laptop, the underused SD card slot offers an option for hard drive expansion without (impractical) external hard drives or (slow) wireless storage, for [custom made flash storage cards](https://9to5mac.com/2014/05/23/three-hacks-for-adding-permanent-storage-to-your-macbook-air-or-retina-pro-through-the-sd-card-slot/) which don't stick out. Of course, the iPhone doesn't have the option for memory expansion. 

This means there's only one way forward: deleting things. 
To find the main culprit (videos, music, games, maps for GPS navigation, ...), open 'Settings' and go to General > Storage & iCloud Usage > Manage Storage. After some calculating, the primary space-eaters will show up at the top. 

![iPhone storage](/images/blog/2017/02/iPhone-screenshot.png)


For me, iMessage occupied the largest chunk by far, accounting for about half of my constantly full storage space. This is mainly due to sending and receiving pictures and videos. 

The first option is the easiest one: just delete conversations (swipe one left and hit 'Delete'). You will see space become available instantly. 

However, if you are somewhat sentimental about pictures of your loved ones' or your own kids/cats/..., you may want to back up these pictures if not the complete conversations. 
Luckily, if you are also receiving these messages on a Mac, you can go to `~/Library/Messages/` (where `~` is short for your home directory, e.g. `/Users/John/`) and find all conversations and pictures there. You can include this folder in your backup routine and you will never really lose them. 

These 'Attachments' are not stored per conversation, nor are they in chronological order. It is therefore next to impossible to find a particular photo in this structure. I therefore chose to put all of these files in one folder, ordered by date of creation. The following describes how to do this with a simple bash command. 

### TL;DR / n00b
If you just want to run the script, copy this to the Terminal application line by line, ignoring the `$`, and hit enter after each one (provided without any warranty or responsibility):

{% highlight bash %}
$ brew install coreutils
$ cd /Users/John/Library/Messages/Attachments/
$ mkdir /Users/John/Pictures/iMessage/
$ OIFS="$IFS"
$ IFS=$"\n"
$ find . -type f | while read f; do gcp --backup=t "${f}" "/Users/John/Pictures/iMessage/""$(gdate -r "$f" +"%Y%m%d")"-"$(basename $f)"; done
$ IFS="$OIFS"
{% endhighlight %}

Make sure to replace all instances of 'John' with the name of your home folder. If you are not sure about this, type `cd ~` and hit enter in the Terminal, then type `pwd` and hit enter to see the correct path of the form `/Users/[your_name]`. 


### Get the GNU developer tools

As my solution is based on the GNU version of `date` and `cp`, I got the [GNU core](http://www.gnu.org/software/coreutils/coreutils.html) utilities using [Homebrew](https://brew.sh/): 

{% highlight bash %}
$ brew install coreutils
{% endhighlight %}

[These get the prefix 'g'](http://stackoverflow.com/questions/27514652/cp-illegal-option-b-on-mac), e.g. `gcp` and `gdate`. 


### Prepend the date to the file name

For this, we want to adopt the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard or similar, so that alphabetical ordering of the files results in chronological ordering as well. You may also want to add the time of creation. Ideally, the person who sent it (or to whom you sent it) would be part of this file name, but this requires interpreting the conversations themselves which adds a whole new level of complexity. 

Using `gdate` from the Coreutils package, the following command returns the date in YYYYMMDD format, e.g. '20150321'. 
Extra quotation marks around the file name should mitigate issues caused by spaces. 
{% highlight bash %}
$ gdate -r "$FILENAME" +"%Y%m%d"
{% endhighlight %}

### Get file name 

As several files will have the same creation date, I chose to preserve the original file name as well, even though it is usually fairly unsemantic (e.g. 'IMG-4701.jpeg'). The complete file name includes the full path, so in this case we need only the '[basename](http://stackoverflow.com/a/3362952/3193542)':

{% highlight bash %}
$ basename "$FILENAME"
{% endhighlight %}


### Don't overwrite files with the same name

To [preserve all files with identical file names](http://unix.stackexchange.com/questions/16669/copy-files-with-renaming) and the same creation date – though these would typically be the same files – the `--backup` option of gcp can be used. Instead of overwriting a file with the same name, a tilde is added at the end. 

To preserve multiple copies, `--backup=t` appends '.~1~', '.~2~', ... to the file name. 


### Ignore file names with spaces

If some of your files are going to contain spaces (e.g. Mac's terrible 'Screen Shot 2017-02-25 at 18.05.30.png'), looping over the list of files is going to be a bit less than straightforward. 
I'd be keen to learn about more elegant ways, but a quick and effective hack seems to be to [temporarily modify the `IFS` variable](http://stackoverflow.com/questions/7039130/iterate-over-list-of-files-with-spaces) (the Internal Field Separator) to separate the file names by newlines:

{% highlight bash %}
$ OIFS="$IFS" # store to change back later
$ IFS=$"\n"
$ # ... 
$ IFS="$OIFS"
{% endhighlight %}

### Putting it all together

The following bash script copies all files in the current folder `.`, including subdirectories, to the (existing!) `~/Pictures/iMessage/` folder. Note that the originals will still be there, so this is a non-destructive operation. 

{% highlight bash %}
$ OIFS="$IFS"
$ IFS=$"\n"
$ find . -type f | while read f
$ do
$    gcp --backup=t "$f" "/Users/John/Pictures/iMessage/""$(gdate -r "$f" +"%Y%m%d")"-"$(basename $f)"
$ done
$ IFS="$OIFS"
{% endhighlight %}

Or as a oneliner (minus modifying the IFS): 

{% highlight bash %}
$ find . -type f | while read f; do gcp --backup=t "${f}" "/Users/John/Pictures/iMessage/""$(gdate -r "$f" +"%Y%m%d")"-"$(basename $f)"; done
{% endhighlight %}


### Clean up

You can now delete conversations from your phone and/or computer, and empty the Attachments folder. 

Any comments: <a href="mailto:info@brechtdeman.com" target="_self">info@brechtdeman.com</a>.

