# -*- coding: utf-8 -*-

# Copyright(C) 2009-2011  Romain Bignon, Florent Fourcot
#
# This file is part of weboob.
#
# weboob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# weboob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with weboob. If not, see <http://www.gnu.org/licenses/>.


import re

from weboob.capabilities.bank import Account
from weboob.capabilities.base import NotAvailable
from weboob.tools.browser import BasePage


__all__ = ['AccountsList']


class AccountsList(BasePage):
    def on_loaded(self):
        pass

    def get_list(self):
        l = []
        for td in self.document.xpath('.//td[@nowrap="nowrap"]'):
            account = Account()
            link = td.xpath('.//a')[0]
            account.id = re.search('\d', link.attrib['href']).group(0)
            account.label = link.text
            urltofind = './/a[@href="' + link.attrib['href'] + '"]'
            linkbis = self.document.xpath(urltofind).pop() 
            account.balance = float(linkbis.text.replace('.', '').replace(',','.'))
            account.coming = NotAvailable
            l.append(account)

        return l
