## Work Experience
{%- for workplace in input['work'] %}

### {{ workplace.company }} - {{ workplace.position }}
#### {{ workplace.startDate }} - {{ workplace.endDate }}

{{ workplace.summary }}
{% for highlight in workplace.highlights %}
* {{ highlight }}
{%- endfor -%}
{% endfor %}