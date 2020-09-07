CHANGES
=======

3.5 2020-09-07
--------------
* Issue 87: Adjustments to how authenticate is used and documented, removed embedded client_id and secret
  Added documentation for getting a client_id and secret.
  Deprecated "client_secret_filename" in config.
* Issue 82: Feature request: Option to add phone number when creating new contact
* Updated dependencies.
* Issue 89: Support XDG Spec, files located in the old locations is still used if
  they exists but XDG locations are preferred.

  ex.

  - $XDG_CONFIG_HOME/goobookrc
  - $XDG_CACHE_HOME/goobook_cache
  - $XDG_DATA_HOME/goobook_auth.json

* Issue 75: Added unauthenticate command.

3.4 2019-09-10
--------------
* Issue 82: Cannot add contacts anymore
* Bug in add caused email to be used instead of name even when there was a name.

3.3 2018-12-14
--------------
* Issue 73 (reopened): Accept org name as display_name
* Issue 80: Implemented street addresses for dquery (again).
* Reimplemented IM contact support for dquery

3.2 2018-11-18
--------------
* Issue 17: Feature request: simple query output format to ease goobook use with notmuch
* dquery: Don't print header if there is no groups.
* Issue 69: Added note about regexps to man page.
* Issue 79: Fixed parsing of birthdays without date (fix is to ignore them)

3.1 2018-10-28
--------------
* dquery now prints each match only once.
* Fixed "goobook dump_contacts -p"
* Fixed dquery display of contacts with groups
* Issue 73: add organization/job fields

3.0.2 2018-10-25
----------------
* dquery now prints birthday
* Issue 59: Auto reload after add
* Fixed searching for contact groups
* Issue 77: Fixed add command
* Don't populate the cache with _invalid_ contacts by Matteo Landi

3.0.1 2018-10-22
----------------
* Fixed MANIFEST so rst files is included in src bundles.

3.0.0 2018-10-17
-----------------
* Supports Python 3.6 but not 2.x.
* dump_* format changed from xml to json because of change to different google library.
* Removed last traces of keyring support.
* Implement support for fuzzy finding contacts and groups by Matteo Landi

Note, 2.x was never released.

1.10 2016-07-04
---------------
* Change required versions for oauth2client/httplib2
* Update GooBook's manpage

1.9 2015-06-03
--------------
* #55 Fixed argument conflict between goobook and oauth2client

1.8 2015-06-03
--------------

* Fixed so that the included client_secrets.json is installed with the source.

1.7 2015-06-02
--------------
* Google no longer support ClientLogin (simple username/password)
* Removed support for ClientLogin
* Added OAuth2 support
* Removed support for .netrc
* Removed email, password, passwordeval fields from config
* Removed support for keyring, this might be temporary
* Removed support for executable .goobookrc

1.6   2014-07-02
----------------
* Issue 41 Changed keyring dependency into an extra.
* Issue 43 depend on setuptools>=0.7 instead of distribute (they have merged)
* add support for default group by Samir Benmendil
* Issue 42 Include a manual page
* Removed dependency on hcs_utils, included the used module instead. On request, to simplify for packagers.

1.5   2013-08-03
----------------
* Issue 39 Support for hcs-utils>=1.3
* Issue 40 Removed bundled distribute_setup.py
* Dropping support for Python 2.6, only Python 2.7 is now supported
  If you can't upgrade to 2.7 stay with 1.4.

1.4   2012-11-10
----------------
* No longer necessary to configure goobook to be able to generate a configuration template...
* Fixed issue 28: No Protocol is set on GTalk IM
* Fixed issue 32: Encoding problem of unicode chars on non unicode terminal.
* Fixed issue 34: Unable to query due to keyring/DBus regression
* Fixed issue 35: passwordeval
* Fixed issue 36: When the contact has no title mutt will use the extra_str as the title.

1.4a5  never released
---------------------
* Correctly decode encoded From headers, by Jonathan Ballet
* Fixed IM without protocol, Issue 26
* Fixed encoding issues on OS X, Issue 33
* passwordeval, get password from a command by Zhihao Yuan

1.4a4 2011-02-26
----------------

* Fixed bug in parsing postal addresses.
* Adjusted output format for postal addresses.

1.4a3 2011-02-26
----------------

* Added contacts are now added to "My Contacts", this fixes problem with
  searching now finding contacts you have added with goobook.
* Searches also matches on phonenumber (Patch by Marcus Nitzschke).
* Detailed, human readable, search results (Patch by Marcus Nitzschke).

1.4a2 2010-10-26
----------------

* When a query match a email-address, only show that address and not
  all the contacts addresses.
* Added option to filter contacts that are in no groups (default on).

1.4a1 2010-09-24
----------------

* Fixed mailing to groups
* Improved some error messages
* Isssue 20: Encoding on some Mac OS X
* Issue 21: Cache file never expires
* Support for auth via keyring


1.3 2010-07-17
--------------

No changes since 1.3rc1

1.3rc1 2010-06-24
-----------------

* Support for executable .goobookrc (replaces direct GnuPG support)
* Faster, more compact cache
* dump commands no longer use the cache
* Caching most contact data but not all

1.3a1 2010-04-21
----------------

* Python 2.5 compability
* Added flags --verbose and --debug
* Added possibility to add a contact from the command-line.
* Added possibility to prompt for password.
* New command: dump_contacts
* New command: dump_groups
* New dependency, hcs_utils
* Now caching all contact data.
* Support for using a GnuPG encrypted config file (later replaced).
* Fixed bug when checking for the config file.
* Major refactoring

1.2, 2010-03-12
---------------

* Issue 14: Only search in these fields: name, nick, emails, group name.
  In 1.1 the group URL was also searched, which gave false positives.
* Auto create cache if it doesn't exist.

1.1, 2010-03-10
---------------

* Use current locale to decode queries.
* Encode printed text using current locale.
* Added option to specify different configfile.
* Some documentation/help updates.
* The .goobookrc is now really optional.
* Added config-template command.
* Issue 13: Added support for contact groups.
* New cache format, no longer abook compatible (JSON).

1.0, 2010-02-20
---------------

* Issue 2: BadAuthentication error can create a problematic cache file so
  subsequent runs fail
* Issue 6: cache management needs improvements
  - reload, force refresh command
  - configurable cache expiry time
* Issue 7: Should probably set safe permissions on settings.pyc
* Issue 8: 'add' doesn't strip extraneous quotation marks
* Issue 9: Indentation error when run without arguments
* Issue 10: Query doesn't browse nicknames
* New abook compatible cache format.
* sort results
* Using SSL
* New config format
* .netrc support
* Supports adding non-ASCII From: headers.

r8, 2009-12-10
--------------

...

