========================
{{project_name}}
========================

{{project_name}} moves to Django (about time!)


Installation of Dependencies
============================

First, make sure you are using virtualenv (http://www.virtualenv.org)::

    $ mkvirtualenv --distribute {{project_name}}

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to be able to change settings using the `--settings` flag.

In Linux and Mac OSX, you can install virtualenvwrapper (http://http://virtualenvwrapper.readthedocs.org/en/latest/), which will take care of adding the project path to the `site-directory` for you::

    $ cd {{project_name}} && add2virtualenv `pwd`

Virtualenvwrapper takes care of this for you by creating the exact same file
using the `add2virtualenv` command (see above).

Then, depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt
    $ npm install
    $ npm watch

For production::

    $ pip install -r requirements/prod.txt
    $ npm install
    $ npm run-script prod

*note: We install production requirements this way because many Platforms as a Services expect a requirements.txt file in the root of projects.*


Acknowledgements
================

    - Many thanks to our Dear Lord Krishna, who has given me the intelligence to get this far!
    - And of course many thanks to my Guru Maharaja who has inspired me to bring this site to life!
    - and all the contributors_

.. _contributors: https://gitlab.com/{{user}}/{{project_name}}/blob/master/CONTRIBUTORS.txt
