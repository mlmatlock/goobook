#!/bin/fish

# Test reStructuredText to html conversion.

for rst in *.rst
  rst2html5.py --strict $rst $rst.html
end
