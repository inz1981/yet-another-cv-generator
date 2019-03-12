## Education
{%- for education in input['education'] %}

### {{ education.institution }}
#### {{ education.area }}, {{ education.studyType }}
{{ education.startDate }} - {{ education.endDate }}

{% for course in education.courses -%}
* {{ course }}
{% endfor %}
{%- endfor -%}