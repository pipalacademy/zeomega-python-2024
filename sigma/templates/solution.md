# {{title}}

Solutions to {{title}}.

{% for problem in problems %}
## {{ problem.title }}

{{problem.get_description()}}

### Solution {.unnumbered}

```python
{{ problem.get_solution() }}
```

{% set discussion = problem.get_discussion() %}

{% if discussion %}

### Discussion {.unnumbered }

{{ discussion }}

{% endif %}

{% endfor %}
