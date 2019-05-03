## PyPI

Package is hosted here: https://pypi.python.org/pypi/arctic/

## General upload and packaging docs

https://realpython.com/pypi-publish-python-package/

The version number is of the format: <MAJOR>.<MINOR>.<BUGFIX> 
For minor bug fixes increment the BUGFIX number. For new features increment the minor letter. MAJOR is only 
for a major (and possibly non backwards compatible) overhaul of arctic.

## Pre-requisites

* Ensure you have pypandoc installed for converting the `README.md` to rst for pypi.
* Configure `.pypirc` to have appropriate credentials for upload. `@burrowsa` `@jamesblackburn` have access

```
pip install pypandoc
```

## Procedure

1. Confirm the version number is sane: `grep version= setup.py`
1. Ensure the working directory is clean: `git status`
1. Register the egg: `python setup.py register -r pypi`
1. Upload the source-dist: `python setup.py sdist upload -r pypi`
1. Upload the egg: `python setup.py build bdist_egg upload -r pypi`
1. Tag the package: `git tag v1.0.0 -m "Tagging v1.0.0" && git push --tags`
1. Update the version number in setup.py and push to master
