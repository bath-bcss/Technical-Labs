---
layout: default
title: "2021 lectures"
permalink: "/notes/2021/"
---

# 2021 Notes

These are the notes for 2020:

{% assign sorted = site.notes2021 | sort: 'date' %}
{% for doc in sorted %}
1. [{{ doc.title }}]({{ doc.url }})
{% endfor %}
