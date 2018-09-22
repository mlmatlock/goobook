=========
 goobook
=========

-------------------------------------------------------------------
access your Google contacts from mutt or the command line
-------------------------------------------------------------------


:Author: This manual page has been written by Dariusz Dwornikowski and Christer Sjöholm
:Date:   2018-09-22
:Manual section: 1
:Manual group: User Manuals

.. :Copyright: public domain
.. :Version: 0.1


SYNOPSIS
--------
**goobook**  [ options ] COMMAND


DESCRIPTION
-----------
**goobook** can be used to access your Google contacts from the command line. It can also
be easily integrated into MUAs such as mutt. It can be used from mutt the same
way as abook.


OPTIONS
-------

-h, --help
  show the help message and exit

-c FILE, --config FILE
  specify alternative configuration file

-v, --verbose
  be verbose about what is going on (stderr)

-V, --version
  print version and exit

-d, --debug
  output debug information to stderr


COMMAND
-------

authenticate
  allow goobook to access your Google contacts using OAuth2

add
  read an email address from stdin and add the From: address to your Google contacts

config-template
  create a config template of **~/.goobookrc**

dump_contacts
  dump all your contacts to XML (stdout)

dump_groups
  dump your contact groups to XML (stdout)

dquery QUERY_STRING
  search contacts for QUERY_STRING, nice vcard like output

query QUERY_STRING
  search contacts for QUERY_STRING, plain text output

reload
  reload contacts from Google and update cache


CONFIGURATION
-------------
| For most users it will be enough to run:
|
|    **goobook** authenticate

| To have access to more advanced options, you can generate a config file by doing:
|
|    **goobook** config-template > ~/.goobookrc

An example config can look like this::

    [DEFAULT]
    oauth_db_filename: ~/.goobook_auth.json
    cache_filename: ~/.goobook_cache
    cache_expiry_hours: 24


SEE ALSO
--------
Website: https://pypi.python.org/pypi/goobook/
