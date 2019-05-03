---
layout: default
permalink: /archive/
---

<div class="listing">
   {% for post in site.posts %}
   <div class="post">
      <p class="date">{{ post.date | date: "%Y-%m-%d" }}</p>
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <p class="post-summary">{{ post.excerpt }}</p>
   </div>
   <hr>
   {% endfor %}
</div>
