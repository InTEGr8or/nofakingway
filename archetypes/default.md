---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
author: {{ .Site.Params.author.name }
featured_image:
draft: true
---
