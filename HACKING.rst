Release HOWTO
=============

To make a release, edit "version" in setup.py and run:

  pipenv run python setup.py egg_info -Db "" sdist bdist_wheel

To upload the generated source and wheel distribution to PyPI, run:

  pipenv run twine upload dist/*  ## Run on only the files you actually want to upload

Note that if you ignore the ``egg_info -Db ""`` part, Distribute will generate
a development release tarball with ``.dev``.
