#!/bin/fish

# Test reStructuredText to html conversion.
#
# You need to have done: pipenv install --dev

mkdir -p build/doc/

echo Writing html to ./build/doc/

for rst in *.rst
  pipenv run rst2html5.py --strict $rst build/doc/$rst.html
end
