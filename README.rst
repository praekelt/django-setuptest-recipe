Django Setuptest Recipe
=======================
**Recipe to prevent django-setuptest from polluting module being tested with
downloaded eggs.**

.. contents:: Contents
    :depth: 5

Motivation
----------

django-setuptest downloads eggs required for a test run and places them in the
module directory. For example, if the module to be tested is called ``foo``
then the command ``python setup.py test`` causes ``src/foo`` to be polluted
with many eggs. There is currently no way to instruct setuptools to store these
eggs in another location.

``django-setuptest-recipe`` addresses this shortcoming by wrapping the Python
interpreter to be aware of egg locations.

Usage
-----

Add the following to your ``buildout.cfg``::

    parts=
        ...
        setuptest-runner

    [setuptest-runner]
    recipe = django-setuptest-recipe
    eggs = ${buildout:eggs}

An executable file called ``setuptest-runner`` is created in the ``bin``
directory. You can now do ``/path/to/instance/bin/setuptest-runner setup.py
test`` from within the ``src/foo`` directory.

