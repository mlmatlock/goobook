#!/usr/bin/env python
'''
The idea is make an interface to google contacts that mimics the behaviour of
abook for mutt. It's developed in python and uses the fine
google data api (gdata).

'''

import sys
import os
import re
import pickle
import ConfigParser
from datetime import datetime
from os.path import realpath, expanduser

from gdata.contacts.service import ContactsService, ContactsQuery
from gdata.contacts import ContactEntry, Email
import atom

CONFIG_PATH = '~/.goobookrc'
CONFIG_EXAMPLE = '''[DEFAULT]
username: user@gmail.com
password: top secret
max_results: 9999
cache_filename: ~/.goobook_cache
cache_expiry_days: 1
'''

class GooBook(object):
    '''This class can't be used as a library as it looks now, it user sys.stdin
    print and sys.exit().'''
    def __init__ (self, config):
        self.username = config.get('DEFAULT', 'username')
        self.password = config.get('DEFAULT', 'password')
        self.max_results = config.get('DEFAULT', 'max_results')
        self.cache_filename = config.get('DEFAULT', 'cache_filename')
        self.cache_filename = realpath(expanduser(self.cache_filename))
        self.cache_expiry_days = config.get('DEFAULT', 'cache_expiry_days')

        self.addrbk = {}

    def query(self, query):
        """
        Do the query, and print it out in
        """
        self.load()
        match = re.compile(query, re.I).search
        resultados = dict([(k, v) for k, v in self.addrbk.items()
                           if match(k) or match(v)])
        # mutt's query_command expects the first line to be a message,
        # which it discards.
        print "\n",
        for (name, mail) in resultados.items():
            print "%s\t%s" % (name, mail)

    def load(self):
        """
        Load the cached addressbook feed, or fetch it (again) if it is
        old or missing or invalid or anyting
        """
        try:
            picklefile = file(self.cache_filename, 'rb')
        except IOError:
            # we should probably catch picke errors too...
            self.fetch()
            #  simplifico el feed, con formato 'titulo'\t'email' sin ''
        else:
            stamp, self.addrbk = pickle.load(picklefile) #optimizar
            if (datetime.now() - stamp).days > self.cache_expiry_days:
                self.fetch()
        finally:
            self.store()


    def fetch(self):
        """
        Actually go out on the wire and fetch the addressbook.

        """
        client = ContactsService()
        client.ssl = True
        client.ClientLogin(self.username, self.password)
        query = ContactsQuery()
        query.max_results = self.max_results
        feed = client.GetContactsFeed(query.ToUri())
        for ent in feed.entry:
            for i in ent.email:
                if ent.title.text:
                    self.addrbk[i.address] = ent.title.text
                else:
                    self.addrbk[i.address] = i.address

    def store(self):
        """
        Pickle the addressbook and a timestamp
        """
        if self.addrbk: # never store a empty addressbook
            picklefile = file(self.cache_filename, 'wb')
            stamp = datetime.now()
            pickle.dump((stamp, self.addrbk), picklefile)

    def add(self):
        """
        Add an address from From: field of a mail.
        This assumes a single mail file is supplied through stdin.
        """

        from_line = ""
        for line in sys.stdin:
            if line.startswith("From: "):
                from_line = line
                break
        if from_line == "":
            print "Not a valid mail file!"
            sys.exit(2)
        #In a line like
        #From: John Doe <john@doe.com>
        els = from_line.split()
        #Drop "From: "
        del els[0]
        #get the last element as mail
        mailaddr = els[-1]
        if mailaddr.startswith("<"):
            mailaddr = mailaddr[1:]
        if mailaddr.endswith(">"):
            mailaddr = mailaddr[:-1]
        #and the rest as name
        name = " ".join(els[:-1])
        #save to contacts
        client = ContactsService()
        client.ssl = True
        client.ClientLogin(self.username, self.password)
        new_contact = ContactEntry(title=atom.Title(text=name))
        new_contact.email.append(Email(address=mailaddr, primary='true'))
        contact_entry = client.CreateContact(new_contact)
        print contact_entry

def usage():
    print """\
Usage: goobook.py <command> [<arg>]
Commands:
   reload
   query <name>
   add <mail.at.stdin>\
"""
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        usage()
    config = ConfigParser.SafeConfigParser()
    try:
        config.readfp(open(os.path.expanduser(CONFIG_PATH)))
    except (IOError, ConfigParser.ParsingError):
        print >> sys.stderr, "Failed to read %s\n\nExample:\n\n%s" % (
            CONFIG_PATH, CONFIG_EXAMPLE)
        sys.exit(1)
    goobk = GooBook(config)
    if sys.argv[1] == "query":
        if len(sys.argv) < 3:
            usage()
        goobk.query(sys.argv[2])
    elif sys.argv[1] == "add":
        goobk.add()
    elif sys.argv[1] == "reload":
        goobk.fetch()
        goobk.store()
    else:
        usage()

if __name__ == '__main__':
    main()