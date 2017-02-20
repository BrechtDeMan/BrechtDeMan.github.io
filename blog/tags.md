---
layout: page
title: Tags
---

<!-- From http://pavdmyt.com/how-to-implement-tags-at-jekyll-website/ -->

<!-- Get the tag name for every tag on the site and set them
to the `site_tags` variable. -->
{% capture site_tags %}{% for tag in site.tags %}{{ tag | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}

<!-- `tag_words` is a sorted array of the tag names. -->
{% assign tag_words = site_tags | split:',' | sort %}

<!-- List of all tags -->
<ul class="tags">
  {% for item in (0..site.tags.size) %}{% unless forloop.last %}
    {% capture this_word %}{{ tag_words[item] }}{% endcapture %}
    <li>
      <a href="#{{ this_word | cgi_escape }}" class="tag" target="_self">{{ this_word }}
        <span>({{ site.tags[this_word].size }})</span>
      </a>
    </li>
  {% endunless %}{% endfor %}
</ul>

<!-- Posts by Tag -->
<div>
  {% for item in (0..site.tags.size) %}{% unless forloop.last %}
    {% capture this_word %}{{ tag_words[item] }}{% endcapture %}
    <h2 id="{{ this_word | cgi_escape }}">{{ this_word }}</h2>
    <table width="100%">
    {% for post in site.tags[this_word] %}{% if post.title != null %}
      <tr>
        <td>
          <span style="float: left; text-align: left;">
            <a href="{{ post.url }}" target="_self">{{ post.title }}</a>
          </span>
        </td>
        <td>
          <span style="float: right; text-align: right; white-space: nowrap;">
            {{ post.date | date_to_string }}
          </span>
        </td>
      </tr>
    {% endif %}{% endfor %}
    </table>
  {% endunless %}{% endfor %}
</div>
