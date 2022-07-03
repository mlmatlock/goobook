#!/bin/fish

# Test reStructuredText to html conversion.
#
# You need to have done: poetry install --dev

mkdir -p build/doc/

echo Writing html to ./build/doc/

for rst in *.rst
  poetry run rst2html5.py --strict $rst build/doc/$rst.html
end
