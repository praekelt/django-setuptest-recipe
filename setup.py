from setuptools import setup

setup(
    name = "django-setuptest-recipe",
    entry_points = {'zc.buildout': ['default = django_setuptest_recipe.recipe:Recipe']},
    version='0.1',
    description='Recipe to prevent django-setuptest from polluting module being tested with downloaded eggs',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    install_requires = [
        'djangorecipe',
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
