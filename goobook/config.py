# -*- coding: UTF-8 -*-
# vim: fileencoding=UTF-8 filetype=python ff=unix et ts=4 sw=4 sts=4 tw=120
# author: Christer Sjöholm -- hcs AT furuvik DOT net

import os
import pathlib
import sys
from os.path import realpath, expanduser
import configparser
import logging

import oauth2client.client
import xdg

from goobook.storage import Storage

log = logging.getLogger(__name__)  # pylint: disable=invalid-name
LEGACY_CONFIG_FILE = pathlib.Path('~/.goobookrc').expanduser()
LEGACY_AUTH_FILE = pathlib.Path('~/.goobook_auth.json').expanduser()
LEGACY_CACHE_FILE = pathlib.Path('~/.goobook_cache').expanduser()

TEMPLATE = '''\
# Use this template to create your ~/.goobookrc

# "#" or ";" at the start of a line makes it a comment.

[DEFAULT]
# The following are optional, defaults are shown when not other specified.

# This file is written by the oauth library, and should be kept secure,
# it's like a password to your google contacts.
# default is to place it in the XDG_DATA_HOME
;oauth_db_filename: ~/.goobook_auth.json

;cache_filename: ~/.goobook_cache   # default is in the XDG_CACHE_HOME
;cache_expiry_hours: 24
;filter_groupless_contacts: yes

# New contacts will be added to this group in addition to "My Contacts"
# Note that the group has to already exist on google or an error will occur.
# One use for this is to add new contacts to an "Unsorted" group, which can
# be sorted easier than all of "My Contacts".
;default_group:
'''


def read_config(config_file=None):
    """Reads the ~/.goobookrc and any authentication data.

    returns the configuration as a dictionary.

    """
    config = Storage({  # Default values
        'cache_filename': None,
        'oauth_db_filename': None,
        'cache_expiry_hours': '24',
        'filter_groupless_contacts': True,
        'default_group': ''})

    # Search for config file to use
    if config_file:  # config file explicitly given on the commandline
        config_file = os.path.expanduser(config_file)
    else:  # search for goobookrc in XDG dirs and homedir
        config_files = [dir_ / "goobookrc" for dir_ in [xdg.XDG_CONFIG_HOME] +
                        xdg.XDG_CONFIG_DIRS] + [LEGACY_CONFIG_FILE]
        log.debug("config file search path: %s", config_files)
        for config_file_ in config_files:
            if config_file_.exists():
                config_file = str(config_file_)
                log.debug("found config file: %s", config_file)
                break
        else:
            log.debug("no config file found")
            config_file = None
        # else:  # .goobookrc in home directory
        #     config_file = os.path.expanduser(CONFIG_FILE)

    if config_file:
        parser = _get_config(config_file)
    else:
        parser = None

    if parser:
        config.get_dict().update(dict(parser.items('DEFAULT', raw=True)))
        # Handle not string fields
        if parser.has_option('DEFAULT', 'filter_groupless_contacts'):
            config.filter_groupless_contacts = parser.getboolean('DEFAULT', 'filter_groupless_contacts')

    if "client_secret_filename" in config:
        print("WARNING: setting client_secret_filename in {} is deprecated".format(config_file), file=sys.stderr)

    # Search for cache file to use
    if config.cache_filename:  # If explicitly specified in config file
        config.cache_filename = realpath(expanduser(config.cache_filename))
    else:  # search for goobook_cache in XDG dirs and homedir
        cache_files = [xdg.XDG_CACHE_HOME / "goobook_cache", LEGACY_CACHE_FILE]
        log.debug("cache file search path: %s", cache_files)
        for cache_file in cache_files:
            cache_file = cache_file.resolve()
            if cache_file.exists():
                log.debug("found cache file: %s", cache_file)
                break
        else:  # If there is none, create in XDG_CACHE_HOME
            cache_file = xdg.XDG_CACHE_HOME / "goobook_cache"
            log.debug("no cache file found, will use %s", cache_file)
        config.cache_filename = str(cache_file)

    # Search for auth file to use
    if config.oauth_db_filename:  # If explicitly specified in config file
        config.oauth_db_filename = realpath(expanduser(config.oauth_db_filename))
    else:  # search for goobook_auth.json in XDG dirs and homedir
        auth_files = [dir_ / "goobook_auth.json" for dir_ in [xdg.XDG_DATA_HOME] +
                      xdg.XDG_DATA_DIRS] + [LEGACY_AUTH_FILE]
        log.debug("auth file search path: %s", auth_files)
        for auth_file in auth_files:
            auth_file = auth_file.resolve()
            if auth_file.exists():
                log.debug("found auth file: %s", auth_file)
                break
        else:  # If there is none, create in XDG_DATA_HOME
            auth_file = xdg.XDG_DATA_HOME / "goobook_auth.json"
            log.debug("no auth file found, will use %s", auth_file)
        config.oauth_db_filename = str(auth_file)

    config.store = oauth2client.file.Storage(config.oauth_db_filename)

    config.creds = config.store.get() if auth_file.exists() else None

    log.debug(config)
    return config


def _get_config(config_file):
    """find, read and parse configuraton."""
    parser = configparser.SafeConfigParser()
    if os.path.lexists(config_file):
        try:
            log.info('Reading config: %s', config_file)
            inp = open(config_file)
            parser.read_file(inp)
            return parser
        except (IOError, configparser.ParsingError) as err:
            raise ConfigError("Failed to read configuration %s\n%s" % (config_file, err))
    return None


class ConfigError(Exception):
    pass
