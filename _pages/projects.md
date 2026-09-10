---
layout: page
title: Projects
permalink: /projects/
description: Security tools, ADCS labs, Wireshark dissectors, RF experiments, and competition projects by Trevor Kems.
eyebrow: Tools / Labs / Hardware
intro: Practical tools for investigating systems, reproducing security problems, and learning by building.
wide: true
---
<div class="project-grid">
{% for project in site.data.projects %}
<article class="project-card">
  <p class="eyebrow">{{ project.type }}</p>
  <h2>{{ project.title }}</h2>
  <p>{{ project.description }}</p>
  <ul class="tags" aria-label="Project topics">{% for tag in project.tags %}<li>{{ tag }}</li>{% endfor %}</ul>
  <a href="{{ project.url }}">View source <span aria-hidden="true">&rarr;</span></a>
</article>
{% endfor %}
</div>

<section class="section archive-section" aria-labelledby="archive-heading">
  <p class="eyebrow">Earlier projects / Archive</p>
  <h2 id="archive-heading">From the student workbench.</h2>
  <p>Earlier hardware and software projects that helped build the foundation for my security work.</p>
  <ul class="archive-list">
    <li><a href="{{ '/seniordesign/' | relative_url }}">IoT device for the Cyber Defense Competition</a><span>Senior design · Vulnerable devices, firmware, and lab environments</span></li>
    <li><a href="{{ '/cpre-186/' | relative_url }}">CPR E 186: LEDs and Sound</a><span>Arduino, custom PCB design, and music-reactive lighting</span></li>
    <li><a href="{{ '/coms-309/' | relative_url }}">COM S 309: Multiplayer Game with Phone Integration</a><span>Android integration, backend game logic, and database design</span></li>
  </ul>
  <p>The <a href="{{ '/research/#movienite' | relative_url }}">DLink Movienite investigation</a> and other hardware writeups are collected in Research.</p>
</section>