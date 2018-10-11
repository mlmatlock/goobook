#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: fileencoding=UTF-8 filetype=python ff=unix et ts=4 sw=4 sts=4 tw=120
# author: Christer Sjöholm -- hcs AT furuvik DOT net


import argparse
import logging
import os
import json
import sys

import oauth2client.client
import oauth2client.file
import oauth2client.tools
import pkg_resources
from pkg_resources import resource_filename

import goobook.config
from goobook.goobook import GooBook, Cache, GoogleContacts, parse_groups, parse_contacts
from goobook.storage import unstorageify

log = logging.getLogger(__name__)  # pylint: disable=invalid-name

CONFIG_FILE = '~/.goobookrc'
SCOPES = 'https://www.google.com/m8/feeds'  # read/write access to Contacts and Contact Groups


def main():
    parser = argparse.ArgumentParser(description='Search you Google contacts from mutt or the command-line.')
    parser.add_argument('-c', '--config', help='Specify alternative configuration file.', metavar="FILE")
    parser.add_argument('-v', '--verbose', dest="log_level", action='store_const',
                        const=logging.INFO, help='Be verbose about what is going on (stderr).')
    parser.add_argument('-V', '--version',
                        action='version',
                        version='%%(prog)s %s' % pkg_resources.get_distribution("goobook").version,
                        help="Print version and exit")
    parser.add_argument('-d', '--debug', dest="log_level", action='store_const',
                        const=logging.DEBUG, help='Output debug info (stderr).')
    parser.set_defaults(config=CONFIG_FILE, log_level=logging.ERROR)

    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser('add',
                                       description='Create new contact, if name and email is not given the'
                                       ' sender of a mail read from stdin will be used.')
    parser_add.add_argument('name', nargs='?', metavar='NAME',
                            help='Name to use.')
    parser_add.add_argument('email', nargs='?', metavar='EMAIL',
                            help='E-mail to use.')
    parser_add.set_defaults(func=do_add)

    parser_config_template = subparsers.add_parser('config-template',
                                                   description='Prints a template for .goobookrc to stdout')
    parser_config_template.set_defaults(func=do_config_template)

    parser_dump_contacts = subparsers.add_parser('dump_contacts',
                                                 description='Dump contacts as JSON.')
    parser_dump_contacts.add_argument('-p', '--parse', action='store_true', help='Dump parsed contact instead of raw.')
    parser_dump_contacts.set_defaults(func=do_dump_contacts)

    parser_dump_groups = subparsers.add_parser('dump_groups',
                                               description='Dump groups as JSON.')
    parser_dump_groups.add_argument('-p', '--parse', action='store_true', help='Dump parsed contact instead of raw.')
    parser_dump_groups.set_defaults(func=do_dump_groups)

    parser_query = subparsers.add_parser('query',
                                         description='Search contacts using query (regex).')
    parser_query.add_argument('query', help='regex to search for.', metavar='QUERY')
    parser_query.set_defaults(func=do_query)

    parser_query_details = subparsers.add_parser(
        'dquery',
        description='Search contacts using query (regex) and print out all info.')
    parser_query_details.add_argument('query', help='regex to search for.')
    parser_query_details.set_defaults(func=do_query_details)

    parser_reload = subparsers.add_parser('reload',
                                          description='Force reload of the cache.')
    parser_reload.set_defaults(func=do_reload)

    parser_auth = subparsers.add_parser('authenticate',
                                        description='Google OAuth authentication.',
                                        formatter_class=argparse.RawDescriptionHelpFormatter,
                                        parents=[oauth2client.tools.argparser])
    parser_auth.set_defaults(func=do_authenticate)

    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    if 'func' not in args:
        parser.error('To few arguments.')

    try:
        if args.func is do_config_template:
            config = None
        else:
            config = goobook.config.read_config(args.config)
        args.func(config, args)
    except goobook.config.ConfigError as err:
        sys.exit('Configuration error: ' + str(err))

##############################################################################
# sub commands


def do_add(config, args):
    goobk = GooBook(config)
    if args.name and args.email:
        goobk.add_mail_contact(args.name, args.email)
    else:
        goobk.add_email_from(sys.stdin)


def do_config_template(_config, _args):
    print(goobook.config.TEMPLATE)


def do_dump_contacts(config, args):
    goco = GoogleContacts(config)
    contacts = goco.fetch_contacts()
    if args.parse:
        groupname_by_id = parse_groups(goco.fetch_contact_groups())
        contacts = unstorageify(list(parse_contacts(goco.fetch_contacts(), groupname_by_id)))

    print(json.dumps(contacts, sort_keys=True, indent=4, ensure_ascii=False))


def do_dump_groups(config, args):
    goco = GoogleContacts(config)
    groups = goco.fetch_contact_groups()
    if args.parse:
        groupname_by_id = parse_groups(goco.fetch_contact_groups())
        groups = unstorageify(list(groupname_by_id.values()))

    print(json.dumps(groups, sort_keys=True, indent=4, ensure_ascii=False))


def do_query(config, args):
    goobk = GooBook(config)
    goobk.query(args.query)


def do_query_details(config, args):
    goobk = GooBook(config)
    goobk.query_details(args.query)


def do_reload(config, _args):
    cache = Cache(config)
    cache.load(force_update=True)


def do_authenticate(config, args):
    store = config.store
    creds = config.creds

    if not creds or creds.invalid:
        client_secret_filename = config.client_secret_filename
        if not os.path.exists(client_secret_filename):
            client_secret_filename = resource_filename(__name__, 'client_secret.json')
        flow = oauth2client.client.flow_from_clientsecrets(client_secret_filename, SCOPES)
        creds = oauth2client.tools.run_flow(flow, store, args)
    else:
        print('You are already authenticated.')


if __name__ == '__main__':
    main()
