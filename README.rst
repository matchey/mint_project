
=====
Touroku
=====

Touroku is a simple Django app to set Web-based dict-lib. Visitors can add a function name.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "touroku" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'touroku',
    ]

2. Include the touroku URLconf in your project urls.py like this::

    url(r'^touroku', include('touroku.urls')),

3. Run `python manage.py migrate` to create the touroku models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a touroku (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/touroku to participate in the touroku.
