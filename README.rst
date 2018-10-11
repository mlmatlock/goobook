:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
GooBook -- Access your Google contacts from the command line.
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

.. contents:: **Table of Contents**
   :depth: 1

About
=====

The purpose of GooBook is to make it possible to use your Google Contacts from
the command-line and from MUAs such as Mutt.
It can be used from Mutt the same way as abook.

Installation Instructions
=========================

There is a number of ways to install Python software.

- Using pip
- Using a source tarball
- Using source directly from gitorius
- From a distribution specific repository

Which version to use
--------------------

If you only have Python 2.7 you need to use GooBook 1.x.
If you have Python 3.6+ you need to use GooBook 3.x.

There will be no further feature releases in the 1.x series.

pip
---

This is the recommended way to install goobook for most users that
don't have it available in their distribution.
When installing this way you will not need to download anything manually.

Install like this::

    $ pip install --user goobook

This will install goobook as ~/.local/bin/goobook (In a UNIX environment).


Pipenv
------

This is the recommended way if you want to run from a git checkout.
Install pipenv if you don't have it, https://pipenv.readthedocs.io.

clone the git repos, cd into in, and run::

    $ pipenv install

Goobook is now installed in a virtualenv created by pipenv.
you can test pipenv by running::

    $ pipenv run goobook

To locate the virtualenv where goobook is installed::

    $ pipenv --venv

Source installation from tarball
--------------------------------

Download the source tarball, uncompress it, then run the install command::

    $ tar -xzvf goobook-*.tar.gz
    $ cd goobook-*
    $ sudo python ./setup.py install


Configuration
=============

For most users it will be enough to to run::

    $ goobook authenticate

and follow the instructions.

To get access too more settings you can create a configuration file::

    goobook config-template > ~/.goobookrc

It will look like this::


    # "#" or ";" at the start of a line makes it a comment.
    [DEFAULT]
    # The following are optional, defaults are shown

    # This file is written by the oauth library, and should be kept secure,
    # it's like a password to your google contacts.
    ;oauth_db_filename: ~/.goobook_auth.json

    # The client secret file is not really secret.
    ;client_secret_filename: ~/.goobook_client_secret.json

    ;cache_filename: ~/.goobook_cache
    ;cache_expiry_hours: 24
    ;filter_groupless_contacts: yes

    # New contacts will be added to this group in addition to "My Contacts"
    # Note that the group has to already exist on google or an error will occur.
    # One use for this is to add new contacts to an "Unsorted" group, which can
    # be sorted easier than all of "My Contacts".
    ;default_group:


Proxy settings
--------------

If you use a proxy you need to set the https_proxy environment variable.

Mutt
----

If you want to use goobook from mutt.

Set in your .muttrc file::

    set query_command="goobook query %s"

to query address book. (Normally bound to "Q" key.)

If you want to be able to use <tab> to complete email addresses instead of Ctrl-t add this:

    bind editor <Tab> complete-query

To add email addresses (with "a" key normally bound to create-alias command)::

    macro index,pager a "<pipe-message>goobook add<return>" "add the sender address to Google contacts"

If you want to add an email's sender to Contacts, press a while it's selected in the index or pager.

Usage
=====

To query your contacts::

    $ goobook query QUERY

The add command reads a email from STDIN and adds the From address to your Google contacts::

    $ goobook add

The cache is updated automatically according to the configuration but you can also force an update::

    $ goobook reload

For more commands see::

    $ goobook -h

and::

    $ goobook COMMAND -h

Links, Feedback and getting involved
====================================

- PyPI home: https://pypi.org/project/goobook/
- Code Repository: http://gitlab.com/goobook/goobook
- Issue tracker: https://gitlab.com/goobook/goobook/issues
- Mailing list: http://groups.google.com/group/goobook
