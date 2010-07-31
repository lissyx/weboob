#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright(C) 2010  Christophe Benz
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.


from __future__ import with_statement

from setuptools import setup


with open('README') as f:
    readme_data = f.read()

setup(
    name='weboob-core',
    version='0.1',
    description='Weboob, Web Out Of Browsers - core library',
    long_description=readme_data,
    author='Romain Bignon',
    author_email='weboob@lists.symlink.me',
    maintainer='Christophe Benz',
    maintainer_email='christophe.benz@gmail.com',
    license='GPLv3',
    url='http://www.weboob.org',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Internet',
        ],
    # keywords='',
    namespace_packages = [
        'weboob',
        'weboob.applications',
        'weboob.tools',
        'weboob.tools.application',
	],
    packages=[
        'weboob',
        'weboob.applications',
        'weboob.applications.weboobcfg',
        'weboob.applications.weboobdebug',
        'weboob.applications.weboobtests',
        'weboob.capabilities',
        'weboob.core',
        'weboob.tools',
        'weboob.tools.application',
        'weboob.tools.application.formatters',
        'weboob.tools.browser',
        'weboob.tools.config',
        'weboob.tools.parsers',
        ],
    scripts=[
        'scripts/weboob-config',
        # 'scripts/weboob-debug',
        # 'scripts/weboob-tests',
        ],
    install_requires=[
        'elementtidy', # python-elementtidy
        'lxml', # python-lxml
        'mechanize', # python-mechanize
        'python-dateutil', # python-dateutil
        'PyYAML', # python-yaml
        ],
    # package name / Debian package name
    #
    # Recommends
    # html2text / python-html2text
    # PrettyTable / python-prettytable
    #
    # Suggests
    # ClientForm / python-clientform
    # ipython / ipython
    # nose / python-nose
    # pysqlite / python-pysqlite2
)