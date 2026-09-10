---
layout: page
title: Search
permalink: /search/
description: Search Trevor Kems' technical articles and project archive.
---
<div id="search-container">
  <label for="search-input">Search articles by title or topic</label>
  <input type="search" id="search-input" placeholder="Try firmware, IoT, or hardware…" autocomplete="off">
  <ul id="results-container" aria-live="polite"></ul>
</div>
<noscript><p>Search requires JavaScript. You can also <a href="{{ '/categories/' | relative_url }}">browse by category</a> or visit the <a href="{{ '/blog/' | relative_url }}">blog archive</a>.</p></noscript>
<script src="{{ '/assets/simple-jekyll-search.min.js' | relative_url }}"></script>
<script>
SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: document.getElementById('results-container'),
  searchResultTemplate: '<li><h2><a href="{url}">{title}</a></h2><span class="meta">{date}</span></li>',
  json: '{{ "/search.json" | relative_url }}'
});
</script>