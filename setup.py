#!/usr/bin/env python
# vim: fileencoding=UTF-8 filetype=python ff=unix expandtab sw=4 sts=4 tw=120
# author: Christer Sjöholm -- goobook AT furuvik DOT net

import os
import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()
NEWS = open(os.path.join(HERE, 'CHANGES.rst')).read()


setuptools.setup(
    name='goobook',
    version='3.0.1',
    description='Search your google contacts from the command-line or mutt.',
    long_description=README + '\n\n' + NEWS,
    long_description_content_type="text/x-rst",
    author='Christer Sjöholm',
    author_email='goobook@furuvik.net',
    url='http://gitlab.com/goobook/goobook',
    download_url='http://pypi.python.org/pypi/goobook',
    classifiers=[f.strip() for f in """
        Development Status :: 5 - Production/Stable
        Environment :: Console
        Operating System :: OS Independent
        Programming Language :: Python
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.6
        Intended Audience :: End Users/Desktop
        License :: OSI Approved :: GNU General Public License (GPL)
        Topic :: Communications :: Email :: Address Book
    """.splitlines() if f.strip()],
    keywords='abook mutt e-mail gmail google address-book',
    license='GPLv3',
    install_requires=[
        'google-api-python-client>=1.6.4',
        'simplejson>=2.1.0',
        'oauth2client>=1.5.0,<5.0.0dev',
    ],
    extras_require={
    },
    include_package_data=True,
    zip_safe=False,
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['goobook = goobook.application:main']}
)
