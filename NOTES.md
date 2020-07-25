# Known issues
- form can be NAV back and reposted - there is no resubmission prevention now

check if form is valid firs....
- https://sixfeetup.com/blog/django-form-data-in-post

# TODO:
- session key
- failed post reloads values?
- dynamic include templates https://stackoverflow.com/a/12669962/140618

```
{% if foo.paid %}
    {% with template_name=foo.id|stringformat:"s"|add:".html" %}
        {% include "foo/customization/"|add:template_name %}
    {% endwith %}
{% endif %}
```

# DONE:
use hidden fields for the meta-data about the survey response posting
post and persist as JSON using https://medium.com/@philamersune/using-postgresql-jsonfield-in-sqlite-95ad4ad2e5f1

https://paltman.com/how-to-store-arbitrary-data-in-a-django-model/
https://github.com/PythonExpert/simple-json-text-field

# Ideas
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page


## Data Models

http://www.erdiagrams.com/datamodel-survey-idef1x.html

https://my.vertabelo.com/model/we3KCfe3paun8lDzz8v5B0mEY6X39WkL

https://stackoverflow.com/questions/1651849/survey-data-model


# Admin stie
## Inline Forms

https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin

https://stackoverflow.com/questions/47258289/differences-between-stacked-inline-and-tabular-inline


https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views

https://swapps.com/blog/working-with-nested-forms-with-django/



