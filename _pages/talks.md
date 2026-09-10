---
layout: page
title: Talks
permalink: /talks/
description: Trevor Kems on ADCS security, IoT vulnerabilities, RF protocols, RFID, and hardware reverse engineering at Splunk .conf, SecDSM, and community events.
eyebrow: Speaking / Technical community
intro: Sharing the process behind the findings, with practical details people can take back to their own work.
wide: true
---
<p><a href="https://www.youtube.com/playlist?list=PLhTiWSKaxggd48yvhqjFNGWVARPqkE2Rb">Watch the talks playlist &rarr;</a></p>
<section class="section" aria-labelledby="featured-talks"><h2 id="featured-talks">Featured presentations</h2>
{% for talk in site.data.talks %}{% if talk.featured %}{% include talk.html talk=talk %}{% endif %}{% endfor %}
</section>
<section class="section" aria-labelledby="community-talks"><h2 id="community-talks">Community &amp; earlier talks</h2>
{% for talk in site.data.talks %}{% unless talk.featured %}{% include talk.html talk=talk %}{% endunless %}{% endfor %}
</section>
<p class="fine-print">Opinions on this site and at events not sponsored by my employer are my own, and do not represent current or former employers.</p>