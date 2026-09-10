---
layout: page
permalink: /categories/
title: Categories
description: Browse Trevor Kems' technical posts by research topic and project category.
---
<div id="archives">
{% assign category_names = site.posts | map: 'categories' | join: '|' | split: '|' | uniq | sort %}
{% for category_name in category_names %}
  <section class="archive-group" id="{{ category_name | slugify }}">
    <h2>{{ category_name }}</h2>
    <ul>{% for post in site.posts %}{% assign post_categories = post.categories | join: '|' | split: '|' %}{% if post_categories contains category_name %}<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>{% endif %}{% endfor %}</ul>
  </section>
{% endfor %}
</div>
