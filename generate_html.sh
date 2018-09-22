#!/bin/fish

# Test reStructuredText to html conversion.

mkdir -p build/doc/

echo Writing html to ./build/doc/

for rst in *.rst
  rst2html5.py --strict $rst build/doc/$rst.html
end
