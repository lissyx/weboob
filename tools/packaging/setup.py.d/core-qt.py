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


from setuptools import setup

import os


os.system('make -C weboob/tools/application/qt')

setup(
    name='weboob-core-qt',
    version='0.1',
    description='Weboob, Web Out Of Browsers - core library, Qt configuration GUI',
    long_description='Configure backends using a Qt GUI.',
    author='Romain Bignon',
    author_email='weboob@lists.symlink.me',
    maintainer='Christophe Benz',
    maintainer_email='christophe.benz@gmail.com',
    license='GPLv3',
    url='http://www.weboob.org',
    namespace_packages = [
        'weboob',
        'weboob.applications',
        'weboob.tools',
        'weboob.tools.application',
        ],
    packages=[
        'weboob',
        'weboob.applications.qweboobcfg',
        'weboob.tools.application.qt',
        ],
    scripts=[
        'scripts/weboob-config-qt',
        ],
    install_requires=[
        'weboob-core', # python-weboob-core
        'PyQt', # python-qt4
        ],
)