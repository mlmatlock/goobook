Release HOWTO
=============

To make a release, edit "version" in pyproject.toml and run:

  poetry build

To upload the generated source and wheel distribution to PyPI, run:

  poetry publish
