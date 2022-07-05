Release HOWTO
=============

To make a release, edit "version" in pyproject.toml and run::

  poetry build

To upload the generated source and wheel distribution to PyPI, run::

  poetry publish

Linting
=======

Use the provided scripts to check, verify and validate the package and
documentation.

* The ``scripts/check.sh`` is used for general checks of the package code.

* Use ``scripts/check-man.sh`` to verify that the manual page can be created.

* Use ``scripts/check-rst.sh`` to verify that the documentation can be created.
